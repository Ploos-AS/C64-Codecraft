---
title: Indexed addressing and tables
course: 00-intro
lesson: 11
level: absolute-beginner
prerequisites: [10-jsr-rts-and-stack]
labs: [first-table]
---

# Indexed addressing and tables

## What you will learn

You will learn how a sequence of bytes can form a table and how X can select an entry with indexed addressing.

## The idea

```asm
    ldx #$00
    lda colours,x

colours:
    .byte $00,$06,$0e,$03
```

`colours,x` means: start at address `colours`, then add X to select a byte. If X is `$02`, A receives the third table entry, `$0e`.

A label such as `colours` is a name the assembler resolves to an address. It is not a runtime framework feature.

## Bytes and cycles

Absolute,X `LDA` is 3 bytes. It normally takes 4 cycles, with an additional cycle when the effective read crosses a page boundary.

This is our first direct encounter with data placement affecting timing.

## Scene connection

**Why does a demo coder care about this?**

Tables replace repeated calculations with prepared data. Colour sequences are a simple beginning; later the same idea becomes sine tables, sprite paths, raster values, animation frames and precalculated effect data.

## Lab

Create a four-byte colour table. Load each entry using X and predict A before stepping the instruction. Change the table without changing the code that reads it.

## Checkpoint

You understand labels as addresses, byte tables and indexed addressing with X.

## Next

We connect the table directly to VIC-II and build the first data-driven colour effect.
