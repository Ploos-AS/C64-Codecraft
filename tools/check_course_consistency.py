#!/usr/bin/env python3
"""Bilingual structural and lesson-metadata checks for C64 Codecraft."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
COURSE_RE = re.compile(r"^(\d{2})-(.+)$")
LESSON_RE = re.compile(r"^(\d{2})-.*\.md$")
REQUIRED_META = ("title", "course", "lesson", "level", "prerequisites", "labs")


def blocks(lang):
    base = COURSE / lang
    result = {}
    if not base.exists():
        return result
    for path in base.iterdir():
        if path.is_dir() and (match := COURSE_RE.fullmatch(path.name)):
            result[match.group(1)] = path
    return result


def lesson_map(path):
    result = {}
    for file in path.glob("*.md"):
        if match := LESSON_RE.fullmatch(file.name):
            result.setdefault(match.group(1), []).append(file)
    return result


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    data = {}
    for raw in text[4:end].splitlines():
        if ":" in raw:
            key, value = raw.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def contiguous(numbers, label, errors):
    if not numbers:
        errors.append(f"{label}: no lessons")
        return
    ints = sorted(int(n) for n in numbers)
    expected = list(range(1, max(ints) + 1))
    if ints != expected:
        errors.append(f"{label}: lesson sequence is {ints}, expected {expected}")


def main():
    errors = []
    en = blocks("en")
    no = blocks("no")

    if not en or not no:
        errors.append("both course/en and course/no must contain course blocks")
    if set(en) != set(no):
        errors.append(f"course blocks differ: EN={sorted(en)} NO={sorted(no)}")

    for label, mapping in (("EN", en), ("NO", no)):
        if mapping:
            nums = sorted(int(n) for n in mapping)
            expected = list(range(0, max(nums) + 1))
            if nums != expected:
                errors.append(f"{label} course sequence is {nums}, expected {expected}")

    total_lessons = 0
    for number in sorted(set(en) & set(no)):
        en_map = lesson_map(en[number])
        no_map = lesson_map(no[number])

        for label, mapping, path in (("EN", en_map, en[number]), ("NO", no_map, no[number])):
            duplicates = sorted(n for n, files in mapping.items() if len(files) != 1)
            if duplicates:
                errors.append(f"{label} course {number}: duplicate lesson numbers {duplicates}")
            contiguous(mapping, f"{label} course {number}", errors)

            for lesson_number, files in mapping.items():
                if len(files) != 1:
                    continue
                file = files[0]
                rel = file.relative_to(ROOT)
                meta = frontmatter(file)
                if meta is None:
                    errors.append(f"{rel}: missing or malformed frontmatter")
                    continue
                missing = [key for key in REQUIRED_META if key not in meta]
                if missing:
                    errors.append(f"{rel}: missing metadata: {', '.join(missing)}")
                if meta.get("course") != path.name:
                    errors.append(f"{rel}: course metadata {meta.get('course')!r} != {path.name!r}")
                if meta.get("lesson") != lesson_number:
                    errors.append(f"{rel}: lesson metadata {meta.get('lesson')!r} != {lesson_number!r}")

            if not (path / "README.md").exists():
                errors.append(f"{label} course {number} missing README.md")

        if set(en_map) != set(no_map):
            errors.append(f"course {number} lesson numbers differ: EN={sorted(en_map)} NO={sorted(no_map)}")
        total_lessons += len(en_map)

    appendix = ROOT / "appendix"
    if not (appendix / "README.md").exists():
        errors.append("appendix/README.md missing")
    for required in ("docs/COURSE-INDEX.md", "docs/PREREQUISITES.md"):
        if not (ROOT / required).exists():
            errors.append(f"{required} missing")

    if errors:
        print("C64 Codecraft course consistency: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"C64 Codecraft course consistency: PASS ({len(en)} bilingual course blocks, {total_lessons} lesson pairs, metadata checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
