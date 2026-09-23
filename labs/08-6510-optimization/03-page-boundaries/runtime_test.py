#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'page-boundaries.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected_state = {0xc000:0x11,0xc001:0x22}
for address, value in expected_state.items():
    if cpu.mem[address] != value:
        raise SystemExit(f'state assertion failed at {address:04x}')
print('03-page-boundaries runtime PASS')
