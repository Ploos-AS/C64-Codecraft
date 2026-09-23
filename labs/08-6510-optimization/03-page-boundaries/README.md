# Lab 08.03 — Page-boundary experiment

## Goal
Create two indexed-read cases whose base addresses make page crossing easy to observe and measure.

One table is page-aligned. A second begins near the end of a page so selected indexes cross into the next page.

Use VICE and the cycle-counting appendix to measure the exact addressing-mode behaviour. Do not generalize the result to stores or other indexed modes without checking them separately.

**Why does a demo coder care?** Data placement can change timing even when the source instruction looks identical.
