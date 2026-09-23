#!/usr/bin/env python3
"""Lightweight bilingual course consistency checks.

This intentionally checks structure before translation wording. EN/NO filenames
may differ, so parity is primarily based on numeric lesson prefixes.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"

COURSE_RE = re.compile(r"^(\d{2})-")
LESSON_RE = re.compile(r"^(\d{2})-.*\.md$")


def blocks(lang: str):
    base = COURSE / lang
    result = {}
    if not base.exists():
        return result
    for p in base.iterdir():
        if p.is_dir():
            m = COURSE_RE.match(p.name)
            if m:
                result[m.group(1)] = p
    return result


def lessons(path: Path):
    nums = set()
    for p in path.glob("*.md"):
        m = LESSON_RE.match(p.name)
        if m:
            nums.add(m.group(1))
    return nums


def main():
    errors = []
    en = blocks("en")
    no = blocks("no")

    if set(en) != set(no):
        errors.append(
            f"course blocks differ: EN={sorted(en)} NO={sorted(no)}"
        )

    for number in sorted(set(en) & set(no)):
        en_lessons = lessons(en[number])
        no_lessons = lessons(no[number])
        if en_lessons != no_lessons:
            errors.append(
                f"course {number} lesson numbers differ: "
                f"EN={sorted(en_lessons)} NO={sorted(no_lessons)}"
            )

        for label, path in (("EN", en[number]), ("NO", no[number])):
            if not (path / "README.md").exists():
                errors.append(f"{label} course {number} missing README.md")

    appendix = ROOT / "appendix"
    if not (appendix / "README.md").exists():
        errors.append("appendix/README.md missing")

    if errors:
        print("C64 Codecraft course consistency: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "C64 Codecraft course consistency: PASS "
        f"({len(en)} bilingual course blocks)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
