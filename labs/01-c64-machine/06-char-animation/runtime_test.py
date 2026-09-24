#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'char-animation.prg'
cases=[(0,bytes([0x18]*8)),(1,bytes([0x00,0x18,0x18,0x7e,0x18,0x18,0x00,0x00])),(2,bytes([0x00,0x00,0x3c,0x7e,0x3c,0,0,0])),(3,bytes([0,0,0,0xff,0,0,0,0]))]
for frame,expected in cases:
    cpu=CPU(mem=load_prg(prg),pc=0x0810); cpu.mem[0xfb]=frame; cpu.run(limit=128)
    actual=bytes(cpu.mem[0xc800:0xc808])
    if actual!=expected or cpu.mem[0xfb] != ((frame+1)&0xff):
        raise SystemExit(f'frame {frame} mismatch: {actual.hex()} next={cpu.mem[0xfb]}')
print('01.06 runtime PASS')
