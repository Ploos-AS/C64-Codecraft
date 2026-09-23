---
title: Sett sammen en multipart demo
course: 09-packing-loading
lesson: 08
level: advanced
prerequisites: [07-part-contracts]
labs: [multipart-demo]
---
# Sett sammen en multipart demo
En multipart demo er nå en sekvens av eksplisitte states:

```text
boot -> load/depack part A -> run A
     -> transition/load B -> run B
     -> transition/load C -> run C
     -> ending
```

Det interessante arbeidet ligger i boundaries: hva forblir resident, når loading skjer, hvor packed data ligger, når depacking er trygt og hvilken machine state leveres videre.

Bygg hver part uavhengig og integrer via dokumenterte contracts.

## Failure paths
Development builds skal gjøre loader/depacker failures synlige i stedet for å hoppe til invalid memory. Release behaviour kan være kompakt, men debugging trenger evidence.

## Lab
Koble minst tre små teaching-parts til en repeatable sequence fra ett disk image.

## Neste
Vi kvalifiserer disken som reproducible scene release artifact.
