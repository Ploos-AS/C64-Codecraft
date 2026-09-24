#!/usr/bin/env python3
"""Contract tests for the fail-closed M0.2 VICE runner."""

from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from vice_machine_runner import (
    AssertionMismatch,
    MachineObservation,
    MachineProfile,
    QualificationUnavailable,
    assert_memory,
    find_vice,
    require_state_backend,
)

profile = MachineProfile()
if profile.video != "PAL" or profile.model != "C64" or profile.emulator != "x64sc":
    raise SystemExit("default machine profile changed unexpectedly")

with patch("shutil.which", return_value=None):
    try:
        find_vice()
    except QualificationUnavailable as exc:
        if "x64sc not found" not in str(exc):
            raise
    else:
        raise SystemExit("missing-emulator fail-closed test failed")

# First M0.2 target: Lab 00.03 must leave VIC-II border/background at $05/$00.
observed = MachineObservation(memory={0xD020: 0x05, 0xD021: 0x00}, stop_reason="rts")
assert_memory(observed, {0xD020: 0x05, 0xD021: 0x00})

try:
    assert_memory(observed, {0xD020: 0x06})
except AssertionMismatch:
    pass
else:
    raise SystemExit("intentional machine-state mismatch did not fail")

try:
    assert_memory(MachineObservation(memory={0xD020: 0x05}), {0xD021: 0x00})
except QualificationUnavailable as exc:
    if "did not observe required address" not in str(exc):
        raise
else:
    raise SystemExit("missing machine observation did not fail closed")

try:
    require_state_backend()
except QualificationUnavailable as exc:
    if "emulator_state must remain false" not in str(exc):
        raise
else:
    raise SystemExit("missing-state-backend fail-closed test failed")

print(
    "VICE machine-runner contract tests: PASS "
    "(profile, binary, positive/negative/missing-state assertions, backend)"
)
