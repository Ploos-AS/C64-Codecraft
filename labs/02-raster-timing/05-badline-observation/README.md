# Lab 02.05 — Badline observation

This lab prepares a controlled observation rather than encoding a magic badline formula.

Record $D011 and a raster sample, then use the VICE monitor together with the lesson to identify display-fetch pressure and how YSCROLL/display state participates.

Do not generalize one observed timing trace to every VIC-II/video standard.

**Why does a demo coder care?** The VIC-II can steal bus time from the CPU; cycle budgets must include the video chip's work.
