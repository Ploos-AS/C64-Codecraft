# Lab 08.06 — Self-modifying code

## Goal
Use self-modifying code deliberately: patch an operand in writable RAM, then execute the changed instruction.

The starter changes the immediate operand of `lda #$00` before calling the routine. Inspect the instruction bytes before and after the patch in VICE.

## Safety contract
Document:
- code must reside in writable/visible RAM,
- which operand bytes are patched,
- who owns the code region,
- when patching is allowed,
- whether interrupts can observe a half-updated state.

**Why does a demo coder care?** SMC can move work out of a hot path, but it replaces abstraction with an explicit memory/timing contract.
