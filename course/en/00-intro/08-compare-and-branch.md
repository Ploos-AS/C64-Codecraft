---
title: Compare, flags and branches
course: 00-intro
lesson: 08
level: absolute-beginner
prerequisites: [07-x-y-and-counters]
labs: []
---

# Compare, flags and branches

## What you will learn

You will learn how `CPX` compares X with a value, how the zero flag records equality, and how `BNE` can change program flow.

## Why this matters on the C64

Loops and decisions are essential for drawing, copying, animation, tables and almost every non-trivial effect.

## The idea

Consider:

```asm
cpx #$10
```

The CPU performs a comparison without replacing X. Among the resulting flags, the zero flag becomes set when X equals `$10`.

`BNE` means **Branch if Not Equal**. In practical terms after this comparison, it branches when the zero flag is clear.

```asm
loop:
    inx
    cpx #$10
    bne loop
```

This repeats until X reaches `$10`, assuming X had a suitable starting value.

## What the machine does

A branch does not call a hidden loop mechanism. It changes where the CPU continues execution. The program counter is redirected when the branch condition is true.

## Bytes and cycles

Conditional branches use relative addressing. A branch costs 2 cycles when not taken, normally 3 when taken, and one additional cycle if a taken branch crosses a page boundary.

You do not need to optimize page placement yet. Notice the important scene-coding fact: **control flow can change timing**.

## Scene connection

**Why does a demo coder care about this?**

Loops save code size, but their timing depends on branches. Later, when raster timing matters, a branch that takes a different path—or crosses a page—can shift hardware writes by a cycle. Beginner control flow grows directly into advanced timing work.

## Lab

Trace a loop beginning with X=`$0d` and ending at `$10`. Record X, whether equality is reached, and whether `BNE` is taken on every pass.

Then change the limit and predict the number of iterations.

## Checkpoint

You should be able to explain comparison, the zero flag, conditional branching and why branch timing is not always constant.

## Next

We combine X, a loop and VIC-II to make hardware state change repeatedly.
