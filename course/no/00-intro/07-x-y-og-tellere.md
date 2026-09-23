---
title: X, Y og tellere
course: 00-intro
lesson: 07
level: absolute-beginner
prerequisites: [06-sta-foerste-synlige-resultat]
labs: []
---

# X, Y og tellere

X og Y er 8-bit registre som blant annet passer godt som tellere og indekser.

```asm
ldx #$00
inx
inx
```

Etter dette inneholder X `$02`.

Vi kan bruke `INX`, `INY`, `DEX` og `DEY` til å endre registrene ett steg. Siden de er 8-bit vil `$ff + 1` wrappe til `$00`.

## Bytes og cycles

`LDX #value` = 2 bytes / 2 cycles.  
`INX` = 1 byte / 2 cycles.

Vi måler før vi begynner å optimalisere.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Tellere og indekser brukes til fargetabeller, skjermposisjoner, sprites, lookup tables og etter hvert sine tables og animasjon.

## Lab

Følg X på papir fra `$00` til `$05`. Start så på `$fe` og observer `$fe → $ff → $00`.

## Kontrollpunkt

Du skal forstå X/Y som 8-bit tellere/indekser og wraparound.

## Neste

En teller blir virkelig nyttig når programmet kan bestemme om det skal fortsette.
