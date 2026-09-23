---
title: Fine pluss coarse scrolling
course: 03-smooth-scrolling
lesson: 02
level: intermediate
prerequisites: [01-d016-fine-x-scroll]
labs: [fine-coarse-scroll]
---
# Fine pluss coarse scrolling
En kontinuerlig character scroller har to rytmer.

Hver frame endres $D016 fine-scroll phase. Når phase krysser character-grensen flyttes screen-raden én character og nye data settes inn ved kanten.

```text
frame: endre fine phase
frame: endre fine phase
...
boundary:
    shift screen codes én celle
    sett inn neste character
    wrap/reset fine phase
```

Eksakt retning og phase-sekvens må stemme med hvordan VIC-II tolker scroll-feltet.

## Budsjetter coarse-steget
De fleste frames er billige. Coarse-update-framen er dyrere fordi mange screen bytes kopieres. Denne periodiske timing-spiken må passe frame-planen.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Smoothness kommer ofte fra en billig hardware-operasjon kombinert med sjeldnere memory work. Mønsteret går igjen i mange C64-effekter.

## Lab
Kombiner one-row coarse shift med $D016 fine scrolling og marker coarse-update-framen med border timing probe.

## Neste
Vi erstatter faste innkommende characters med en ordentlig text stream.
