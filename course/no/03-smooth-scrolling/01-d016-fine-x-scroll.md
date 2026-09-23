---
title: $D016 fine X scrolling
course: 03-smooth-scrolling
lesson: 01
level: intermediate
prerequisites: [02-raster-timing/10-raster-splits]
labs: [fine-x-scroll]
---
# $D016 fine X scrolling
De lave tre X-scroll-bitene i $D016 lar VIC-II flytte character-display horisontalt i sub-character-steg. Andre bits i $D016 styrer andre display features og må bevares.

Fine scrolling alene flytter bare displayet innen et begrenset område. Det skaper ikke en endeløs strøm av nye characters.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Fine scroll er hardware-halvdelen av en klassisk smooth scroller. Den andre halvdelen er nøye timet vedlikehold av screen memory.

## Lab
Endre bare X-scroll-feltet i $D016 gjennom hele området mens andre bits bevares. Observer movement uten å endre screen RAM.

## Neste
Vi kombinerer fine movement med coarse row shift fra tidligere.
