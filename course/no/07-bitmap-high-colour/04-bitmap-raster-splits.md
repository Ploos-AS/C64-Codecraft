---
title: Raster splits i bitmap graphics
course: 07-bitmap-high-colour
lesson: 04
level: advanced
prerequisites: [03-asset-pipeline]
labs: [07.04-bitmap-raster-splits]
---
# Raster splits i bitmap graphics
Et bitmap tvinger ikke én display state for hele framen. Raster-scheduled writes kan endre valgt VIC-II-state mellom regioner.

Start med en enkel shared-colour-endring på kjent line. Resonner deretter om mer ambisiøse splits først etter at badlines, bitmap fetch activity og aktuelle registers er tatt med.

Frame-planen fra tidligere kurs gjelder fortsatt.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Raster splits lar begrenset per-cell colour-information suppleres med endringer over vertical position. Dette er conceptual bridge mot high-colour display techniques.

## Lab
Lag et bitmap med to rasterregions via dokumentert registerendring. Mål IRQ/timing cost og marker berørte lines.

## Neste
Vi studerer ideen bak FLI i stedet for å starte med en kopiert FLI-rutine.
