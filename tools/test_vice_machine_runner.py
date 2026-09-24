#!/usr/bin/env python3
"""Contract tests for the fail-closed M0.2 VICE runner."""

from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from vice_machine_runner import (
    MachineProfile,
    QualificationUnavailable,
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

try:
    require_state_backend()
except QualificationUnavailable as exc:
    if "emulator_state must remain false" not in str(exc):
        raise
else:
    raise SystemExit("missing-state-backend fail-closed test failed")

print("VICE machine-runner contract tests: PASS (profile, binary, state backend)")
