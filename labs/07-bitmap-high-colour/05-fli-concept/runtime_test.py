#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'fli-concept.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810); cpu.run(limit=128)
a=bytes(cpu.mem[0xc000:0xc008]); b=bytes(cpu.mem[0xc010:0xc018])
if a != bytes(range(8)) or b != bytes([0,6,14,3,1,3,14,6]): raise SystemExit(f'FLI model mismatch: {a.hex()} {b.hex()}')
print('07.05 runtime PASS')
