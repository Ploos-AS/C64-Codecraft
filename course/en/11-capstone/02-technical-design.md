---
title: Technical design
course: 11-capstone
lesson: 02
level: capstone
prerequisites: [01-concept-and-scope]
labs: [11.02-technical-design]
---
# Technical design
Create the engineering maps before the production grows.

Document:
- global memory map and resident regions;
- per-part memory ownership;
- zero-page ownership;
- VIC-II banks and display data;
- IRQ/raster schedule;
- music init/play/cue contract;
- loader/depacker plan if multipart;
- frame budgets for critical regions;
- transition entry/exit state.

Mark assumptions that are not yet proven.

## Risk order
Prototype the highest-risk mechanism early. A stable raster trick, loader constraint or memory collision discovered at the end is much more expensive to fix.

## Gate
Every major part has a feasible memory/timing contract and each major technical risk has a planned experiment.

## Next
Build the smallest end-to-end skeleton.
