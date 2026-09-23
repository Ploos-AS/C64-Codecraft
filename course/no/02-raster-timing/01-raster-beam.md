---
title: Tenk i rasterlinjer
course: 02-raster-timing
lesson: 01
level: intermediate
prerequisites: [01-c64-machine/17-sprite-animasjon]
labs: [02.01-raster-beam]
---
# Tenk i rasterlinjer
VIC-II bygger videobildet over tid. Raster-posisjonen går gjennom scan lines og starter så en ny frame. En register-write kan derfor påvirke ulike deler av samme frame avhengig av tidspunkt.

## PAL og NTSC
Video-standardene har ulik frame-struktur og timing. Bruk aldri én modells konstanter skjult overalt; timingverdier må navngi target.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En C64-demo er ofte koreografi mellom 6510 og VIC-II. Kode kan synkroniseres direkte med videohardwaren.

## Lab
Observer raster/debug-info i VICE på eksplisitt valgt modell og noter modellen sammen med observasjonene.

## Neste
Vi leser og programmerer rasterposisjon via $D011/$D012.
