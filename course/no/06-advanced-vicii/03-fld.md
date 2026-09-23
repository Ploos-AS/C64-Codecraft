---
title: FLD — flexible line distance
course: 06-advanced-vicii
lesson: 03
level: advanced
prerequisites: [02-sprite-dma]
labs: [fld]
---
# FLD — flexible line distance
FLD (*Flexible Line Distance*) manipulerer VIC-II vertical display timing slik at character rows kan forskyves og gi kontrollerte vertikale gaps/movement.

Effekten er knyttet til forholdet mellom raster position, $D011 vertical scroll state og når VIC-II gjør character-row fetch activity. Her er en uforklart delay-loop spesielt farlig.

Vi modellerer først relevant raster/badline behaviour og implementerer deretter en target-specific timed sequence.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
FLD gjør kunnskap om display fetch timing til vertical movement uten å redraw en hel bitmap. Det forbereder også resonnementet som trengs for mer aggressive VIC-II tricks.

## Lab
På dokumentert target-model lager du kontrollert vertical displacement og annoterer hver timing-critical register-write.

## Neste
Vi undersøker den mer aggressive familien av line-crunch-teknikker.
