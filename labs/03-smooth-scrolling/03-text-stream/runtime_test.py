#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'text-stream.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
cpu.mem[0xfb]=0
cpu.run(limit=64)
if cpu.mem[0x0427] != 3 or cpu.mem[0xfb] != 1:
    raise SystemExit(f'text stream mismatch: char={cpu.mem[0x0427]:02x} index={cpu.mem[0xfb]}')
print(f'03.03 runtime PASS ({cpu.instructions} instructions)')
