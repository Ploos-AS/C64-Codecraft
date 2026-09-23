# Lab 06.05 — Opening-border qualification

## Goal
Build a controlled experiment for border-opening techniques without presenting one fragile register-write recipe as universal.

The starter waits for a fresh raster transition, snapshots $D011/$D016, and marks a short observation window with the border colour.

## Qualification notebook
Record:
- VIC-II/video standard,
- target raster line,
- $D011 and $D016 before the experiment,
- badline/sprite activity,
- exact instruction path and measured result.

Only after those assumptions are known should you introduce the control-register writes described in the lesson.

**Why does a demo coder care?** Border tricks depend on *when* VIC-II samples display-control state, not merely on writing a magic value.
