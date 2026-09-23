#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'tables-precalc.prg'
mem = load_prg(prg)
cpu = CPU(mem=mem, pc=0x0810)
cpu.run(limit=64)

expected = {0x00fb: 3, 0xc000: 12, 0xc001: 12}
for address, value in expected.items():
    actual = cpu.mem[address]
    if actual != value:
        raise SystemExit(f'RAM assertion failed at {address:04x}: {actual:02x} != {value:02x}')
print(f'08.04 runtime PASS ({cpu.instructions} instructions)')
