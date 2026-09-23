---
title: FLI-konseptet
course: 07-bitmap-high-colour
lesson: 05
level: advanced
prerequisites: [04-bitmap-raster-splits]
labs: [07.05-fli-concept]
---
# FLI-konseptet
FLI (*Flexible Line Interpretation*) er en family-defining idé: nøye timede VIC-II registerendringer påvirker display-fetch behaviour slik at colour/display-information kan oppdateres oftere enn i vanlig bitmap-oppsett.

Fleksibiliteten er ikke gratis. Den gir strenge raster timing-krav, betydelige data-behov og karakteristiske display constraints/artifacts avhengig av implementation.

Før kode modellerer vi:
- hvilke display-data VIC-II normalt fetcher;
- når fetches skjer;
- hvilke registerendringer som påvirker sekvensen;
- hvilken ekstra colour freedom vi får;
- hvilken CPU/memory/display cost vi betaler.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
FLI er et klassisk eksempel på å utnytte hardware sequencing til å skape en graphics mode maskinen ikke tilbyr som en enkel mode-bit.

## Lab
Tegn line-by-line conceptual fetch/state diagram som sammenligner vanlig multicolor bitmap med FLI-strategien i senere target-specific lab.

## Neste
Vi sammenligner FLI-family variants og velger etter constraints, ikke prestige.
