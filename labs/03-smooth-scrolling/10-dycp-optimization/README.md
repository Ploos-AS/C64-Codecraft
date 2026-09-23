# Lab 03.10 — DYCP optimization study

## Goal
Compare a general indexed loop with a deliberately specialized/unrolled data path.

Both paths copy eight prepared bytes to separate buffers. Use the cycle-counting appendix and VICE to compare instruction count, branches, code size and maintainability.

Do not declare one version universally “better”; record the tradeoff and the timing constraint that motivates it.

**Why does a demo coder care?** Scene optimization is measured specialization: cycles, bytes, memory layout and code complexity are exchanged deliberately.
