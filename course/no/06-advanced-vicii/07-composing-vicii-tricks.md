---
title: Kombiner avanserte VIC-II effects
course: 06-advanced-vicii
lesson: 07
level: advanced
prerequisites: [06-side-border-timing]
labs: [06.07-composing-vicii-tricks]
---
# Kombiner avanserte VIC-II effects
En teknikk som virker alene kan feile når en annen effect endrer DMA, register state eller tilgjengelige cycles.

Behandle hver advanced effect som en timing contract:
- nødvendig entry phase;
- critical raster/cycle windows;
- VIC-II state assumptions;
- sprite/badline assumptions;
- registers og memory den eier;
- tid den etterlater til annet arbeid.

Kombiner contracts før du kombinerer code.

Når krav kolliderer må scheduling, representation eller visual design endres. Ikke skjul konflikten med uforklarte delays.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Advanced scene code er systems engineering under artistic constraints. Det sterkeste trikset er ofte arkitekturen som lar flere enklere tricks sameksistere.

## Lab
Kombiner to tidligere kvalifiserte effects, oppdater frame budget og dokumenter alle endrede timing assumptions.

## Kontrollpunkt
Du kan resonnere om VIC-II fetch/DMA behaviour, kvalifisere model-sensitive tricks og integrere dem uten å behandle timing som magi.

## Neste
Neste blokk studerer bitmap- og high-colour-teknikker, inkludert FLI-family concepts og deres memory/timing trade-offs.
