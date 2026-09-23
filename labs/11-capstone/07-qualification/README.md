# Lab 11.07 — Capstone qualification

## Goal
Prove the production against its declared target instead of relying on “works on my emulator”.

Build a qualification matrix covering:
- clean reproducible build,
- boot/start path,
- required PAL/NTSC targets,
- VICE configuration/version,
- real C64 hardware when available,
- memory/ZP ownership,
- IRQ/raster stability,
- SID/music continuity,
- loader and transitions,
- cold/warm/repeated runs where relevant.

Record failures as evidence, not as embarrassment. A limitation may be acceptable when it is explicit.

The starter writes a qualification bitmap to RAM. Each bit should correspond to documented evidence, not optimism.

**Why does a demo coder care?** A release is qualified against a target machine contract, not against the developer's memory of the last successful run.
