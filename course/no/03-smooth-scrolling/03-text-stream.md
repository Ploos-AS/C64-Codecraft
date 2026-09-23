---
title: Gi scrolleren en text stream
course: 03-smooth-scrolling
lesson: 03
level: intermediate
prerequisites: [02-fine-pluss-coarse]
labs: [scroll-text-stream]
---
# Gi scrolleren en text stream
En scroller trenger state utenfor den synlige raden: pointer eller index inn i message-data.

```asm
message:
    .text "C64 CODECRAFT   "
    .byte 0
```

Ved hver coarse update hentes neste message-verdi, konverteres dersom source encoding krever det, skrives som screen code ved innkommende kant, og stream-posisjonen flyttes videre.

En terminator kan starte teksten på nytt, bytte message eller trigge annen handling.

## Hold representasjoner eksplisitte
Source text, PETSCII og screen codes er relaterte, men ikke identiske representasjoner. Ikke skjul konverteringer bak uforklarte konstanter.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En scroller er både effekt og data pipeline. Scene-produksjoner kan legge greetings, credits og synchronization commands i samme stream.

## Lab
Scroll en terminert message kontinuerlig. Legg til én dokumentert control value som endrer en ufarlig effect parameter i stedet for å vise et tegn.

## Neste
Nå lar vi colour bevege seg sammen med characters.
