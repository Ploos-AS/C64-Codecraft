---
title: Kvalifiser mini-demo-parten
course: 05-demo-architecture
lesson: 07
level: advanced
prerequisites: [06-transitions]
labs: [05.07-mini-demo-qualification]
---
# Kvalifiser mini-demo-parten
Den integrerte parten har nå nok bevegelige deler til at «det så riktig ut én gang» ikke er en nyttig acceptance test.

Qualification bør dekke:
- clean assembly fra source;
- dokumentert memory map uten utilsiktet overlap;
- eksplisitte target video model(s);
- stable raster-regions over sustained execution;
- korrekt music cadence;
- coarse-scroll/DYCP worst-case frames;
- sprite movement og animation;
- cue transitions;
- entry/exit ownership;
- repeatable emulator test procedure;
- real hardware testing når tilgjengelig.

Automatiser deterministic checks der toolchain faktisk støtter dem. Ikke påstå emulator state verification som ikke er kvalifisert.

## Release evidence
PRG/binary skal være reproducible fra source. Noter assembler/tool versions og generated-data steps.

## Kontrollpunkt
Du har designet, integrert, målt og kvalifisert en liten scene-style demo-part i stedet for bare å samle effects.

## Neste
Neste kurs går inn i avanserte VIC-II-teknikker: sprite multiplexing, FLD, open borders, line crunching og andre timing-sensitive tricks.
