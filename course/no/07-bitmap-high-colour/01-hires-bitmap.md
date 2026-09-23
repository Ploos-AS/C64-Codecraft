---
title: Hires bitmap mode
course: 07-bitmap-high-colour
lesson: 01
level: advanced
prerequisites: [06-advanced-vicii/07-composing-vicii-tricks]
labs: [hires-bitmap]
---
# Hires bitmap mode
Bitmap mode endrer hvordan VIC-II tolker display memory. I stedet for å velge character glyphs for hver screen-cell leverer bitmap-data pixel patterns, mens screen memory bidrar med colour-information.

En standard bitmap bruker 8000 bytes for 320x200 pixel-feltet. Organiseringen er fortsatt sterkt knyttet til 8x8 display-cells og er ikke en enkel moderne linear framebuffer.

Layouten betyr mye for plotting, image conversion og scheduled updates.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Bitmap mode gir pixel-level artwork, men bruker mye mer memory enn charset. Cell-layout må forstås før converters eller avanserte bitmap tricks brukes.

## Lab
Lag et lite generated test pattern, finn bytes i bitmap memory og verifiser hvordan tilhørende screen-memory colour-data påvirker bildet.

## Neste
Vi bytter horizontal resolution mot flere colour choices i multicolor bitmap mode.
