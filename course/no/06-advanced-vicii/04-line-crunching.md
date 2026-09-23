---
title: Line crunching
course: 06-advanced-vicii
lesson: 04
level: advanced
prerequisites: [03-fld]
labs: [06.04-line-crunch-probe]
---
# Line crunching
Line-crunch-effects påvirker bevisst VIC-II display sequencing på snevert definerte rastertidspunkt.

I motsetning til vanlig scrolling avhenger resultatet av intern display timing state, ikke bare av at et register skrives et sted på linjen. Implementasjoner er derfor følsomme for model, cycle og surrounding DMA.

Codecraft behandler line crunching som hardware-timing experiment:
1. oppgi target;
2. forklar VIC-II-state som påvirkes;
3. utled nødvendig write window;
4. instrumenter den;
5. test sustained stability.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Line crunching viser punktet der register programming blir utnyttelse av videochipens sequencing behaviour.

## Lab
Implementer et minimalt dokumentert target-specific crunch experiment før det kombineres med andre effects.

## Neste
Vi går fra vertical sequencing til selve border-områdene.
