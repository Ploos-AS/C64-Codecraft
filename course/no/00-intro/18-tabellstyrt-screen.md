---
title: En tabellstyrt screen-effekt
course: 00-intro
lesson: 18
level: absolute-beginner
prerequisites: [17-fyll-en-screen-rad]
labs: [00.09-table-driven-screen]
---

# En tabellstyrt screen-effekt

Nå kombinerer vi tabeller, indexing, loops og to C64-minneområder.

```asm
    ldx #$00
loop:
    lda chars,x
    sta $0400,x
    lda colours,x
    sta $d800,x
    inx
    cpx #data_end-chars
    bne loop
    rts

chars:
    .byte $01,$02,$03,$04,$05,$06,$07,$08

colours:
    .byte $02,$08,$07,$05,$0e,$04,$06,$01

data_end:
```

I et virkelig prosjekt vil vi normalt definere og validere tabellengder eksplisitt. Eksemplet holdes lite slik at den datadrevne ideen er tydelig først.

## Hva har endret seg?

Loop-strukturen er den samme, men både character og colour kommer nå fra data. Effekt-design flyttes gradvis fra instruksjonssekvenser til tabeller.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Mønsteret vokser naturlig til logoer, animasjon, fargemønstre og scrollers. Senere kan generated/precalculated tables flytte kostbart arbeid ut av raster-kritisk kode.

## Lab

Design et åtte-cellers mønster ved kun å endre de to tabellene. Gjør så tabellene med vilje forskjellige i lengde og forklar hvorfor robust kildekode bør oppdage eller hindre dette.

### Challenge

Lag en gradient eller et symmetrisk mønster kun med data. Ingen Codecraft runtime eller framework.

## Kontrollpunkt

Du kan koordinere flere tabeller med én indeks og forklare hvorfor separasjon av kode og data er nyttig for effekter.

## Neste

Introblokken har nå gitt oss nok ASM til å gå systematisk inn i C64 memory map og banking.
