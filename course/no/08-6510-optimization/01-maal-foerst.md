---
title: Mål før du optimaliserer
course: 08-6510-optimization
lesson: 01
level: advanced
prerequisites: [07-bitmap-high-colour/07-high-colour-integration]
labs: [08.01-measure-first]
---
# Mål før du optimaliserer
Velg en virkelig hot path fra en tidligere effect. Noter instruction path, cycles under relevante conditions, code/data-bytes, call frequency og timing deadline.

Average cost kan skjule problemet. For raster work er ofte worst relevant path viktigst.

Bruk border probes, debugger traces og manuell cycle accounting som komplementær evidens.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En routine som blir 20% raskere, men aldri lå på critical path, forbedrer kanskje ingenting. Optimization starter med å finne hva som faktisk begrenser effekten.

## Lab
Lag baseline report for én scroller-, sprite- eller raster-routine. Ingen optimalisering før baseline finnes.

## Neste
Vi bruker knappe zero-page-bytes der de gir målbar verdi.
