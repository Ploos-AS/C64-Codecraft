---
title: $D018 — locating screen and character data
course: 01-c64-machine
lesson: 06
level: beginner
prerequisites: [05-vic-banks]
labs: []
---

# $D018 — locating screen and character data

VIC-II register $D018 contains memory-pointer fields used to select the screen matrix and character or bitmap data within the current VIC bank.

For text modes:

- bits 4-7 select the screen matrix in 1 KiB steps within the 16 KiB bank;
- bits 1-3 select character data in 2 KiB steps.

Do not treat a $D018 value as a magic constant. Decode the fields and calculate the resulting VIC-relative locations.

## A useful mental model

First choose the 16 KiB VIC bank. Then use $D018 to choose important structures **inside that bank**.

This gives a two-stage address calculation:

**VIC bank base + $D018-selected offset**

The CPU still needs its own usable address mapping to write the data.

## Scene connection

**Why does a demo coder care about this?**

Relocating screens and charsets lets effects reserve memory deliberately, switch between prepared screens, use custom graphics and avoid collisions with music/code.

## Lab

Take several hypothetical $D018 values and decode screen/charset offsets. Combine them with different VIC bank bases and calculate the resulting absolute RAM locations.

## Checkpoint

You can explain the two-stage VIC memory selection: CIA2 chooses the 16 KiB bank; $D018 selects structures inside it.

## Next

We use this knowledge to design a real memory plan before writing a custom charset.
