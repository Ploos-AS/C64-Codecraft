#!/usr/bin/env python3
"""Fail-closed M0.2 VICE machine-runner contract."""

from dataclasses import dataclass, field
from pathlib import Path
import re
import shutil
import socket
import struct
import subprocess
import time
from typing import Protocol


class QualificationUnavailable(RuntimeError):
    pass


class AssertionMismatch(AssertionError):
    pass


@dataclass(frozen=True)
class MachineProfile:
    video: str = "PAL"
    model: str = "C64"
    emulator: str = "x64sc"


@dataclass(frozen=True)
class MachineObservation:
    memory: dict[int, int] = field(default_factory=dict)
    registers: dict[str, int] = field(default_factory=dict)
    stop_reason: str = ""


class StateBackend(Protocol):
    name: str

    def observe(
        self, *, binary: str, prg: Path, profile: MachineProfile
    ) -> MachineObservation:
        ...


class ViceBinaryMonitorProtocol:
    """Minimal fail-closed VICE binary-monitor protocol codec."""

    STX = 0x02
    API_VERSION = 0x02
    MEM_GET = 0x01
    CHECKPOINT_INFO = 0x11
    CHECKPOINT_SET = 0x12
    CHECKPOINT_DELETE = 0x13
    EXIT = 0xAA
    BANKS_AVAILABLE = 0x82

    @classmethod
    def memory_get_request(cls, start: int, end: int, request_id: int = 1, bank_id: int = 0) -> bytes:
        if not (0 <= start <= end <= 0xFFFF):
            raise ValueError("invalid memory range")
        body = struct.pack("<BHHBH", 1, start, end, 0, bank_id)
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", len(body), request_id)
            + bytes((cls.MEM_GET,))
            + body
        )

    @classmethod
    def banks_available_request(cls, request_id: int = 1) -> bytes:
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", 0, request_id)
            + bytes((cls.BANKS_AVAILABLE,))
        )

    @classmethod
    def banks_available_response(cls, packet: bytes, request_id: int = 1):
        if len(packet) < 14 or packet[6] != cls.BANKS_AVAILABLE or packet[7]:
            raise QualificationUnavailable("invalid VICE banks-available response")
        if struct.unpack_from("<I", packet, 8)[0] != request_id:
            raise QualificationUnavailable("VICE banks response request-id mismatch")
        body_len = struct.unpack_from("<I", packet, 2)[0]
        body = packet[12:12 + body_len]
        if len(body) < 2:
            raise QualificationUnavailable("truncated VICE banks response")
        count = struct.unpack_from("<H", body, 0)[0]
        offset, banks = 2, {}
        for _ in range(count):
            if offset >= len(body):
                raise QualificationUnavailable("truncated VICE bank item")
            item_size = body[offset]
            item = body[offset + 1:offset + 1 + item_size]
            if len(item) != item_size or item_size < 3:
                raise QualificationUnavailable("invalid VICE bank item")
            bank_id = struct.unpack_from("<H", item, 0)[0]
            name_len = item[2]
            if 3 + name_len > len(item):
                raise QualificationUnavailable("invalid VICE bank name")
            banks[item[3:3 + name_len].decode("ascii", "strict").lower()] = bank_id
            offset += 1 + item_size
        return banks

    @classmethod
    def checkpoint_set_request(cls, address: int, request_id: int = 2) -> bytes:
        if not 0 <= address <= 0xFFFF:
            raise ValueError("invalid checkpoint address")
        body = struct.pack("<HHBBBBB", address, address, 1, 1, 4, 1, 0)
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", len(body), request_id)
            + bytes((cls.CHECKPOINT_SET,))
            + body
        )

    @classmethod
    def checkpoint_response(cls, packet: bytes, request_id: int | None = None):
        if len(packet) < 35 or packet[6] != cls.CHECKPOINT_INFO or packet[7]:
            raise QualificationUnavailable("invalid VICE checkpoint response")
        response_id = struct.unpack_from("<I", packet, 8)[0]
        if request_id is not None and response_id != request_id:
            raise QualificationUnavailable("VICE checkpoint response request-id mismatch")
        body_len = struct.unpack_from("<I", packet, 2)[0]
        if body_len < 23 or len(packet) != 12 + body_len:
            raise QualificationUnavailable("invalid VICE checkpoint response length")
        body = packet[12:]
        return {
            "number": struct.unpack_from("<I", body, 0)[0],
            "hit": bool(body[4]),
            "start": struct.unpack_from("<H", body, 5)[0],
            "end": struct.unpack_from("<H", body, 7)[0],
            "hit_count": struct.unpack_from("<I", body, 13)[0],
        }

    @classmethod
    def checkpoint_delete_request(cls, checkpoint_number: int, request_id: int) -> bytes:
        body = struct.pack("<I", checkpoint_number)
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", len(body), request_id)
            + bytes((cls.CHECKPOINT_DELETE,))
            + body
        )

    @classmethod
    def exit_request(cls, request_id: int = 3) -> bytes:
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", 0, request_id)
            + bytes((cls.EXIT,))
        )

    @classmethod
    def memory_get_response(cls, packet: bytes, request_id: int = 1) -> bytes:
        if len(packet) < 12:
            raise QualificationUnavailable("truncated VICE binary-monitor response")
        stx, api = packet[0], packet[1]
        body_len = struct.unpack_from("<I", packet, 2)[0]
        response_type, error = packet[6], packet[7]
        response_id = struct.unpack_from("<I", packet, 8)[0]
        if stx != cls.STX or api != cls.API_VERSION:
            raise QualificationUnavailable("invalid VICE binary-monitor response header")
        if response_type != cls.MEM_GET or response_id != request_id or error:
            raise QualificationUnavailable(
                f"VICE memory response mismatch: type={response_type:#04x} "
                f"error={error:#04x} request={response_id:#010x}"
            )
        if len(packet) != 12 + body_len or body_len < 2:
            raise QualificationUnavailable("invalid VICE memory response length")
        segment_len = struct.unpack_from("<H", packet, 12)[0]
        data = packet[14:]
        if segment_len != len(data):
            raise QualificationUnavailable("VICE memory segment length mismatch")
        return data


