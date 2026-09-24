#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
cpu=CPU(mem=load_prg(Path(__file__).parent/'build'/'release-craft.prg'),pc=0x0810)
cpu.run(limit=128)
expected=bytes([67,67,82,67,48,48,48,49])
actual=bytes(cpu.mem[0xc000:0xc000+len(expected)])
if actual != expected: raise SystemExit(f'RAM mismatch: {actual.hex()} != {expected.hex()}')
print('10.06 runtime PASS')
