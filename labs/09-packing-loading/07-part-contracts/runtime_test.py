#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'part-contracts.prg'
mem = load_prg(prg)
cpu = CPU(mem=mem, pc=0x0810)
cpu.run(limit=200)

expected = bytes([0x00,0x40,0x00,0x40,0x00,0x40,0xff,0x5f,0x00,0x60,0x00,0x60,0x00,0x60,0xff,0x7f])
actual = bytes(cpu.mem[0xc000:0xc010])
if actual != expected:
    raise SystemExit(f'RAM assertion failed: {actual.hex()} != {expected.hex()}')
print(f'09.07 runtime PASS ({cpu.instructions} instructions)')
