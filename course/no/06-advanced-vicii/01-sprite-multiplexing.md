---
title: Sprite multiplexing
course: 06-advanced-vicii
lesson: 01
level: advanced
prerequisites: [05-demo-architecture/07-mini-demo-kvalifisering]
labs: [06.01-sprite-multiplex-model]
---
# Sprite multiplexing
VIC-II eksponerer åtte hardware sprites, men sprite-enhetene kan gjenbrukes på forskjellige vertikale posisjoner i samme frame.

En sprite multiplexer holder en større logical sprite-list, bestemmer hvilke objects som skal vises neste og skriver hardware-sprite state på nytt etter at tidligere bruk er trygt ferdig.

Første versjon prioriterer correctness:
- sorter eller schedule logical sprites etter Y;
- tildel hardware sprite slots;
- oppdater position, pointer, colour og mode state;
- schedule updates før hvert reuse point;
- definer hva som skjer når behovet overstiger tilgjengelig tid/slots.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Multiplexing gjør timing-kunnskap til en tilsynelatende hardware-utvidelse. Det er et klassisk eksempel på å få mer ut av maskinen ved scheduling.

## Lab
Vis mer enn åtte logical sprites ved separate Y-posisjoner. Instrumenter hvert reuse point med border/debugger.

## Neste
Vi studerer hvorfor sprite DMA endrer cycle budget rundt reuse points.
