# Lab 01.09 — Sprite 9-bit X position

## Goal
Treat sprite X as a 9-bit coordinate.

The low eight bits go to $D000. Sprite 0's ninth X bit is bit 0 of $D010. The example represents X=300 as low byte 44 plus the high bit.

Modify the coordinate on both sides of 255 and predict both registers first.

**Why does a demo coder care?** Motion code and multiplexers must update $D010 without damaging the high bits of other sprites.
