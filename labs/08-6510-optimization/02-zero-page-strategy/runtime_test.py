#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'zero-page-strategy.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected = bytes(range(8,0,-1))
actual = bytes(cpu.mem[0xc000:0xc000+len(expected)])
if actual != expected:
    raise SystemExit(f'RAM assertion failed: {actual.hex()} != {expected.hex()}')
expected_state = {0xfa:1,0xfb:1}
for address, value in expected_state.items():
    if cpu.mem[address] != value:
        raise SystemExit(f'state assertion failed at {address:04x}')
print('02-zero-page-strategy runtime PASS')
