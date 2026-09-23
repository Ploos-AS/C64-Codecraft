# Lab 07.02 — Multicolor bitmap data

## Goal
Read bitmap bytes as four 2-bit pixel groups rather than eight 1-bit pixels.

The program copies one 8-byte pattern to $2000 and stores teaching colour values separately. Use the lesson to identify which colour source each 2-bit value selects.

## Modify
Change one pair of bits at a time and predict which logical colour selector changes.

**Why does a demo coder care?** Multicolor graphics are encoded data plus several colour sources; understanding both is essential for converters and effects.
