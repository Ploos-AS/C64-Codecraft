---
title: Bygg frame budget
course: 05-demo-architecture
lesson: 02
level: advanced
prerequisites: [01-part-design]
labs: [frame-budget]
---
# Bygg frame budget
List alle recurring jobs og hvor de kan kjøre: IRQ entry/exit, music play, rasterbar writes, scroller fine update, periodisk coarse update, sprite movement/animation, cue handling og deferred preparation.

Mål relevante worst paths, ikke bare average frame. En coarse-scroll-frame eller animation update kan koste mer enn vanlig frame.

Reserver margin. En plan som bare virker når alle paths er best-case er skjør.

## Critical versus deferred
Legg bare position-sensitive work i cycle-critical region. Flytt table preparation, message parsing og fleksibelt arbeid til sikre windows.

## Lab
Lag frame-budget table med målte eller utledede kostnader og finn mest constrained window.

## Neste
Vi avstemmer schedulen med memory map.
