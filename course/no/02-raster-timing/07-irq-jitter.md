---
title: IRQ jitter
course: 02-raster-timing
lesson: 07
level: intermediate
prerequisites: [06-border-som-timing-probe]
labs: [02.07-irq-jitter-probe]
---
# IRQ jitter
En raster IRQ ber om service ved en definert videoposisjon, men CPU-en starter ikke nødvendigvis første handler-instruksjon på nøyaktig samme cycle hver gang.

CPU-en kan være i ferd med å fullføre en instruksjon når request blir serviceable. Interrupt entry har også definert CPU-adferd, og annen maskinaktivitet må kontrolleres eller forstås.

Resultatet er **jitter**: handleren kan starte med litt timing-usikkerhet selv om raster line er riktig.

## Line accuracy er ikke cycle accuracy
For mye arbeid er line-level scheduling nok. For en registerendring som må treffe eksakt horizontal position er det ikke nok.

Stable raster-teknikker fjerner usikkerheten før cycle-critical kode.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Noen få cycles variasjon kan flytte en synlig register-write horisontalt. Stabilitet er derfor et engineering-problem.

## Lab
Bruk border timing probe ved IRQ-entry og observer variasjon mellom frames i kontrollert miljø.

## Neste
Vi bygger et stabilization stage før effekten.
