# Lab 04.06 — Music sync events

## Goal
Turn musical progress into explicit effect events rather than making graphics guess what the player is doing.

The teaching player increments a tick. A separate sync routine derives a coarse event every eight ticks and stores it at $c000. Visual code can consume that event independently.

## Modify
Change the event divisor and use the event value to select border colours or motion-table phases.

**Why does a demo coder care?** Strong demo sync comes from shared timing/state contracts between music and effects, not accidental visual timing.
