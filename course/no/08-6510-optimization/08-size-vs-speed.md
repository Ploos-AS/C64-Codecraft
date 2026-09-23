---
title: Size, speed og production constraints
course: 08-6510-optimization
lesson: 08
level: advanced
prerequisites: [07-undocumented-opcodes]
labs: [08.08-size-vs-speed]
---
# Size, speed og production constraints
Raskest er ikke alltid best. En 4K intro, en one-file demo-part og en disk-loaded multipart production kan ha svært forskjellige constraints.

Mulige mål:
- minimum cycles i raster window;
- minimum code/data bytes;
- minimum load time;
- nok free memory til graphics/music;
- predictable timing;
- maintainable iteration før release.

Optimalisering av én metric kan skade en annen.

## Sizecoding mindset
Sizecoding oppmuntrer til reuse, computed data, overlappende roller og kompakte instruction choices. Speed coding kan i stedet bruke memory på tables og unrolled code. Begge er gyldige når production goal krever dem.

## Lab
Ta én routine og lag to varianter: primært optimized for cycles og primært for bytes. Dokumenter forskjellige valg uten å kåre en universell vinner.

## Neste
Vi avslutter med evidence-driven optimization av en virkelig effect.
