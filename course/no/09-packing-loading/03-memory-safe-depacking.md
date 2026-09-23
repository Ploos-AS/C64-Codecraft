---
title: Memory-safe depacking
course: 09-packing-loading
lesson: 03
level: advanced
prerequisites: [02-reproducible-packing]
labs: [09.03-memory-safe-depacking]
---
# Memory-safe depacking
En depacker leser compressed input, skriver expanded output og kjører code mens begge representations midlertidig kan eksistere samtidig.

Før den kjøres kartlegges:
- packed source range;
- depacker code/state;
- output range;
- stack/zero-page needs;
- resident music/IRQ code;
- buffers;
- banking requirements.

Overlappende source/destination er bare trygt når konkret format/depacker eksplisitt støtter arrangementet.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En perfekt effect er ubrukelig hvis transition-time depacking overskriver player, stack eller bytes som ennå ikke er lest.

## Lab
Tegn komplett memory timeline for et packed asset fra loaded bytes til endelig expanded placement.

## Neste
Vi legger flere files i et reproducible disk image.
