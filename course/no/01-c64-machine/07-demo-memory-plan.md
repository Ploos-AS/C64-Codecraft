---
title: Planlegg minnet før effekten
course: 01-c64-machine
lesson: 07
level: beginner
prerequisites: [06-d018-screen-og-charset]
labs: []
---

# Planlegg minnet før effekten

En demo-part er enklere å bygge når store memory users planlegges før de kolliderer.

En enkel plan kan reservere områder for:

- programkode;
- zero-page variables/pointers;
- stack;
- screen matrix;
- custom charset;
- sprite-data;
- music og player;
- effect tables;
- midlertidige buffers.

Eksakte adresser avhenger av part, toolchain, loader og hardware configuration. Codecraft har ingen universell runtime-layout.

## Constraints betyr noe

Spør for hvert område:

1. Må CPU lese/skrive det?
2. Må VIC-II hente det?
3. Må ROM eller I/O være synlig samtidig?
4. Kreves alignment?
5. Kan page crossing skade timing?
6. Kan data gjenbrukes eller kastes etter init?

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Memory planning er optimalisering før instruction optimization. God layout kan gjøre grafikk tilgjengelig, frigjøre RAM under ROM, forenkle pointers og fjerne timing penalties.

## Lab

Lag et memory-map-dokument for en tenkt one-part demo med screen, ett 2 KiB charset, sprite-data, music, code og tables. Marker CPU- og VIC-II-krav separat.

## Kontrollpunkt

Du kan resonnere om memory placement som hardware/software-constraints i stedet for å kopiere faste adresser.

## Neste

Nå lager vi character-data selv og peker VIC-II på dem.
