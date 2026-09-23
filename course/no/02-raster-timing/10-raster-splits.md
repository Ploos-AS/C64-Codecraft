---
title: Raster splits og IRQ scheduling
course: 02-raster-timing
lesson: 10
level: intermediate
prerequisites: [09-foerste-rasterbar]
labs: [raster-splits]
---
# Raster splits og IRQ scheduling
En raster split endrer display state på valgt vertikal posisjon slik at forskjellige regioner i samme frame kan bruke forskjellige innstillinger.

En vanlig arkitektur er en IRQ chain: hver handler gjør arbeidet sitt, programmerer neste raster line, acknowledge-er aktuell source og returnerer. Neste IRQ håndterer neste region.

Split-arbeid kan være colours, scroll values, screen/charset pointers, sprite state og music scheduling.

## Budsjetter hver region
Hver handler bruker cycles og kan møte badlines eller sprite DMA. Split-arkitekturen trenger derfor en frame plan, ikke bare en liste rasterlinjer.

Flytt ikke-kritisk arbeid ut av de strammeste seksjonene når mulig.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Raster splits lar én fysisk C64-frame oppføre seg som flere forskjellig konfigurerte display-zones. Det er grunnlag for scrollers, statusområder, logoer og multipart-lignende effekter.

## Lab
Bygg en two-region split som endrer background colour på to planlagte linjer. Dokumenter deretter framen som timeline med IRQ-work og kjent VIC-II-aktivitet.

## Kontrollpunkt
Du kan forklare IRQ chain, planlegge flere rasterregioner og resonnere om cycle budgets.

## Neste
Neste blokk kombinerer raster timing med $D016 fine scrolling til en smooth character scroller.
