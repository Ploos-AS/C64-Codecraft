---
title: Your first hardware sprite
course: 01-c64-machine
lesson: 12
level: beginner
prerequisites: [11-character-scrolling]
labs: [first-sprite]
---

# Your first hardware sprite

The VIC-II provides eight hardware sprites. A standard monochrome sprite is 24 pixels wide by 21 pixels high and uses 63 bytes of bitmap data, conventionally stored in a 64-byte-aligned slot.

Sprite pointer bytes live at the end of the active 1 KiB screen matrix. A pointer selects a 64-byte block inside the current VIC bank.

To show sprite 0 you need, at minimum:

1. sprite bitmap data in VIC-visible memory;
2. sprite 0's pointer set correctly;
3. X/Y position registers configured;
4. sprite colour configured;
5. sprite 0 enabled.

Important registers include $d000/$d001 for sprite 0 position, $d015 for enable and $d027 for sprite 0 colour.

## Scene connection

**Why does a demo coder care about this?**

Sprites provide independently positioned graphics without rewriting the screen underneath them. They become building blocks for logos, objects, sprite scrollers and, later, multiplexing far beyond the nominal eight-sprite limit.

## Lab

Create a simple monochrome sprite shape, place it in a correctly aligned VIC-visible slot, calculate its sprite pointer, and display sprite 0. Move X/Y and change its colour.

## Checkpoint

You understand sprite data size, 64-byte slot/pointer addressing, the basic sprite registers and the steps required to display one sprite.

## Next

Next we move the sprite from a table and meet 9-bit X positioning.
