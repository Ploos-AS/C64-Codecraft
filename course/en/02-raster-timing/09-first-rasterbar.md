---
title: Your first controlled rasterbar
course: 02-raster-timing
lesson: 09
level: intermediate
prerequisites: [08-stable-raster]
labs: [first-rasterbar]
---
# Your first controlled rasterbar
A rasterbar changes a colour register at controlled raster positions. The beginner version can change $D020 or $D021 across successive lines using a colour table.

Conceptually:

```asm
    ldx #$00
bar:
    lda colours,x
    sta $d020
    ; model-specific line synchronization/delay here
    inx
    cpx #bar_length
    bne bar
```

The omitted synchronization is deliberately not a fake universal delay. It belongs to the target-specific lab and must be cycle-accounted.

## Data and timing meet
The colour table defines the look. The timing code defines where the look appears. This separation lets art/data change without rewriting the synchronization core.

## Scene connection
**Why does a demo coder care about this?**
Rasterbars are simple enough to understand yet expose the defining C64 scene skill: changing hardware state while the beam is drawing the frame.

## Lab
Create a symmetric colour table, run it through the stable timing lab and verify that the bar remains fixed across frames.

## Next
One interrupt can schedule more than one visual region: raster splits.
