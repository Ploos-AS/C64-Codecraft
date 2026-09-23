---
title: Border som timing probe
course: 02-raster-timing
lesson: 06
level: intermediate
prerequisites: [05-badlines]
labs: [02.06-border-timing-probe]
---
# Border som timing probe
En border-colour-write gir et synlig merke for når kode kjører relativt til raster.

```asm
    inc $d020
    ; koden som måles
    dec $d020
```

Dette er ikke alene et presisjonsinstrument, men det visualiserer CPU-tid svært godt. Et bredere farget område betyr at mer tid gikk mellom writene.

## Mål bevisst
Hold target-maskinmodell fast. Vit om interrupts, badlines eller sprite DMA kan forekomme i måleområdet. For eksakt arbeid kombinerer vi visuell probe med emulator/debugger cycle-info.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Border timing gjør usynlig execution cost synlig. Border er et klassisk praktisk timing/debug-verktøy i scene-koding.

## Lab
Mål to rutiner med border writes. Forutsi hvilken som er raskest fra cycle counts før kjøring.

## Neste
Vi bruker proben til å se IRQ entry jitter.
