---
title: PAL, NTSC og playback cadence
course: 04-sid-music
lesson: 05
level: intermediate
prerequisites: [04-irq-playback]
labs: [04.05-playback-rate-model]
---
# PAL, NTSC og playback cadence
En tune kan forvente calls knyttet til en bestemt video/frame rate eller annen timing source. PAL og NTSC har ikke identisk frame timing.

Dermed er «call play once per frame» ikke automatisk portable.

Riktig strategi avhenger av player/tune: bruk cadence den deklarerer, adapter scheduling når det er riktig, eller target én standard eksplisitt.

## Oppgi target
En demo kan legitimt være PAL-only eller støtte begge standarder. Poenget er at valget skal være eksplisitt og testet.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Feil cadence endrer musical tempo og kan ødelegge synchronization mellom audio og effects.

## Lab
Kjør dokumentert test tune under eksplisitte PAL- og NTSC-modeller. Sammenlign frame-driven playback og noter konsekvensen.

## Neste
Vi lager synchronization state som visual code kan bruke.
