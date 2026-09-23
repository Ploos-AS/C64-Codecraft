---
title: Organiser en virkelig production
course: 10-production-craft
lesson: 01
level: advanced
prerequisites: [09-packing-loading/09-release-d64]
labs: [10.01-project-layout]
---
# Organiser en virkelig production
En større demo trenger source tree som gjør ownership synlig.

Skill authored source, generated data, third-party inputs, build scripts, tools/configuration, documentation og release output. Generated artifacts skal være reproducible fremfor håndredigerte.

Part boundaries skal være forståelige fra treet og ikke skjules bak et custom framework.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En production kan tunes i måneder. Tydelig struktur gjør aggressiv low-level code lettere å endre uten å miste oversikt over assets, generated tables eller part contracts.

## Lab
Refactor teaching multipart demo til eksplisitt production tree og rebuild fra clean checkout.

## Neste
Vi lærer å lese mer enn én ekte assembler dialect.
