#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg

prg=Path(__file__).parent/'build'/'playback-rate-model.prg'

def run_case(frame, tick, policy):
    cpu=CPU(mem=load_prg(prg),pc=0x0810)
    cpu.mem[0xfb]=frame; cpu.mem[0xfc]=tick; cpu.mem[0xfd]=policy
    cpu.run(limit=64)
    return cpu.mem[0xfb],cpu.mem[0xfc]

cases=[
    ((0,0,0),(1,1)),
    ((0,0,1),(1,0)),
    ((1,0,1),(2,1)),
]
for args,expected in cases:
    actual=run_case(*args)
    if actual != expected:
        raise SystemExit(f'playback model mismatch {args}: {actual} != {expected}')
print('04.05 runtime PASS (three playback-policy cases)')
