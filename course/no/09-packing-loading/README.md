---
title: Packing, loading og multipart demos
course: 09-packing-loading
lesson: overview
level: advanced
prerequisites: [08-6510-optimization]
labs: []
---
# Packing, loading og multipart demos
En production som er større enn én resident part trenger en ny type engineering: data må lagres, lastes, pakkes ut og overleveres mellom parts uten å bryte memory- eller timing-contracts.

Blokken starter med transparent offline packing og disk images og går videre mot loaders og multipart architecture. Tool-valg skal være replaceable; formats, constraints og interfaces må forstås.
