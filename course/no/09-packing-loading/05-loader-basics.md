---
title: Loader basics og contracts
course: 09-packing-loading
lesson: 05
level: advanced
prerequisites: [04-disk-image]
labs: [09.05-loader-basics]
---
# Loader basics og contracts
En loader flytter data fra storage til memory layout produksjonen trenger.

Start med correctness før speed. Definer loader contract:
- requested file/part identity;
- destination eller file-defined load address;
- memory som må forbli resident;
- machine/IRQ state som kreves under loading;
- success/failure behaviour;
- state som leveres tilbake.

KERNAL-assisted loading er nyttig for å forstå flow og for non-time-critical transitions. Mer spesialiserte loaders introduseres senere når production constraint begrunner dem.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Loader er infrastructure som deles av parts. En tydelig contract hindrer hver effect i å finne opp inkompatible assumptions.

## Lab
Load neste part/data-file under dokumentert enkel loader contract og verifiser destination bytes før execution.

## Neste
Vi undersøker hva som endres når music eller visuals skal fortsette under loading.
