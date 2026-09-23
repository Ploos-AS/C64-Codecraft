---
title: Side-border timing
course: 06-advanced-vicii
lesson: 06
level: advanced
prerequisites: [05-opening-borders]
labs: [06.06-side-border-timing]
---
# Side-border timing
En side-border-effect krever register activity innenfor et smalt horizontal timing window. Raster-line synchronization alene er derfor ikke nok: critical write må skje på riktig cycle phase.

Alt vi har lært virker nå sammen:
- IRQ jitter og stabilization;
- instruction-cycle accounting;
- page-cross behaviour;
- badlines;
- sprite DMA;
- deterministic code paths;
- VIC-II model differences.

## Engineer pathen
Start fra stable entry point. Tell cycles frem til critical write. Hold path deterministisk og bevis timingen med instrumentation/debugger evidence.

Ikke cargo-cult en kjede NOPs. En delay har bare mening relativt til kjent entry phase og target.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Dette er cycle-exact coding i tydelig form: synlig hardware-resultat avhenger av at en write lander i et svært lite timing window.

## Lab
Lag minimalt target-specific side-border timing experiment og dokumenter cycle path fra stabilized entry til critical write.

## Neste
Vi lærer å kombinere avanserte tricks uten å ødelegge timing assumptions.
