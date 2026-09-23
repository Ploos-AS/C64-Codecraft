---
title: Integrer memory map
course: 05-demo-architecture
lesson: 03
level: advanced
prerequisites: [02-frame-budget]
labs: [integrated-memory-map]
---
# Integrer memory map
Plasser nå code og data sammen: main code, IRQ code, zero-page state, music/player, screen matrices, charset/DYCP-data, sprite frames, tables og buffers.

For hver region noter:
- start/slutt;
- CPU visibility;
- VIC-II visibility;
- alignment;
- lifetime;
- om ROM/I/O banking betyr noe;
- ownership og overwrite-regler.

Ikke lag en universell Codecraft-layout. Layout følger constraints i denne parten.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Memory layout kan fjerne runtime copies, unngå conflicts og gjøre timing enklere. Architecture er allerede optimization.

## Lab
Lag et non-overlapping map og forklar hvert alignment- og bank-valg.

## Neste
Vi bygger IRQ chain fra frame-planen.
