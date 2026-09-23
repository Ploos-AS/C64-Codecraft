---
title: Part state og music cues
course: 05-demo-architecture
lesson: 05
level: advanced
prerequisites: [04-irq-chain]
labs: [part-cues]
---
# Part state og music cues
Hold musical events separat fra low-level effect implementation.

En cue kan oppdatere kompakt part state: active palette, sprite formation, scroller mode, rasterbar table eller transition request. Effect code leser state på sikre tidspunkt.

Da slipper vi song-specific tests inne i hver raster-critical routine.

## State changes har også timing
Noen state-endringer kan skje straks. Andre må commit-es ved frame boundary eller før bestemt rasterregion. Definer når cue blir synlig.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Et ryddig cue/state-lag lar koreografien utvikles uten å destabilisere cycle-critical code.

## Lab
Bruk minst tre music cues til uavhengige visual state-endringer og dokumenter når hver blir aktiv.

## Neste
Vi legger til entry/exit transitions slik at parten får lifecycle.
