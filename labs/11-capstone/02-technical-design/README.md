# Lab 11.02 — Capstone technical design

## Goal
Turn the production brief into explicit machine contracts.

Before integrating effects, document:
- memory map and banking,
- zero-page ownership,
- VIC-II/SID/CIA ownership,
- raster/IRQ schedule,
- music init/play contract,
- asset locations,
- loader/part plan,
- PAL/NTSC policy,
- debug/qualification strategy.

The starter emits a tiny state descriptor to RAM as a reminder that design decisions should become inspectable implementation state where useful.

**Why does a demo coder care?** Technical design is how individually valid effects are prevented from colliding later.
