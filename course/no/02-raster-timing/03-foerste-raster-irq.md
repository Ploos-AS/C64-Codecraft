---
title: Din første raster IRQ
course: 02-raster-timing
lesson: 03
level: intermediate
prerequisites: [02-d011-d012]
labs: [first-raster-irq]
---
# Din første raster IRQ
En VIC-II raster interrupt kan be om CPU-oppmerksomhet ved en programmert raster line.

Grunnstegene er: installer IRQ-handler passende for execution environment; velg linje via $D011/$D012; enable raster IRQ via $D01A; acknowledge VIC-II source via $D019; bevar nødvendig machine state; og returner korrekt.

Vector-oppsett er forskjellig for KERNAL-samarbeid og mer fullstendig takeover. Vi lærer begge uten en skjult wrapper.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Raster IRQ planlegger arbeid relativt til beam uten å bruke hele framen på polling. Det ligger bak raster splits, music scheduling og mange effekter.

## Lab
Installer minimal raster IRQ i dokumentert lab-miljø og endre $D020 kort i handleren. Bruk border som timing probe.

## Neste
IRQ kommer til riktig område, ikke automatisk eksakt cycle. Nå teller vi cycles.
