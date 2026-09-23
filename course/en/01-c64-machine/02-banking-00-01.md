---
title: Banking with $00 and $01
course: 01-c64-machine
lesson: 02
level: beginner
prerequisites: [01-memory-map]
labs: [banking-observation]
---

# Banking with $00 and $01

The 6510 differs from a plain 6502 by including a small I/O port. Its data-direction register is at $0000 and data register at $0001.

On the C64, low bits associated with LORAM, HIRAM and CHAREN participate in deciding whether BASIC ROM, KERNAL ROM, character ROM or I/O is visible in parts of the CPU address space.

This is **banking**: changing what a range of CPU addresses exposes without changing the 16-bit address itself.

## Be careful

$00/$01 are fundamental machine-configuration state, not casual scratch bytes. Changing them without understanding the current environment can hide ROM or I/O and break code that expects it.

Also distinguish CPU visibility from VIC-II memory access. The VIC-II has its own view and banking rules, which we study later.

## Scene connection

**Why does a demo coder care about this?**

Banking lets programs use RAM underneath ROM and control when I/O or character ROM is visible. This is valuable when fitting code, music, graphics and buffers into 64 KiB.

## Lab

In VICE, inspect $00/$01 in a normal environment. Use reference documentation to decode the relevant bits before changing anything. Predict which regions would change visibility for a proposed configuration.

## Checkpoint

You understand the role of $00/$01, the idea of LORAM/HIRAM/CHAREN, and why CPU banking is not the same as VIC-II banking.

## Next

With I/O visible, we map the VIC-II register block instead of memorizing isolated addresses.
