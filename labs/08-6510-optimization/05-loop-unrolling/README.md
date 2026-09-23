# Lab 08.05 — Loop-unrolling tradeoff

## Goal
Compare a compact loop with an unrolled equivalent that copies the same eight bytes.

Record execution cost **and** code size. Then state which constraint would justify either version in a real part.

**Why does a demo coder care?** Unrolling can buy runtime at the cost of bytes, cache-of-thought complexity and maintainability; scene code chooses that trade deliberately.
