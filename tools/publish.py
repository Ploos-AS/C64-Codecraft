#!/usr/bin/env python3
"""Validate canonical course sources and emit deterministic publication manifests."""
from __future__ import annotations
import argparse, html, json, re, shutil
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
    ap.add_argument("command", choices=("check", "manifest", "site"))
    ap.add_argument("--out", default="build/publication-manifest.json")
    args = ap.parse_args()
    data = validate()
    if args.command == "check":
        print(f"publication sources: PASS ({len(data['no'])} NO / {len(data['en'])} EN)")
        return
    if args.command == "site":
        out = ROOT / "build/site"
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)
        (out / ".nojekyll").write_text("", encoding="utf-8")
        cards = []
        for lang in LANGS:
            lang_dir = out / lang
            lang_dir.mkdir()
            links = []
            for src_name in data[lang]:
                src = ROOT / src_name
                raw = src.read_text(encoding="utf-8")
                title = next((line[2:].strip() for line in raw.splitlines() if line.startswith("# ")), src.parent.name)
                dst = lang_dir / (src.parent.name + ".html")
                body = "<pre>" + html.escape(raw) + "</pre>"
                dst.write_text(f"<!doctype html><meta charset='utf-8'><title>{html.escape(title)}</title><h1>{html.escape(title)}</h1>{body}", encoding="utf-8")
                links.append(f"<li><a href='{src.parent.name}.html'>{html.escape(title)}</a></li>")
            (lang_dir / "index.html").write_text("<!doctype html><meta charset='utf-8'><h1>C64 Codecraft</h1><ul>"+"".join(links)+"</ul>", encoding="utf-8")
            cards.append(f"<p><a href='{lang}/'>{lang.upper()}</a></p>")
        (out / "index.html").write_text("<!doctype html><meta charset='utf-8'><title>C64 Codecraft</title><h1>C64 Codecraft</h1><p>From Zero to Demo Coder</p>"+"".join(cards), encoding="utf-8")
        print(out.relative_to(ROOT))
        return
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(out.relative_to(ROOT))

if __name__ == "__main__":
    main()
