#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'indirect-indexed.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
cpu.run(limit=128)
actual=bytes(cpu.mem[0x0400:0x0410])
expected=bytes(range(1,17))
if actual != expected:
    raise SystemExit(f'indirect copy mismatch: {actual.hex()}')
src=cpu.mem[0xfb] | (cpu.mem[0xfc] << 8)
if bytes(cpu.mem[src:src+16]) != expected:
    raise SystemExit(f'source pointer/data mismatch at {src:04x}')
print(f'00.06 runtime PASS ({cpu.instructions} instructions)')
