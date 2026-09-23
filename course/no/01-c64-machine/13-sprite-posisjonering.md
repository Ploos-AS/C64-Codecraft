---
title: Sprite movement og 9-bit X
course: 01-c64-machine
lesson: 13
level: beginner
prerequisites: [12-foerste-sprite]
labs: [01.09-sprite-9bit-x]
---

# Sprite movement og 9-bit X

Sprite Y-position passer i én byte. X trenger ni bits fordi koordinatområdet går forbi 255.

For sprite 0 skrives de lave åtte X-bitene til $d000. Den niende X-biten er bit 0 i $d010. De andre bitene i $d010 tilhører de andre spritene, så de må bevares.

Dette gir oss en viktig grunn til å lære read-modify-write på bits i stedet for å overskrive et helt hardware-register blindt.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Sprite movement krysser ofte 255-grensen. Delte bit-registre som $d010 lærer samtidig en viktig hardware-vane: endre bare bitene du faktisk eier.

## Lab

Flytt sprite 0 til posisjoner både under og over 255. Observer hoppet når niende bit mangler, og implementer så korrekt high-bit-håndtering uten å ødelegge bits for andre sprites.

## Kontrollpunkt

Du forstår hvorfor sprite X er 9-bit og hvorfor $d010 må behandles forsiktig.

## Neste

Nå driver vi X/Y fra tabeller i stedet for å beregne alle posisjoner i hot path.
