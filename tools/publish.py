#!/usr/bin/env python3
"""Validate canonical course sources and emit deterministic publication manifests."""
from __future__ import annotations
import argparse, html, json, re, shutil, subprocess

try:
    import markdown
except ImportError:
    markdown = None
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
            if not re.search(r"(?m)^#\s+\S", text):
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
    ap.add_argument("command", choices=("check", "manifest", "site", "book"))
    ap.add_argument("--out", default="build/publication-manifest.json")
    args = ap.parse_args()
    data = validate()
    if args.command == "check":
        print(f"publication sources: PASS ({len(data['no'])} NO / {len(data['en'])} EN)")
        return
    if args.command == "book":
        if shutil.which("pandoc") is None:
            raise SystemExit("book build requires pandoc")
        if shutil.which("ebook-convert") is None:
            raise SystemExit("book build requires Calibre ebook-convert for Kindle/AZW3")
        out = ROOT / "build/books"
        out.mkdir(parents=True, exist_ok=True)
        for lang in LANGS:
            sources = [str(ROOT / p) for p in data[lang]]
            base = out / f"C64-Codecraft-{lang.upper()}"
            metadata = ROOT / f"book/metadata-{lang}.yaml"
            cover_svg = ROOT / f"book/cover-{lang}.svg"
            cover = out / f"cover-{lang}.png"
            if cover_svg.exists():
                if shutil.which("rsvg-convert") is None:
                    raise SystemExit("book build requires rsvg-convert for production covers")
                subprocess.run(["rsvg-convert", "-w", "1600", "-h", "2560",
                                "-o", str(cover), str(cover_svg)], check=True)
            common = ["pandoc", "--standalone", "--toc", "--toc-depth=3",
                      "--metadata-file", str(metadata)]
            epub = str(base) + ".epub"
            kindle = str(base) + ".azw3"
            pdf = str(base) + ".pdf"
            ebook_args = common + sources + ["--css", str(ROOT / "book/epub.css")]
            if cover.exists():
                ebook_args += ["--epub-cover-image", str(cover)]
            subprocess.run(ebook_args + ["-o", epub], check=True)
            subprocess.run(["ebook-convert", epub, kindle], check=True)
            pdf_sources = sources
            if cover.exists():
                cover_md = out / f".cover-{lang}.md"
                cover_md.write_text(
                    f"\\begin{{titlepage}}\\centering\\includegraphics[width=\\paperwidth,height=\\paperheight,keepaspectratio]{{{cover}}}\\end{{titlepage}}\\clearpage\n",
                    encoding="utf-8",
                )
                pdf_sources = [str(cover_md)] + sources
            subprocess.run(common + pdf_sources + ["--pdf-engine=xelatex", "-o", pdf], check=True)
            print(str(base.relative_to(ROOT)) + ".{epub,azw3,pdf}")
        return
    if args.command == "site":
        if markdown is None:
            raise SystemExit("site build requires Python package: markdown")
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
            for idx, src_name in enumerate(data[lang]):
                src = ROOT / src_name
                raw = src.read_text(encoding="utf-8")
                title = next((line[2:].strip() for line in raw.splitlines() if line.startswith("# ")), src.parent.name)
                dst = lang_dir / (src.parent.name + ".html")
                body = markdown.markdown(raw, extensions=["fenced_code", "tables"])
                key = src.parent.name
                other = "en" if lang == "no" else "no"
                prev_link = f"<a href='{Path(data[lang][idx-1]).parent.name}.html'>← Previous</a>" if idx else ""
                next_link = f"<a href='{Path(data[lang][idx+1]).parent.name}.html'>Next →</a>" if idx + 1 < len(data[lang]) else ""
                nav = f"<nav>{prev_link} <a href='index.html'>Index</a> <a href='../{other}/{key}.html'>{other.upper()}</a> {next_link}</nav>"
                css = "<style>body{max-width:72ch;margin:2rem auto;padding:0 1rem;font:18px/1.6 system-ui,sans-serif}pre{overflow:auto;padding:1rem;background:#eee}code{font-family:ui-monospace,monospace}nav{display:flex;gap:1rem;flex-wrap:wrap;border-bottom:1px solid #aaa;padding-bottom:1rem;margin-bottom:2rem}table{border-collapse:collapse}td,th{border:1px solid #aaa;padding:.35rem}</style>"
                page = f"<!doctype html><html lang='{lang}'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(title)} — C64 Codecraft</title>{css}<body>{nav}<main>{body}</main>{nav}</body></html>"
                dst.write_text(page, encoding="utf-8")
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
