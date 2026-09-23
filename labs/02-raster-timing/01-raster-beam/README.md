# Lab 02.01 — Raster beam observation

Read the VIC-II raster position and make the moving beam observable without assuming a universal video standard.

The program samples $D012 into $c000 and records bit 7 of $D011 in $c001. Invoke it at different moments and inspect the samples.

**Why does a demo coder care?** Raster effects start by treating video position as changing hardware state, not as a delay-loop guess.
