---
title: Din første fargeloop
course: 00-intro
lesson: 09
level: absolute-beginner
prerequisites: [08-compare-og-branch]
labs: [colour-loop]
---

# Din første fargeloop

Nå kombinerer vi teller, register-transfer, VIC-II-write og branch.

```asm
    ldx #$00

loop:
    txa
    sta $d020
    inx
    cpx #$10
    bne loop
```

Hver iterasjon kopierer X til A, skriver A til border-fargeregisteret, øker X og går tilbake så lenge X ikke har nådd `$10`.

## Hva ser du egentlig?

CPU-en er mye raskere enn menneskesynet. Du skal derfor **ikke forvente 16 tydelige, rolige fargetrinn**.

Forskjellen mellom CPU-hastighet, display-timing og det øyet oppfatter er selve læringspoenget. Senere synkroniserer vi effekter mot VIC-II-rasteren i stedet for å gjette med delay-loops.

## Bytes og cycles

De fleste iterasjonene tar branchen; den siste gjør det ikke. Allerede denne lille effekten har derfor forskjellig control-flow timing på siste runde.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Vi har allerede byggesteiner til en effekt: state, en verdi som endres, hardware-write og repetisjon. Men vi mangler synkronisering.

Neste scene-spørsmål blir derfor ikke bare «endrer fargen seg?», men:

**Når endres den? Hvor ofte? Hvor befinner rasterstrålen seg akkurat da?**

Dette leder senere direkte til rasterbars og cycle-exact kode.

## Lab

Kjør loopen i VICE. Endre start/sluttverdier. Fjern `TXA` og forklar hvorfor X ikke lenger påvirker verdien `STA` skriver. Single-step noen iterasjoner og observer X, A og `$D020`.

**Challenge:** lag en variant som går baklengs gjennom et fargeområde med instruksjonene vi allerede har lært.

## Kontrollpunkt

Du kan nå kombinere registre, transfer, hardware-store, increment, compare og branch til en ekte liten C64-loop, og har møtt den første praktiske grunnen til at timing betyr noe.

## Neste

Neste bygger vi gjenbrukbare rutiner med `JSR`, `RTS` og stack.
