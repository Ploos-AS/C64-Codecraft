#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'fli-family.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810); cpu.run(limit=128)
a=bytes(cpu.mem[0xc000:0xc00c]); e=bytes([1,1,1,2,3,3,3,4,4,4,4,3])
if a != e: raise SystemExit(f'FLI family mismatch: {a.hex()}')
print('07.06 runtime PASS')
