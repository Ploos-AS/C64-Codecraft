---
title: Én SID voice
course: 04-sid-music
lesson: 02
level: intermediate
prerequisites: [01-moet-sid]
labs: [first-sid-voice]
---
# Én SID voice
For å forstå en player senere styrer vi først én voice direkte.

Et nyttig eksperiment setter frequency, waveform/control og ADSR og bruker gate-bit til å starte og release en note. Eksakt frequency-registerverdi avhenger av SID clock/model assumptions, så laben navngir target eksplisitt.

Ikke bland oscillator waveform og envelope: waveform bestemmer den repeterende formen; ADSR former amplitude over tid.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Du trenger ikke bli SID-composer for å skrive demoer, men forståelse av hva playeren endrer hjelper ved debugging av silence, conflicts og timing-sensitive integration.

## Lab
Lag én tone, endre frequency og endre deretter attack/release. Beskriv den hørbare forskjellen.

## Neste
I stedet for å komponere soundtrack i assembler integrerer vi et eksisterende SID player-interface.
