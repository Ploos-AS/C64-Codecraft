---
title: Bytes, words, minne og adresser
course: 00-intro
lesson: 03
level: absolute-beginner
prerequisites: [02-binaer-og-hex]
labs: []
---

# Bytes, words, minne og adresser

## Hva du skal lære

Hva en byte er, hva C64-programmerere mener med et word, hvordan minne kan forstås som nummererte lagringsplasser, og hva en adresse som `$d020` betyr.

## Ideen

Tenk på minnet som en lang rekke nummererte bokser. Hver boks har en **adresse** og kan holde én byte.

6510 har et 16-bit adresserom: 65 536 mulige adresser fra `$0000` til `$ffff`.

Et **word** i vanlig 6502/6510-sammenheng er 16 bits, altså to bytes, og kan representere en adresse i dette adresserommet.

Ikke alle adresser betyr vanlig RAM hele tiden. C64 kan mappe ROM og I/O-maskinvare inn i deler av det samme adresserommet.

## En første viktig adresse

Med normal C64 I/O-mapping er `$d020` VIC-II-registeret for border-fargen.

Når vi senere kjører:

```asm
sta $d020
```

ber vi ikke et grafikkbibliotek om å endre kanten. CPU-en skriver direkte til adressen VIC-II styres gjennom.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Kode, grafikk, musikk, tabeller, stack og hardware-registre trenger plass. Etter hvert blir selve minnelayouten en del av designet av demo-effekten.

## Kontrollpunkt

Du skal kunne forklare byte, word, adresse, 16-bit adresserom og forskjellen mellom en adresse og verdien som ligger eller skrives der.

## Neste

Neste leksjon møter vi selve 6510-prosessoren.
