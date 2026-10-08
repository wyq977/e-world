#!/usr/bin/env python3
"""Append new entries to e-world.bib. Append-only: refuses to touch existing
entries and refuses duplicate citekeys or DOIs. Run only on the human's
explicit instruction (AGENTS.md). Usage: python3 scripts/bib_add.py new.bib
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
bib = ROOT / "e-world.bib"
new = Path(sys.argv[1]).read_text()
old = bib.read_text()
keys_old = set(re.findall(r"^@\w+\{([^,]+),", old, re.M))
dois_old = {d.lower() for d in re.findall(r"^\s*doi\s*=\s*\{([^}]+)\}", old, re.M | re.I)}
entries = re.findall(r"(@\w+\{[^@]*\n\})", new)
added = []
for e in entries:
    k = re.match(r"@\w+\{([^,]+),", e).group(1)
    d = re.search(r"^\s*doi\s*=\s*\{([^}]+)\}", e, re.M | re.I)
    if k in keys_old: print(f"skip {k}: key exists"); continue
    if d and d.group(1).lower() in dois_old: print(f"skip {k}: DOI exists"); continue
    added.append(e); keys_old.add(k)
if added:
    with bib.open("a") as f:
        f.write("\n" + "\n\n".join(added) + "\n")
print(f"appended {len(added)} entries")
