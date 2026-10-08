#!/usr/bin/env python3
"""Render the wiki (index, sources, concepts, gaps, log) as one HTML page for the
Claude Artifact. Usage: python3 scripts/build_wiki_page.py <out.html>
Minimal markdown support, no dependencies.
"""
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "wiki"

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return {}, text
    fm, cur = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        if line.startswith("  ") and cur is not None:
            k, _, v = line.strip().partition(":"); fm[cur][k.strip()] = v.split(" #")[0].strip().strip('"\''); continue
        k, _, v = line.partition(":"); k, v = k.strip(), v.split(" #")[0].strip()
        if v == "": fm[k] = {}; cur = k
        else: fm[k] = v.strip('"\''); cur = None
    return fm, text[m.end():]

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_([^_\n]+)_(?!\w)", r"<em>\1</em>", s)
    def link(m):
        text, href = m.group(1), m.group(2)
        if href.startswith("http"): return f'<a href="{href}" target="_blank" rel="noopener">{text}</a>'
        # wiki-internal: ../concepts/x.md, x.md, concepts/x.md, sources/x.md
        slug = re.sub(r"\.md$", "", href.split("/")[-1])
        kind = "concepts" if "concepts" in href else "sources" if "sources" in href else None
        return f'<a href="#{(kind + "-" if kind else "") + slug}" data-slug="{slug}">{text}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"\[(\w+\d{4}[a-z]?)\]", r'<a class="cite" href="#sources-\1">[\1]</a>', s)
    return s

