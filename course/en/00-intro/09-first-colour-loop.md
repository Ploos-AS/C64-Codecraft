---
title: Your first colour loop
course: 00-intro
lesson: 09
level: absolute-beginner
prerequisites: [08-compare-and-branch]
labs: [00.02-colour-loop]
---

# Your first colour loop

## What you will learn

You will combine a counter, transfer instruction, VIC-II store and branch into your first repeating hardware-oriented loop.

## The idea

```asm
    ldx #$00

loop:
    txa
    sta $d020
    inx
    cpx #$10
    bne loop
```

`TXA` transfers X into A. `STA $D020` then writes that value to the border-colour register.

The loop walks through sixteen values.

## What the machine does

Each iteration:

1. copies X to A;
2. writes A to `$D020`;
3. increments X;
4. compares X with `$10`;
5. branches back while X is not `$10`.

This is our first small effect loop built entirely from ordinary 6510 instructions and memory-mapped C64 hardware.

## What will you actually see?

The CPU is vastly faster than human vision. This loop changes the border values very quickly, so you should **not assume you will see sixteen clean colour steps**.

That mismatch between CPU speed, display timing and human perception is itself an important observation. Later we will synchronize effects to the VIC-II raster rather than using arbitrary delay loops.

## Bytes and cycles

Now the cycle count starts becoming interesting. Most iterations take the branch; the final one does not. Therefore even this tiny loop does not have identical control-flow timing on its last pass.

Count the instructions and cycles using the reference tables supplied by the course.

## Scene connection

**Why does a demo coder care about this?**

This tiny program already contains several ingredients of an effect: state, a changing value, a hardware write and repetition. But it lacks synchronization.

A demo coder does not merely ask, “does the value change?” The next questions become: **when does it change, how often, and where is the raster beam when it happens?**

Those questions eventually lead to raster bars and cycle-exact code.

## Lab

### Observe

Run the loop and compare what you expected with what VICE displays.

### Modify

Change the start value and loop limit.

### Break

Remove `TXA`. Explain why incrementing X no longer changes the value stored by `STA`.

### Debug

Single-step several iterations in the VICE monitor. Watch X, A and `$D020`.

### Optimize

Calculate the approximate cycle cost of one taken iteration. Do not optimize it yet.

### Challenge

Make the loop run backward through a range of colour values using the instructions already introduced.

## Checkpoint

You can now combine registers, transfer, hardware stores, increment, comparison and branching into a real C64 loop—and you have encountered the first reason timing matters.

## Next

Before building larger effects, we need reusable pieces of code: `JSR`, `RTS` and the stack.
