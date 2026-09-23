---
title: Integrer high-colour graphics
course: 07-bitmap-high-colour
lesson: 07
level: advanced
prerequisites: [06-fli-family]
labs: [high-colour-integration]
---
# Integrer high-colour graphics
En high-colour raster routine kan bruke mye av framen og legge sterke føringer på memory placement. Integration starter derfor med timing- og memory-contracts, ikke med å legge til features til noe går i stykker.

Plasser music playback, transitions, sprite work og decompression/preparation i windows graphics-rutinen faktisk etterlater.

Hvis assets må konverteres eller precalculates skal build-steget være reproducible.

## Qualification
Test sustained raster stability, worst-case music/effect paths, memory overlap, target VIC-II model og clean regeneration av graphics-data.

Real hardware testing er spesielt verdifullt for model-sensitive display tricks når hardware er tilgjengelig.

## Kontrollpunkt
Du kan forklare bitmap representations, bygge reproducible assets, resonnere om FLI-family mechanisms og integrere high-colour display som del av en constrained production.

## Neste
Neste blokk fokuserer på advanced 6510 optimization: zero-page strategy, page boundaries, unrolling, self-modifying code og nøye begrunnede undocumented opcodes.
