---
title: Character-animasjon
course: 01-c64-machine
lesson: 10
level: beginner
prerequisites: [09-custom-charset]
labs: [01.06-char-animation]
---

# Character-animasjon

Hvis flere screen-celler bruker samme screen code, peker de på samme character shape. Endrer vi formen, kan alle cellene endres samtidig.

En enkel metode er å ha flere 8-byte frames og kopiere valgt frame inn i aktiv character-slot.

```asm
    ldx #$07
copy_frame:
    lda frame1,x
    sta charset_base + 8,x
    dex
    bpl copy_frame
```

Her møter vi `BPL`: branch så lenge negative flag er clear. Start på 7 og decrement for å kopiere nøyaktig åtte bytes.

## Data mot bandwidth

Animasjon er ikke gratis. Oppdatering av character RAM bruker CPU-cycles og memory bandwidth. Noen ganger er det billigere å lagre flere characters og endre screen codes; andre effekter tjener på å modifisere charset direkte.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Demoer bytter hele tiden memory mot CPU time. Character animation viser dette tidlig: lagre flere frames, kopiere data, endre data in-place eller endre references.

## Lab

Animer ett character mellom to 8-byte frames. Legg samme screen code i flere celler og observer hvordan én charset-update påvirker alle.

## Kontrollpunkt

Du forstår character reuse, frame-data og memory-versus-CPU-avveiningen.

## Neste

Før smooth pixel scrolling lærer vi coarse character scrolling.
