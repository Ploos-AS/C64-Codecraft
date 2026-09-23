---
title: Line crunching
course: 06-advanced-vicii
lesson: 04
level: advanced
prerequisites: [03-fld]
labs: [line-crunch]
---
# Line crunching
Line-crunch effects deliberately interfere with VIC-II display sequencing at narrowly defined raster times.

Unlike ordinary scrolling, success depends on internal display timing state, not merely on writing a register sometime during a line. Implementations are therefore sensitive to model, cycle and surrounding DMA.

Codecraft treats line crunching as a hardware-timing experiment:
1. state the target;
2. explain the VIC-II state being influenced;
3. derive the required write window;
4. instrument it;
5. test sustained stability.

## Scene connection
**Why does a demo coder care about this?**
Line crunching shows the point where register programming becomes exploitation of the video chip's sequencing behaviour.

## Lab
Implement a minimal, documented target-specific crunch experiment before combining it with any other effect.

## Next
We move from vertical sequencing to the borders themselves.
