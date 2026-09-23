---
title: Coarse character scrolling
course: 01-c64-machine
lesson: 11
level: beginner
prerequisites: [10-character-animation]
labs: [coarse-scroll]
---

# Coarse character scrolling

A basic horizontal character scroll can move screen codes one cell at a time.

For a 40-column row, one approach is to copy cells 1..39 into 0..38 and insert a new character at the right edge.

```asm
    ldx #$00
shift:
    lda $0401,x
    sta $0400,x
    inx
    cpx #39
    bne shift
```

This is **coarse scrolling**: movement happens in 8-pixel character steps.

## Think about cost

The loop performs many reads, writes and branches. A real scroller also needs incoming text data, wrapping and usually colour handling.

Do not hide this work. Count it. Later smooth scrolling will combine VIC-II fine-scroll registers with occasional coarse screen updates.

## Scene connection

**Why does a demo coder care about this?**

The scroller is a scene staple and a perfect systems exercise: data stream, screen memory, timing, character graphics and later raster synchronization all meet here.

## Lab

Shift one row left by one character and insert a fixed screen code at the right. Then replace the fixed code with bytes from a message table.

## Checkpoint

You understand coarse scrolling and why smooth scrolling will need both hardware fine-scroll and memory updates.

## Next

Before fine scrolling, we meet the other major VIC-II object system: hardware sprites.
