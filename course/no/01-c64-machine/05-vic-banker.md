---
title: VIC-II sine 16 KiB-banker
course: 01-c64-machine
lesson: 05
level: beginner
prerequisites: [04-moet-cia]
labs: [01.03-vic-bank-d018]
---

# VIC-II sine 16 KiB-banker

VIC-II ser ikke bare CPU-ens komplette 64 KiB-adresserom. For graphics fetches arbeider den innenfor én 16 KiB-bank om gangen.

CIA2 port A deltar i valget mellom:

- $0000-$3fff
- $4000-$7fff
- $8000-$bfff
- $c000-$ffff

CIA2-bitene for bankvalg er active-low, så bitmønsteret er lett å lese feil. Utled alltid ønsket bank fra en pålitelig referanse og bevar andre port-bits når registeret endres.

## CPU view mot VIC-II view

CPU banking via $00/$01 og VIC-II bank selection løser forskjellige problemer. Dette skillet må være klart før screen- eller character-data flyttes.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

En VIC-bank er et 16 KiB graphics workspace. Screen matrices, character sets, bitmap-data og sprite-data må ligge der VIC-II kan hente dem. Bankvalget legger derfor føringer på memory layout for en effekt eller demo-part.

## Lab

Tegn alle fire 16 KiB-bankene. Velg én og marker mulige steder for screen og character data. Ikke skriv CIA2 blindt; finn først hvilke bits som må bevares.

## Kontrollpunkt

Du forstår at VIC-II bruker én valgt 16 KiB-bank og at dette er noe annet enn CPU banking via $00/$01.

## Neste

Innenfor banken forteller $D018 hvor viktige display-data ligger.
