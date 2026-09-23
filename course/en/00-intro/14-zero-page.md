---
title: Zero page — valuable low memory
course: 00-intro
lesson: 14
level: absolute-beginner
prerequisites: [13-addressing-modes]
labs: [zero-page]
---

# Zero page — valuable low memory

Zero page is the first 256 addresses, `$0000-$00ff`. Because the high address byte is implicitly zero, many 6502/6510 instructions can encode zero-page accesses more compactly and often execute them faster than absolute accesses.

For example, conceptually compare:

```asm
lda $c000
lda $00f0
```

When the second operand is assembled using a zero-page form, the CPU needs only one address byte in the instruction.

## Important C64 reality

Zero page is not an empty scratchpad. The C64 system, KERNAL/BASIC environment and your own program may already have uses for locations there. In particular, `$00/$01` have special significance on the C64, including memory configuration through the 6510's integrated I/O port. Do not claim arbitrary zero-page addresses without understanding the environment.

## Scene connection

**Why does a demo coder care about this?**

Zero page is scarce, useful and fast. Serious C64 code deliberately allocates it for hot variables and pointers. Resource allocation becomes part of effect design.

## Lab

Compare the assembled bytes and documented cycles for equivalent zero-page and absolute accesses. Do not optimize blindly: explain what resource is being consumed.

## Checkpoint

You know the zero-page range, why it is special, and why its locations must be allocated deliberately.

## Next

Zero page becomes even more powerful when two bytes hold an address: a pointer.
