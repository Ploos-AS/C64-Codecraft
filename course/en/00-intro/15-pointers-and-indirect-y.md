---
title: Pointers and indirect indexed addressing
course: 00-intro
lesson: 15
level: absolute-beginner
prerequisites: [14-zero-page]
labs: [00.06-indirect-indexed]
---

# Pointers and indirect indexed addressing

## What you will learn

A pointer is data that contains an address. On the 6510, a two-byte zero-page pointer can be combined with Y to reach data indirectly.

Conceptually:

```asm
ptr = $f0

    lda #<$0400
    sta ptr
    lda #>$0400
    sta ptr+1

    ldy #$00
    lda (ptr),y
```

`<` asks the assembler for the low byte of an address; `>` asks for the high byte. With `ptr=$0400` and Y=0, `LDA (ptr),Y` reads from `$0400`.

## Why pointers matter

A hard-coded address fixes the routine to one location. A pointer lets data choose the location while the same routine stays unchanged.

Indirect,Y is especially useful for walking through buffers and data whose base address is chosen at runtime.

## Bytes and cycles

`LDA (zp),Y` is 2 bytes and normally 5 cycles, plus a cycle when the effective read crosses a page boundary.

Again, flexibility has a timing cost that we can reason about.

## Scene connection

**Why does a demo coder care about this?**

Pointers let reusable routines operate on different screens, buffers, tables and effect data. They also expose a classic 8-bit trade-off: more flexible addressing versus tighter fixed-address code.

## Lab

Point at a known byte, read it through `(ptr),Y`, then increment Y and read the next byte. Move the pointer to different data without changing the read loop.

## Checkpoint

You understand a 16-bit pointer, low/high address bytes, zero-page pointer storage and `(zp),Y`.

## Next

We now have enough addressing knowledge to work with C64 screen RAM and colour RAM rather than only a single VIC-II register.
