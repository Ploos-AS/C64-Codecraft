# Lesson ↔ Lab Mapping

This document defines the pedagogical relationship between lessons and practical labs.

A lesson does **not** need its own lab. Several foundation lessons deliberately feed one later lab. Every lab, however, must declare the lesson it reinforces in `lab.yml`.

## Policy

- `course:` identifies the course block.
- `lesson:` identifies the primary lesson reinforced by the lab.
- A lab may depend on concepts from earlier lessons.
- Missing one-to-one coverage is not an error.
- A lab pointing to a nonexistent lesson **is** an error and is checked by CI.
- Labs are numbered independently from lessons; their order represents the practical progression inside a course.
- The English and Norwegian lesson tracks share the same numeric lesson identity, so one lab mapping applies to both languages.

## Coverage model

| Course | Lesson range | Lab range | Model |
|---|---:|---:|---|
| 00 | 01–18 | 01–09 | foundation concepts converge into practical ASM exercises |
| 01 | 01–17 | 01–12 | machine concepts converge into VIC-II/charset/sprite work |
| 02 | 01–10 | 01–10 | close lesson/lab progression |
| 03 | 01–10 | 01–10 | close lesson/lab progression |
| 04 | 01–06 | 01–06 | close lesson/lab progression |
| 05 | 01–07 | 01–07 | close lesson/lab progression |
| 06 | 01–07 | 01–07 | qualification-oriented advanced VIC-II labs |
| 07 | 01–07 | 01–07 | bitmap/high-colour progression |
| 08 | 01–09 | 01–09 | measurement-led optimization progression |
| 09 | 01–09 | 01–09 | packing/loading/multipart progression |
| 10 | 01–07 | 01–07 | production workflow progression |
| 11 | 01–09 | 01–09 | capstone production progression |

## Machine-readable source

The authoritative mapping for an individual lab is its `labs/<course>/<lab>/lab.yml`, for example:

```yaml
id: 11.07-qualification
course: 11-capstone
lesson: 07
```

Do not duplicate a second exhaustive mapping table here. That would create two sources of truth. CI reads the metadata and verifies that the referenced English lesson exists; EN/NO structural CI separately verifies that the same lesson number exists in Norwegian.

## Design rule

The mapping answers **“which lesson does this practical exercise primarily reinforce?”**, not “which lesson owns this code?”. Codecraft teaches transferable 6510/C64 knowledge rather than a framework, so labs may intentionally combine material learned earlier.

When a lab's pedagogical target changes, update `lab.yml` in the same commit as the lab and lesson changes.
