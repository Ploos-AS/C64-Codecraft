---
title: FLI-family trade-offs
course: 07-bitmap-high-colour
lesson: 06
level: advanced
prerequisites: [05-fli-concept]
labs: [07.06-fli-family]
---
# FLI-family trade-offs
There is not one universal high-colour solution. FLI-related techniques and later variants make different compromises around colour freedom, visible artifacts, border behaviour, CPU availability, memory layout and converter support.

Names alone are not enough. For any chosen format document:
- exact target and display dimensions;
- colour constraints;
- memory footprint;
- raster routine requirements;
- CPU time left for music/effects;
- known visual artifacts;
- tool support and data format.

Do not choose a format merely because it is considered more advanced.

## Scene connection
**Why does a demo coder care about this?**
The best graphics mode is the one whose constraints fit the production. A technically impressive format can be the wrong architectural choice if it consumes the time needed by the rest of the part.

## Lab
Compare at least two documented bitmap/high-colour approaches using the same production requirements. Make a constraint matrix, not a winner ranking.

## Next
We integrate high-colour graphics with music and the rest of a demo part.
