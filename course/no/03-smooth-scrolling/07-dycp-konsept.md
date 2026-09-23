---
title: DYCP-konseptet
course: 03-smooth-scrolling
lesson: 07
level: intermediate
prerequisites: [06-phase-shifted-sine]
labs: [03.07-dycp-concept]
---
# DYCP-konseptet
**DYCP** betyr *Different Y Character Positions*. I stedet for at alle characters i scrolleren deler samme vertikale baseline kan hvert tegn vises på forskjellig Y-posisjon, ofte langs en bølge.

Et vanlig character screen er cell-basert, så vilkårlig per-character vertical pixel placement er ikke gratis. En DYCP trenger derfor en representation og update-strategi som skaper eller rekonstruerer character-bildet ved ønsket offset.

Det finnes flere historiske implementation families. Codecraft bygger først én forståelig variant og sammenligner senere alternativer i stedet for å hevde at én algoritme er universell.

## Design før kode
For hvert synlig character spør vi:

- hvilket source glyph trengs?
- hvilken vertical offset ønsker phase?
- hvilke destination character-data må genereres eller velges?
- hvor mye arbeid skjer per frame?
- hva kan precalculates?

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
DYCP er et klassisk steg fra «scroll tekst» til å manipulere character graphics som effect-data under stramt frame budget.

## Lab
Design en åtte-character wave på papir. Noter glyph, phase, ønsket vertical offset og nødvendige output rows.

## Neste
Vi konstruerer shifted character-data fra source glyphs.
