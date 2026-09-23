---
title: Coarse character scrolling
course: 01-c64-machine
lesson: 11
level: beginner
prerequisites: [10-character-animasjon]
labs: [01.07-char-scroll-data]
---

# Coarse character scrolling

En enkel horizontal character scroll kan flytte screen codes én celle om gangen.

For en 40-kolonners rad kan vi kopiere celle 1..39 til 0..38 og legge et nytt tegn på høyre side.

```asm
    ldx #$00
shift:
    lda $0401,x
    sta $0400,x
    inx
    cpx #39
    bne shift
```

Dette er **coarse scrolling**: bevegelsen skjer i steg på 8 pixels.

## Tenk kostnad

Loopen gjør mange reads, writes og branches. En virkelig scroller trenger også innkommende text-data, wrapping og vanligvis colour handling.

Vi skjuler ikke arbeidet. Vi teller det. Senere kombinerer smooth scrolling VIC-II fine-scroll-register med periodiske coarse screen updates.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Scrolleren er en scene-klassiker og en perfekt systems-øvelse: data stream, screen memory, timing, character graphics og senere raster synchronization møtes.

## Lab

Flytt én rad ett character til venstre og sett inn en fast screen code på høyre side. Bytt så den faste verdien med bytes fra en message table.

## Kontrollpunkt

Du forstår coarse scrolling og hvorfor smooth scrolling trenger både hardware fine-scroll og memory updates.

## Neste

Før fine scrolling møter vi VIC-II sitt andre store object-system: hardware sprites.
