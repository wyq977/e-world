#!/usr/bin/env python3
"""Render wiki/candidates.md as a standalone HTML page (for the Claude Artifact).
Usage: python3 scripts/build_candidates_page.py <out.html>
"""
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
md = (ROOT / "wiki" / "candidates.md").read_text()

tiers, cur = [], None
for line in md.splitlines():
    m = re.match(r"^## (Tier \d+) — (.*)$", line)
    if m:
        cur = {"id": m.group(1).lower().replace(" ", ""), "name": m.group(1), "desc": m.group(2), "rows": []}
        tiers.append(cur); continue
    if cur and line.startswith("|") and not line.startswith("|--") and not line.startswith("| #"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 5:
            cur["rows"].append(dict(n=cells[0], title=cells[1], who=cells[2], status=cells[3], ev=cells[4]))

def status_key(s):
    s = s.lower()
    return "ingested" if s.startswith("ingested") else "staged" if s.startswith("staged") else "bib" if s.startswith("bib") else "missing"

counts = {"ingested": 0, "staged": 0, "bib": 0, "missing": 0}
for t in tiers:
    for r in t["rows"]:
        counts[status_key(r["status"])] += 1
total = sum(counts.values())

def row_html(r):
    k = status_key(r["status"])
    ev = html.escape(r["ev"])
    ev = re.sub(r"book:(\d+)", r'<span class="ev book" title="citations in Ramdas &amp; Wang">book ×\1</span>', ev)
    ev = ev.replace("SAVI", '<span class="ev savi" title="SAVI 2022 reading list">SAVI</span>')
    ev = re.sub(r"\bweb\b", '<span class="ev web" title="web check, Oct 2026">web</span>', ev)
    return (f'<tr data-status="{k}"><td class="n">{html.escape(r["n"])}</td>'
            f'<td class="t">{html.escape(r["title"])}<div class="who">{html.escape(r["who"])}</div></td>'
            f'<td class="s"><span class="chip {k}">{html.escape(r["status"])}</span></td>'
            f'<td class="e">{ev}</td></tr>')

sections = "".join(
    f'<section id="{t["id"]}"><h2><span class="tier">{html.escape(t["name"])}</span> {html.escape(t["desc"])}</h2>'
    f'<div class="wrap"><table><thead><tr><th>#</th><th>Paper</th><th>Status</th><th>Evidence</th></tr></thead>'
    f'<tbody>{"".join(row_html(r) for r in t["rows"])}</tbody></table></div></section>'
    for t in tiers)

page = f"""<title>E-world Reading Queue</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:wght@400;600&display=swap">
<style>
/* Layout: one narrow reading column; tables run full width inside it; a sticky filter row. */
:root {{
  --bg:#f7f6f2; --fg:#1f2a2e; --muted:#5e6b70; --rule:#d9d6cc; --card:#ffffff;
  --accent:#0e6b5c; --accent-soft:#e1efea;
  --ok:#0e6b5c; --ok-bg:#dcefe7; --mid:#8a5a00; --mid-bg:#f6e7c3; --no:#8b3a3a; --no-bg:#f4dede;
  --display:"Fraunces", Georgia, serif; --body:"Source Sans 3", "Helvetica Neue", Arial, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#171b1d; --fg:#e6e4dc; --muted:#a3aba8; --rule:#333a3c; --card:#1f2527;
  --accent:#6fc2ad; --accent-soft:#1e3330; --ok:#6fc2ad; --ok-bg:#1e3330; --mid:#e0b25a; --mid-bg:#3a2f14; --no:#e08a8a; --no-bg:#3b2222; color-scheme:dark }} }}
:root[data-theme="dark"] {{
  --bg:#171b1d; --fg:#e6e4dc; --muted:#a3aba8; --rule:#333a3c; --card:#1f2527;
  --accent:#6fc2ad; --accent-soft:#1e3330; --ok:#6fc2ad; --ok-bg:#1e3330; --mid:#e0b25a; --mid-bg:#3a2f14; --no:#e08a8a; --no-bg:#3b2222; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); font-size:16px; line-height:1.45; padding-inline:16px; padding-block:24px 64px; }}
main {{ max-width:900px; margin:0 auto; }}
h1 {{ font-family:var(--display); font-weight:600; font-size:clamp(1.8rem,4vw,2.6rem); line-height:1.1; margin:0 0 .3rem; text-wrap:balance; }}
.sub {{ color:var(--muted); max-width:65ch; margin:0 0 1.2rem; }}
.sub code {{ font-size:.9em; }}
.summary {{ display:flex; flex-wrap:wrap; gap:8px 18px; align-items:baseline; margin-bottom:1.2rem; font-variant-numeric:tabular-nums; }}
.summary b {{ font-family:var(--display); font-size:1.4rem; font-weight:500; }}
.filters {{ position:sticky; top:env(safe-area-inset-top,0px); z-index:2; background:var(--bg); padding-block:8px; display:flex; flex-wrap:wrap; gap:8px; border-bottom:1px solid var(--rule); margin-bottom:1.5rem; }}
.filters button {{ font:inherit; font-size:.9rem; padding:4px 12px; border-radius:999px; border:1px solid var(--rule); background:var(--card); color:var(--fg); cursor:pointer; }}
.filters button[aria-pressed="true"] {{ background:var(--accent); border-color:var(--accent); color:var(--bg); }}
.filters button:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
section {{ margin-bottom:2.2rem; }}
h2 {{ font-family:var(--display); font-weight:500; font-size:1.3rem; margin:0 0 .6rem; text-wrap:balance; }}
.tier {{ color:var(--accent); font-variant:small-caps; letter-spacing:.03em; margin-right:.3em; }}
.wrap {{ overflow-x:auto; }}
table {{ width:100%; border-collapse:collapse; min-width:560px; }}
th {{ text-align:left; font-size:.75rem; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); font-weight:600; padding:6px 8px; border-bottom:1px solid var(--rule); }}
td {{ padding:9px 8px; border-bottom:1px solid var(--rule); vertical-align:top; }}
td.n {{ color:var(--muted); font-variant-numeric:tabular-nums; width:2.2em; }}
td.t {{ min-width:0; }}
.who {{ color:var(--muted); font-size:.88rem; }}
.chip {{ display:inline-block; font-size:.78rem; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; }}
.chip.staged {{ background:var(--ok-bg); color:var(--ok); }}
.chip.ingested {{ background:var(--accent); color:var(--bg); }}
.chip.bib {{ background:var(--mid-bg); color:var(--mid); }}
.chip.missing {{ background:var(--no-bg); color:var(--no); }}
td.e {{ font-size:.88rem; color:var(--muted); }}
.ev {{ display:inline-block; padding:0 6px; border-radius:3px; background:var(--accent-soft); color:var(--accent); font-weight:600; margin-right:4px; }}
tr[hidden] {{ display:none; }}
section.empty {{ display:none; }}
.legend {{ font-size:.9rem; color:var(--muted); max-width:65ch; }}
footer {{ margin-top:2rem; padding-top:1rem; border-top:1px solid var(--rule); color:var(--muted); font-size:.88rem; max-width:65ch; }}
footer a {{ color:var(--accent); }}
</style>
<main>
<h1>E-world Reading Queue</h1>
<p class="sub">Proposed ingestion order for the e-value literature wiki, foundations first. The agent proposes; only a human adds a paper to the bibliography or stages its PDF.</p>
<div class="summary"><span><b>{total}</b> titles</span><span><b>{counts["ingested"]}</b> ingested</span><span><b>{counts["staged"]}</b> staged</span><span><b>{counts["bib"]}</b> in bib, not staged</span><span><b>{counts["missing"]}</b> missing</span></div>
<div class="filters" role="group" aria-label="Filter by status">
<button id="f-all" data-f="all" aria-pressed="true">All</button>
<button id="f-ingested" data-f="ingested" aria-pressed="false">Ingested</button>
<button id="f-missing" data-f="missing" aria-pressed="false">Missing</button>
<button id="f-bib" data-f="bib" aria-pressed="false">In bib</button>
<button id="f-staged" data-f="staged" aria-pressed="false">Staged</button>
</div>
{sections}
<p class="legend"><b>Evidence</b>: <i>book ×N</i> is the approximate number of times the paper is cited in Ramdas and Wang, <i>Hypothesis testing with e-values</i> (2025). <i>SAVI</i> marks the 2022 Safe Anytime-Valid Inference workshop reading list. <i>web</i> marks an October 2026 web check.</p>
<footer>Generated from <code>wiki/candidates.md</code> in the e-world repository. Status: <i>ingested</i> = source page exists in the wiki; <i>staged</i> = PDF copied to inbox, awaiting <code>make approve</code>; <i>bib</i> = in e-world.bib, PDF not yet staged; <i>missing</i> = not in the bibliography.</footer>
</main>
<script>
(function(){{
  var btns=document.querySelectorAll('.filters button');
  function apply(f){{
    btns.forEach(function(b){{b.setAttribute('aria-pressed', String(b.dataset.f===f));}});
    document.querySelectorAll('tbody tr').forEach(function(tr){{tr.hidden = (f!=='all' && tr.dataset.status!==f);}});
    document.querySelectorAll('section').forEach(function(s){{
      var vis=s.querySelectorAll('tbody tr:not([hidden])').length; s.classList.toggle('empty', vis===0);
    }});
    try{{localStorage.setItem('ew-filter',f);}}catch(e){{}}
  }}
  btns.forEach(function(b){{b.addEventListener('click',function(){{apply(b.dataset.f);}});}});
  var saved=null; try{{saved=localStorage.getItem('ew-filter');}}catch(e){{}}
  if(saved && saved!=='all') apply(saved);
}})();
</script>
"""
Path(sys.argv[1]).write_text(page)
print(f"wrote {sys.argv[1]}: {total} rows, {counts}")
