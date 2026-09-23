---
title: Colour i scrolleren
course: 03-smooth-scrolling
lesson: 04
level: intermediate
prerequisites: [03-text-stream]
labs: [03.04-colour-scroll]
---
# Colour i scrolleren
Screen RAM og colour RAM er separate. Hvis designet krever at colour følger character-cellene må effekten oppdatere begge representasjonene bevisst.

Mulige design:

- shift colour RAM sammen med screen codes;
- fast colour for hvert nytt character;
- repeating colour table;
- colour fra scroller phase;
- endre global/background colours i stedet for per-cell colour.

Alle har ulik CPU- og memory-kostnad.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Den billigste representasjonen som gir ønsket uttrykk er ofte best. Å flytte 40 colour values ved hver coarse update kan være unødvendig hvis table eller global register gir samme inntrykk.

## Lab
Implementer to colour-strategier og sammenlign cycle cost med border timing probe.

## Neste
Vi scheduler scrolleren i en rasterregion i stedet for å la main loop bestemme tidspunktet.
