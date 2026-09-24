#!/usr/bin/env python3
"""Fail-closed M0.2 VICE machine-runner contract.

The runner keeps emulator transport separate from assertion semantics. A
backend may only return observations it can prove; missing observations fail
closed instead of being treated as zero/default state.
"""

from dataclasses import dataclass, field
from pathlib import Path
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
    """Machine-readable state returned by a qualified emulator backend."""

    memory: dict[int, int] = field(default_factory=dict)
    registers: dict[str, int] = field(default_factory=dict)
    stop_reason: str = ""


class StateBackend(Protocol):
    """Transport boundary for a qualified emulator-state implementation."""

    name: str

    def observe(
        self, *, binary: str, prg: Path, profile: MachineProfile
    ) -> MachineObservation:
        ...


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
    """Assert byte values while failing closed for unobserved addresses."""

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
