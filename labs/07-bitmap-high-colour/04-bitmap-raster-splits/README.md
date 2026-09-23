# Lab 07.04 — Bitmap raster-split model

## Goal
Model a display as regions with different VIC-II state.

Two raster positions select two teaching colour states. Polling keeps the state change visible and inspectable; it is not claimed to be a production split or cycle-stable switch.

## Challenge
List every VIC-II register and memory-region dependency that a real bitmap/text or bitmap/bitmap split would need to own and restore.

**Why does a demo coder care?** Raster splits let one frame contain multiple display configurations, but every configuration has a timing and memory contract.
