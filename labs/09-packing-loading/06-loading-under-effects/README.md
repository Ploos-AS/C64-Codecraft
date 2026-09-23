# Lab 09.06 — Loading under effects

## Goal
Model loading as work that must coexist with an active effect and music.

The starter divides each teaching frame into three jobs: music, effect update and loader progress. It does not pretend to implement a real disk protocol.

## Qualification tasks
For a real loader, document:
- CPU time consumed per service opportunity,
- IRQ/NMI/CIA ownership,
- disk/device timing assumptions,
- destination memory,
- whether the visible effect touches that memory,
- music-player deadlines,
- failure/retry behaviour.

Then decide where loader service can safely run.

**Why does a demo coder care?** Loading under an effect is scheduling and resource arbitration, not simply calling LOAD in the background.
