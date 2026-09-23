---
title: VIC-II as a register block
course: 01-c64-machine
lesson: 03
level: beginner
prerequisites: [02-banking-00-01]
labs: [vic-register-map]
---

# VIC-II as a register block

You already know $d020. Now stop treating it as an isolated magic address.

With I/O mapped in, VIC-II registers occupy $d000-$d02e, mirrored through the VIC-II portion of the I/O area. Registers control sprite positions and enables, raster state, display modes, memory selection, colours, interrupts and more.

Examples you will meet repeatedly include:

- $d011: control register 1 and raster high-bit/display controls
- $d012: raster line low byte
- $d016: control register 2
- $d018: memory pointers
- $d019/$d01a: interrupt status/enable
- $d020: border colour
- $d021: background colour 0

Do not memorize the entire chip now. Learn to read the register map and understand individual bits when a lesson needs them.

## Scene connection

**Why does a demo coder care about this?**

VIC-II demo coding is register programming plus precise knowledge of when the chip reads memory and updates state. Raster effects, sprites, custom character sets and display tricks all grow from this map.

## Lab

Use a VIC-II register reference to locate border/background colour, raster line and interrupt registers. For each, identify whether you need to think about a whole byte or individual bits.

## Checkpoint

You now see $d020 as one member of a coherent VIC-II register interface.

## Next

The C64 has more than graphics hardware. Next we meet the two CIA chips and the timing/input jobs they perform.
