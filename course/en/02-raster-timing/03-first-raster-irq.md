---
title: Your first raster IRQ
course: 02-raster-timing
lesson: 03
level: intermediate
prerequisites: [02-d011-d012]
labs: [02.03-irq-contract]
---
# Your first raster IRQ
A VIC-II raster interrupt can request CPU attention at a programmed raster line.

The essentials are: install an IRQ handler appropriate to the execution environment; select the line through $D011/$D012; enable raster IRQ through $D01A; acknowledge the VIC-II source through $D019; preserve required machine state; and return correctly.

Exact vector setup differs between KERNAL-cooperative code and fuller machine takeover. We learn both rather than hide the difference behind a wrapper.

## Scene connection
**Why does a demo coder care about this?**
Raster IRQs schedule work relative to the beam without consuming the whole frame in polling. They underpin raster splits, music scheduling and many effects.

## Lab
Install a minimal raster IRQ in the documented lab environment and briefly change $D020 inside it. Use the border as a timing probe.

## Next
An IRQ reaches the right neighbourhood, not automatically the exact cycle. Now we count cycles.
