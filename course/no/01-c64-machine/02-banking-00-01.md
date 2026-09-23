---
title: Banking med $00 og $01
course: 01-c64-machine
lesson: 02
level: beginner
prerequisites: [01-memory-map]
labs: [01.02-banking]
---

# Banking med $00 og $01

6510 skiller seg fra en vanlig 6502 ved å ha en liten integrert I/O-port. Data-direction register ligger på $0000 og data register på $0001.

På C64 deltar lave bits knyttet til LORAM, HIRAM og CHAREN i å bestemme om BASIC ROM, KERNAL ROM, character ROM eller I/O er synlig i deler av CPU-adresserommet.

Dette er **banking**: vi endrer hva CPU-adresser viser uten å endre selve 16-bit-adressen.

## Vær forsiktig

$00/$01 er grunnleggende maskinkonfigurasjon, ikke tilfeldige scratch-bytes. Feil endring kan skjule ROM eller I/O og ødelegge for kode som forventer dem.

Skill også mellom CPU visibility og VIC-II memory access. VIC-II har sitt eget perspektiv og egne banking-regler.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Banking lar programmer bruke RAM under ROM og kontrollere når I/O eller character ROM er synlig. Det er verdifullt når kode, musikk, grafikk og buffers skal få plass i 64 KiB.

## Lab

Inspiser $00/$01 i VICE i et normalt miljø. Bruk referansedokumentasjon til å dekode relevante bits før noe endres. Forutsi hvilke områder som blir synlige i en foreslått konfigurasjon.

## Kontrollpunkt

Du forstår rollen til $00/$01, LORAM/HIRAM/CHAREN og at CPU-banking ikke er det samme som VIC-II-banking.

## Neste

Med I/O synlig kartlegger vi VIC-II-registerblokken.
