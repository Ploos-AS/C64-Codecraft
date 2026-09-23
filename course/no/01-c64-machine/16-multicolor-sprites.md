---
title: Multicolor sprites
course: 01-c64-machine
lesson: 16
level: beginner
prerequisites: [15-sine-tabeller]
labs: [01.11-multicolor-sprite]
---

# Multicolor sprites

VIC-II-sprites kan bruke multicolor mode. I stedet for at hver bitmap-bit representerer én høyoppløst pixel, velger bit-par mellom fire colour choices. Horizontal resolution reduseres, men flere farger blir tilgjengelige.

To multicolor-verdier deles globalt via $d025 og $d026, mens hver sprite også har sitt eget colour register, for eksempel $d027 for sprite 0.

Multicolor enable styres via bits i $d01c.

## Avveiningen

Monochrome sprite mode gir høyere horisontal detalj. Multicolor gir rikere palette med lavere horizontal resolution.

Det er ikke bare bedre mot dårligere; det er et kunstnerisk og teknisk valg.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

C64-grafikk består av constrained choices. God scene-grafikk utnytter hardware-avveiningene i stedet for å skjule dem.

Shared multicolors betyr også at flere sprites kan designes som ett koordinert visuelt system.

## Lab

Konverter en enkel sprite fra monochrome til multicolor. Identifiser hver 2-bit pixelverdi, sett shared colours og sprite-specific colour, og sammenlign resultatet.

## Kontrollpunkt

Du forstår 2-bit multicolor sprite-modellen, shared colours, per-sprite colour og resolution-avveiningen.

## Neste

Nå kombinerer vi frames, movement og colour til en animert sprite uten å lage et runtime-framework.
