#!/usr/bin/env python3
"""Bilingual structural consistency checks for C64 Codecraft."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
COURSE_RE = re.compile(r"^(\d{2})-(.+)$")
LESSON_RE = re.compile(r"^(\d{2})-.*\.md$")


def blocks(lang):
    base = COURSE / lang
    result = {}
    if not base.exists():
        return result
    for path in base.iterdir():
        if not path.is_dir():
            continue
        match = COURSE_RE.fullmatch(path.name)
        if match:
            result[match.group(1)] = path
    return result


def lesson_map(path):
    result = {}
    for file in path.glob("*.md"):
        match = LESSON_RE.fullmatch(file.name)
        if match:
            number = match.group(1)
            result.setdefault(number, []).append(file)
    return result


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

    # Course numbering itself must be continuous from 00.
    if en:
        nums = sorted(int(n) for n in en)
        expected = list(range(0, max(nums) + 1))
        if nums != expected:
            errors.append(f"EN course sequence is {nums}, expected {expected}")
    if no:
        nums = sorted(int(n) for n in no)
        expected = list(range(0, max(nums) + 1))
        if nums != expected:
            errors.append(f"NO course sequence is {nums}, expected {expected}")

    total_lessons = 0
    for number in sorted(set(en) & set(no)):
        en_map = lesson_map(en[number])
        no_map = lesson_map(no[number])

        for label, mapping, path in (
            ("EN", en_map, en[number]),
            ("NO", no_map, no[number]),
        ):
            duplicates = sorted(n for n, files in mapping.items() if len(files) != 1)
            if duplicates:
                errors.append(f"{label} course {number}: duplicate lesson numbers {duplicates}")
            contiguous(mapping, f"{label} course {number}", errors)
            if not (path / "README.md").exists():
                errors.append(f"{label} course {number} missing README.md")

        if set(en_map) != set(no_map):
            errors.append(
                f"course {number} lesson numbers differ: "
                f"EN={sorted(en_map)} NO={sorted(no_map)}"
            )
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

    print(
        "C64 Codecraft course consistency: PASS "
        f"({len(en)} bilingual course blocks, {total_lessons} lesson pairs)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
