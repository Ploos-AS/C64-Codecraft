---
title: $D018 — plassering av screen og charset
course: 01-c64-machine
lesson: 06
level: beginner
prerequisites: [05-vic-banker]
labs: []
---

# $D018 — plassering av screen og charset

VIC-II-register $D018 inneholder memory-pointer-felt som velger screen matrix og character- eller bitmap-data innenfor aktiv VIC-bank.

I text modes:

- bits 4-7 velger screen matrix i 1 KiB-steg innenfor 16 KiB-banken;
- bits 1-3 velger character data i 2 KiB-steg.

Ikke behandle en $D018-verdi som en magisk konstant. Dekod feltene og beregn VIC-relative plasseringer.

## Nyttig mental modell

Velg først 16 KiB VIC-bank. Bruk så $D018 til å velge strukturer **inni banken**:

**VIC bank base + offset valgt av $D018**

CPU-en må samtidig ha en mapping som lar programmet skrive dataene.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Relocation av screens og charsets lar effekter planlegge minnet bevisst, bytte mellom ferdige screens, bruke custom graphics og unngå kollisjoner med music/code.

## Lab

Dekod flere hypotetiske $D018-verdier. Kombiner dem med forskjellige VIC-bankbaser og regn ut absolutte RAM-plasseringer.

## Kontrollpunkt

Du kan forklare totrinns VIC memory selection: CIA2 velger 16 KiB-bank, $D018 velger strukturer inni den.

## Neste

Nå lager vi en konkret memory plan før første custom charset.
