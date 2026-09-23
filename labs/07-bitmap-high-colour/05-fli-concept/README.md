# Lab 07.05 — FLI data and timing model

## Goal
Understand FLI as a coordinated stream of display-state changes, not as a magic graphics mode.

The starter builds a small per-band state table containing teaching screen-selection and colour values. It does **not** perform the cycle-sensitive VIC-II writes required by a real FLI implementation.

## Qualification notebook
For a real experiment, document:
- target VIC-II/video standard,
- bitmap and screen-memory layout,
- which registers change per raster region,
- badline/DMA interaction,
- exact write windows,
- visible side effects.

**Why does a demo coder care?** FLI buys additional colour freedom by spending timing, memory and display-state complexity.
