---
title: Compose advanced VIC-II effects
course: 06-advanced-vicii
lesson: 07
level: advanced
prerequisites: [06-side-border-timing]
labs: [06.07-composing-vicii-tricks]
---
# Compose advanced VIC-II effects
A technique that works alone may fail when another effect changes DMA, register state or available cycles.

Treat each advanced effect as a timing contract:
- required entry phase;
- critical raster/cycle windows;
- VIC-II state assumptions;
- sprite/badline assumptions;
- registers and memory it owns;
- time it leaves for other work.

Compose contracts before composing code.

When two requirements conflict, change scheduling, representation or visual design. Do not hide the conflict with unexplained delays.

## Scene connection
**Why does a demo coder care about this?**
Advanced scene code is systems engineering under artistic constraints. The strongest trick is often the architecture that lets several simpler tricks coexist.

## Lab
Combine two previously qualified effects, update the frame budget, and document every changed timing assumption.

## Checkpoint
You can reason about VIC-II fetch/DMA behaviour, qualify model-sensitive tricks and integrate them without treating timing as magic.

## Next
The next block studies bitmap and high-colour techniques, including FLI-family concepts and their memory/timing trade-offs.
