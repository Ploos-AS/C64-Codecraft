---
title: JSR, RTS og stack
course: 00-intro
lesson: 10
level: absolute-beginner
prerequisites: [09-foerste-fargeloop]
labs: [first-subroutine]
---

# JSR, RTS og stack

## Hva du skal lære

Hvordan kode kan legges i en subroutine, kalles med `JSR`, returnere med `RTS`, og hvilken rolle stack har uten at du trenger å mestre den ennå.

## Ideen

```asm
    lda #$06
    jsr set_border
    rts

set_border:
    sta $d020
    rts
```

`JSR` flytter kjøringen til en subroutine. CPU-en lagrer returinformasjon på stack. `RTS` bruker informasjonen til å fortsette etter kallet.

6502/6510-stack ligger i page 1, `$0100-$01ff`, og den 8-bit stack pointeren velger posisjon i denne siden.

## Bytes og cycles

`JSR absolute` = 3 bytes / 6 cycles. `RTS` = 1 byte / 6 cycles.

Subroutines kan gjøre kildekoden ryddigere og unngå duplisering, men kall er ikke gratis. Senere velger demo-kode bevisst mellom subroutines, inline code og unrolled code.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

En virkelig demo trenger struktur: init, music play, effect update, tegning og transitions. Subroutines hjelper med dette, mens timing-kritiske inner loops senere kan unngå JSR/RTS-overhead.

## Lab

Flytt en border-write til en subroutine. Single-step JSR/RTS i VICE og observer PC/SP dersom monitor-oppsettet ditt støtter det. Kall så rutinen med to forskjellige verdier i A.

## Kontrollpunkt

Du kan forklare subroutine, JSR, RTS, returinformasjon og den grunnleggende rollen til stack.

## Neste

Nå går vi fra hardkodede verdier til tabeller.
