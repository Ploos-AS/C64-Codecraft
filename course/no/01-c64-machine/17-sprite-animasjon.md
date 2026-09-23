---
title: Sprite-animasjon som data
course: 01-c64-machine
lesson: 17
level: beginner
prerequisites: [16-multicolor-sprites]
labs: [sprite-animation]
---

# Sprite-animasjon som data

En sprite pointer velger en 64-byte slot. Det gjør frame-animasjon enkel: plasser flere sprite frames i passende slots og endre pointer-byte i stedet for å kopiere 63 bytes hver frame.

Konseptuelt:

```asm
    ldx anim_phase
    lda frame_pointers,x
    sta screen_base + $03f8
```

For sprite 0 ligger pointeren på screen_base + $03f8. Eksakte pointer-verdier avhenger av hvor frames ligger i aktiv VIC-bank.

## Copy eller switch?

To strategier:

- kopier nye bitmap-bytes til én sprite-slot;
- behold flere frames og bytt pointer.

Pointer switching bruker mer memory, men mye mindre CPU-tid per frame. Kopiering kan spare VIC-visible memory, men bruker bandwidth.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Dette er samme memory-versus-time-valg som ved character animation, nå direkte koblet til VIC-II object hardware. Scene-kode vinner ofte ved å velge riktig representasjon før instruction optimization begynner.

## Lab

Plasser minst to sprite frames i aligned slots. Lag en pointer table og animer sprite 0 ved å bytte pointer. Kombiner dette med sine movement-tabellen fra tidligere.

## Kontrollpunkt

Du kan beregne sprite pointer values og animere ved frame switching i stedet for blind bitmap-kopiering.

## Neste

Graphics-grunnlaget er nå sterkt nok for neste hovedtema: raster timing, interrupts og smooth hardware-synkroniserte effekter.