class ViceBinaryMonitorClient:
    """Persistent synchronous VICE binary-monitor transport."""

    def __init__(self, host="127.0.0.1", port=6502, timeout=2.0):
        self.host, self.port, self.timeout = host, port, timeout

    @staticmethod
    def _recv_exact(sock, count):
        data = bytearray()
        while len(data) < count:
            chunk = sock.recv(count - len(data))
            if not chunk:
                raise QualificationUnavailable("VICE binary-monitor connection closed")
            data.extend(chunk)
        return bytes(data)

    def _packet(self, sock):
        header = self._recv_exact(sock, 12)
        body_len = struct.unpack_from("<I", header, 2)[0]
        return header + self._recv_exact(sock, body_len)

    @staticmethod
    def _request_id(packet):
        return struct.unpack_from("<I", packet, 8)[0]

    def run_until(self, address: int, start: int, end: int, prg: Path, entry_address: int | None = None) -> bytes:
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.settimeout(self.timeout)

                sock.sendall(ViceBinaryMonitorProtocol.banks_available_request(1))
                while True:
                    packet = self._packet(sock)
                    if self._request_id(packet) == 0xFFFFFFFF:
                        continue
                    if self._request_id(packet) != 1:
                        raise QualificationUnavailable("unexpected VICE banks response")
                    banks = ViceBinaryMonitorProtocol.banks_available_response(packet, 1)
                    break
                bank_id = banks.get("cpu")
                if bank_id is None:
                    bank_id = banks.get("current")
                if bank_id is None:
                    raise QualificationUnavailable(
                        f"VICE exposes no CPU/current bank; available={sorted(banks)}"
                    )

                # Prove the autostarted PRG is actually resident before execution.
                # PRG bytes 0-1 are the little-endian load address; compare the
                # complete payload with VICE CPU-visible memory fail-closed.
                prg_bytes = Path(prg).read_bytes()
                load_address = struct.unpack_from("<H", prg_bytes, 0)[0]
                payload = prg_bytes[2:]
                sock.sendall(
                    ViceBinaryMonitorProtocol.memory_get_request(
                        load_address, load_address + len(payload) - 1, 2, bank_id
                    )
                )
                while True:
                    packet = self._packet(sock)
                    if self._request_id(packet) == 0xFFFFFFFF:
                        continue
                    if self._request_id(packet) != 2:
                        raise QualificationUnavailable(
                            "unexpected VICE pre-execution memory response"
                        )
                    loaded = ViceBinaryMonitorProtocol.memory_get_response(packet, 2)
                    print(f"VICE pre-exec bank={bank_id} banks={banks} load={load_address:#06x} payload={loaded.hex()}")
                    break
                if loaded != payload:
                    raise QualificationUnavailable(
                        f"VICE autostart payload mismatch at {load_address:#06x}: "
                        f"expected={payload.hex()} observed={loaded.hex()}"
                    )

                # Optionally gate execution on the lab entry point first. The
                # entry checkpoint is temporary so it cannot catch the wait loop
                # again after the target checkpoint has been installed.
                if entry_address is not None:
                    sock.sendall(ViceBinaryMonitorProtocol.checkpoint_set_request(entry_address, 3))
                    while True:
                        packet = self._packet(sock)
                        if self._request_id(packet) == 3:
                            entry_checkpoint = ViceBinaryMonitorProtocol.checkpoint_response(packet, 3)
                            break
                    sock.sendall(ViceBinaryMonitorProtocol.exit_request(4))
                    while True:
                        packet = self._packet(sock)
                        if self._request_id(packet) == 4 and packet[7]:
                            raise QualificationUnavailable("VICE rejected entry monitor exit")
                        if self._request_id(packet) == 0xFFFFFFFF and packet[6] == 0x62:
                            break

                    sock.sendall(
                        ViceBinaryMonitorProtocol.checkpoint_delete_request(
                            entry_checkpoint["number"], 5
                        )
                    )
                    while True:
                        packet = self._packet(sock)
                        if self._request_id(packet) == 5:
                            if packet[6] != ViceBinaryMonitorProtocol.CHECKPOINT_DELETE or packet[7]:
                                raise QualificationUnavailable("VICE rejected entry checkpoint delete")
                            break
                    checkpoint_request_id, exit_request_id, memory_request_id = 6, 7, 8
                else:
                    checkpoint_request_id, exit_request_id, memory_request_id = 3, 4, 5

                sock.sendall(
                    ViceBinaryMonitorProtocol.checkpoint_set_request(
                        address, checkpoint_request_id
                    )
                )
                while True:
                    packet = self._packet(sock)
                    if self._request_id(packet) == checkpoint_request_id:
                        target_checkpoint = ViceBinaryMonitorProtocol.checkpoint_response(
                            packet, checkpoint_request_id
                        )
                        break

                sock.sendall(ViceBinaryMonitorProtocol.exit_request(exit_request_id))
                while True:
                    packet = self._packet(sock)
                    request_id = self._request_id(packet)
                    if request_id == exit_request_id and packet[7]:
                        raise QualificationUnavailable("VICE rejected monitor exit")
                    if request_id == 0xFFFFFFFF and packet[6] == 0x62:
                        break

                request_id = memory_request_id
                state_bank_id = banks.get("io", bank_id)
                sock.sendall(
                    ViceBinaryMonitorProtocol.memory_get_request(start, end, request_id, state_bank_id)
                )
                while True:
                    packet = self._packet(sock)
                    response_id = self._request_id(packet)
                    if response_id in (0xFFFFFFFF, exit_request_id):
                        # EXIT may acknowledge after the asynchronous stopped event.
                        continue
                    if response_id != request_id:
                        raise QualificationUnavailable(
                            f"unexpected VICE binary-monitor request id "
                            f"{response_id:#010x}"
                        )
                    data = ViceBinaryMonitorProtocol.memory_get_response(packet, request_id)
                    print(f"VICE post-exec bank={state_bank_id} range={start:#06x}-{end:#06x} data={data.hex()}")
                    return data
        except (OSError, TimeoutError) as exc:
            raise QualificationUnavailable(
                f"VICE binary-monitor transport failed: {exc}"
            ) from exc


