# Lab 02.02 — Raster-line wait

Wait for a chosen raster-line low byte and change the border. This is a teaching probe, not yet an IRQ or a cycle-stable effect.

The target is deliberately below 256 so this lab can focus on $D012 before combining it with the high raster bit.

Change TARGET and observe where the border transition moves.

**Why does a demo coder care?** Synchronization means waiting for machine state, not inserting unexplained delays.
