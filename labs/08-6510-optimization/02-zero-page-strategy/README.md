# Lab 08.02 — Zero-page strategy

## Goal
Treat zero page as allocated shared infrastructure, not free scratch space.

The lab assigns named bytes for a pointer, phase and temporary value, then uses the pointer for an indirect-indexed copy.

## Exercise
Create a zero-page ownership table for music, effects, loader and transition code. Identify lifetime conflicts before optimizing access.

**Why does a demo coder care?** Zero page can improve important paths, but careless ownership makes integrated demos fragile.
