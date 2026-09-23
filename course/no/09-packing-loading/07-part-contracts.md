---
title: Contracts mellom demo-parts
course: 09-packing-loading
lesson: 07
level: advanced
prerequisites: [06-loading-under-effects]
labs: [09.07-part-contracts]
---
# Contracts mellom demo-parts
Hver part skal deklarere hva den trenger ved entry og hva den garanterer ved exit.

Nyttige contract fields:
- entry address;
- loaded memory ranges;
- zero-page/stack ownership;
- VIC-II bank/display assumptions;
- IRQ/NMI/CIA state;
- music/player state;
- resident loader buffers;
- exit reason/next-part request.

Contract er ikke en Codecraft runtime API. Det er documentation og vanlig assembly-level agreement mellom components.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Parts kan utvikles og optimaliseres uavhengig bare når grensene er eksplisitte.

## Lab
Skriv contracts for to eksisterende teaching-parts og løs alle conflicting memory/state assumptions før transition linkes.

## Neste
Vi setter sammen komplett multipart flow.
