---
title: STA og ditt første synlige C64-resultat
course: 00-intro
lesson: 06
level: absolute-beginner
prerequisites: [05-lda-immediate]
labs: [first-border-colour]
---

# STA og ditt første synlige C64-resultat

## Hva du skal lære

Hvordan `STA` lagrer A til en adresse, og hvordan `LDA` + `STA` kan styre border-fargen via VIC-II.

```asm
lda #$06
sta $d020
```

Første instruksjon legger `$06` i A. Den andre skriver A til `$d020`, VIC-II-registeret for border-farge ved normal I/O-mapping.

- `#$06` = **verdien $06**
- `$d020` = **adressen $d020**

Det finnes ikke noe grafikk-framework mellom koden og VIC-II.

## Bytes og cycles

```text
A9 06       ; LDA #$06 — 2 bytes, 2 cycles
8D 20 D0    ; STA $D020 — 3 bytes, 4 cycles
```

Totalt: **5 bytes og 6 cycles**.

Adressen ligger som `20 D0` i instruksjonen. 6502-familien lagrer 16-bit operand-adresser med lav byte først. Little-endian kommer vi tilbake til senere.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Velg eller beregn en verdi og skriv den til hardware på riktig tidspunkt: dette grunnmønsteret vokser senere til rasterbars, splits og langt mer avanserte effekter.

## Lab

Bygg programmet med vanlig 64tass. Kjør det i VICE. Endre fargen og forutsi resultatet. Finn bytes `A9 06 8D 20 D0` i output.

**Challenge:** finn VIC-II-adressen for background colour i C64-referansematerialet og sett både border og bakgrunn uten en Codecraft-API.

## Kontrollpunkt

Du skal kunne forklare verdi mot adresse, `LDA`, `STA`, og hvorfor en write til `$D020` endrer border.

## Neste

Nå trenger vi tellere og repetisjon.
