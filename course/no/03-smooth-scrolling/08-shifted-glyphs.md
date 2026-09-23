---
title: Bygg vertically shifted glyphs
course: 03-smooth-scrolling
lesson: 08
level: intermediate
prerequisites: [07-dycp-konsept]
labs: [shifted-glyphs]
---
# Bygg vertically shifted glyphs
Et 8x8 glyph består av åtte row-bytes. Å flytte synlige pixels vertikalt betyr å velge hvor source rows havner i et større destination-vindu.

Pedagogisk starter vi med offline transformation: ta ett source glyph og generer varianter for vertical offsets. Inspiser hver output-byte.

Da blir representasjonen konkret før optimalisering.

## Precompute eller rebuild?
To hovedvalg:

- precalculate shifted variants og velg dem ved runtime;
- generer/rebuild destination character-data mens demoen kjører.

Precalculation koster memory. Runtime generation koster cycles og writes til VIC-visible memory. Hybrid-design er mulig.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Den viktige ferdigheten er ikke å memorere én DYCP-rutine. Det er å transformere graphics til en representation som gjør runtime-effekten billig nok.

## Lab
Generer vertical variants av flere glyphs for et lite offset-område. Verifiser bytes visuelt og beregn memory cost.

## Neste
Vi kobler shifted glyph selection til den bevegelige text stream.
