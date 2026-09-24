#!/usr/bin/env python3
"""Fail-closed M0.2 VICE machine-runner contract."""

from dataclasses import dataclass, field
from pathlib import Path
import re
import shutil
import subprocess
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
