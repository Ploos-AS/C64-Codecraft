# Lab 02.06 — Border timing probe

## Goal
Turn a VIC-II colour register into a visual timing probe.

Wait for a chosen raster line, change the border before a small work block, then restore it. Compare variants in VICE rather than treating the pulse width as a universal cycle measurement.

## Modify
Add/remove instructions inside `work` and observe the horizontal edge movement.

**Why does a demo coder care?** A border probe makes timing visible and is a classic way to reason about where CPU work lands on the raster.
