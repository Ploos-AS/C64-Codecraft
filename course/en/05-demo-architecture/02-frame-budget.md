---
title: Build the frame budget
course: 05-demo-architecture
lesson: 02
level: advanced
prerequisites: [01-part-design]
labs: [05.02-frame-budget]
---
# Build the frame budget
List every recurring job and where it may execute: IRQ entry/exit, music play, rasterbar writes, scroller fine update, occasional coarse update, sprite movement and animation, cue handling and deferred preparation.

Measure worst relevant paths, not only the average frame. A coarse-scroll frame or animation update may cost more than an ordinary frame.

Reserve margin. A plan that works only when every path is best-case is fragile.

## Critical versus deferred
Put only position-sensitive work in the cycle-critical region. Move table preparation, message parsing and other flexible work to safe windows.

## Lab
Create a frame-budget table with measured or derived costs and identify the most constrained window.

## Next
We reconcile that schedule with the memory map.
