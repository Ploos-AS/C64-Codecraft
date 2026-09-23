---
title: Screen RAM and colour RAM
course: 00-intro
lesson: 16
level: absolute-beginner
prerequisites: [15-pointers-and-indirect-y]
labs: [00.07-screen-and-colour]
---

# Screen RAM and colour RAM

## What you will learn

You will learn how the normal C64 text screen is represented by character codes in screen RAM and colours in colour RAM.

With the normal startup layout, the text screen begins at `$0400` and colour RAM begins at `$d800`.

```asm
    lda #$01
    sta $0400

    lda #$07
    sta $d800
```

The first store selects the screen code for the first cell; the second selects that cell's foreground colour.

## An important distinction

Screen RAM does not contain pixels. In text mode it contains screen codes. VIC-II uses those codes to select character shapes from character data. Colour RAM supplies per-cell colour information.

This separation between **what character** and **what colour** is our first small taste of the C64 graphics architecture.

## Scene connection

**Why does a demo coder care about this?**

Text mode is not merely for text. Custom character sets, scrollers, logos and many effects build on the same screen/character machinery.

## Lab

Change the first few screen cells and their colours. Predict which address corresponds to the second and third cell.

## Checkpoint

You understand the basic roles of screen RAM and colour RAM and that screen codes are not pixel data.

## Next

We use indexed addressing to write a whole row instead of one cell.
