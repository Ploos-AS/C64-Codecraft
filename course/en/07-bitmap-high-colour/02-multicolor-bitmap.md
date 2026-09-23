---
title: Multicolor bitmap mode
course: 07-bitmap-high-colour
lesson: 02
level: advanced
prerequisites: [01-hires-bitmap]
labs: [multicolor-bitmap]
---
# Multicolor bitmap mode
Multicolor bitmap interprets pixel data in two-bit groups. This provides more colour selections within each 8x8 cell at the cost of horizontal resolution.

The available colour sources come from bitmap-associated screen data, colour RAM and a shared background colour. The exact bit-pair mapping should be treated as part of the display format and verified in the lab.

The key idea is that bitmap bytes alone do not describe the complete image.

## Scene connection
**Why does a demo coder care about this?**
C64 graphics formats are compromises between resolution, colour freedom, memory and timing. Multicolor bitmap makes those trade-offs explicit.

## Lab
Encode one 8x8 cell manually before using any converter. Account for every pixel pair and every colour source.

## Next
We turn those memory structures into a reproducible asset pipeline.
