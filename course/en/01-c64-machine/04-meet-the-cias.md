---
title: Meet CIA1 and CIA2
course: 01-c64-machine
lesson: 04
level: beginner
prerequisites: [03-vic-ii-register-map]
labs: []
---

# Meet CIA1 and CIA2

The C64 contains two 6526 Complex Interface Adapters.

CIA1 is mapped at $dc00-$dc0f and is heavily involved in keyboard/joystick I/O and timers. CIA2 is mapped at $dd00-$dd0f and participates in serial/user-port functions, timers and selection of the VIC-II's 16 KiB memory bank.

Each CIA contains I/O ports, two timers, a time-of-day clock and interrupt-control facilities.

## Do not conflate timers with raster timing

CIA timers can generate interrupts and provide useful timing, but VIC-II raster position is a different hardware timeline. Later demo code may deliberately use or disable different interrupt sources depending on the effect.

## Scene connection

**Why does a demo coder care about this?**

CIA2 affects which 16 KiB bank VIC-II sees. CIA timers and interrupt sources also matter when taking control of a machine that normally has KERNAL-managed interrupts running.

## Lab

Locate the CIA1/CIA2 register blocks and identify port A/B, timer registers and interrupt-control register in reference documentation. Find the CIA2 port bits associated with VIC bank selection, but do not change them blindly yet.

## Checkpoint

You know there are two CIAs, where they are mapped, their broad responsibilities, and why CIA2 matters to VIC-II memory selection.

## Next

Next we combine CPU banking, VIC banking and memory placement into a practical scene-oriented memory plan.
