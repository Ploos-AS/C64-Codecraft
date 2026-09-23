---
title: STA and your first visible C64 result
course: 00-intro
lesson: 06
level: absolute-beginner
prerequisites: [05-lda-immediate]
labs: [first-border-colour]
---

# STA and your first visible C64 result

## What you will learn

You will learn how `STA` stores A to an address and combine it with `LDA` to control the VIC-II border colour.

## Why this matters on the C64

This is the point where CPU instructions become visibly connected to C64 hardware.

## The idea

`STA` means **STore Accumulator**.

```asm
lda #$06
sta $d020
```

The first instruction puts `$06` in A. The second writes A to address `$d020`.

With the normal C64 I/O mapping, `$d020` is the VIC-II border-colour register. The visible border therefore changes.

Notice the important difference:

- `#$06` means **the value $06**.
- `$d020` here means **the address $d020**.

## What the machine does

1. `LDA #$06`: A becomes `$06`.
2. `STA $D020`: the CPU writes `$06` to the VIC-II register at `$D020`.
3. VIC-II uses the low colour bits and the border appears blue.

No graphics framework is involved. You are controlling the C64 hardware through its memory-mapped register.

## Bytes and cycles

The pair assembles to:

```text
A9 06       ; LDA #$06 — 2 bytes, 2 cycles
8D 20 D0    ; STA $D020 — 3 bytes, 4 cycles
```

Total for these two instructions: **5 bytes and 6 CPU cycles**.

The address appears as `20 D0` in the instruction encoding. The 6502 family stores a 16-bit address operand low byte first. We will return to this little-endian convention when pointers and words need it.

## Scene connection

**Why does a demo coder care about this?**

You have just used the core mechanism behind a huge amount of C64 demo programming: calculate or choose a value, then write it to hardware at the right moment.

A static border colour is trivial. Repeated and precisely timed writes to VIC-II registers eventually become raster bars, splits and much more.

We are not jumping there yet—but the path has started.

## Lab

### Learn

Build a minimal program containing the two instructions using the course's ordinary 64tass workflow.

### Observe

Run it in VICE and observe the border. Inspect A and `$D020` with the VICE monitor if available in your local setup.

### Modify

Try another value from `$00` through `$0f`. Predict the colour before running.

### Break

Change the store address deliberately. Observe that loading A correctly is not enough; the destination matters.

### Debug

Check the assembled bytes. Find `A9 06 8D 20 D0` (or your modified colour value) and connect every byte back to the source.

### Optimize

Count the bytes and cycles. There is nothing useful to optimize yet; the purpose is to develop the measurement habit.

### Challenge

Set both border and background to deliberately chosen colours. Find the VIC-II background-colour address from the provided C64 reference material rather than inventing a Codecraft API.

## Checkpoint

You should be able to explain the difference between value and address, load A with an immediate value, store A to an absolute address, and describe why writing to `$D020` changes the border.

## Next

Next we make the CPU do something repeatedly: loops, counters and branches—the first step from a static register write toward animation and effects.
