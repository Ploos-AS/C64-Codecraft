---
title: Din første datadrevne fargeeffekt
course: 00-intro
lesson: 12
level: absolute-beginner
prerequisites: [11-indeksert-adressering-og-tabeller]
labs: [colour-table]
---

# Din første datadrevne fargeeffekt

Nå kombinerer vi tabell, indexed load, VIC-II-write og loop.

```asm
    ldx #$00

loop:
    lda colours,x
    sta $d020
    inx
    cpx #colours_end-colours
    bne loop
    rts

colours:
    .byte $00,$06,$0e,$03,$01,$07

colours_end:
```

Assembler-uttrykket `colours_end-colours` gir lengden på tabellen. Vi slipper dermed å hardkode samme antall et annet sted.

## Hva ser du?

Som i forrige fargeloop skjer writene ekstremt raskt. Det nye poenget er ikke en jevn visuell effekt ennå: **kode og effektdata er nå separert**.

Endrer du tabellen, lager samme kode en annen sekvens.

## Bytes og cycles

`LDA colours,x` kan få en page-crossing penalty. `BNE` har fortsatt ulik timing på tatt og ikke-tatt branch.

Timing-kunnskapen bygges dermed gradvis før raster-synkronisering introduseres.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Datadrevne effekter er grunnleggende. En tabell kan være farger nå og senere sine wave, sprite movement eller raster schedule. Precalculation bytter ofte minne mot CPU-tid—en sentral avveining i C64 demo-koding.

## Lab

Endre bare tabellen og observer at loopen er uendret. Gjør tabellen kortere og lengre og kontroller at assembler-uttrykket følger størrelsen.

**Challenge:** lag en symmetrisk color ramp kun ved å endre data.

## Kontrollpunkt

Du kan bygge en liten datadrevet C64-rutine med label, tabell, indexed addressing, hardware-write og loop.

## Neste

Neste lærer vi flere addressing modes og zero page, som åpner for pointers og mer effektiv effektkode.
