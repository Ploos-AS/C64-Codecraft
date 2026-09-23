---
title: Bygg partens IRQ chain
course: 05-demo-architecture
lesson: 04
level: advanced
prerequisites: [03-memory-integration]
labs: [05.04-irq-chain-model]
---
# Bygg partens IRQ chain
Gjør raster-planen om til scheduled handlers.

Én handler kan kjøre music og general frame state i trygg region. En annen kan forberede stable rasterbar. En tredje kan endre $D016 eller annen display state for scroller-regionen.

Hver handler har eksplisitt jobb, budget og neste raster target.

Hold ownership tydelig: hvem acknowledge-er VIC-II source, hvem scheduler neste line, og hvilke registers/state må overleve hvert call.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
IRQ chain er timeline-controller i mange klassiske demo-parts. God struktur gjør cycle-critical code lettere å resonnere om.

## Lab
Implementer chain først med border colours som markerer hver handler. Legg inn ekte effect work først når schedulen er synlig korrekt.

## Neste
Vi kobler music cues til part state i stedet for å spre special cases gjennom IRQ-koden.
