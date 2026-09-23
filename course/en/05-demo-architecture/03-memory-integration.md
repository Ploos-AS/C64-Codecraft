---
title: Integrate the memory map
course: 05-demo-architecture
lesson: 03
level: advanced
prerequisites: [02-frame-budget]
labs: [05.03-memory-integration]
---
# Integrate the memory map
Now place code and data together: main code, IRQ code, zero-page state, music/player, screen matrices, charset/DYCP data, sprite frames, tables and buffers.

For each region record:
- start/end;
- CPU visibility requirements;
- VIC-II visibility requirements;
- alignment;
- lifetime;
- whether ROM/I/O banking matters;
- ownership and overwrite rules.

Do not invent a universal Codecraft layout. The layout follows this part's constraints.

## Scene connection
**Why does a demo coder care about this?**
Memory layout can remove runtime copies, avoid conflicts and make timing easier. Architecture is already optimization.

## Lab
Produce a non-overlapping map and explain every alignment or bank choice.

## Next
We build an IRQ chain that reflects the frame plan.
