---
title: FLI-family trade-offs
course: 07-bitmap-high-colour
lesson: 06
level: advanced
prerequisites: [05-fli-konsept]
labs: [07.06-fli-family]
---
# FLI-family trade-offs
Det finnes ikke én universell high-colour-løsning. FLI-relaterte teknikker og senere variants gjør forskjellige kompromisser mellom colour freedom, visible artifacts, border behaviour, CPU availability, memory layout og converter support.

Navn alene er ikke nok. For valgt format dokumenteres:
- exact target og display dimensions;
- colour constraints;
- memory footprint;
- raster routine requirements;
- CPU-tid igjen til music/effects;
- kjente visual artifacts;
- tool support og data format.

Ikke velg format bare fordi det regnes som mer avansert.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Beste graphics mode er den hvis constraints passer produksjonen. Et teknisk imponerende format kan være feil architecture hvis det bruker tiden resten av parten trenger.

## Lab
Sammenlign minst to dokumenterte bitmap/high-colour approaches mot samme production requirements. Lag constraint matrix, ikke winner ranking.

## Neste
Vi integrerer high-colour graphics med music og resten av en demo-part.
