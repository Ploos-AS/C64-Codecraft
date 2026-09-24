#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'asset-pipeline.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810); cpu.run(limit=128)
bitmap=bytes([0x18,0x3c,0x7e,0xff,0xff,0x7e,0x3c,0x18])
screen=bytes([0x16,0x26,0x36,0x46,0x56,0x66,0x76,0x86])
if bytes(cpu.mem[0x2000:0x2008]) != bitmap or bytes(cpu.mem[0x0400:0x0408]) != screen:
    raise SystemExit('asset pipeline RAM mismatch')
print('07.03 runtime PASS')
