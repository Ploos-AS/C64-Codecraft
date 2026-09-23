---
title: Part state and music cues
course: 05-demo-architecture
lesson: 05
level: advanced
prerequisites: [04-irq-chain]
labs: [05.05-part-state-and-cues]
---
# Part state and music cues
Keep musical events separate from low-level effect implementation.

A cue can update compact part state: active palette, sprite formation, scroller mode, rasterbar table, transition request. Effect code reads that state at safe points.

This avoids burying song-specific tests inside every raster-critical routine.

## State changes need timing too
Some state can change immediately. Other changes must be committed at a frame boundary or before a particular raster region. Define when a cue becomes visible.

## Scene connection
**Why does a demo coder care about this?**
A clean cue/state layer lets choreography evolve without destabilizing cycle-critical code.

## Lab
Use at least three music cues to change independent visual state and document when each change becomes active.

## Next
We add entry and exit transitions so the part has a lifecycle.
