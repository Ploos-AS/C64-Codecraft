---
title: Page boundaries og deterministic timing
course: 08-6510-optimization
lesson: 03
level: advanced
prerequisites: [02-zero-page-strategy]
labs: [08.03-page-boundaries]
---
# Page boundaries og deterministic timing
Noen indexed memory accesses kan bruke en ekstra cycle når effective address krysser en page boundary. Branch timing avhenger også av om en taken branch krysser page.

I vanlig kode kan dette være en liten performance-detalj. I cycle-exact code kan det bli uønsket timing-variasjon.

Alignment kan derfor være et timing-verktøy, ikke bare et estetisk linker-valg.

## Bevis pathen
Ikke legg inn alignment directives blindt. Finn eksakt access/branch der timing betyr noe og plasser code/data slik at relevant path får ønsket behaviour.

## Lab
Lag en liten routine der timing endres over page boundary, observer den og plasser deretter code/data bevisst for deterministic critical path.

## Neste
Vi optimaliserer control flow og layout sammen.
