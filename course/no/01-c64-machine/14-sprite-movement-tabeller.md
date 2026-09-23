---
title: Sprite movement-tabeller
course: 01-c64-machine
lesson: 14
level: beginner
prerequisites: [13-sprite-posisjonering]
labs: []
---

# Sprite movement-tabeller

En movement table inneholder posisjoner som er forberedt på forhånd.

```asm
    ldx phase
    lda xpos,x
    sta $d000
    lda ypos,x
    sta $d001
```

Når `phase` økes velges neste koordinatpar. Ved slutten av tabellen wrap-er vi tilbake.

For 9-bit X kan den niende biten ligge i en companion table eller utledes kontrollert.

## Hvorfor tabeller?

Kompleks movement kan være dyr å beregne hver frame. Precalculated tables bytter memory mot forutsigbart runtime-arbeid.

Tabellen kan lages for hånd, genereres av script eller eksporteres fra et verktøy. Runtime-formatet er fortsatt vanlige bytes som 6510 leser direkte.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Precalculation er en sentral demoscene-teknikk. En tabell kan gjøre dyr matematikk om til noen få indexed loads med forutsigbar timing.

## Lab

Lag en kort X/Y-path og animer sprite 0 gjennom den. Legg til wrapping og estimer instruction-kostnaden per update.

## Kontrollpunkt

Du kan drive sprite movement fra data med phase/index og forklare memory-versus-runtime-avveiningen.

## Neste

Nå genererer vi en klassisk movement table: sine wave.
