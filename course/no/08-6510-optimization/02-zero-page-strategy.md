---
title: Zero-page strategy
course: 08-6510-optimization
lesson: 02
level: advanced
prerequisites: [01-maal-foerst]
labs: [08.02-zero-page-strategy]
---
# Zero-page strategy
Zero page gir kortere og ofte raskere addressing forms og kreves av viktige indirect addressing modes. Men zero-page-space er delt, begrenset og kan også brukes av operating environment eller integrerte players.

Behandle den som resource budget.

Gode kandidater er ofte brukte pointers, counters eller state på en målt hot path. Cold data fortjener ikke zero page bare fordi det tilfeldigvis finnes plass.

## Ownership
Dokumenter hver reserverte byte/range og lifetime. Integration bugs fra overlappende zero-page ownership kan være langt vanskeligere enn vanlig RAM-overlap.

## Lab
Flytt valgt hot state til zero page, mål cycle/byte-endringen og oppdater partens memory contract.

## Neste
Memory placement påvirker også timing ved page boundaries.
