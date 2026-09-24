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
    if 'C64 I/O access d020' not in str(exc):
        raise
else:
    raise SystemExit('C64 I/O fail-closed self-test failed')

io_read_mem = bytearray(65536)
io_read_mem[0:3] = bytes([0xad, 0x12, 0xd0])  # LDA $D012
try:
    CPU(mem=io_read_mem, pc=0).run(limit=1)
except RuntimeError as exc:
    if 'C64 I/O access d012' not in str(exc):
        raise
else:
    raise SystemExit('C64 I/O read fail-closed self-test failed')

# JSR/RTS must preserve an initially empty stack and resume after the call.
call_mem = bytearray(65536)
call_mem[0x0200:0x0207] = bytes([0x20, 0x06, 0x02, 0xa9, 0x2a, 0x60, 0x60])
call_cpu = CPU(mem=call_mem, pc=0x0200)
call_cpu.run(limit=8)
if call_cpu.a != 0x2a or call_cpu.sp != 0xff:
    raise SystemExit(f'JSR/RTS self-test failed: A={call_cpu.a:02x} SP={call_cpu.sp:02x}')

# DEX must wrap and set N/Z deterministically.
dex_mem = bytearray(65536)
dex_mem[0:4] = bytes([0xa2, 0x01, 0xca, 0x60])
dex_cpu = CPU(mem=dex_mem, pc=0)
dex_cpu.run(limit=4)
if dex_cpu.x != 0 or not (dex_cpu.p & 0x02) or (dex_cpu.p & 0x80):
    raise SystemExit(f'DEX self-test failed: X={dex_cpu.x:02x} P={dex_cpu.p:02x}')

# Indexed addressing into C64 I/O must also fail closed.
indexed_io = bytearray(65536)
indexed_io[0:5] = bytes([0xa2, 0x20, 0xbd, 0xf2, 0xcf])  # LDX #$20; LDA $CFF2,X -> $D012
try:
    CPU(mem=indexed_io, pc=0).run(limit=2)
except RuntimeError as exc:
    if 'C64 I/O read d012' not in str(exc):
        raise
else:
    raise SystemExit('indexed C64 I/O read fail-closed self-test failed')

indirect_io = bytearray(65536)
indirect_io[0:4] = bytes([0xa0, 0x12, 0xb1, 0xfb])  # LDY #$12; LDA ($FB),Y
indirect_io[0xfb] = 0x00
indirect_io[0xfc] = 0xd0
try:
    CPU(mem=indirect_io, pc=0).run(limit=2)
except RuntimeError as exc:
    if 'C64 I/O read d012' not in str(exc):
        raise
else:
    raise SystemExit('indirect C64 I/O read fail-closed self-test failed')

for addr in (0x0000, 0x0001):
    port_read = bytearray(65536)
    port_read[0x0200:0x0203] = bytes([0xad, addr & 0xff, 0x00])  # LDA $0000/$0001
    try:
        CPU(mem=port_read, pc=0x0200).run(limit=1)
    except RuntimeError as exc:
        if '6510 processor-port access' not in str(exc):
            raise
    else:
        raise SystemExit(f'6510 processor-port read {addr:04x} fail-closed self-test failed')

print('CPU/RAM harness self-tests: PASS (state, stack, flags, C64 I/O and 6510 port fail-closed)')
