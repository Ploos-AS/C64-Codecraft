# Lab 05.07 — Mini-demo qualification

## Goal
Integrate earlier course ideas into a small, inspectable demo-part architecture.

The starter combines:
- frame state,
- a tiny music-style tick,
- a phase-shifted motion lookup,
- raster-position scheduling,
- a visible transition cue.

It intentionally remains ordinary 6510 source rather than a Codecraft runtime.

## Qualification tasks
1. Build cleanly with 64tass.
2. Document memory and zero-page ownership.
3. Identify recurring work and its frame budget.
4. Replace at least one teaching stub with a technique from Courses 02–04.
5. Demonstrate a transition between two visible states.
6. Record PAL/NTSC assumptions instead of claiming universal cycle stability.

**Why does a demo coder care?** A demo is integration: independent effects, music, timing and transitions must share one machine without accidental conflicts.
