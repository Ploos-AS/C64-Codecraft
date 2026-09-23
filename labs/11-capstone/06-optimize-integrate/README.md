# Lab 11.06 — Optimize and integrate

## Goal
Optimize the integrated production against measured constraints.

Do not optimize isolated routines simply because they look slow. Start from the first playable and identify the actual failing budget: raster time, code size, memory overlap, loader window, music deadline or transition jitter.

## Pass
1. capture a baseline,
2. identify one constrained path,
3. change one thing,
4. re-measure,
5. regression-test neighbouring systems,
6. keep or revert,
7. update the technical design.

The starter exposes separate music/effect/transition jobs so their costs and ownership can be reasoned about independently.

**Why does a demo coder care?** The fastest effect is irrelevant if its optimization breaks music, loading or the next raster split.
