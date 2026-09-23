---
title: Undocumented opcodes
course: 08-6510-optimization
lesson: 07
level: advanced
prerequisites: [06-self-modifying-code]
labs: [08.07-undocumented-opcodes]
---
# Undocumented opcodes
The NMOS 6510 has instruction encodings beyond the documented instruction set. Some have historically been used in C64 software and demos because a useful combined operation can save bytes or cycles.

They are not a free optimization tier. Behaviour and suitability differ between opcodes, CPU implementations and emulators, and some encodings are unsuitable for dependable code.

For each candidate:
1. document the operation and flags;
2. identify the target CPU assumption;
3. verify assembler syntax/support;
4. compare documented-instruction alternative;
5. test on qualified emulation and real hardware when possible;
6. use it only when the benefit matters.

## Scene connection
**Why does a demo coder care about this?**
Knowing undocumented instructions is part of understanding historical 6510 practice. Scene credibility also means knowing when *not* to use one.

## Lab
Evaluate one well-documented candidate against an ordinary instruction sequence. Record cycles, bytes, assumptions and test evidence before deciding whether the production may use it.

## Next
We separate speed optimization from sizecoding.
