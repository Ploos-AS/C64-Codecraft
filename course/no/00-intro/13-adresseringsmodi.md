---
title: Adresseringsmodi — samme instruksjon, forskjellig kilde
course: 00-intro
lesson: 13
level: absolute-beginner
prerequisites: [12-foerste-fargetabell]
labs: [addressing-modes]
---

# Adresseringsmodi — samme instruksjon, forskjellig kilde

## Hva du skal lære

En addressing mode forteller CPU-en hvordan operanden skal tolkes. Du har allerede brukt flere former; nå setter vi navn på ideen.

```asm
lda #$06       ; immediate: selve verdien
lda $0400      ; absolute: les fra denne adressen
lda colours,x  ; absolute,X: baseadresse pluss X
```

Mnemonic er fortsatt `LDA`, men hvor verdien kommer fra er forskjellig.

## Hvorfor dette betyr noe

Addressing modes påvirker hva koden kan uttrykke, antall bytes og ofte cycle-kostnad. På 6510 er dette en del av CPU-modellen, ikke Codecraft-syntaks.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Valg av addressing mode kan være et valg mellom fleksibilitet, bytes og cycles. Timing-kritiske effekter kan senere avhenge av akkurat hvilken variant som brukes.

## Lab

For hvert eksempel: avgjør om operanden er en verdi, adresse eller baseadresse modifisert av X. Assembler og sammenlign kodestørrelsen.

## Kontrollpunkt

Du kan forklare addressing mode og kjenne igjen immediate, absolute og absolute,X.

## Neste

Nå går vi til en spesielt verdifull del av adresserommet: zero page.
