---
title: Loading mens demoen fortsetter
course: 09-packing-loading
lesson: 06
level: advanced
prerequisites: [05-loader-basics]
labs: [loading-under-effects]
---
# Loading mens demoen fortsetter
En seamless transition kan kreve at music eller en visual effect lever videre mens data til neste part lastes.

Det gir konkurrerende krav til CPU time, interrupts, I/O, memory buffers og noen ganger drive communication timing.

Ikke start med å skrive fastloader. Definer først hva som må holdes levende og hvor mye interruption som tolereres. Mål deretter vanlig loader path og finn faktisk bottleneck.

## Resident core
En multipart production har ofte nytte av en bevisst liten resident region med bare state/code som virkelig må overleve mellom parts. Ownership skal dokumenteres.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Opplevd continuity er del av presentation. Loader engineering kan være like viktig for flow som selve effects.

## Lab
Hold én enkel frame-driven visual eller music-test levende rundt et kontrollert loading experiment. Dokumenter hva valgt loading method kan og ikke kan bevare.

## Neste
Vi definerer contracts mellom uavhengig bygde demo-parts.
