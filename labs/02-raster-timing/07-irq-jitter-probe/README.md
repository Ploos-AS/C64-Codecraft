# Lab 02.07 — IRQ jitter probe

## Goal
Observe why “IRQ happened on this raster line” does not automatically mean “handler work starts on the same horizontal cycle”.

This lab supplies a raster-polling baseline with a border marker. Use the lesson to compare that deterministic polling path with an IRQ-driven version and inspect entry variation in VICE.

## Challenge
Instrument your Course 02.03 IRQ experiment with the same border marker and compare repeated frames.

**Why does a demo coder care?** Stable effects require separating raster-line synchronization from exact horizontal-cycle synchronization.
