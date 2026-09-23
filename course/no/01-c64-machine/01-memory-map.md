---
title: 64 KiB memory map
course: 01-c64-machine
lesson: 01
level: beginner
prerequisites: [00-intro/18-tabellstyrt-screen]
labs: [memory-map]
---

# 64 KiB memory map

6510 kan adressere $0000-$ffff: 65 536 CPU-adresser. Men en adresse viser ikke alltid den samme fysiske ressursen.

Viktige områder i normal C64-konfigurasjon:

- $0000-$00ff: zero page, med $00/$01 spesielle på C64
- $0100-$01ff: CPU stack page
- fra $0400: default screen RAM
- $a000-$bfff: BASIC ROM normalt synlig
- $d000-$dfff: I/O normalt synlig, blant annet VIC-II, SID, colour RAM og CIA
- $e000-$ffff: KERNAL ROM normalt synlig

Det finnes RAM under ROM/I/O i viktige områder. Hva CPU-en ser avhenger av memory configuration.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

En demo trenger bevisste plasseringer for kode, grafikk, musikk, tabeller og buffers. Banking kan gjøre skjult RAM tilgjengelig, mens hardware I/O må være synlig når registre skal brukes.

Memory layout er dermed en del av programarkitekturen.

## Lab

Tegn kartet og plasser kode/data fra tidligere leksjoner. Marker $0400, $d020 og $d800, og deretter ROM- og I/O-områdene.

## Kontrollpunkt

Du forstår 64 KiB CPU-adresserom og at synlig RAM/ROM/I/O avhenger av konfigurasjon.

## Neste

Nå ser vi på den spesielle 6510-porten på $00/$01.
