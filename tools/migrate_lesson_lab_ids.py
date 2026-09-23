#!/usr/bin/env python3
"""Migrate lesson labs: metadata to canonical lab.yml IDs.

lab.yml is authoritative. A lab's course + lesson identifies the lesson whose
frontmatter should reference that lab. Both EN and NO are updated identically.

Usage:
  python3 tools/migrate_lesson_lab_ids.py --check
  python3 tools/migrate_lesson_lab_ids.py --write
"""

import argparse
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_ROOT = ROOT / "course"
LABS_ROOT = ROOT / "labs"
LESSON_RE = re.compile(r"^(\d{2})-.*\.md$")


def scalar(path, key):
    prefix = key + ":"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    raise ValueError(f"{path}: missing {key}:")


def mapping():
    result = defaultdict(list)
    for path in sorted(LABS_ROOT.glob("*/*/lab.yml")):
        lab_id = scalar(path, "id")
        course = scalar(path, "course")
        lesson = scalar(path, "lesson")
        result[(course, lesson)].append(lab_id)
    return {key: sorted(value) for key, value in result.items()}


def desired_line(ids):
    return "labs: [" + ", ".join(ids) + "]"


def migrate(write=False):
    lab_map = mapping()
    changed = []
    errors = []

    for language in ("en", "no"):
        for course_dir in sorted((COURSE_ROOT / language).glob("[0-9][0-9]-*")):
            course = course_dir.name
            for path in sorted(course_dir.glob("[0-9][0-9]-*.md")):
                match = LESSON_RE.match(path.name)
                if not match:
                    continue
                lesson = match.group(1)
                text = path.read_text(encoding="utf-8")
                lines = text.splitlines(keepends=True)
                if not lines or lines[0].strip() != "---":
                    errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
                    continue

                end = next((i for i in range(1, len(lines))
                            if lines[i].strip() == "---"), None)
                if end is None:
                    errors.append(f"{path.relative_to(ROOT)}: unterminated frontmatter")
                    continue

                indexes = [i for i in range(1, end)
                           if lines[i].startswith("labs:")]
                if len(indexes) != 1:
                    errors.append(
                        f"{path.relative_to(ROOT)}: expected exactly one labs: field"
                    )
                    continue

                newline = "\r\n" if lines[indexes[0]].endswith("\r\n") else "\n"
                replacement = desired_line(lab_map.get((course, lesson), [])) + newline
                if lines[indexes[0]] != replacement:
                    changed.append(str(path.relative_to(ROOT)))
                    if write:
                        lines[indexes[0]] = replacement
                        path.write_text("".join(lines), encoding="utf-8")

    if errors:
        print("Lesson lab migration: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    if changed:
        mode = "updated" if write else "needs migration"
        print(f"Lesson lab migration: {len(changed)} files {mode}")
        for path in changed:
            print(f"- {path}")
        return 0 if write else 1

    print("Lesson lab migration: PASS (frontmatter already canonical)")
    return 0


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()
    return migrate(write=args.write)


if __name__ == "__main__":
    raise SystemExit(main())
