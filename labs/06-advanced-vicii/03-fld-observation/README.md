# Lab 06.03 — FLD preparation probe

## Goal
Prepare and observe the control state FLD techniques depend on without publishing an unverified cycle-sensitive write sequence.

The starter records $D011 and the current raster position. Use the lesson and VICE to study how vertical scroll/display state relates to badline timing.

## Qualification before implementing FLD
Document target VIC-II/video standard, exact raster position, $D011 state, badline assumptions and the measured write window.

**Why does a demo coder care?** FLD is controlled interference with VIC-II display timing; the assumptions are part of the effect.
