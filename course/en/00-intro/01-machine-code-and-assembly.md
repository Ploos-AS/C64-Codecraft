---
title: What are machine code and assembly?
course: 00-intro
lesson: 01
level: absolute-beginner
prerequisites: []
labs: []
---

# What are machine code and assembly?

You do not need previous programming, machine-code or assembly experience for this course.

## What you will learn

By the end of this lesson you should understand the difference between machine code and assembly language, what an assembler does, and why C64 Codecraft works close to the hardware.

## Why this matters on the C64

The C64's 6510 CPU executes machine-code instructions. Demo code gets much of its character from deliberately controlling the machine: memory, VIC-II graphics, SID sound and eventually exact timing.

Assembly gives us a readable way to describe those CPU instructions without hiding the machine.

## The idea

A CPU does not execute words such as `LDA` and `STA`. It executes numbers: bytes in memory that encode instructions and their operands.

For example, later you will meet:

```asm
lda #$06
sta $d020
```

Those two lines are assembly language. An assembler such as 64tass translates them into the bytes understood by the 6510.

Do not worry about `#$06` or `$d020` yet. We will introduce hexadecimal, registers, addresses and the instructions themselves before expecting you to use them.

## What the machine does

At the simplest level our workflow is:

1. We write assembly source.
2. 64tass converts it to machine code.
3. The machine code is loaded into a C64 or emulator.
4. The 6510 fetches and executes the instructions.
5. Those instructions can change memory and hardware.

VICE lets us observe this process without replacing the real C64 programming model.

## Bytes and cycles

Machine code is made of bytes. CPU instructions also take time to execute, measured in clock cycles.

Both will matter greatly in demo coding. For now, remember only that an instruction has a size and a time cost. We will learn how to reason about both gradually.

## Scene connection

**Why does a demo coder care about this?**

A demo is not merely a picture or animation produced by a high-level engine. Classic C64 effects often come from carefully chosen instructions interacting directly with the hardware, sometimes with individual cycles becoming important.

That journey starts here: understanding what code the 6510 is actually executing.

## Checkpoint

You should now be able to explain:

- machine code is the byte representation executed by the CPU;
- assembly is a human-readable representation of CPU instructions;
- an assembler translates assembly source into machine code;
- C64 Codecraft will expose rather than hide the C64 hardware;
- bytes and CPU cycles will become important as we progress.

## Next

Next we learn the small amount of binary and hexadecimal needed to read C64 code and addresses comfortably.
