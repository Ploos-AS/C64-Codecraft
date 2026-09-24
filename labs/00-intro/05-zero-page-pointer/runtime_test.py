#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'zero-page-pointer.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
cpu.run(limit=128)
if cpu.mem[0xfb] != 0 or cpu.mem[0xfc] != 4:
    raise SystemExit(f'pointer mismatch: {cpu.mem[0xfc]:02x}{cpu.mem[0xfb]:02x}')
actual=bytes(cpu.mem[0x0400:0x0410])
if actual != bytes([1])*16:
    raise SystemExit(f'fill mismatch: {actual.hex()}')
print(f'00.05 runtime PASS ({cpu.instructions} instructions)')
