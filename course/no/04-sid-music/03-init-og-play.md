---
title: Music init og play routines
course: 04-sid-music
lesson: 03
level: intermediate
prerequisites: [02-foerste-voice]
labs: [music-init-play]
---
# Music init og play routines
Mange C64 music players eksponerer et lite machine-code-interface: initialization entry point som kalles én gang og play entry point som kalles gjentatte ganger med nødvendig rate.

Eksakt calling convention, subtune selection, clobbered registers, memory range og playback rate tilhører den konkrete music/player. Les dokumentasjon eller eksportert metadata; ikke anta en universell contract.

```asm
    ; init i henhold til player contract
    jsr music_init

frame:
    ; ved riktig cadence
    jsr music_play
```

Codecraft legger ikke sin egen API-wrapper rundt dette.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Reelle productions integrerer kode og musikk fra forskjellige tools/authors. Å respektere playerens memory- og calling-contract er demo architecture.

## Lab
Integrer en redistributable/open test tune eller course-owned test player med dokumentert contract. Marker memory-bruken i demo memory map.

## Neste
Vi scheduler play-calls fra frame/IRQ-strukturen.
