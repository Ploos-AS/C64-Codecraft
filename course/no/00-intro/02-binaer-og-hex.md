---
title: Binær og hexadecimal uten mystikk
course: 00-intro
lesson: 02
level: absolute-beginner
prerequisites: [01-maskinkode-og-assembler]
labs: []
---

# Binær og hexadecimal uten mystikk

## Hva du skal lære

Hvorfor datamaskiner bruker binær, hvorfor C64-programmerere vanligvis skriver verdier i hexadecimal, og hvordan de små verdiene vi trenger først henger sammen.

## Hvorfor dette betyr noe på C64

C64-kode er full av verdier som `$00`, `$06`, `$ff`, `$d020` og `$0400`. Hex er en kompakt måte å skrive bitmønstre og adresser på.

## Ideen

En **bit** er 0 eller 1. Åtte bits er en **byte**, som kan ha 256 forskjellige mønstre.

Hexadecimal bruker seksten sifre: `0-9` og `A-F`. Ett hex-siffer tilsvarer fire bits, så to hex-sifre tilsvarer én byte.

I kurset betyr `$` foran et tall hexadecimal:

- `$00` = `00000000`
- `$06` = `00000110`
- `$0f` = `00001111`
- `$ff` = `11111111`

Du trenger ikke bli en menneskelig basekonverterer. Målet er å kjenne igjen mønstrene og bli komfortabel gjennom bruk.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Hardware-registre, farger, sprites, VIC-II-modi, interrupt-flagg og bitmasker blir langt enklere å forstå når binær og hex føles naturlig.

## Lab

Konverter `$00`, `$01`, `$0f`, `$10` og `$ff` til binær. Del deretter `11110000` i to grupper på fire bits og finn hex-verdien.

## Kontrollpunkt

Du skal forstå bit, byte, binær, hexadecimal, `$`-notasjon og hvorfor to hex-sifre passer nøyaktig til én byte.

## Neste

Neste leksjon gjør bits og bytes om til verdier, words, minne og adresser.
