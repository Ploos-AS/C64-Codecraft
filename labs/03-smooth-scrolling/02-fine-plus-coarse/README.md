# Lab 03.02 — Fine plus coarse scrolling

## Goal
Combine the 0–7 VIC-II fine-scroll phase with a coarse one-character screen shift.

Each invocation decrements the fine phase. When it wraps, the top row shifts left by one character.

This remains manually invoked so the state transition is easy to inspect before raster scheduling.

**Why does a demo coder care?** A smooth scroller is two mechanisms coordinated by one state machine: pixel movement and character movement.
