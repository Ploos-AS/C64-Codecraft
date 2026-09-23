---
title: Sprite DMA og CPU-tid
course: 06-advanced-vicii
lesson: 02
level: advanced
prerequisites: [01-sprite-multiplexing]
labs: [06.02-sprite-dma-probe]
---
# Sprite DMA og CPU-tid
Synlige sprites krever VIC-II memory fetches. Disse konkurrerer med CPU-en om bus time, så CPU-budget er ikke konstant over en line når sprite DMA er aktiv.

Eksakt schedule avhenger av VIC-II-modell og active sprite state. Ikke memorer en universell «sprite koster N cycles»-regel løsrevet fra betingelsene.

For en multiplexer betyr dette dobbelt: sprites skaper visual workload og kan samtidig redusere CPU-tiden for å forberede senere sprites.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En effect kan feile bare når nok sprites er aktive fordi maskinens bus schedule har endret seg under ellers korrekt kode.

## Lab
Mål samme timed routine med forskjellige active-sprite patterns på eksplisitt emulator-model. Noter hvor tilgjengelig CPU-tid endres.

## Neste
Vi går tilbake til badlines og lærer hvordan vertical display timing kan manipuleres.
