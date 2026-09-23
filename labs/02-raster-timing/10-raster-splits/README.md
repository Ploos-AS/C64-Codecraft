# Lab 02.10 — Raster splits

## Goal
Change VIC-II presentation state at two distinct raster positions.

The teaching version uses polling and border/background colours so each split is obvious. It avoids pretending that polling is the final architecture for a real demo.

## Observe
Identify the state owned by the top, middle and bottom regions. Move SPLIT1/SPLIT2 and document what remains safe and what begins to depend on tighter timing.

## Challenge
Sketch the IRQ scheduler that would replace this polling structure in a production part.

**Why does a demo coder care?** Raster splits let one frame behave like several display regions with different hardware state.
