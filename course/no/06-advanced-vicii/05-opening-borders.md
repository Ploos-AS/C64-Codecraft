---
title: Åpne borders
course: 06-advanced-vicii
lesson: 05
level: advanced
prerequisites: [04-line-crunching]
labs: [06.05-opening-borders]
---
# Åpne borders
Normal C64-display har border-regions styrt av VIC-II display sequencing. Nøye timede endringer i display-control state kan påvirke når border state etableres eller slippes, slik at graphics kan bli synlig i områder som normalt dekkes av border.

Det finnes forskjellige vertical- og side-border-teknikker. De er ikke én generell «open border»-switch, og timing-kravene er forskjellige.

Leksjonen skiller først mekanismene og target assumptions. Executable code hører hjemme i target-specific labs med cycle annotations.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Åpne borders endrer de tilsynelatende fysiske grensene til standarddisplayet og ble et viktig visuelt kjennetegn ved avanserte C64-produksjoner.

## Lab
Reproduser én dokumentert border-opening-mekanisme på oppgitt VIC-II-target og verifiser den over mange frames før content legges til.

## Neste
Side-border-arbeid krever spesielt presis horizontal timing.
