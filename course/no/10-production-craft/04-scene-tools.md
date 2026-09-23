---
title: Arbeid med scene-tools
course: 10-production-craft
lesson: 04
level: advanced
prerequisites: [03-debugger-workflow]
labs: [10.04-scene-tools]
---
# Arbeid med scene-tools
En production kan kombinere command-line assemblers med spesialiserte graphics-, music- og debugging-tools.

Eksempler på tool categories:
- sprite/charset/bitmap editors og converters;
- SID trackers/composers som GoatTracker-workflows;
- emulator/debuggers;
- packers og disk-image tools;
- host-side generators for tables og assembly-data.

GUI-tools kan kjøre native på host mens reproducible build fortsatt er command-line-driven.

## Bevar source
Lagre lovlige editable source assets der licensing tillater det, pluss nok metadata til å reprodusere eksporterte C64-data. Ikke la binary export være eneste gjenværende master.

## Lab
Ta ett editable graphics- eller music-testasset gjennom dokumentert export/import pipeline og reproduser bytes som assembly-build bruker.

## Neste
Vi gjør provenance og credits til first-class production data.
