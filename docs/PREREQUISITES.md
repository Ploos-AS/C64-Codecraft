# Prerequisite graph

The course is deliberately linear at the block level while individual lessons may refer back to earlier concepts.

```mermaid
flowchart TD
  C00["00 Assembly foundations"] --> C01["01 C64 machine"]
  C01 --> C02["02 Raster timing"]
  C02 --> C03["03 Smooth scrolling / DYCP"]
  C03 --> C04["04 SID music"]
  C04 --> C05["05 Demo architecture"]
  C05 --> C06["06 Advanced VIC-II"]
  C06 --> C07["07 Bitmap / high colour"]
  C07 --> C08["08 6510 optimization"]
  C08 --> C09["09 Packing / loading"]
  C09 --> C10["10 Production craft"]
  C10 --> C11["11 Capstone"]

  A["Appendices A-R"] -. reference .-> C00
  A -. reference .-> C11
```

## Dependency policy

- A learner may explore ahead, but labs can assume completed prerequisite blocks.
- Appendices are references, not prerequisite courses.
- EduCPU is optional deeper background and is **not** a C64 Codecraft prerequisite.
- Tool knowledge should be introduced when needed; no editor extension is a prerequisite.
- Advanced timing examples must state target machine/video assumptions.

## Lesson metadata

New lessons should use frontmatter fields such as:

```yaml
title: ...
course: ...
lesson: ...
level: ...
prerequisites: [...]
labs: [...]
```

The consistency tooling can become stricter as older lessons are normalized to this schema.
