#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'char-scroll-data.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
for i in range(39):
    cpu.mem[0x0401+i]=i+1
cpu.run(limit=256)
expected=bytes(range(1,40))
actual=bytes(cpu.mem[0x0400:0x0427])
if actual != expected or cpu.mem[0x0427] != 1:
    raise SystemExit(f'char scroll mismatch: row={actual.hex()} tail={cpu.mem[0x0427]:02x}')
print(f'01.07 runtime PASS ({cpu.instructions} instructions)')
