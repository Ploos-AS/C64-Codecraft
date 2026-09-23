#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'phase-shifted-sine.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
cpu.run(limit=256)
expected=bytes((8,13,15,13,8,3,1,3))
actual=bytes(cpu.mem[0xc000:0xc008])
if actual != expected or cpu.mem[0xfb] != 1:
    raise SystemExit(f'sine state mismatch: output={actual.hex()} phase={cpu.mem[0xfb]}')
print(f'03.06 runtime PASS ({cpu.instructions} instructions)')
