#!/usr/bin/env python3
"""Contract tests for the fail-closed M0.2 VICE runner."""

from pathlib import Path
import sys
import tempfile
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
    qualify,
    require_state_backend,
    ViceMonitorTranscriptBackend,
    ViceBinaryMonitorProtocol,
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


class ContractBackend:
    name = "contract-test"

    def observe(self, *, binary, prg, profile):
        if binary != "/usr/bin/x64sc" or profile.video != "PAL":
            raise SystemExit("runner did not pass backend context")
        return observed


with tempfile.TemporaryDirectory() as tmp:
    prg = Path(tmp) / "lab.prg"
    prg.write_bytes(b"\x01\x08")
    with patch("vice_machine_runner.find_vice", return_value="/usr/bin/x64sc"), patch(
        "vice_machine_runner.vice_version", return_value="VICE 3.9"
    ):
        result = qualify(
            prg,
            expected_memory={0xD020: 0x05, 0xD021: 0x00},
            backend=ContractBackend(),
        )
        if result["backend"] != "contract-test" or result["observation"] != observed:
            raise SystemExit("backend integration result changed unexpectedly")

transcript = """
>D000:D020 05 00 12 34
C:D800: 01 02 03 04
"""
parsed = ViceMonitorTranscriptBackend.parse_memory(transcript)
if parsed[0xD020] != 0x05 or parsed[0xD021] != 0x00 or parsed[0xD800] != 0x01:
    raise SystemExit("VICE monitor transcript parser produced wrong memory state")

try:
    ViceMonitorTranscriptBackend.parse_memory("monitor prompt only")
except QualificationUnavailable:
    pass
else:
    raise SystemExit("empty monitor transcript did not fail closed")

request = ViceBinaryMonitorProtocol.memory_get_request(0xD020, 0xD021, 0x12345678)
expected_body = bytes((0x01, 0x20, 0xD0, 0x21, 0xD0, 0x00, 0x00, 0x00))
expected_request = (
    bytes((0x02, 0x02, 0x08, 0x00, 0x00, 0x00))
    + bytes((0x78, 0x56, 0x34, 0x12, 0x01))
    + expected_body
)
if request != expected_request:
    raise SystemExit(f"VICE memory-get packet changed unexpectedly: {request.hex()}")

response = (
    bytes((0x02, 0x02, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00))
    + bytes((0x78, 0x56, 0x34, 0x12))
    + bytes((0x02, 0x00, 0x05, 0x00))
)
if ViceBinaryMonitorProtocol.memory_get_response(response, 0x12345678) != b"\x05\x00":
    raise SystemExit("VICE memory-get response decoded incorrectly")

for broken in (response[:8], response[:-1], response[:7] + b"\x81" + response[8:]):
    try:
        ViceBinaryMonitorProtocol.memory_get_response(broken, 0x12345678)
    except QualificationUnavailable:
        pass
    else:
        raise SystemExit("malformed VICE binary response did not fail closed")

print(
    "VICE machine-runner contract tests: PASS "
    "(profile, binary, assertions, fail-closed state, backend integration)"
)
