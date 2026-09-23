---
title: Ditt første custom character
course: 01-c64-machine
lesson: 08
level: beginner
prerequisites: [07-demo-memory-plan]
labs: [01.04-custom-character]
---

# Ditt første custom character

I standard character mode er en character shape et 8x8 bitmap lagret som åtte bytes: én byte per rad.

```asm
my_char:
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11011011
    .byte %11111111
    .byte %00100100
    .byte %01011010
    .byte %10100101
```

Hver bit styrer en pixel i den monochrome character-cellen.

For å vise eget charset plasserer vi character-data på en VIC-II-gyldig plassering, setter riktig VIC-bank og $D018 character pointer, og legger riktig screen code i screen matrix.

## Hvorfor ikke skjule dette i en graphics API?

Fordi sammenhengen mellom bits, bytes, character-adresser og VIC-II fetches er akkurat det kurset skal lære. Conversion tools kan komme senere uten å erstatte forståelsen.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Custom charsets gjør text mode til et kompakt graphics system. De brukes til logoer, tile graphics, scrollers, animasjon og mange klassiske demo-effekter med langt mindre data enn full bitmap.

## Lab

Tegn et 8x8-mønster på papir, kod hver rad som én byte, plasser det i et custom charset og vis det. Endre én bit og forutsi hvilken pixel som endres.

## Kontrollpunkt

Du forstår at et monochrome character består av åtte bitmap-bytes og hvordan VIC-bank/$D018/screen code kobles sammen.

## Neste

Neste utvider vi fra ett tegn til et lite custom charset og begynner å behandle character graphics som effekt-assets.
