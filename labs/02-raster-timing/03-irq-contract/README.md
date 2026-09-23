# Lab 02.03 — Raster IRQ contract

Build the register setup for a VIC-II raster interrupt while keeping takeover details explicit.

This lab snapshots the current $D011 and IRQ vector bytes, then programs a raster compare below line 256 and enables VIC-II raster IRQ generation. It does **not** replace the system IRQ vector yet; the lesson and debugger are used to inspect the contract safely.

Inspect $D012, $D01A and the saved state at $c000-$c002.

**Why does a demo coder care?** IRQ code is a contract: source, mask, vector, acknowledgement and restoration all matter.
