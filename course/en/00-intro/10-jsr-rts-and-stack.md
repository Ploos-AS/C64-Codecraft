---
title: JSR, RTS and the stack
course: 00-intro
lesson: 10
level: absolute-beginner
prerequisites: [09-first-colour-loop]
labs: [first-subroutine]
---

# JSR, RTS and the stack

## What you will learn

You will learn how to put a useful piece of code in a subroutine, call it with `JSR`, return with `RTS`, and understand the stack's role without needing to master it yet.

## The idea

```asm
    lda #$06
    jsr set_border
    rts

set_border:
    sta $d020
    rts
```

`JSR` transfers execution to a subroutine. The CPU keeps return information on its stack. `RTS` uses that information to continue after the call.

The 6502/6510 stack lives in page 1, `$0100-$01ff`, and the 8-bit stack pointer selects a position within that page.

## Bytes and cycles

`JSR absolute` is 3 bytes / 6 cycles. `RTS` is 1 byte / 6 cycles.

A subroutine can make source clearer and avoid duplicated code, but calls are not free. Later demo code will deliberately choose between calls, inline code and unrolled code.

## Scene connection

**Why does a demo coder care about this?**

Real demos need structure: initialization, music play routines, effect updates, drawing and transitions. Subroutines help organize them. Timing-critical inner loops may later avoid JSR/RTS overhead. Both choices are tools.

## Lab

Move a border write into a subroutine. Single-step the JSR and RTS in VICE and observe PC/SP if your monitor setup permits. Then call the routine with two different values in A.

## Checkpoint

You can explain subroutine, JSR, RTS, return information and the beginner role of the stack.

## Next

Next we stop hard-coding every value and learn to read data from tables.
