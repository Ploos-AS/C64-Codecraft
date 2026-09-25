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

    @classmethod
    def memory_get_request(cls, start: int, end: int, request_id: int = 1) -> bytes:
        if not (0 <= start <= end <= 0xFFFF):
            raise ValueError("invalid memory range")
        body = struct.pack("<BHHBH", 0, start, end, 0, 0)
        return (
            bytes((cls.STX, cls.API_VERSION))
            + struct.pack("<II", len(body), request_id)
            + bytes((cls.MEM_GET,))
            + body
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
    """Small synchronous transport used by the qualified M0.2 backend."""

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

    def read_memory(self, start: int, end: int) -> bytes:
        request_id = 1
        request = ViceBinaryMonitorProtocol.memory_get_request(start, end, request_id)
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.settimeout(self.timeout)
                sock.sendall(request)
                header = self._recv_exact(sock, 12)
                body_len = struct.unpack_from("<I", header, 2)[0]
                body = self._recv_exact(sock, body_len)
        except (OSError, TimeoutError) as exc:
            raise QualificationUnavailable(
                f"VICE binary-monitor transport failed: {exc}"
            ) from exc
        return ViceBinaryMonitorProtocol.memory_get_response(
            header + body, request_id
        )


class ViceBinaryMonitorBackend:
    """Qualified VICE 3.9 binary-monitor transport for bounded memory reads."""

    name = "vice-binary-monitor"

    def __init__(
        self,
        expected_addresses=(0xD020, 0xD021),
        host="127.0.0.1",
        port=6502,
        startup_timeout=5.0,
        rom_dir=None,
    ):
        self.expected_addresses = tuple(expected_addresses)
        self.host, self.port = host, port
        self.startup_timeout = startup_timeout
        self.rom_dir = Path(rom_dir).resolve() if rom_dir is not None else None

    def observe(self, *, binary: str, prg: Path, profile: MachineProfile):
        if profile.video.upper() != "PAL":
            raise QualificationUnavailable(
                f"VICE binary backend currently qualifies PAL only, got {profile.video}"
            )
        if not self.expected_addresses:
            raise QualificationUnavailable("no memory addresses requested")
        start, end = min(self.expected_addresses), max(self.expected_addresses)
        command = [
            "xvfb-run", "-a", binary,
            "-binarymonitor",
            "-binarymonitoraddress", f"ip4://{self.host}:{self.port}",
            "-console",
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
                        f"{output[-1000:]}"
                    )
                try:
                    data = client.read_memory(start, end)
                    memory = {
                        address: data[address - start]
                        for address in self.expected_addresses
                    }
                    return MachineObservation(
                        memory=memory, stop_reason="binary-monitor-memory-read"
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


def assert_memory(observation: MachineObservation, expected: dict[int, int]):
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
        if actual != value:
            raise AssertionMismatch(
                f"{address:#06x}: expected {value:#04x}, observed {actual:#04x}"
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
