---
title: Bygg første DYCP
course: 03-smooth-scrolling
lesson: 09
level: intermediate
prerequisites: [08-shifted-glyphs]
labs: [first-dycp]
---
# Bygg første DYCP
Nå kombinerer vi fire systemer:

1. smooth horizontal text stream;
2. phase for hver synlig character-posisjon;
3. sine-derived vertical offset;
4. shifted glyph-data eller en annen eksplisitt vertical-placement-representation.

Første versjon prioriterer sporbarhet fremfor cleverness. Eleven skal kunne følge en message-byte til source glyph, valgt offset og endelig visible data.

## Hold timing synlig
Instrumenter update med border. Skill arbeid som må skje i raster-critical region fra data preparation som kan kjøres andre steder.

Hvis første implementation overskrider budsjettet er det nyttig evidens. Mål før optimalisering.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Dette er nå umiskjennelig en demo-effekt: text, tables, generated graphics, raster scheduling og cycle budgeting virker sammen.

## Lab
Bygg en kort DYCP med lite alphabet/message og moderat wave. Noter kostnad for ordinary frames og coarse-update frames.

## Neste
Vi optimaliserer fra målinger, ikke folklore.
