#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'loader-basics.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=128)
expected = {0xfb: 0, 0xfc: 0x00, 0xfd: 0x40, 0xfe: 1}
for addr, value in expected.items():
    if cpu.mem[addr] != value:
        raise SystemExit(f'assertion failed at {addr:04x}: {cpu.mem[addr]:02x} != {value:02x}')
if cpu.sp != 0xff:
    raise SystemExit(f'stack not restored: {cpu.sp:02x}')
print(f'09.05 runtime PASS ({cpu.instructions} instructions)')
