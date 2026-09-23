---
title: Bygg et reproducible disk image
course: 09-packing-loading
lesson: 04
level: advanced
prerequisites: [03-memory-safe-depacking]
labs: [09.04-disk-image-contract]
---
# Bygg et reproducible disk image
Et disk image er et build artifact, ikke en manuelt kuratert mystery file.

Source tree skal beskrive hvilke files som går inn i image, C64-visible names/order der det betyr noe og hvordan image genereres. Clean build skal kunne gjenskape release-image fra source assets og tools.

Ikke commit copyrighted system ROMs bare for å gjøre emulator-start praktisk.

## Inspiser resultatet
Automated checks kan verifisere forventede directory entries og payload hashes/sizes der tooling støtter det. Emulator qualification er en separat concern.

## Lab
Generer en .d64 med boot/entry-program og minst to part/data-files og verifiser directory fra build.

## Neste
Vi skiller vanlig file loading fra en demo-loader architecture.
