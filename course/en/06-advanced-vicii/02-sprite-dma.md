---
title: Sprite DMA and CPU time
course: 06-advanced-vicii
lesson: 02
level: advanced
prerequisites: [01-sprite-multiplexing]
labs: [sprite-dma-timing]
---
# Sprite DMA and CPU time
Visible sprites require VIC-II memory fetches. Those fetches compete with the CPU for bus time, so the CPU budget is not constant across a line when sprite DMA is active.

The exact schedule depends on VIC-II model and active sprite state. Do not memorize a universal "sprite costs N cycles" rule detached from its conditions.

For a multiplexer, this matters twice: sprites create the visual workload and can also reduce the CPU time available to prepare later sprites.

## Scene connection
**Why does a demo coder care about this?**
An effect can fail only when enough sprites are active because the machine's bus schedule changed underneath otherwise correct code.

## Lab
Measure the same timed routine with different active-sprite patterns on an explicit emulator model. Record where available CPU time changes.

## Next
We return to badlines and learn how vertical display timing can be manipulated.
