---
title: Bygg et lite custom charset
course: 01-c64-machine
lesson: 09
level: beginner
prerequisites: [08-foerste-custom-character]
labs: [small-custom-charset]
---

# Bygg et lite custom charset

Et monochrome C64-character bruker åtte bytes. Et komplett sett med 256 characters bruker derfor 2048 bytes, og character N starter på charset_base + N*8.

```text
character 0 -> base + 0*8
character 1 -> base + 1*8
character 2 -> base + 2*8
...
```

En liten effekt trenger ikke bruke alle tegnene, men VIC-II-strukturen reserverer fortsatt posisjoner i charset.

## Fra ett tegn til assets

Definer flere relaterte former: animation frames, logo tiles eller deler av et mønster. Legg screen codes i screen RAM for å komponere større grafikk.

Hold kildeformatet forståelig først. Asset converters kan senere generere samme byteformat fra mer grafiske workflows.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Character mode bytter fleksibilitet mot kompakte data. Gjenbruk av 8-byte tiles kan bygge mye større grafikk, og endring av character-data kan animere alle screen-celler som peker på samme character.

## Lab

Lag fire custom characters og arranger screen codes som en liten 2x2-grafikk. Beregn byte-offset for hvert tegn før du assemblerer.

## Kontrollpunkt

Du kan beregne character offsets og bruke flere custom characters som gjenbrukbare graphics assets.

## Neste

Nå utnytter vi gjenbruk direkte ved å animere character-data.
