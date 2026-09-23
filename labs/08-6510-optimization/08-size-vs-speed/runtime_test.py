#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'size-vs-speed.prg'
cpu = CPU(mem=load_prg(prg), pc=0x0810)
cpu.run(limit=512)
expected = bytes(range(1,9))
if bytes(cpu.mem[0xc000:0xc008]) != expected: raise SystemExit('compact copy assertion failed')
if bytes(cpu.mem[0xc010:0xc018]) != expected: raise SystemExit('expanded copy assertion failed')
if cpu.sp != 0xff: raise SystemExit(f'stack not restored: {cpu.sp:02x}')
print(f'08.08 runtime PASS ({cpu.instructions} instructions)')
