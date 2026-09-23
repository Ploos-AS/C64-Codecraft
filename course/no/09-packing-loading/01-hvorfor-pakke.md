---
title: Hvorfor pakke demo-data?
course: 09-packing-loading
lesson: 01
level: advanced
prerequisites: [08-6510-optimization/09-optimaliseringspass]
labs: [packing-baseline]
---
# Hvorfor pakke demo-data?
Packing reduserer stored size ved å transformere code eller assets til en compressed representation pluss et depacking-steg.

Det kan forbedre diskbruk og transfer/load time, men koster andre steder: depacker code, CPU time, temporary memory, destination constraints og build complexity.

Behold alltid original generated asset/code som conceptual input. Packed bytes er en delivery representation.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Packing kan gjøre en større production praktisk, men bare når depacking passer memory- og transition-planen.

## Lab
Mål uncompressed sizes for én part og dens viktigste assets. Definer hvilken constraint packing skal forbedre før tool velges.

## Neste
Vi gjør packing-steget reproducible og replaceable.
