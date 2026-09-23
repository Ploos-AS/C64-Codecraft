# Lab 02.09 — First rasterbar

## Goal
Create a small raster-colour band from synchronized writes.

This first version intentionally uses raster-line polling so the relationship between line selection and colour data stays visible. It is not presented as cycle-stable production code.

## Modify
Change the colour table and starting line. Then compare the result near display activity discussed in the badline lesson.

**Why does a demo coder care?** Rasterbars combine synchronization, prepared colour data and strict timing—the core vocabulary of many classic effects.
