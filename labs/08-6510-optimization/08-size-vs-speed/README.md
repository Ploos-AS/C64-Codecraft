# Lab 08.08 — Size versus speed

## Goal
Compare two implementations of the same result under different constraints.

The compact path loops over eight bytes. The speed-oriented teaching candidate is unrolled. Both produce inspectable output.

Measure:
- code bytes,
- data bytes,
- execution cycles for the tested path,
- integration consequences.

Then choose based on a stated production constraint rather than declaring a universal winner.

**Why does a demo coder care?** A 4K intro, a raster-critical routine and a loader do not optimize for the same thing.
