---
title: C64 som maskin
course: 01-c64-machine
lesson: overview
level: beginner
prerequisites: [00-intro]
labs: []
---

# C64 som maskin

Du kan nå skrive små 6510-rutiner. Denne blokken bygger modellen du trenger for å forstå hvor kode, RAM, ROM og hardware befinner seg.

Vi dekker CPU-ens 64 KiB adresserom, synlighet av RAM/ROM/I/O, 6510-porten på $00/$01, VIC-II-registerområdet og CIA-brikkene.

Scene-målet er praktisk: adresser skal slutte å være magiske tall, og du skal begynne å resonnere om maskinens konfigurasjon.
