# Lab 01.08 — First sprite

## Goal
Connect sprite data, its 64-byte block, the screen's sprite pointer table and VIC-II registers.

With the normal startup screen at $0400 and VIC bank 0, pointer $80 selects the sprite block at $2000. Sprite 0 is positioned and enabled.

Inspect $07f8 and explain the pointer calculation before modifying it.

**Why does a demo coder care?** Sprite pointers are memory-layout decisions, not magic constants.
