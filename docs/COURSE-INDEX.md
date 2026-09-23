# C64 Codecraft — Course Index

**From Zero to Demo Coder**

This is the canonical human-readable course map. English and Norwegian tracks are developed in parallel and should remain equivalent in learning goals, labs and progression.

## Main course

| Course | Topic | English | Norsk |
|---|---|---|---|
| 00 | Assembly foundations | `course/en/00-intro/` | `course/no/00-intro/` |
| 01 | The C64 machine | `course/en/01-c64-machine/` | `course/no/01-c64-machine/` |
| 02 | Raster timing | `course/en/02-raster-timing/` | `course/no/02-raster-timing/` |
| 03 | Smooth scrolling / DYCP | `course/en/03-smooth-scrolling/` | `course/no/03-smooth-scrolling/` |
| 04 | SID music | `course/en/04-sid-music/` | `course/no/04-sid-music/` |
| 05 | Demo architecture | `course/en/05-demo-architecture/` | `course/no/05-demo-architecture/` |
| 06 | Advanced VIC-II | `course/en/06-advanced-vicii/` | `course/no/06-advanced-vicii/` |
| 07 | Bitmap and high colour | `course/en/07-bitmap-high-colour/` | `course/no/07-bitmap-high-colour/` |
| 08 | Advanced 6510 optimization | `course/en/08-6510-optimization/` | `course/no/08-6510-optimization/` |
| 09 | Packing/loading/multipart | `course/en/09-packing-loading/` | `course/no/09-packing-loading/` |
| 10 | Production craft | `course/en/10-production-craft/` | `course/no/10-production-craft/` |
| 11 | Capstone | `course/en/11-capstone/` | `course/no/11-capstone/` |

## Progression

```text
absolute beginner
  -> 6510 assembly
  -> C64 memory + VIC-II
  -> raster timing
  -> scrolling / DYCP
  -> SID + sync
  -> demo architecture
  -> advanced VIC-II
  -> bitmap / high colour
  -> optimization
  -> packing / loading / multipart
  -> production workflow
  -> original released demo
```

## Appendices

Tool references:
A 64tass · B ACME · C KickAssembler · D VICE · E scene asset tools · F packing/disk tools · G OCI environment.

Technical references:
H 6510 · I addressing modes · J memory map · K VIC-II · L SID · M CIA · N PETSCII/screen codes · O PAL/NTSC · P cycle counting · Q layouts · R troubleshooting.

See `appendix/README.md`.

## Source-of-truth rule

Lessons are authored as Markdown in Git. Generated site/book/PDF/EPUB outputs must be derived artifacts and must not become independently edited course sources.
