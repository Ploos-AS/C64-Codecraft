---
title: Kvalifisering
course: 11-capstone
lesson: 07
level: capstone
prerequisites: [06-optimize-og-integrate]
labs: [11.07-qualification]
---
# Kvalifisering
Oppgi hva releasen støtter.

Hvis PAL er primary target skal det sies eksplisitt. Hvis NTSC støttes må det testes, ikke utledes fra en PAL-run. Timing-sensitive code skal identifisere relevante VIC-II/video assumptions.

Qualification dekker:
- clean build;
- komplett run fra boot til ending;
- sustained raster stability;
- music cadence og sync;
- loader/depacker transitions;
- worst-case effect paths;
- generated asset reproduction;
- disk contents;
- emulator procedure;
- real C64 testing når hardware er tilgjengelig.

En manual test er ikke en automated assertion. Registrer hver ærlig.

## Gate
Ingen kjent blocker gjenstår mot deklarert target policy.

## Neste
Freeze kandidaten og forbered public release.
