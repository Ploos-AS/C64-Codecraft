# Lab 07.03 — Bitmap asset pipeline contract

## Goal
Treat converted graphics as reproducible binary assets with an explicit memory contract.

The source contains a tiny stand-in asset so the lab remains self-contained. The important exercise is to replace it with converter output while preserving documented sizes and destinations.

## Contract
Record:
- source-art format,
- conversion command/tool/version,
- bitmap output size,
- screen/colour companion data,
- load addresses,
- palette assumptions.

**Why does a demo coder care?** Scene graphics must survive the path from artist tool to exact VIC-II memory without hidden manual steps.
