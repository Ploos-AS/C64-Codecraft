---
title: Møt CIA1 og CIA2
course: 01-c64-machine
lesson: 04
level: beginner
prerequisites: [03-vic-ii-register-map]
labs: [cia-map]
---

# Møt CIA1 og CIA2

C64 har to 6526 Complex Interface Adapters.

CIA1 ligger på $dc00-$dc0f og brukes mye til keyboard/joystick I/O og timers. CIA2 ligger på $dd00-$dd0f og deltar blant annet i serial/user-port-funksjoner, timers og valg av VIC-II sin 16 KiB memory bank.

Hver CIA har I/O-porter, to timers, time-of-day clock og interrupt-kontroll.

## Ikke bland CIA-timing og raster-timing

CIA timers kan generere interrupts og gi timing, men VIC-II raster position er en annen hardware-tidslinje. Senere kan demo-kode bevisst bruke eller slå av forskjellige interrupt sources.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

CIA2 påvirker hvilken 16 KiB-bank VIC-II ser. CIA timers og interrupts betyr også noe når demoen tar kontroll over en maskin som normalt har KERNAL-styrte interrupts.

## Lab

Finn CIA1/CIA2-registerblokkene og identifiser port A/B, timer-registre og interrupt-control register i referansedokumentasjon. Finn CIA2-bitene som er knyttet til VIC bank selection, men ikke endre dem blindt ennå.

## Kontrollpunkt

Du kjenner de to CIA-chipene, adressene deres, hovedrollene og hvorfor CIA2 er viktig for VIC-II memory selection.

## Neste

Neste kombinerer vi CPU-banking, VIC-banking og memory placement til en praktisk scene-orientert memory plan.
