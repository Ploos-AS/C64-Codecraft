---
title: Din første instruksjon — LDA
course: 00-intro
lesson: 05
level: absolute-beginner
prerequisites: [04-moet-6510]
labs: []
---

# Din første instruksjon — LDA

## Hva du skal lære

Hva `LDA` gjør og hva **immediate addressing** betyr.

## Ideen

`LDA` betyr **LoaD Accumulator**.

```asm
lda #$06
```

`#` forteller at `$06` er selve verdien. Dette kalles immediate addressing.

Før: `A = $00`

Etter `lda #$06`: `A = $06`

## Fra assembly til maskinkode

Instruksjonen bruker 2 bytes og 2 cycles og blir:

```text
A9 06
```

`A9` er opcode for LDA immediate. `06` er operand.

Nå har vi koblet lesbar assembly direkte til ekte maskinkode.

## Flagg

LDA oppdaterer blant annet zero- og negative-flagg. Vi trenger ikke memorere reglene ennå; flaggene får praktiske oppgaver når vi begynner å ta beslutninger i koden.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Før en farge, sprite-posisjon eller kontrollverdi kan skrives til hardware, må verdien ofte gjøres klar i et CPU-register. Immediate loads brukes også mye ved initialisering av effekter.

## Lab

Endre `lda #$06` til `lda #$0e`. Forutsi både A og maskinkoden før du assemblerer.

Sammenlign deretter `#$06` og `$06`. `#` er ikke pynt; den endrer addressing mode og dermed betydningen.

## Kontrollpunkt

Du skal kunne lese `lda #$06`, forklare immediate addressing og kjenne igjen `A9 06`.

## Neste

Nå skal verdien i A ut til VIC-II med `STA`.
