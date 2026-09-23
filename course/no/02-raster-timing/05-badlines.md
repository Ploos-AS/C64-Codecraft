---
title: Badlines og VIC-II bus-tid
course: 02-raster-timing
lesson: 05
level: intermediate
prerequisites: [04-cycle-budgets]
labs: [02.05-badline-observation]
---
# Badlines og VIC-II bus-tid
I normale character display modes gjør VIC-II periodisk ekstra memory fetches for display-data. Disse **badlines** reduserer CPU-tiden på de aktuelle rasterlinjene.

Eksakt condition avhenger av display state og vertical fine-scroll/raster-forhold; vi utleder den når $D011 manipuleres. Sprite DMA kan også bruke bus-tid.

**CPU-en eier ikke hver bus-cycle.**

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Badlines er en del av maskinen du komponerer med. Avanserte effekter planlegger rundt, flytter, undertrykker eller utnytter VIC-II fetch behaviour.

## Lab
På eksplisitt PAL- eller NTSC-modell: identifiser candidate badlines fra referansemateriale og verifiser redusert CPU availability.

## Neste
Vi bruker border som oscilloskop og begynner å fjerne timing-usikkerhet.
