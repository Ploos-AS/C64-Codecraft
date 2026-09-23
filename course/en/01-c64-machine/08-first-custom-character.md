---
title: Your first custom character
course: 01-c64-machine
lesson: 08
level: beginner
prerequisites: [07-demo-memory-plan]
labs: [01.04-custom-character]
---

# Your first custom character

In standard character mode, a character shape is an 8x8 bitmap stored as eight bytes: one byte per row.

For example:

```asm
my_char:
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11011011
    .byte %11111111
    .byte %00100100
    .byte %01011010
    .byte %10100101
```

Each bit controls a pixel in the monochrome character cell.

To display your own character set, place character data at a VIC-II-valid location, configure the appropriate VIC bank and $D018 character pointer, then place the corresponding screen code in the screen matrix.

## Why not hide this in a graphics API?

Because the relationship between bits, bytes, character addresses and VIC-II fetches is exactly what we want to learn. Conversion tools can come later without replacing that understanding.

## Scene connection

**Why does a demo coder care about this?**

Custom charsets turn text mode into a compact graphics system. They underpin logos, tile graphics, scrollers, animations and many classic demo effects while using far less data than a full bitmap.

## Lab

Draw an 8x8 pattern on paper, encode each row as a byte, place it in a custom charset and display it. Flip one bit and predict the changed pixel before running.

## Checkpoint

You understand that a monochrome character is eight bytes of bitmap data and how VIC bank/$D018/screen code connect to display it.

## Next

Next we expand from one character to a small custom charset and begin treating character graphics as effect assets.
