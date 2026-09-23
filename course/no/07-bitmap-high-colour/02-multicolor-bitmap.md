---
title: Multicolor bitmap mode
course: 07-bitmap-high-colour
lesson: 02
level: advanced
prerequisites: [01-hires-bitmap]
labs: [multicolor-bitmap]
---
# Multicolor bitmap mode
Multicolor bitmap tolker pixel-data i to-bit groups. Det gir flere colour selections innenfor hver 8x8-cell mot lavere horizontal resolution.

Tilgjengelige colour sources kommer fra bitmap-tilknyttet screen-data, colour RAM og shared background colour. Eksakt bit-pair mapping behandles som del av display-formatet og verifiseres i lab.

Hovedpoenget er at bitmap-bytes alene ikke beskriver hele bildet.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
C64 graphics formats er kompromisser mellom resolution, colour freedom, memory og timing. Multicolor bitmap gjør trade-offs tydelige.

## Lab
Encode én 8x8-cell manuelt før converter brukes. Gjør rede for hver pixel pair og hver colour source.

## Neste
Vi gjør memory-strukturene til en reproducible asset pipeline.
