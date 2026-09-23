#!/usr/bin/env python3
"""Discover and run every lab declaring verification.cpu_state: true."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / 'labs'

def cpu_state_enabled(meta):
    for line in meta.read_text(encoding='utf-8').splitlines():
        if line.strip() == 'cpu_state: true':
            return True
    return False

def main():
    tests = []
    for meta in sorted(LABS.glob('*/*/lab.yml')):
        if cpu_state_enabled(meta):
            test = meta.parent / 'runtime_test.py'
            if not test.exists():
                print(f'FAIL: {meta.relative_to(ROOT)} declares cpu_state=true without runtime_test.py')
                return 1
            tests.append(test)

    if not tests:
        print('CPU/RAM qualification: no opted-in labs')
        return 0

    for test in tests:
        rel = test.relative_to(ROOT)
        print(f'==> {rel}', flush=True)
        result = subprocess.run([sys.executable, str(test)], cwd=ROOT)
        if result.returncode:
            return result.returncode

    print(f'CPU/RAM qualification: PASS ({len(tests)} labs)')
    return 0

if __name__ == '__main__':
    sys.exit(main())
