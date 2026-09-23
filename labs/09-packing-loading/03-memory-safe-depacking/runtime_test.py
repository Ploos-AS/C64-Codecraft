#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'memory-safe-depacking.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected = bytes([0x00,0x30,0xff,0x37,0x00,0x40,0xff,0x47,0x00,0x08,0xff,0x0f,0x00,0xc0,0xff,0xcf])
actual = bytes(cpu.mem[0xc000:0xc000+len(expected)])
if actual != expected:
    raise SystemExit(f'RAM assertion failed: {actual.hex()} != {expected.hex()}')
print('03-memory-safe-depacking runtime PASS')
