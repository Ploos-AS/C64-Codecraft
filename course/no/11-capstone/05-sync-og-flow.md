---
title: Music sync og flow
course: 11-capstone
lesson: 05
level: capstone
prerequisites: [04-effects-og-assets]
labs: [capstone-sync]
---
# Music sync og flow
Gjør cues til production structure.

Bruk playerens dokumenterte state/cue-interface eller eksplisitt integration counter. Driv transitions, palette changes, effect phases eller part changes fra bevisste events.

Ikke scrape undocumented player internals og kall resultatet et interface.

Se hele produksjonen gjentatte ganger. Technical correctness er nødvendig, men pacing oppleves over tid.

## Gate
Viktige transitions er deterministic og cue source er dokumentert. Produksjonen når samme intended structure ved gjentatte runs.

## Neste
Mål den virkelige builden og optimaliser bare det som begrenser den.
