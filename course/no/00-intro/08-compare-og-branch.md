---
title: Compare, flagg og branches
course: 00-intro
lesson: 08
level: absolute-beginner
prerequisites: [07-x-y-og-tellere]
labs: []
---

# Compare, flagg og branches

## Hva du skal lære

Hvordan `CPX` sammenligner X med en verdi, hvordan zero flag kan vise equality, og hvordan `BNE` endrer programflyten.

```asm
loop:
    inx
    cpx #$10
    bne loop
```

`CPX` sammenligner uten å erstatte X. Etter denne sammenligningen kan `BNE` — **Branch if Not Equal** — hoppe tilbake så lenge verdiene ikke er like.

En branch er ikke en skjult loop-funksjon. Den endrer hvor PC fortsetter kjøringen.

## Bytes og cycles

Conditional branches bruker relative addressing. En branch bruker 2 cycles når den ikke tas, normalt 3 når den tas, og én ekstra cycle hvis en tatt branch krysser en page boundary.

Du trenger ikke optimalisere plasseringen ennå. Poenget er viktig: **control flow kan endre timing**.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Loops sparer kode, men branchene påvirker timing. Senere kan én cycle være forskjellen mellom en stabil rastereffekt og synlig jitter.

## Lab

Trace en loop fra X=`$0d` til `$10`. Noter X, resultatet av sammenligningen og om BNE tas.

## Kontrollpunkt

Du skal forstå comparison, zero flag, conditional branch og hvorfor branch-timing ikke alltid er konstant.

## Neste

Nå kobler vi loopen til VIC-II.