class ViceBinaryMonitorBackend:
    """VICE binary-monitor transport with deterministic execution stop."""

    name = "vice-binary-monitor"

    def __init__(
        self,
        expected_addresses=(0xD020, 0xD021),
        host="127.0.0.1",
        port=6502,
        startup_timeout=5.0,
        rom_dir=None,
        stop_address=0x0822,
        entry_address=None,
    ):
        self.expected_addresses = tuple(expected_addresses)
        self.host, self.port = host, port
        self.startup_timeout = startup_timeout
        self.rom_dir = Path(rom_dir).resolve() if rom_dir is not None else None
        self.stop_address = stop_address
        self.entry_address = entry_address

    def observe(self, *, binary: str, prg: Path, profile: MachineProfile):
        if profile.video.upper() != "PAL":
            raise QualificationUnavailable(
                f"VICE binary backend currently qualifies PAL only, got {profile.video}"
            )
        if not self.expected_addresses:
            raise QualificationUnavailable("no memory addresses requested")
        start, end = min(self.expected_addresses), max(self.expected_addresses)
        prg = prg.resolve()
        command = [
            "xvfb-run", "-a", binary,
            "-binarymonitor",
            "-binarymonitoraddress", f"ip4://{self.host}:{self.port}",
            "-console",
            "-sounddev", "dummy",
            "-virtualdev8",
            "-autostartprgmode", "1",
            "-pal",
        ]
        if self.rom_dir is not None:
            command += [
                "-kernal", str(self.rom_dir / "kernal.rom"),
                "-basic", str(self.rom_dir / "basic.rom"),
                "-chargen", str(self.rom_dir / "chargen.rom"),
            ]
        command += ["-autostart", str(prg)]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )
        deadline = time.monotonic() + self.startup_timeout
        client = ViceBinaryMonitorClient(
            self.host, self.port, timeout=min(1.0, self.startup_timeout)
        )
        last_error = None
        try:
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    output = process.stdout.read() if process.stdout else ""
                    raise QualificationUnavailable(
                        f"VICE exited before monitor became ready: {process.returncode}: "
                        f"{output[-4000:]}"
                    )
                try:
                    data = client.run_until(self.stop_address, start, end, prg, self.entry_address)
                    memory = {
                        address: data[address - start]
                        for address in self.expected_addresses
                    }
                    return MachineObservation(
                        memory=memory,
                        stop_reason=f"temporary-exec-checkpoint-{self.stop_address:#06x}",
                    )
                except QualificationUnavailable as exc:
                    last_error = exc
                    time.sleep(0.05)
            raise QualificationUnavailable(
                f"VICE binary monitor did not become readable: {last_error}"
            )
        finally:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)


