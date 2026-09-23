---
title: Din første hardware-sprite
course: 01-c64-machine
lesson: 12
level: beginner
prerequisites: [11-character-scrolling]
labs: [first-sprite]
---

# Din første hardware-sprite

VIC-II har åtte hardware sprites. En standard monochrome sprite er 24x21 pixels og bruker 63 bytes bitmap-data, vanligvis plassert i en 64-byte-aligned slot.

Sprite pointer-bytes ligger på slutten av aktiv 1 KiB screen matrix. En pointer velger en 64-byte-blokk innenfor gjeldende VIC-bank.

For å vise sprite 0 trenger du minst:

1. sprite bitmap-data i VIC-synlig minne;
2. korrekt sprite 0 pointer;
3. X/Y position registers;
4. sprite colour;
5. sprite 0 enabled.

Viktige registre inkluderer $d000/$d001 for sprite 0-posisjon, $d015 for enable og $d027 for sprite 0-colour.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Sprites gir uavhengig posisjonert grafikk uten å skrive om screen under dem. De blir byggesteiner for logoer, objekter, sprite scrollers og senere multiplexing langt forbi den nominelle grensen på åtte sprites.

## Lab

Lag en enkel monochrome sprite, plasser den i en korrekt aligned VIC-visible slot, beregn sprite pointer og vis sprite 0. Flytt X/Y og endre fargen.

## Kontrollpunkt

Du forstår sprite-datastørrelse, 64-byte slot/pointer-adressering, grunnregistrene og stegene som kreves for å vise én sprite.

## Neste

Neste flytter vi spriten fra en tabell og møter 9-bit X-position.
