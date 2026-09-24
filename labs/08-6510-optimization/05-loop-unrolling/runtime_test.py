#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'loop-unrolling.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected = bytes([0x18,0x3c,0x7e,0xff,0xff,0x7e,0x3c,0x18])
looped = bytes(cpu.mem[0xc000:0xc000+len(expected)])
unrolled = bytes(cpu.mem[0xc010:0xc010+len(expected)])
if looped != expected:
    raise SystemExit(f'looped RAM assertion failed: {looped.hex()} != {expected.hex()}')
if unrolled != expected:
    raise SystemExit(f'unrolled RAM assertion failed: {unrolled.hex()} != {expected.hex()}')
print('05-loop-unrolling runtime PASS')
