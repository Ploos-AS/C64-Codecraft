---
title: Build the part IRQ chain
course: 05-demo-architecture
lesson: 04
level: advanced
prerequisites: [03-memory-integration]
labs: [part-irq-chain]
---
# Build the part IRQ chain
Turn the raster plan into scheduled handlers.

One handler may service music and general frame state in a safe region. Another may prepare a stable rasterbar. Another may change $D016 or other display state for the scroller region.

Each handler has an explicit job, budget and next raster target.

Keep ownership clear: who acknowledges the VIC-II source, who schedules the next line, and which registers/state must survive each call.

## Scene connection
**Why does a demo coder care about this?**
An IRQ chain is the timeline controller of many classic demo parts. Good structure makes cycle-critical code easier to reason about.

## Lab
Implement the chain first with border colours marking each handler. Add real effect work only after the schedule is visibly correct.

## Next
We attach music cues to part state rather than scattering special cases through IRQ code.
