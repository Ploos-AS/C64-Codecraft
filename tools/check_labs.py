#!/usr/bin/env python3
"""Structural checks for Codecraft labs without external Python dependencies."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
REQUIRED = {"README.md", "main.asm", "Makefile", "lab.yml"}


def scalar(text, key):
    prefix = key + ":"
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return None


def main():
    errors = []
    count = 0
    ids = set()

    for meta in sorted(LABS.glob("*/*/lab.yml")):
        count += 1
        lab = meta.parent
        missing = sorted(name for name in REQUIRED if not (lab / name).exists())
        if missing:
            errors.append(f"{lab.relative_to(ROOT)} missing: {', '.join(missing)}")

        text = meta.read_text(encoding="utf-8")
        lab_id = scalar(text, "id")
        assembler = scalar(text, "assembler")
        if not lab_id:
            errors.append(f"{meta.relative_to(ROOT)} missing id")
        elif lab_id in ids:
            errors.append(f"duplicate lab id: {lab_id}")
        else:
            ids.add(lab_id)

        if assembler != "64tass":
            errors.append(
                f"{meta.relative_to(ROOT)}: early reference lab assembler must be 64tass"
            )

    if count == 0:
        errors.append("no labs discovered")

    if errors:
        print("C64 Codecraft labs: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"C64 Codecraft labs: PASS ({count} labs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
