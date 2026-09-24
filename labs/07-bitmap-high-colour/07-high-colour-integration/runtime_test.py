#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
from cpu6502_harness import CPU, load_prg
prg=Path(__file__).parent/'build'/'high-colour-integration.prg'
cpu=CPU(mem=load_prg(prg),pc=0x0810)
cpu.run(limit=128)
expected={0xfb:1,0xfc:1,0xfd:0,0xfe:0,0xc000:1,0xc010:0,0xc020:0}
for a,v in expected.items():
    if cpu.mem[a] != v:
        raise SystemExit(f'high-colour integration state mismatch at {a:04x}: {cpu.mem[a]:02x} != {v:02x}')
if cpu.sp != 0xff:
    raise SystemExit(f'stack not restored: {cpu.sp:02x}')
print(f'07.07 runtime PASS ({cpu.instructions} instructions)')