class ViceMonitorTranscriptBackend:
    """Parser/transport prototype for a textual VICE monitor transcript.

    Transport is deliberately opt-in: until a packaged VICE invocation is
    qualified, observe() fails closed. parse_memory() can be independently
    tested against captured monitor output without claiming emulator support.
    """

    name = "vice-monitor-transcript"
    _MEMORY_LINE = re.compile(
        r"^\s*(?:(?:>[A-Za-z0-9]+:)|(?:[A-Za-z0-9]+:))?(?P<address>[0-9A-Fa-f]{4})"
        r"(?:\s+|:)\s*(?P<bytes>(?:[0-9A-Fa-f]{2}(?:\s+|$))+)"
    )

    @classmethod
    def parse_memory(cls, transcript: str) -> dict[int, int]:
        memory = {}
        for line in transcript.splitlines():
            match = cls._MEMORY_LINE.match(line)
            if not match:
                continue
            address = int(match.group("address"), 16)
            for token in match.group("bytes").split():
                if address > 0xFFFF:
                    break
                memory[address] = int(token, 16)
                address += 1
        if not memory:
            raise QualificationUnavailable(
                "VICE monitor transcript contained no machine-readable memory"
            )
        return memory

    def observe(self, *, binary: str, prg: Path, profile: MachineProfile):
        raise QualificationUnavailable(
            "VICE monitor transcript transport is not qualified for the "
            "packaged emulator; parser exists but emulator_state must remain false"
        )


def find_vice(binary="x64sc"):
    path = shutil.which(binary)
    if not path:
        raise QualificationUnavailable(f"{binary} not found")
    return path


def vice_version(binary):
    result = subprocess.run(
        [binary, "-version"], text=True, capture_output=True, timeout=10
    )
    output = (result.stdout + result.stderr).strip()
    if result.returncode:
        raise QualificationUnavailable(
            f"cannot identify VICE version: exit {result.returncode}: {output}"
        )
    if not output:
        raise QualificationUnavailable("VICE returned no version information")
    return output.splitlines()[0]


def assert_memory(observation: MachineObservation, expected: dict[int, int], masks: dict[int, int] | None = None):
    masks = masks or {}
    for address, value in expected.items():
        if not 0 <= address <= 0xFFFF:
            raise ValueError(f"invalid C64 address: {address:#x}")
        if not 0 <= value <= 0xFF:
            raise ValueError(f"invalid byte expectation at {address:#06x}: {value}")
        if address not in observation.memory:
            raise QualificationUnavailable(
                f"backend did not observe required address {address:#06x}"
            )
        actual = observation.memory[address]
        mask = masks.get(address, 0xFF)
        if not 0 <= mask <= 0xFF:
            raise ValueError(f"invalid mask at {address:#06x}: {mask}")
        if (actual & mask) != (value & mask):
            raise AssertionMismatch(
                f"{address:#06x}: expected {value:#04x}, observed {actual:#04x}, mask {mask:#04x}"
            )


def require_state_backend(backend=None):
    if backend is None:
        raise QualificationUnavailable(
            "no qualified machine-readable VICE state backend is configured; "
            "emulator_state must remain false"
        )
    if not callable(getattr(backend, "observe", None)):
        raise QualificationUnavailable("configured state backend has no observe()")
    return backend


def qualify(
    prg: Path,
    expected_memory: dict[int, int] | None = None,
    profile=MachineProfile(),
    backend: StateBackend | None = None,
):
    if not prg.is_file():
        raise FileNotFoundError(prg)
    binary = find_vice(profile.emulator)
    version = vice_version(binary)
    state_backend = require_state_backend(backend)
    observation = state_backend.observe(binary=binary, prg=prg, profile=profile)
    if not isinstance(observation, MachineObservation):
        raise QualificationUnavailable(
            "state backend returned an invalid observation object"
        )
    assert_memory(observation, expected_memory or {})
    return {
        "emulator": binary,
        "version": version,
        "profile": profile,
        "backend": state_backend.name,
        "observation": observation,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("prg", type=Path)
    args = parser.parse_args()
    try:
        qualify(args.prg)
    except QualificationUnavailable as exc:
        raise SystemExit(f"UNAVAILABLE: {exc}")
