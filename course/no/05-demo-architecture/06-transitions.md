---
title: Entry, exit og transitions
course: 05-demo-architecture
lesson: 06
level: advanced
prerequisites: [05-part-state-og-cues]
labs: [part-transitions]
---
# Entry, exit og transitions
En demo-part trenger definerte grenser.

Ved entry etableres bare machine state parten eier: memory configuration, VIC-II state, IRQ policy, nødvendig CIA state, music relationship og effect-data.

Ved exit restaureres avtalt environment eller en dokumentert state leveres direkte til neste part.

En transition kan fade colours, flytte sprites, bytte screens eller forberede data for neste part mens nåværende effect fortsatt kjører.

## Ownership contract
Skriv ned hva parten antar, endrer og garanterer ved exit. Dette blir viktig når parts settes sammen av loader eller linkes inn i større production.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En spektakulær isolert effect er ikke ennå en demo. Parts må starte, sameksistere og overlevere kontroll pålitelig.

## Lab
Implementer entry, cue-triggered transition og exit til en enkel successor state.

## Neste
Vi kvalifiserer hele mini-demo-parten under emulator/debugger-observasjon.
