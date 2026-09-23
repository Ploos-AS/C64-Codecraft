---
title: Zero page — verdifullt lavt minne
course: 00-intro
lesson: 14
level: absolute-beginner
prerequisites: [13-adresseringsmodi]
labs: [zero-page]
---

# Zero page — verdifullt lavt minne

Zero page er de første 256 adressene, `$0000-$00ff`. Fordi høy adressebyte implisitt er null, kan mange 6502/6510-instruksjoner kode zero-page-access mer kompakt og ofte raskere enn absolute access.

## Viktig C64-realitet

Zero page er ikke et tomt scratchpad. C64-systemet, KERNAL/BASIC-miljøet og ditt eget program kan allerede bruke adresser der. `$00/$01` har dessuten en spesiell rolle på C64, blant annet for memory configuration via 6510 sin integrerte I/O-port.

Vi tar derfor ikke tilfeldige zero-page-adresser uten å forstå miljøet.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Zero page er knapp, nyttig og rask. Seriøs C64-kode fordeler den bevisst til hot variables og pointers. Ressursfordeling blir en del av effekt-design.

## Lab

Sammenlign assemblerte bytes og dokumenterte cycles for tilsvarende zero-page og absolute access. Forklar hvilken knapp ressurs optimaliseringen bruker.

## Kontrollpunkt

Du kjenner zero-page-området, hvorfor det er spesielt, og hvorfor adresser der må fordeles bevisst.

## Neste

To zero-page-bytes kan holde en adresse: en pointer.
