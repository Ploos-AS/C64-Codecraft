---
title: Design a demo part
course: 05-demo-architecture
lesson: 01
level: advanced
prerequisites: [04-sid-music/06-music-sync]
labs: [part-design]
---
# Design a demo part
Before writing the integration code, define the part.

Our teaching part contains:
- SID music playback;
- a rasterbar region;
- a smooth scroller or compact DYCP region;
- sine-driven sprites;
- music cues that change visual state;
- an entry, running state and exit/transition.

Draw the frame vertically and mark where each visible region belongs. Then draw memory and CPU-time plans beside it.

## Scene connection
**Why does a demo coder care about this?**
The hard part of a demo is often not inventing one effect. It is making several effects coexist predictably.

## Lab
Produce three diagrams: screen/raster layout, memory map and frame-time plan.

## Next
We turn those diagrams into explicit budgets.
