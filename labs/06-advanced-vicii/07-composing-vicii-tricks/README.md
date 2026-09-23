# Lab 06.07 — Composing VIC-II tricks

## Goal
Plan several VIC-II jobs as one frame instead of treating each trick as an isolated snippet.

The starter contains an explicit event table. Each record describes a raster line, a job identifier and a rough teaching budget class. The dispatcher records the selected job state; it does not pretend to be a cycle-exact IRQ engine.

## Integration exercise
For each event, document:
1. required raster line/window,
2. registers owned,
3. memory owned,
4. sprite/badline/DMA interaction,
5. music-player coexistence,
6. entry jitter tolerance,
7. restoration requirements.

Then decide which combinations can coexist on your chosen target.

**Why does a demo coder care?** Advanced effects become production-ready only when their timing and resource contracts compose.
