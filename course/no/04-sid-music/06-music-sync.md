---
title: Synkroniser visuals til music
course: 04-sid-music
lesson: 06
level: intermediate
prerequisites: [05-pal-ntsc-playback]
labs: [04.06-music-sync]
---
# Synkroniser visuals til music
Visual synchronization trenger en pålitelig source for musical state.

Avhengig av music-system kan nyttig state være eksportert song position, pattern/row value, eksplisitt cue-byte eller en counter som integration code oppdaterer ved kjente musical boundaries. Ikke les undocumented intern player-memory og kall det en API.

Et enkelt cue-interface kan la visuals reagere:

```text
cue 0: normal
cue 1: start rasterbar
cue 2: change scroller palette
cue 3: launch sprite formation
```

Eksakt mekanisme tilhører valgt player/composer workflow.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Music sync gjør samtidig lyd og grafikk til koreografi. Det kobler også visual event logic fra skjøre wall-clock delays.

## Lab
Bruk dokumentert cue/state-source til å trigge minst tre synlige endringer mens musikken fortsetter uten avbrudd.

## Kontrollpunkt
Du kan integrere en player, schedule den, oppgi timing-target og eksponere dokumentert synchronization state til visual code.

## Neste
Vi kombinerer music, rasterbars, scroller og sprites til en liten timed demo-part.
