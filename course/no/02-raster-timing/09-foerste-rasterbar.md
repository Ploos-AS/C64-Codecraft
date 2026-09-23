---
title: Din første kontrollerte rasterbar
course: 02-raster-timing
lesson: 09
level: intermediate
prerequisites: [08-stable-raster]
labs: [02.09-first-rasterbar]
---
# Din første kontrollerte rasterbar
En rasterbar endrer et colour register på kontrollerte rasterposisjoner. Nybegynnerversjonen kan endre $D020 eller $D021 over flere linjer fra en colour table.

```asm
    ldx #$00
bar:
    lda colours,x
    sta $d020
    ; model-specific line synchronization/delay here
    inx
    cpx #bar_length
    bne bar
```

Synchronization er med vilje ikke erstattet av en falsk universell delay. Den hører til target-specific lab og skal cycle-accountes.

## Data og timing møtes
Colour table bestemmer utseendet. Timing-koden bestemmer hvor det vises. Dermed kan art/data endres uten å skrive om synchronization-kjernen.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Rasterbars er enkle nok til å forstå, men viser en definerende C64 scene-ferdighet: endre hardware state mens beam tegner framen.

## Lab
Lag en symmetrisk colour table, bruk stable timing-laben og verifiser at baren står fast mellom frames.

## Neste
Én frame kan inneholde flere visuelle regioner: raster splits.
