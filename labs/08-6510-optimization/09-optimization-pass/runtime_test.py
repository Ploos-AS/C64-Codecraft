#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'optimization-pass.prg'
mem = load_prg(prg)
cpu = CPU(mem=mem, pc=0x0810)
cpu.run(limit=256)

expected = bytes((((v << 1) & 0xff) + 3) ^ 0x55 for v in range(16))
actual = bytes(cpu.mem[0xc000:0xc010])
if actual != expected:
    raise SystemExit(f'RAM assertion failed: {actual.hex()} != {expected.hex()}')
print(f'08.09 runtime PASS ({cpu.instructions} instructions)')
