#!/usr/bin/env python3
"""Structural checks for Codecraft labs without external Python dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
COURSE_EN = ROOT / "course" / "en"
REQUIRED = {"README.md", "main.asm", "Makefile", "lab.yml"}
COURSE_RE = re.compile(r"^(\d{2})-")
LAB_RE = re.compile(r"^(\d{2})-(.+)$")
ID_RE = re.compile(r"^(\d{2})\.(\d{2})-(.+)$")
LESSON_RE = re.compile(r"^(\d{2})-.*\.md$")


def scalar(text, key):
    prefix = key + ":"
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return None


def course_lessons():
    result = {}
    for course in sorted(COURSE_EN.iterdir()):
        if not course.is_dir():
            continue
        match = COURSE_RE.match(course.name)
        if not match:
            continue
        result[course.name] = {
            m.group(1)
            for p in course.glob("*.md")
            if (m := LESSON_RE.match(p.name))
        }
    return result


def main():
    errors = []
    count = 0
    ids = set()
    known_courses = course_lessons()

    # Discover lab directories from the directory tree, not from lab.yml.
    # This makes a missing metadata file visible to CI.
    lab_dirs = sorted(
        p for course in LABS.iterdir() if course.is_dir()
        for p in course.iterdir() if p.is_dir()
    )

    for lab in lab_dirs:
        count += 1
        rel = lab.relative_to(ROOT)
        missing = sorted(name for name in REQUIRED if not (lab / name).exists())
        if missing:
            errors.append(f"{rel} missing: {', '.join(missing)}")
            if "lab.yml" in missing:
                continue

        meta = lab / "lab.yml"
        text = meta.read_text(encoding="utf-8")
        lab_id = scalar(text, "id")
        course_id = scalar(text, "course")
        lesson = scalar(text, "lesson")
        assembler = scalar(text, "assembler")

        course_dir = lab.parent.name
        course_match = COURSE_RE.match(course_dir)
        lab_match = LAB_RE.match(lab.name)

        if not course_match:
            errors.append(f"{rel}: invalid course directory name")
            continue
        if not lab_match:
            errors.append(f"{rel}: lab directory must start with two-digit number")
            continue

        expected_course_num = course_match.group(1)
        expected_lab_num = lab_match.group(1)

        if course_id != course_dir:
            errors.append(f"{meta.relative_to(ROOT)}: course={course_id!r}, expected {course_dir!r}")

        if lesson is None or not re.fullmatch(r"\d{2}", lesson):
            errors.append(f"{meta.relative_to(ROOT)}: lesson must be a two-digit lesson number")
        elif course_id in known_courses and lesson not in known_courses[course_id]:
            errors.append(f"{meta.relative_to(ROOT)}: lesson {lesson} not found in course/en/{course_id}")

        if not lab_id:
            errors.append(f"{meta.relative_to(ROOT)} missing id")
        else:
            match = ID_RE.fullmatch(lab_id)
            if not match:
                errors.append(f"{meta.relative_to(ROOT)}: invalid id format {lab_id!r}")
            else:
                if match.group(1) != expected_course_num:
                    errors.append(f"{meta.relative_to(ROOT)}: id course number does not match directory")
                if match.group(2) != expected_lab_num:
                    errors.append(f"{meta.relative_to(ROOT)}: id lab number does not match directory")
            if lab_id in ids:
                errors.append(f"duplicate lab id: {lab_id}")
            else:
                ids.add(lab_id)

        if assembler != "64tass":
            errors.append(f"{meta.relative_to(ROOT)}: reference lab assembler must be 64tass")

    if count == 0:
        errors.append("no labs discovered")

    if errors:
        print("C64 Codecraft labs: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"C64 Codecraft labs: PASS ({count} labs, metadata and lesson links checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
