---
title: A table-driven screen effect
course: 00-intro
lesson: 18
level: absolute-beginner
prerequisites: [17-fill-a-screen-row]
labs: [00.09-table-driven-screen]
---

# A table-driven screen effect

Now we combine the ideas learned so far: tables, indexing, loops and two C64 memory regions.

```asm
    ldx #$00
loop:
    lda chars,x
    sta $0400,x
    lda colours,x
    sta $d800,x
    inx
    cpx #data_end-chars
    bne loop
    rts

chars:
    .byte $01,$02,$03,$04,$05,$06,$07,$08

colours:
    .byte $02,$08,$07,$05,$0e,$04,$06,$01

data_end:
```

For a real project we would normally define and validate table lengths carefully rather than relying on a layout trick. The example is deliberately small so we can see the data-driven idea first.

## What changed?

The loop structure stays constant, but both character and colour now come from data. Effect design begins to move out of instruction sequences and into tables.

## Scene connection

**Why does a demo coder care about this?**

This pattern grows naturally into logos, animations, colour patterns and scrollers. Later, generated/precalculated tables let us move expensive work out of raster-critical code.

## Lab

Design an eight-cell pattern by editing only the two tables. Then deliberately make the tables disagree in length and explain why robust source should detect or prevent that.

### Challenge

Create a moving-looking gradient or symmetric pattern using data only. Do not add a framework or custom runtime.

## Checkpoint

You can coordinate multiple tables with one index and understand why data/code separation is useful for effects.

## Next

We are ready to leave the introductory block and study the C64 memory map and banking more systematically.
