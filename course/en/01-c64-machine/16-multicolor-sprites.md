---
title: Multicolor sprites
course: 01-c64-machine
lesson: 16
level: beginner
prerequisites: [15-sine-tables]
labs: [01.11-multicolor-sprite]
---

# Multicolor sprites

VIC-II sprites can operate in multicolor mode. Instead of interpreting each bitmap bit as one high-resolution pixel, pairs of bits select among four colour choices. Horizontal resolution is reduced, but more colours become available.

For sprites, two multicolor values are shared globally through $d025 and $d026, while each sprite also has its own colour register such as $d027 for sprite 0.

Sprite multicolor enable bits are controlled through $d01c.

## The trade

Monochrome sprite mode gives higher horizontal detail. Multicolor gives a richer palette at lower horizontal resolution.

This is not simply better versus worse. It is an artistic and technical choice.

## Scene connection

**Why does a demo coder care about this?**

C64 graphics are full of constrained choices. Good scene graphics exploit the exact hardware trade-offs rather than wishing them away.

Shared multicolors also mean sprites can be designed as a coordinated visual system.

## Lab

Convert a simple sprite from monochrome to multicolor. Identify each 2-bit pixel value, configure shared colours and the sprite-specific colour, and compare the visual result.

## Checkpoint

You understand the 2-bit multicolor sprite model, shared colours, per-sprite colour and the resolution trade-off.

## Next

We combine frames, movement and colour into an animated sprite object without inventing a runtime framework.
