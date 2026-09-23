---
title: Phase-shifted sine movement
course: 03-smooth-scrolling
lesson: 06
level: intermediate
prerequisites: [05-raster-scheduled-scroller]
labs: [phase-shifted-sine]
---
# Phase-shifted sine movement
Ett sine lookup flytter ett objekt periodisk. Flere lookups med forskjellige phase offsets lager en bølge.

```text
y0 = sine[phase + 0]
y1 = sine[phase + step]
y2 = sine[phase + 2*step]
...
```

På 6510 arrangerer vi normalt tables og indices slik at runtime-arbeidet blir billig. En duplisert eller passende dimensjonert table kan noen ganger fjerne wrap-checks fra critical path; vi bruker memory for å spare cycles.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Phase offsets gjør én liten tabell til koordinert movement for mange elementer. Ideen går igjen i sprite formations, logoer, plasma-lignende indexing og scrollers.

## Lab
Bruk én sine table til flere sprite Y-posisjoner med ulike phases. Sammenlign runtime wrap-check med table-layout som unngår den.

## Neste
Vi bruker samme phase-idé på characters i stedet for sprites.
