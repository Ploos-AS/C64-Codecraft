# Lab 06.06 — Side-border timing probe

## Goal
Measure horizontal timing before attempting a side-border trick.

A raster-line transition establishes a coarse line reference. A tunable delay then moves a border-colour marker horizontally. Change `DELAY` and inspect the marker in VICE.

This is deliberately **not** claimed to open the side border. Polling gives line-level synchronization, not a stable cycle position.

## Challenge
Replace the coarse entry with the stable-raster method you qualified earlier, then document the target VIC-II/video standard before experimenting with $D016 timing.

**Why does a demo coder care?** Side-border techniques expose the difference between choosing a raster line and controlling an exact horizontal cycle.
