#!/usr/bin/env python3
"""Self-tests for the deterministic CPU/RAM harness."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from cpu6502_harness import CPU, load_prg

LAB = ROOT / 'labs/09-packing-loading/07-part-contracts'
mem = load_prg(LAB / 'build/part-contracts.prg')
cpu = CPU(mem=mem, pc=0x0810)
cpu.run(limit=200)

expected = bytes([0x00,0x40,0x00,0x40,0x00,0x40,0xff,0x5f,0x00,0x60,0x00,0x60,0x00,0x60,0xff,0x7f])
actual = bytes(cpu.mem[0xc000:0xc010])
if actual != expected:
    raise SystemExit('positive harness self-test failed')

wrong = bytearray(expected)
wrong[0] ^= 0xff
if actual == bytes(wrong):
    raise SystemExit('negative assertion self-test failed to detect mismatch')

try:
    CPU(mem=bytearray([0x02]) + bytearray(65535), pc=0).run(limit=1)
except RuntimeError as exc:
    if 'unsupported opcode' not in str(exc):
        raise
else:
    raise SystemExit('unsupported-opcode fail-closed self-test failed')

io_mem = bytearray(65536)
io_mem[0:3] = bytes([0x8d, 0x20, 0xd0])  # STA $D020
try:
    CPU(mem=io_mem, pc=0, a=1).run(limit=1)
except RuntimeError as exc:
    if 'C64 I/O write d020' not in str(exc):
        raise
else:
    raise SystemExit('C64 I/O fail-closed self-test failed')

print('CPU/RAM harness self-tests: PASS (positive, negative assertion, fail-closed opcode/I/O)')
