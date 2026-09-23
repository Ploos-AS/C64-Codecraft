---
title: En raster-scheduled smooth scroller
course: 03-smooth-scrolling
lesson: 05
level: intermediate
prerequisites: [04-colour-scrolling]
labs: [raster-scroller]
---
# En raster-scheduled smooth scroller
Nå kombinerer vi blokkene til én effekt:

- raster IRQ velger når scroller-regionen serviceres;
- $D016 gir fine X movement;
- periodiske coarse updates flytter screen-data;
- text stream leverer nye characters;
- colour logic gir paletten.

Skill **critical** og **deferred** work. Registerendringer som må treffe bestemt rasterposisjon hører hjemme i timed section. Message parsing og annen ikke-kritisk preparation kan ofte gjøres et annet sted i framen.

## Tenk frame
Dokumenter framen som timeline. Marker IRQs, badlines, eventuell sprite DMA, coarse-update frames og ledig tid. Scrolleren er nå et scheduled subsystem i demo-parten.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Dette er overgangen fra enkelttriks til effect architecture. En virkelig demo koordinerer flere jobber innenfor ett frame budget.

## Lab
Bygg komplett one-line smooth scroller og dokumenter frame schedule. Mål vanlige frames og coarse-update frames separat.

## Kontrollpunkt
Du kan forklare hele pipelinen fra message byte til smooth visible movement og redegjøre for når arbeidet skjer.

## Neste
Vi bøyer den rette scrolleren til per-character vertical movement: den konseptuelle veien mot DYCP.
