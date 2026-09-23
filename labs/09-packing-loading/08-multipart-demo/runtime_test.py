#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg = Path(__file__).parent / 'build' / 'multipart-demo.prg'
mem = load_prg(prg)

def invoke(cpu, pc):
    cpu.pc = pc
    cpu.sp = 0xff
    cpu.run(limit=256)

# First invocation initializes the state machine then performs LOAD -> INIT.
cpu = CPU(mem=mem, pc=0x0810)
cpu.run(limit=256)
if (cpu.mem[0xfb], cpu.mem[0xfc], cpu.mem[0xfd]) != (1, 0, 0):
    raise SystemExit('initial LOAD -> INIT transition failed')

# Subsequent entry at step advances the persistent state machine.
step = 0x081c
invoke(cpu, step)  # INIT -> RUN
if (cpu.mem[0xfb], cpu.mem[0xfc], cpu.mem[0xfd]) != (2, 0, 0):
    raise SystemExit('INIT -> RUN transition failed')

for _ in range(15):
    invoke(cpu, step)
if (cpu.mem[0xfb], cpu.mem[0xfc], cpu.mem[0xfd]) != (2, 0, 15):
    raise SystemExit('RUN age progression failed')

invoke(cpu, step)  # age 16 -> EXIT
if (cpu.mem[0xfb], cpu.mem[0xfc], cpu.mem[0xfd]) != (3, 0, 16):
    raise SystemExit('RUN -> EXIT transition failed')

invoke(cpu, step)  # EXIT -> next part LOAD
if (cpu.mem[0xfb], cpu.mem[0xfc]) != (0, 1):
    raise SystemExit('EXIT -> next part transition failed')

print('09.08 runtime PASS (multipart state transitions)')
