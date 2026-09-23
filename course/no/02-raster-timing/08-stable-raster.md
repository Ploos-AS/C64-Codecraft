---
title: Mot en stable raster
course: 02-raster-timing
lesson: 08
level: intermediate
prerequisites: [07-irq-jitter]
labs: [stable-raster]
---
# Mot en stable raster
En stable raster-rutine skiller to oppgaver:

1. kom nær ønsket rasterposisjon;
2. fjern gjenværende cycle-usikkerhet før den kritiske sekvensen.

Klassisk C64-kode bruker nøye designede synchronization-teknikker, ofte med en første interrupt og et presist arrangert andre stage. Eksakt sekvens avhenger av VIC-II-modell, interrupt policy og effekt.

Codecraft presenterer ikke en kopiert delay-sekvens som magi. Hver stabilization-sekvens skal forklares med cycles og eksplisitt target-modell.

## Engineering-regel
Når vi er stabilisert må critical path være deterministisk. Unngå uventede branches, page crossings, interrupts eller VIC-II DMA med mindre de er del av timing-designet.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Stable timing åpner for horizontal raster positioning, pålitelige splits og mange VIC-II tricks.

## Lab
Bygg den dokumenterte model-specific two-stage synchronization-laben, annoter instruksjonene med cycles og verifiser repeatability med border/debugger.

## Neste
Nå bruker vi stabiliteten på første kontrollerte rasterbar.
