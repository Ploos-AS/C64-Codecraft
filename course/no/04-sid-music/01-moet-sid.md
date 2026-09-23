---
title: Møt SID
course: 04-sid-music
lesson: 01
level: intermediate
prerequisites: [03-smooth-scrolling/10-dycp-optimalisering]
labs: [04.01-sid-register-map]
---
# Møt SID
C64 SID er en programmerbar sound chip med tre voices samt shared filter- og volume/control-funksjoner. Hovedområdet starter ved $D400.

Hver voice har registers for frequency, pulse width, waveform/control og ADSR envelope. Voices deler filter-relaterte registers.

Vi starter med registermodellen, ikke en music abstraction.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
En demo-part må sameksistere med music player. Forståelse av SID state gjør player calls, timing, memory placement og visual synchronization mindre mystisk.

## Lab
Kartlegg de tre voice-registergruppene og shared registers. Finn bytes for frequency, pulse width, control og envelope.

## Neste
Vi får én voice til å lage en kontrollert tone.
