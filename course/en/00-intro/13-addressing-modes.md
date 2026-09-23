---
title: Addressing modes — same instruction, different source
course: 00-intro
lesson: 13
level: absolute-beginner
prerequisites: [12-first-colour-table]
labs: [addressing-modes]
---

# Addressing modes — same instruction, different source

## What you will learn

An addressing mode tells the CPU how to interpret an instruction's operand. You already know several forms; now we give the idea a name.

```asm
lda #$06       ; immediate: the value itself
lda $0400      ; absolute: read from this address
lda colours,x  ; absolute,X: base address plus X
```

The mnemonic is still `LDA`, but the source of the value is different.

## Why this matters

Addressing modes affect what code can express, its byte size and often its cycle cost. On the 6510 they are part of the programming model, not syntax sugar added by Codecraft.

## Scene connection

**Why does a demo coder care about this?**

Choosing an addressing mode can mean choosing between flexibility, bytes and cycles. Later, tight effects often depend on exactly which form of an instruction is used.

## Lab

For each example, identify whether the operand is a value, an address, or a base address modified by X. Assemble them and compare machine-code size.

## Checkpoint

You can explain what an addressing mode is and recognize immediate, absolute and absolute,X forms.

## Next

Next we visit a particularly valuable part of the address space: zero page.