def md_to_html(md, base_level=2):
    out, i, lines = [], 0, md.splitlines()
    in_list = None; para = []; table = []; code = False
    def flush_para():
        nonlocal para
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
    def flush_list():
        nonlocal in_list
        if in_list: out.append(f"</{in_list}>"); in_list = None
    def flush_table():
        nonlocal table
        if table:
            rows = [r for r in table if not re.match(r"^\|?\s*:?-{2,}", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            if cells:
                h = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
                b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:])
                out.append(f'<div class="wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            table = []
    for line in lines:
        if line.startswith("```"):
            flush_para(); flush_list(); flush_table()
            code = not code; out.append("<pre><code>" if code else "</code></pre>"); continue
        if code: out.append(html.escape(line)); continue
        if line.startswith("|"): flush_para(); flush_list(); table.append(line); continue
        else: flush_table()
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_para(); flush_list()
            lvl = min(6, len(m.group(1)) - 1 + base_level)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m:
            flush_para()
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if in_list != kind: flush_list(); out.append(f"<{kind}>"); in_list = kind
            out.append(f"<li>{inline(m.group(3))}</li>"); continue
        if not line.strip():
            flush_para(); flush_list(); continue
        if line.startswith("<!--"): continue
        if in_list and line.startswith("  "):
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"; continue
        para.append(line.strip())
    flush_para(); flush_list(); flush_table()
    return "\n".join(out)

def page_block(kind, path):
    fm, body = split_frontmatter(path.read_text())
    slug = path.stem
    title = fm.get("title") or re.search(r"^# (.*)$", body, re.M).group(1) if re.search(r"^# (.*)$", body, re.M) else slug
    body = re.sub(r"^# .*\n", "", body, count=1)
    meta = ""
    if kind == "sources":
        who = fm.get("authors", "")
        if isinstance(who, str): who = who.strip("[]")
        links = fm.get("links") or {}
        lk = " · ".join(f'<a href="{v}" target="_blank" rel="noopener">{k}</a>' for k, v in links.items() if v)
        meta = f'<div class="meta"><span class="key">{slug}</span> {html.escape(str(who))} · {html.escape(str(fm.get("year","")))} · {html.escape(str(fm.get("status","")))}{" · " + lk if lk else ""}</div>'
        if fm.get("note"): meta += f'<p class="note">{inline(str(fm["note"]))}</p>'
    elif kind == "concepts":
        meta = f'<div class="meta"><span class="key">{slug}</span> sources: {html.escape(str(fm.get("sources","?")))} · updated {html.escape(str(fm.get("updated","")))}</div>'
    return slug, title, f'<article id="{kind}-{slug}" class="page {kind}"><h2>{inline(str(title))}</h2>{meta}{md_to_html(body, 3)}</article>'

sources = [page_block("sources", p) for p in sorted((W / "sources").glob("*.md"))]
concepts = [page_block("concepts", p) for p in sorted((W / "concepts").glob("*.md"))]
index_html = md_to_html(re.sub(r"^# .*\n", "", (W / "index.md").read_text(), count=1), 3)
gaps_html = md_to_html(re.sub(r"^# .*\n", "", (W / "gaps.md").read_text(), count=1), 3)
log_md = (W / "log.md").read_text()
log_entries = re.findall(r"^## \[(\d{4}-\d{2}-\d{2})\] (\w+) \| (.*)$", log_md, re.M)
log_html = "".join(f'<li><span class="date">{d}</span> <span class="chip {k}">{k}</span> {inline(t)}</li>' for d, k, t in reversed(log_entries))

nav = ('<nav><h3>Index</h3><a href="#index">Overview</a>'
       + '<h3>Sources</h3>' + "".join(f'<a href="#sources-{s}">{inline(str(t))}</a>' for s, t, _ in sources)
       + '<h3>Concepts</h3>' + "".join(f'<a href="#concepts-{s}">{inline(str(t))}</a>' for s, t, _ in concepts)
       + '<h3>Housekeeping</h3><a href="#gaps">Gaps</a><a href="#log">Log</a></nav>')

page = f"""<title>E-world Wiki</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:wght@400;600&family=Source+Code+Pro:wght@400&display=swap">
<style>
/* Layout: sidebar nav on wide screens, stacked on phones; pages as articles with anchors. */
:root {{
  --bg:#f7f6f2; --fg:#1f2a2e; --muted:#5e6b70; --rule:#d9d6cc; --card:#ffffff;
  --accent:#0e6b5c; --accent-soft:#e1efea; --ingest:#dcefe7; --query:#e7e4f6; --lint:#f6e7c3;
  --display:"Fraunces", Georgia, serif; --body:"Source Sans 3", "Helvetica Neue", Arial, sans-serif; --mono:"Source Code Pro", Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#171b1d; --fg:#e6e4dc; --muted:#a3aba8; --rule:#333a3c; --card:#1f2527; --accent:#6fc2ad; --accent-soft:#1e3330; --ingest:#1e3330; --query:#2a2740; --lint:#3a2f14; color-scheme:dark }} }}
:root[data-theme="dark"] {{
  --bg:#171b1d; --fg:#e6e4dc; --muted:#a3aba8; --rule:#333a3c; --card:#1f2527; --accent:#6fc2ad; --accent-soft:#1e3330; --ingest:#1e3330; --query:#2a2740; --lint:#3a2f14; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); font-size:16px; line-height:1.5; padding-inline:16px; padding-block:24px 64px; }}
.shell {{ max-width:1100px; margin:0 auto; display:grid; grid-template-columns:230px minmax(0,1fr); gap:32px; }}
@media (max-width:760px) {{ .shell {{ grid-template-columns:1fr; }} nav {{ position:static; max-height:none; }} }}
nav {{ position:sticky; top:env(safe-area-inset-top,0px); align-self:start; max-height:calc(100vh - 24px); overflow:auto; font-size:.9rem; padding-right:8px; }}
nav h3 {{ font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--muted); margin:1rem 0 .3rem; }}
nav a {{ display:block; color:var(--fg); text-decoration:none; padding:3px 0; border-left:2px solid transparent; padding-left:8px; }}
nav a:hover {{ border-left-color:var(--accent); color:var(--accent); }}
header h1 {{ font-family:var(--display); font-weight:600; font-size:clamp(1.8rem,4vw,2.5rem); margin:0 0 .2rem; }}
header p {{ color:var(--muted); max-width:65ch; margin:0 0 1rem; }}
article.page {{ background:var(--card); border:1px solid var(--rule); border-radius:6px; padding:20px 22px; margin-bottom:28px; min-width:0; }}
article h2 {{ font-family:var(--display); font-weight:500; font-size:1.45rem; margin:0 0 .3rem; text-wrap:balance; }}
article h3 {{ font-size:1rem; text-transform:uppercase; letter-spacing:.05em; color:var(--accent); margin:1.3rem 0 .4rem; }}
article h4 {{ font-size:1rem; margin:1rem 0 .3rem; }}
.meta {{ color:var(--muted); font-size:.88rem; margin-bottom:.6rem; }}
.key {{ font-family:var(--mono); font-size:.8rem; background:var(--accent-soft); color:var(--accent); padding:1px 6px; border-radius:3px; margin-right:6px; }}
.note {{ font-style:italic; border-left:3px solid var(--accent); padding-left:10px; color:var(--fg); }}
p, li {{ max-width:70ch; }}
a {{ color:var(--accent); }}
a.cite {{ font-family:var(--mono); font-size:.8em; text-decoration:none; }}
code {{ font-family:var(--mono); font-size:.86em; background:var(--accent-soft); padding:0 4px; border-radius:3px; }}
pre {{ overflow-x:auto; background:var(--accent-soft); padding:10px; border-radius:4px; }}
pre code {{ background:none; padding:0; }}
.wrap {{ overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; font-size:.92rem; }}
th, td {{ text-align:left; padding:6px 8px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-size:.75rem; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); }}
#log li {{ list-style:none; margin-bottom:6px; }}
#log ul {{ padding:0; }}
.date {{ font-family:var(--mono); font-size:.8rem; color:var(--muted); }}
.chip {{ display:inline-block; font-size:.72rem; font-weight:600; padding:1px 7px; border-radius:4px; text-transform:uppercase; letter-spacing:.04em; }}
.chip.ingest {{ background:var(--ingest); color:var(--accent); }} .chip.query {{ background:var(--query); }} .chip.lint {{ background:var(--lint); }}
:target {{ scroll-margin-top:12px; }}
</style>
<div class="shell">
{nav}
<main>
<header><h1>E-world Wiki</h1><p>Agent-maintained notes on the e-value literature, built only from sources a human approved. {len(sources)} source pages, {len(concepts)} concept pages. Read the overview, then open only what you need.</p></header>
<article id="index" class="page"><h2>Overview</h2>{index_html}</article>
{"".join(b for _, _, b in sources)}
{"".join(b for _, _, b in concepts)}
<article id="gaps" class="page"><h2>Gaps</h2>{gaps_html}</article>
<article id="log" class="page"><h2>Log</h2><ul>{log_html}</ul></article>
</main>
</div>
"""
Path(sys.argv[1]).write_text(page)
print(f"wrote {sys.argv[1]}: {len(sources)} sources, {len(concepts)} concepts")
