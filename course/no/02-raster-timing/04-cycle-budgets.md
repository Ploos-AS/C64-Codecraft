---
title: Cycle budgets
course: 02-raster-timing
lesson: 04
level: intermediate
prerequisites: [03-foerste-raster-irq]
labs: [cycle-budget]
---
# Cycle budgets
Instruction-cycle-tall blir nå et budsjett. For en bestemt VIC-II-modell har en raster line fast timing-struktur, mens VIC-II også kan ta bus-tid fra CPU-en.

Tell execution paths, ikke bare mnemonics. Branches, page crossings, interrupt entry/exit og data-dependent paths endrer timing.

```text
LDA #imm       2
STA abs        4
BNE taken      3
BNE not taken  2
```

Oppgi aldri line-cycle-konstant uten target video standard/model.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Cycle budgeting gjør «raskt nok» til planleggbar engineering.

## Lab
Tell en kort border-rutine for hånd og sammenlign med debugger-observasjoner på valgt modell.

## Neste
VIC-II tar noen ganger en stor strukturert del av budsjettet: badlines.
