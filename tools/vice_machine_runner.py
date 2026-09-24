#!/usr/bin/env python3
"""Fail-closed M0.2 VICE machine-runner prototype.

This module defines the machine-level qualification contract without pretending
that Debian's packaged VICE monitor already provides a qualified state API.
"""

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess


class QualificationUnavailable(RuntimeError):
    pass


@dataclass(frozen=True)
class MachineProfile:
    video: str = "PAL"
    model: str = "C64"
    emulator: str = "x64sc"


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


def require_state_backend():
    raise QualificationUnavailable(
        "no qualified machine-readable VICE state backend is configured; "
        "emulator_state must remain false"
    )


def qualify(prg: Path, profile=MachineProfile()):
    if not prg.is_file():
        raise FileNotFoundError(prg)
    binary = find_vice(profile.emulator)
    version = vice_version(binary)
    require_state_backend()
    return {"emulator": binary, "version": version, "profile": profile}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("prg", type=Path)
    args = parser.parse_args()
    try:
        qualify(args.prg)
    except QualificationUnavailable as exc:
        raise SystemExit(f"UNAVAILABLE: {exc}")
