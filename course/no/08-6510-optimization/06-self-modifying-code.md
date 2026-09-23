---
title: Self-modifying code
course: 08-6510-optimization
lesson: 06
level: advanced
prerequisites: [05-loop-unrolling]
labs: [08.06-self-modifying-code]
---
# Self-modifying code
På C64 ligger code normalt i writable RAM. En routine kan derfor endre operand eller opcode i sin egen instruction stream.

En vanlig disiplinert bruk er å patche address operand til en hot load/store slik at runtime pointer handling forsvinner fra repeated path.

Self-modifying code er ikke automatisk raskere eller bedre. Det bytter setup writes og complexity mot enklere hot path.

## Gjør modification tydelig
Label patch sites, dokumenter hvem som skriver dem og når, og sørg for at code er writable/visible med aktuell banking. Unngå skjulte modifications som gjør debugging umulig.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
SMC er en legitim 6502-family optimization når trade-off er målt og timing-gevinsten faktisk betyr noe.

## Lab
Erstatt én indirect hot-path access med eksplisitt patched absolute operand. Sammenlign setup cost, repeated cost, bytes og readability.

## Neste
Vi undersøker undocumented opcodes med samme evidenskrav.
