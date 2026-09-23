---
title: Sine tables og precalculation
course: 01-c64-machine
lesson: 15
level: beginner
prerequisites: [14-sprite-movement-tabeller]
labs: [01.10-sine-movement]
---

# Sine tables og precalculation

En sine wave er nyttig for jevn periodisk movement, men vi trenger ikke beregne trigonometri på 6510 hver frame.

I stedet genererer vi en byte-tabell på forhånd:

```asm
sine:
    .byte 100,102,105,107,110
    ; ... generated values ...
```

Runtime-koden blir et indexed lookup.

```asm
    ldx phase
    lda sine,x
    sta $d001
    inx
    stx phase
```

Range, lengde og phase mapping er designvalg. En host-side generator er helt grei fordi C64 fortsatt bruker transparente og inspiserbare data.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Sine movement er klassisk scene-vokabular, men den dypere leksjonen er precalculation. Bruk utviklingsmaskinen til å forberede data slik at C64 kan bruke sine knappe cycles på den synlige effekten.

Phase-shifted lookups kan senere lage waves, sprite formations, DYCP og mange andre effekter.

## Lab

Generer eller skriv en liten periodisk tabell og bruk den til sprite Y. Endre amplitude og center. Inspiser de genererte bytes i stedet for å behandle generatoren som magi.

## Kontrollpunkt

Du forstår sine table som precalculated effect-data og kan bruke phase-indexed lookup til periodisk movement.

## Neste

Vi legger til multicolor sprite graphics og møter en ny memory-versus-colour-avveining.
