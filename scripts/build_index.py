#!/usr/bin/env python3
"""Regenerate wiki/index.md from the source and concept pages' frontmatter."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_list import parse_frontmatter
W = Path(__file__).resolve().parent.parent / "wiki"
rows_s, rows_c = [], []
for p in sorted((W / 'sources').glob('*.md')):
    fm = parse_frontmatter(p.read_text())
    rows_s.append(f"- [{p.stem}](sources/{p.stem}.md) — {fm.get('title')} ({fm.get('year')}, {fm.get('status')}). {fm.get('note')}")
for p in sorted((W / 'concepts').glob('*.md')):
    body = p.read_text(); fm = parse_frontmatter(body)
    m = re.search(r"## Definition\n(.+?)(?:\n\n|$)", body, re.S)
    first = re.split(r"(?<=[.!?])\s", m.group(1).strip())[0] if m else ""
    first = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first); first = re.sub(r"\s*\[[A-Za-z]+\d{4}[^\]]*\]", "", first)
    rows_c.append(f"- [{fm.get('title')}](concepts/{p.stem}.md) — {first} ({fm.get('sources')} sources)")
(W / 'index.md').write_text("# e-world wiki index\n\nRead this first. One line per page. Open only what the question needs.\nOther pages: [candidates.md](candidates.md) (proposed reading queue), [gaps.md](gaps.md) (cited works not yet sources), [log.md](log.md).\n\n## Sources\n" + "\n".join(rows_s) + "\n\n## Concepts\n" + "\n".join(rows_c) + "\n")
print(f"index: {len(rows_s)} sources, {len(rows_c)} concepts")
