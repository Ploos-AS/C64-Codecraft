---
title: Pointers og indirect indexed addressing
course: 00-intro
lesson: 15
level: absolute-beginner
prerequisites: [14-zero-page]
labs: [first-pointer]
---

# Pointers og indirect indexed addressing

## Hva du skal lære

En pointer er data som inneholder en adresse. På 6510 kan en to-byte zero-page-pointer kombineres med Y for indirect access.

```asm
ptr = $f0

    lda #<$0400
    sta ptr
    lda #>$0400
    sta ptr+1

    ldy #$00
    lda (ptr),y
```

`<` ber assembleren om lav byte av adressen og `>` om høy byte. Med pointer til `$0400` og Y=0 leser `LDA (ptr),Y` fra `$0400`.

## Hvorfor pointers betyr noe

En hardkodet adresse låser rutinen til ett sted. En pointer lar data bestemme adressen mens rutinen kan være uendret.

## Bytes og cycles

`LDA (zp),Y` er 2 bytes og normalt 5 cycles, pluss én cycle hvis den effektive read-adressen krysser en page boundary.

Fleksibilitet har altså en timing-kostnad vi kan resonnere om.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Pointers lar gjenbrukbare rutiner arbeide på forskjellige screens, buffers, tabeller og effektdata. Samtidig møter vi en klassisk 8-bit-avveining: fleksibel addressing mot strammere fixed-address kode.

## Lab

Pek på en kjent byte og les den via `(ptr),Y`. Øk Y og les neste byte. Flytt pointeren til andre data uten å endre read-loopen.

## Kontrollpunkt

Du forstår 16-bit pointer, low/high address bytes, pointer i zero page og `(zp),Y`.

## Neste

Nå har vi nok addressing-kunnskap til å arbeide med screen RAM og color RAM, ikke bare ett VIC-II-register.
