---
title: Fill a screen row
course: 00-intro
lesson: 17
level: absolute-beginner
prerequisites: [16-screen-and-colour-ram]
labs: [screen-row]
---

# Fill a screen row

A normal C64 text row has 40 cells. X can therefore index a simple row-writing loop.

```asm
    ldx #$00
loop:
    lda #$01
    sta $0400,x
    lda #$07
    sta $d800,x
    inx
    cpx #40
    bne loop
```

This writes the same screen code and colour to the first 40 cells.

## What you are learning

The important step is not the repeated character. You are mapping an index to related locations in two different memory regions.

X selects cell N in both screen RAM and colour RAM.

## Bytes and cycles

The loop repeats useful work but pays loop overhead on every cell. Later we will compare compact loops with unrolled code when speed becomes more important than size.

## Scene connection

**Why does a demo coder care about this?**

Screen rows are natural building blocks for scrollers, text effects and character-based graphics. The same index can coordinate multiple streams of effect data.

## Lab

Change the character and colour. Then use `TXA` as the screen value and observe how the row changes. Predict the final value of X.

## Checkpoint

You can use indexed absolute stores to operate on corresponding screen and colour cells.

## Next

Next the data itself changes per cell: a table-driven row.
