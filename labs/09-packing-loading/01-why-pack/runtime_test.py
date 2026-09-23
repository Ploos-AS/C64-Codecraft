#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'why-pack.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=64)
if cpu.mem[0xc000] != 0x55: raise SystemExit(f'payload assertion failed: {cpu.mem[0xc000]:02x}')
print(f'09.01 runtime PASS ({cpu.instructions} instructions)')
