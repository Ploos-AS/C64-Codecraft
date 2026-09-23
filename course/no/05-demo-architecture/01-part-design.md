---
title: Design en demo-part
course: 05-demo-architecture
lesson: 01
level: advanced
prerequisites: [04-sid-music/06-music-sync]
labs: [part-design]
---
# Design en demo-part
Før integration code skrives definerer vi parten.

Teaching-parten inneholder:
- SID music playback;
- rasterbar-region;
- smooth scroller eller kompakt DYCP-region;
- sine-driven sprites;
- music cues som endrer visual state;
- entry, running state og exit/transition.

Tegn framen vertikalt og marker hvor hver synlig region hører hjemme. Tegn deretter memory- og CPU-time-plan ved siden av.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Det vanskelige er ofte ikke én effekt, men å få flere effects til å sameksistere forutsigbart.

## Lab
Lag tre diagrammer: screen/raster layout, memory map og frame-time plan.

## Neste
Vi gjør diagrammene om til eksplisitte budgets.
