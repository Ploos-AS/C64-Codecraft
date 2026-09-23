---
title: Your first data-driven colour effect
course: 00-intro
lesson: 12
level: absolute-beginner
prerequisites: [11-indexed-addressing-and-tables]
labs: [colour-table]
---

# Your first data-driven colour effect

## What you will learn

You will combine a table, indexed load, VIC-II write and loop.

```asm
    ldx #$00

loop:
    lda colours,x
    sta $d020
    inx
    cpx #colours_end-colours
    bne loop
    rts

colours:
    .byte $00,$06,$0e,$03,$01,$07

colours_end:
```

The assembler expression `colours_end-colours` gives the table length. The source therefore does not need a second hard-coded copy of the number of entries.

## What will you see?

As with the earlier colour loop, the writes happen extremely quickly. The important new idea is not a smooth visual effect yet: **code and effect data are now separate**.

Change the table and the same loop produces a different sequence.

## Bytes and cycles

`LDA colours,x` introduces a possible page-crossing timing penalty. The taken/not-taken `BNE` still makes the final iteration different.

We are accumulating exactly the timing facts that will matter when we later synchronize to the raster.

## Scene connection

**Why does a demo coder care about this?**

Data-driven effects are fundamental. A table can describe colours today and a sine wave, sprite movement or raster schedule later. Precalculation often trades memory for CPU time—one of the central C64 demo-coding decisions.

## Lab

Observe the sequence, modify only the table, deliberately shorten/extend it, and verify the assembler-derived length still follows the data.

**Challenge:** create a symmetric colour ramp in data without changing the loop.

## Checkpoint

You can build a small data-driven C64 routine using a label, table, indexed addressing, hardware write and loop.

## Next

Next we learn more addressing modes and zero page—the foundation for pointers, efficient data access and more serious effect code.
