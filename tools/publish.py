#!/usr/bin/env python3
"""Validate canonical course sources and emit deterministic publication manifests."""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
LANGS = ("no", "en")

def lessons(lang: str) -> list[Path]:
    return sorted((COURSE / lang).glob("*/README.md"))

def validate() -> dict[str, list[str]]:
    result = {}
    errors = []
    for lang in LANGS:
        items = lessons(lang)
        if not items:
            errors.append(f"{lang}: no lessons found")
        rel = [str(p.relative_to(ROOT)) for p in items]
        result[lang] = rel
        for p in items:
            text = p.read_text(encoding="utf-8")
            if not text.startswith("#"):
                errors.append(f"{p.relative_to(ROOT)}: missing top-level heading")
    no_keys = [Path(x).parent.name for x in result["no"]]
    en_keys = [Path(x).parent.name for x in result["en"]]
    if no_keys != en_keys:
        errors.append("NO/EN lesson directory sets differ")
    if errors:
        raise SystemExit("\n".join(errors))
    return result

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("check", "manifest"))
    ap.add_argument("--out", default="build/publication-manifest.json")
    args = ap.parse_args()
    data = validate()
    if args.command == "check":
        print(f"publication sources: PASS ({len(data['no'])} NO / {len(data['en'])} EN)")
        return
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(out.relative_to(ROOT))

if __name__ == "__main__":
    main()
