---
title: X, Y and counters
course: 00-intro
lesson: 07
level: absolute-beginner
prerequisites: [06-sta-first-visible-result]
labs: []
---

# X, Y and counters

## What you will learn

You will learn how the X and Y registers can hold byte-sized values and why counters and indexes are useful.

## Why this matters on the C64

Demo code repeatedly walks through tables, screen positions, sprite data and effect state. X and Y are natural tools for this work.

## The idea

Like A, X and Y are 8-bit registers. Two direct ways to load them are:

```asm
ldx #$00
ldy #$10
```

X and Y can also be changed one step at a time:

```asm
inx
iny
dex
dey
```

An 8-bit register wraps around: incrementing `$ff` gives `$00`, and decrementing `$00` gives `$ff`.

## Smallest useful 6510 example

```asm
ldx #$00
inx
inx
```

After these instructions, X contains `$02`.

## What the machine does

`LDX` establishes the starting value. Each `INX` adds one modulo 256. These instructions also update zero and negative status flags, which soon let branches react to the result.

## Bytes and cycles

`LDX #value` is 2 bytes / 2 cycles. `INX` is 1 byte / 2 cycles.

Again, measure first. Optimization comes when there is a real constraint.

## Scene connection

**Why does a demo coder care about this?**

A counter can select the next colour, character, sprite coordinate or table entry. Later X and Y will index lookup and sine tables and help drive animation without expensive calculations.

## Lab

Use X as a paper counter from `$00` to `$05`. Predict each value before advancing it. Then start at `$fe` and observe the wrap through `$ff` to `$00`.

## Checkpoint

You should understand that X and Y are 8-bit registers, can act as counters/indexes, and wrap at byte boundaries.

## Next

A counter becomes much more useful when code can decide whether to continue. Next: comparisons, flags and branches.
