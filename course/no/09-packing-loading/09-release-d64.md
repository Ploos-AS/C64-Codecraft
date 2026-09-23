---
title: Kvalifiser release-disken
course: 09-packing-loading
lesson: 09
level: advanced
prerequisites: [08-multipart-demo]
labs: [release-d64]
---
# Kvalifiser release-disken
Et release image skal være reproducible og testable fra repository.

Qualification inkluderer:
- clean build av hver part;
- deterministic asset generation der mulig;
- dokumenterte packer/loader versions;
- generated disk directory verification;
- ingen utilsiktet memory overlap;
- hver part transition exercised;
- target PAL/NTSC policy oppgitt;
- sustained music/effect operation der nødvendig;
- emulator test procedure;
- real-hardware test record når tilgjengelig;
- release file hashes fra CI/build tooling når praktisk.

Ikke legg proprietary ROMs eller unlicensed third-party music/art i repository for å gjøre qualification enklere.

## Kontrollpunkt
Du kan konstruere en multipart C64-production der storage, packing, loading, depacking og part boundaries er engineered fremfor improvisert.

## Neste
Neste blokk er production craft: scene tooling, source/data organization, credits, release metadata, debugging workflows og forberedelse til final capstone demo.
