#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
cpu=CPU(mem=load_prg(Path(__file__).parent/'build'/'shifted-glyphs.prg'),pc=0x0810)
cpu.run(limit=128)
expected=bytes([60,102,102,126,102,102,102,0,30,51,51,63,51,51,51,0])
actual=bytes(cpu.mem[51200:51216])
if actual != expected:
    raise SystemExit(f'RAM mismatch: {actual.hex()} != {expected.hex()}')
print(f'03.08 runtime PASS ({cpu.instructions} instructions)')
