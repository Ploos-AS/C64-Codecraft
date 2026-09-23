# Lab 07.07 — High-colour integration contract

## Goal
Integrate high-colour graphics into the same frame that must also support music and effects.

The starter models three scheduled jobs: music, graphics-state update and transition/effect work. Each job writes only teaching state to RAM so the integration contract is visible before cycle-sensitive graphics code is inserted.

## Qualification tasks
1. Define bitmap/screen/colour memory ownership.
2. Define zero-page ownership.
3. Record every raster-critical write window.
4. Add sprite and music DMA/CPU considerations.
5. State PAL/NTSC and VIC-II assumptions.
6. Identify what can run outside critical windows.
7. Define restoration/transition state.

Then replace one teaching job at a time with qualified code.

**Why does a demo coder care?** A high-colour picture that works alone is only a test. A demo part must coexist with everything else in the frame.
