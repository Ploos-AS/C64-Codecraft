---
title: Fyll en screen-rad
course: 00-intro
lesson: 17
level: absolute-beginner
prerequisites: [16-screen-og-colour-ram]
labs: [00.08-fill-row]
---

# Fyll en screen-rad

En normal C64 text-rad har 40 celler. X kan derfor indeksere en enkel loop.

```asm
    ldx #$00
loop:
    lda #$01
    sta $0400,x
    lda #$07
    sta $d800,x
    inx
    cpx #40
    bne loop
```

Dette skriver samme screen code og farge til de første 40 cellene.

## Hva du egentlig lærer

Det viktige er ikke det gjentatte tegnet. Du mapper samme indeks til relaterte posisjoner i to forskjellige minneområder.

X velger celle N både i screen RAM og colour RAM.

## Bytes og cycles

Loopen sparer kode, men betaler loop-overhead for hver celle. Senere sammenligner vi kompakte loops med unrolled code når speed er viktigere enn size.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Screen rows er naturlige byggesteiner for scrollers, texteffekter og character graphics. Samme indeks kan koordinere flere strømmer med effektdata.

## Lab

Endre tegn og farge. Bruk deretter `TXA` som screen-verdi og observer raden. Forutsi sluttverdien i X.

## Kontrollpunkt

Du kan bruke indexed absolute stores på korresponderende screen- og colour-celler.

## Neste

Nå lar vi data endres for hver celle med en tabell.
