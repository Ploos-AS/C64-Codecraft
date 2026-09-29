#!/usr/bin/env python3
from pathlib import Path

data = Path("/tmp/vice-loaded.bin").read_bytes()
needle = bytes.fromhex("a9068d20d0a90e8d21d060")
if needle not in data:
    raise SystemExit(f"expected machine-code state not found: {data.hex()}")
print("VICE M0.1 state smoke: PASS")
