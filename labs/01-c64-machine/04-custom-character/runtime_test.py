#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
cpu=CPU(mem=load_prg(Path(__file__).parent/'build'/'custom-character.prg'),pc=0x0810)
cpu.run(limit=128)
expected=bytes([24,60,126,219,255,36,90,165])
actual=bytes(cpu.mem[51200:51208])
if actual != expected:
    raise SystemExit(f'RAM mismatch: {actual.hex()} != {expected.hex()}')
print(f'01.04 runtime PASS ({cpu.instructions} instructions)')
