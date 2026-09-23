# Lab 08.07 — Undocumented-opcode qualification

## Goal
Learn how to qualify an undocumented opcode before allowing it into production code.

This starter intentionally uses only documented instructions. Your task is to select one opcode discussed in the lesson, verify its behaviour from reliable NMOS 6502/6510 references, then add a guarded experiment.

## Qualification record
For the chosen opcode, record:
- opcode byte and mnemonic used by your assembler,
- addressing mode,
- verified semantics and flags,
- cycle behaviour,
- known stable/common versus unstable/model-sensitive status,
- 64tass syntax/support,
- VICE result,
- real-hardware result when available,
- documented fallback using official opcodes.

Do not generalize from one undocumented opcode to the entire group.

**Why does a demo coder care?** Illegal/undocumented opcodes can save resources, but only when their exact hardware contract is understood.
