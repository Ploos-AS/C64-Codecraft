---
title: Schedule music playback
course: 04-sid-music
lesson: 04
level: intermediate
prerequisites: [03-init-og-play]
labs: [04.04-frame-playback]
---
# Schedule music playback
En music play routine trenger pålitelig cadence. Raster IRQ kan gi denne cadence samtidig som den deltar i visual frame schedule.

Hvor play-call plasseres avhenger av cycle cost og effect layout. Ikke legg den i mest timing-critical section bare fordi en IRQ er praktisk.

Mål player-call med de samme verktøyene som visual routines.

## Respekter contract
Hvis playeren clobber registers eller zero-page locations må surrounding code håndtere det. Hvis visuals og music vil bruke samme memory må layout redesignes.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Music er enda en scheduled workload. Når kostnaden er kjent blir den del av samme engineering-problem som scrollers, sprites og raster effects.

## Lab
Kall dokumentert test player fra raster-scheduled frame og mål execution window med border probe/debugger.

## Neste
Playback cadence er et sted der PAL/NTSC-forskjeller blir svært synlige.
