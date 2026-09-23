# Lab 04.01 — SID register map

## Goal
Meet SID as memory-mapped hardware before writing a player.

The program clears the writable SID register area used by the lesson, then sets the master volume nibble in $D418. Inspect the writes in VICE.

## Observe
Identify the register groups for the three voices and the global filter/volume controls.

**Why does a demo coder care?** Music playback is hardware state updated over time. Understanding the register map makes players less opaque.
