---
title: Self-modifying code
course: 08-6510-optimization
lesson: 06
level: advanced
prerequisites: [05-loop-unrolling]
labs: [self-modifying-code]
---
# Self-modifying code
On the C64, code normally lives in writable RAM. A routine can therefore alter an operand or opcode in its own instruction stream.

A common disciplined use is patching the address operand of a hot load/store so runtime pointer handling disappears from the repeated path.

Self-modifying code is not automatically faster or better. It exchanges setup writes and complexity for a simpler hot path.

## Make modification obvious
Label patch sites, document who writes them and when, and ensure code is writable/visible under the current banking setup. Avoid hidden modifications that make debugging impossible.

## Scene connection
**Why does a demo coder care about this?**
SMC is a legitimate 6502-family optimization technique when its trade-off is measured and its timing advantage matters.

## Lab
Replace one indirect hot-path access with an explicitly patched absolute operand. Compare setup cost, repeated cost, bytes and readability.

## Next
We examine undocumented opcodes with the same evidence standard.
