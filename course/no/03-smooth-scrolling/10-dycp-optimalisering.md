---
title: Optimaliser DYCP
course: 03-smooth-scrolling
lesson: 10
level: intermediate
prerequisites: [09-foerste-dycp]
labs: [03.10-dycp-optimization]
---
# Optimaliser DYCP
Optimalisering starter med målt bottleneck.

Aktuelle grep kan være:

- flytt beregninger til precalculated tables;
- arranger tables for å fjerne wrap branches;
- bruk zero-page state der gevinsten betyr noe;
- align data for å unngå uønskede page-cross penalties;
- oppdater bare data som faktisk endres;
- flytt non-critical work ut av timed region;
- unroll loop når cycle-gevinsten forsvarer ekstra bytes;
- bruk self-modifying code senere når det er tydelig, kontrollert og verdt kostnaden.

Ikke bruk alle teknikker automatisk. Hver optimization koster noe: memory, code size, complexity, flexibility eller setup time.

## Bevis forbedringen
Behold before/after cycle counts og binary-size-endring. En optimization uten måling er bare en hypotese.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Scene credibility kommer fra å forstå trade-offs, ikke fra å pynte kode med obskure tricks. Rask kode skal ha en grunn til å være rask.

## Lab
Velg de to største målte kostnadene i DYCP, optimaliser dem separat og noter cycles/bytes før og etter.

## Kontrollpunkt
Du kan bygge og måle en virkelig table-driven scene-effekt og velge optimalisering fra evidens.

## Neste
Neste blokk introduserer SID music, frame-rate playback og synchronization mellom lyd og visuelle effekter.
