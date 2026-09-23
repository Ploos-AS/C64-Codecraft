---
title: Indeksert adressering og tabeller
course: 00-intro
lesson: 11
level: absolute-beginner
prerequisites: [10-jsr-rts-og-stack]
labs: [00.04-table-indexing]
---

# Indeksert adressering og tabeller

## Hva du skal lære

Hvordan en rekke bytes kan være en tabell, og hvordan X kan velge en verdi med indexed addressing.

## Ideen

```asm
    ldx #$00
    lda colours,x

colours:
    .byte $00,$06,$0e,$03
```

`colours,x` betyr: start på adressen `colours` og legg til X for å velge en byte. Hvis X er `$02`, får A den tredje verdien, `$0e`.

En label som `colours` er et navn assembleren gjør om til en adresse. Det er ikke en Codecraft runtime-funksjon.

## Bytes og cycles

Absolute,X `LDA` er 3 bytes. Den bruker normalt 4 cycles, pluss én hvis den effektive read-adressen krysser en page boundary.

Her møter vi for første gang direkte at plassering av data kan påvirke timing.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Tabeller bytter beregning mot ferdig data. Først bruker vi farger; senere blir samme idé til sine tables, sprite paths, rasterverdier, animasjonsdata og precalculation.

## Lab

Lag en fire-byte fargetabell. Les hver verdi med X og forutsi A før instruksjonen kjøres. Endre tabellen uten å endre koden som leser den.

## Kontrollpunkt

Du forstår labels som adresser, byte-tabeller og indexed addressing med X.

## Neste

Nå kobler vi tabellen direkte til VIC-II.
