#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'reproducible-packing.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected = bytes([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3])
actual = bytes(cpu.mem[0xc000:0xc000+len(expected)])
if actual != expected:
    raise SystemExit(f'RAM assertion failed: {actual.hex()} != {expected.hex()}')
print('02-reproducible-packing runtime PASS')
