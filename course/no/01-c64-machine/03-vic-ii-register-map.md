---
title: VIC-II som registerblokk
course: 01-c64-machine
lesson: 03
level: beginner
prerequisites: [02-banking-00-01]
labs: [vic-register-map]
---

# VIC-II som registerblokk

Du kjenner allerede $d020. Nå slutter vi å behandle den som en isolert magisk adresse.

Når I/O er mappet inn ligger VIC-II-registre på $d000-$d02e, med mirrors videre i VIC-II-delen av I/O-området. Registrene styrer blant annet sprites, raster state, display modes, memory selection, colours og interrupts.

Viktige eksempler:

- $d011: control register 1 og blant annet raster high bit/display controls
- $d012: lav byte av raster line
- $d016: control register 2
- $d018: memory pointers
- $d019/$d01a: interrupt status/enable
- $d020: border colour
- $d021: background colour 0

Ikke memorer hele chipen nå. Lær å lese registerkartet og forstå bits når en leksjon faktisk trenger dem.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

VIC-II demo-koding er registerprogrammering kombinert med presis kunnskap om når chipen leser minne og endrer state. Rastereffekter, sprites, custom charsets og display tricks vokser fra dette registerkartet.

## Lab

Finn border/background, raster line og interrupt-registre i en VIC-II-referanse. Avgjør for hvert register om du først og fremst arbeider med hele byte-verdien eller individuelle bits.

## Kontrollpunkt

Du ser nå $d020 som ett register i et sammenhengende VIC-II-interface.

## Neste

Neste møter vi de to CIA-chipene og rollene deres for timing og input.
