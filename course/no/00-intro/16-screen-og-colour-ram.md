---
title: Screen RAM og colour RAM
course: 00-intro
lesson: 16
level: absolute-beginner
prerequisites: [15-pointers-og-indirect-y]
labs: [00.07-screen-and-colour]
---

# Screen RAM og colour RAM

## Hva du skal lære

Hvordan normal C64 text screen representeres av character codes i screen RAM og farger i colour RAM.

Med normal startup-layout starter text screen på `$0400`, mens colour RAM starter på `$d800`.

```asm
    lda #$01
    sta $0400

    lda #$07
    sta $d800
```

Første store velger screen code for første celle. Den andre velger foreground colour for samme celle.

## Viktig skille

Screen RAM inneholder ikke pixels. I text mode inneholder den screen codes. VIC-II bruker kodene til å velge tegnformer fra character data, mens colour RAM gir fargeinformasjon per celle.

Dette skillet mellom **hvilket tegn** og **hvilken farge** er første møte med C64-grafikkarkitekturen.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Text mode er ikke bare tekst. Custom charsets, scrollers, logoer og mange effekter bygger videre på samme screen/character-maskineri.

## Lab

Endre de første screen-cellene og fargene. Forutsi adressene til celle nummer to og tre.

## Kontrollpunkt

Du forstår grunnrollene til screen RAM og colour RAM, og at screen codes ikke er pixel-data.

## Neste

Nå bruker vi indexed addressing til å skrive en hel rad.
