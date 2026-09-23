---
title: En reproducible graphics pipeline
course: 07-bitmap-high-colour
lesson: 03
level: advanced
prerequisites: [02-multicolor-bitmap]
labs: [07.03-asset-pipeline]
---
# En reproducible graphics pipeline
Reelle productions skriver sjelden tusenvis av bitmap-bytes manuelt. Artwork lages eller konverteres med eksterne tools og assembleres deretter inn i produksjonen.

En god pipeline dokumenterer:
- source asset;
- converter/tool og version;
- command/options;
- target C64-format;
- generated bitmap/screen/colour-data;
- load addresses eller linker placement;
- palette/dithering assumptions.

Generated output kan erstattes; recipe og lovlig source asset er de viktige reproducible inputs.

## Ingen opaque magic
Inspiser små generated samples og sammenlign dem med formatet fra forrige leksjon. En converter sparer arbeid; den erstatter ikke forståelse.

## Lab
Konverter eller generer et lite lovlig course-owned image og reproduser identiske C64-data fra clean checkout.

## Neste
Vi endrer display state mens selve bitmapet tegnes.
