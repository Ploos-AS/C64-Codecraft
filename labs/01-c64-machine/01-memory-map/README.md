# Lab 01.01 — Memory map probe

Write known values to ordinary RAM and VIC-II registers, then inspect them in VICE.

## Goal
Distinguish an address from the device or memory currently visible there.

## Expected result
The border/background change and a marker byte is stored at $c000.

## Observe
Inspect $c000, $d020 and $d021. Explain why the same CPU address space can contain RAM, ROM or I/O depending on mapping.

**Why does a demo coder care?** Every later effect depends on knowing who owns an address and whether CPU/VIC-II can see the intended bytes.
