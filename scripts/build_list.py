#!/usr/bin/env python3
"""Generate e-world.md (the public list) from wiki/sources/*.md frontmatter.

Only pages with `public: true` are listed. Grouped by year descending;
`status: preprint` pages go to a trailing "Preprints" section.
No dependencies beyond the standard library; frontmatter parser is minimal
(flat keys, one nested `links:` mapping, inline lists).
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "wiki" / "sources"
OUT = ROOT / "e-world.md"

HEADER = """---
title: "E-world"
suppress-bibliography: true
---

*This is ongoing collection of literature about e-value (methodology),*
*Pls make a pull request in [github](https://github.com/wyq977/e-world).*
"""

LINK_LABELS = [("pdf", "PDF"), ("arxiv", "arXiv"), ("doi", "DOI"), ("video", "video")]

def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm, cur = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  ") and cur is not None:
            k, _, v = line.strip().partition(":")
            fm[cur][k.strip()] = unquote(v.split(" #")[0])
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.split(" #")[0].strip()
        if v == "":
            fm[k] = {}; cur = k
        else:
            fm[k] = unquote(v); cur = None
    return fm

def main():
    pages = []
    for p in sorted(SRC.glob("*.md")):
        fm = parse_frontmatter(p.read_text())
        if not fm:
            print(f"skip (no frontmatter): {p.name}", file=sys.stderr); continue
        if str(fm.get("public", "false")).lower() != "true":
            continue
        if p.stem != fm.get("citekey"):
            print(f"warn: filename {p.name} != citekey {fm.get('citekey')}", file=sys.stderr)
        pages.append(fm)
    if not pages:
        sys.exit("no public source pages in wiki/sources; e-world.md left untouched")

    def entry(fm):
        links = fm.get("links") or {}
        bits = [f"[{label}]({links[k]})" for k, label in LINK_LABELS if links.get(k)]
        note = (fm.get("note") or "").strip()
        tail = " ".join(x for x in [note, *bits] if x)
        return f"* [@{fm['citekey']}]\n    {tail}\n" if tail else f"* [@{fm['citekey']}]\n"

    out = [HEADER]
    published = [f for f in pages if f.get("status", "published") != "preprint"]
    preprints = [f for f in pages if f.get("status") == "preprint"]
    for year in sorted({int(f["year"]) for f in published}, reverse=True):
        out.append(f"\n## {year}\n")
        for fm in sorted((f for f in published if int(f["year"]) == year), key=lambda f: f["citekey"]):
            out.append("\n" + entry(fm))
    if preprints:
        out.append("\n## Preprints\n")
        for fm in sorted(preprints, key=lambda f: f["citekey"]):
            out.append("\n" + entry(fm))
    OUT.write_text("".join(out))
    print(f"wrote {OUT}: {len(published)} published, {len(preprints)} preprints")

if __name__ == "__main__":
    main()
