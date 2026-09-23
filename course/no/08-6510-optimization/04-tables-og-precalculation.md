---
title: Tables og precalculation
course: 08-6510-optimization
lesson: 04
level: advanced
prerequisites: [03-page-boundaries]
labs: [08.04-tables-precalc]
---
# Tables og precalculation
6510 er ofte raskest når dyre decisions allerede er tatt.

Tables kan erstatte arithmetic, wrapping logic, address calculation, colour generation, animation decisions og annet repeated work. Host-side generation kan flytte enda mer computation ut av runtime.

Men tables bruker memory, og placement, page crossing og indexing blir del av designet.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Precalculation er en definerende måte demo code bytter rikelig offline computation og memory mot knappe runtime cycles.

## Lab
Erstatt én målt runtime calculation med generated lookup-data. Sammenlign runtime cycles, total bytes og build complexity.

## Neste
Vi bytter code size mot speed med loop unrolling.
