#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'hires-bitmap-layout.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810); cpu.run(limit=128)
expected=bytes([0x3c,0x66,0xc3,0xc3,0xc3,0xc3,0x66,0x3c])
if bytes(cpu.mem[0x2000:0x2008]) != expected or cpu.mem[0x0400] != 0x16:
    raise SystemExit('hires bitmap layout mismatch')
print('07.01 runtime PASS')
