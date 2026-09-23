---
title: Technical design
course: 11-capstone
lesson: 02
level: capstone
prerequisites: [01-concept-og-scope]
labs: [capstone-design]
---
# Technical design
Lag engineering maps før produksjonen vokser.

Dokumenter:
- global memory map og resident regions;
- per-part memory ownership;
- zero-page ownership;
- VIC-II banks og display data;
- IRQ/raster schedule;
- music init/play/cue contract;
- loader/depacker plan hvis multipart;
- frame budgets for critical regions;
- transition entry/exit state.

Marker assumptions som ennå ikke er bevist.

## Risk order
Prototype mekanismen med høyest risiko tidlig. Et stable-raster-, loader- eller memory-collision-problem oppdaget på slutten er mye dyrere å rette.

## Gate
Hver major part har feasible memory/timing contract og hver større technical risk har planlagt experiment.

## Neste
Bygg minste end-to-end skeleton.
