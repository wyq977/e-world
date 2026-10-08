# AGENTS.md — e-world

A curated, human-gated knowledge base on e-values and related methodology
(safe testing, test martingales, anytime-valid inference, game-theoretic
statistics). The agent builds and maintains an internal markdown wiki from
sources a human has approved. The public deliverable is a short annotated
list, `e-world.md` → `index.html`, not the wiki itself.

## Layers and ownership

| Path | Owner | Agent may |
|---|---|---|
| `e-world.bib` | human | read only |
| `raw/<citekey>/` | human | read only |
| `inbox/` | human reviews | write (downloads on request), never read as a source |
| `wiki/` | agent | read, write |
| `e-world.md`, `index.html` | generated | regenerate via `make list` |
| `AGENTS.md`, `scripts/`, `Makefile`, `csl/`, `style.css` | shared | edit on request |

Write and Edit calls into `raw/` or `e-world.bib` are blocked by a hook
(`.claude/hooks/protect-sources.sh`). Do not route around it with shell
commands. If something there is wrong, say so and let the human fix it.

## Zotero is read-only. Always.

The human's Zotero library is the database behind this project. The agent
never alters it in any way: no adding, editing, deleting, tagging, moving,
annotating, attaching, note-writing, collection changes, or batch updates,
and no writes to anything under `~/Zotero/`. Only the `zotero_search_*`,
`zotero_get_*`, `zotero_read_*`, `zotero_semantic_search`,
`zotero_list_libraries`, `zotero_switch_library` and
`zotero_export_bibliography` tools are allowed. Every other Zotero tool is
blocked by `.claude/settings.json`; if one is ever needed, the human does it
in Zotero. This holds even when the human asks in passing; confirm first and
point out that it is a Zotero-side change.

## The one rule that has no fallback

A paper exists for this project only when **both** are true:

1. it has an entry in `e-world.bib`, and
2. `raw/<citekey>/` contains the file the human placed there.

Nothing else makes it a source. Not a citation inside another paper, not a
Zotero item, not a web search result, not a file in `inbox/`. When you meet
such a paper, record it in `wiki/gaps.md` and move on. Never create
`raw/<citekey>/` yourself.

## Source versions (decided policy)

One primary file per citekey, chosen in this order:

1. publisher's open-access PDF of the version of record,
2. latest arXiv version (`vN`),
3. any other legitimately available PDF.

`raw/<citekey>/meta.yaml` records which one it is (`version:`), the arXiv id
with version suffix when applicable, and the date added. If the arXiv and
published versions are known to differ materially (renamed theorems, added
sections), the source page gets a short "Versions" note. `paper.txt` is the
text layer: Zotero's own extraction (`.zotero-ft-cache` next to the PDF in
`~/Zotero/storage/<key>/`), or `scripts/pdf2txt.sh` (ghostscript) for a PDF
that is not in Zotero. Read `paper.txt`, not the PDF, for token economy;
open the PDF only for figures, tables, or when the text is garbled.

## Workflows

### Stage — `stage <citekey>` (on explicit request only)

The human's Zotero library is the reviewed collection; the bib is exported
from it with Better BibTeX keys. To stage a paper:

1. Resolve the citekey with `zotero_search_by_citation_key`; list its
   attachments and local paths (`zotero_get_item_children`,
   `zotero_get_attachment_path`).
2. Pick the attachment by the version policy above.
3. Copy into `inbox/<citekey>/`: the PDF as `paper.pdf`, its
   `.zotero-ft-cache` as `paper.txt` (or run `scripts/pdf2txt.sh`), and a
   draft `meta.yaml` with `zotero_item`, `zotero_attachment`, `version`,
   `arxiv`, `doi`, `url`, `added`, `added_by`.
4. Report which attachment you chose and why, and stop.

The human reviews and runs `make approve KEY=<citekey>`, which moves the
folder to `raw/`. You never run `make approve` and never write to `raw/`.
If the paper is not in Zotero, or the only copy there is not an acceptable
version, say so; the human downloads it into `inbox/` by hand.

### Ingest — `ingest <citekey>`

Precondition check first; refuse if the bib entry or `raw/<citekey>/` is
missing. Then:

1. Check `paper.txt` exists; if not, ask the human (it is created at staging).
2. Read `paper.txt`. Give the human a short takeaway list (5–8 lines) and
   wait for a go.
3. Write `wiki/sources/<citekey>.md` from `wiki/templates/source.md`.
4. Propose which `wiki/concepts/` pages to create or change, with one line
   each on what changes. Wait for approval, then apply.
5. Add or update the line in `wiki/index.md`.
6. Append `## [YYYY-MM-DD] ingest | <citekey>` to `wiki/log.md`.
7. Note unknown cited works in `wiki/gaps.md`.
8. Run `make list` and show the diff of `e-world.md`.

One citekey per ingest. No batching unless the human says so explicitly.

### Query

Read `wiki/index.md` first, then only the pages it points to. Do not open
`raw/` during a query unless asked to verify a quotation. Answer from the
wiki only. If the wiki does not cover the question, say exactly that; do not
fill the gap from training knowledge or the web. Cite citekeys. If the
human wants an answer kept, file it under `wiki/concepts/` or as a section
of an existing page, and log it as `query`.

### Lint — `lint`

Report, do not fix without approval: contradictions between pages, concepts
mentioned in 2+ source pages without their own page, orphan pages, source
pages not linked from any concept page, bib entries with no source page,
source pages with no bib entry, `gaps.md` items that have since been added
to the bib. Log as `lint`.

## Page conventions

- Filenames: source pages use the bib citekey verbatim; concept pages use
  lowercase kebab-case slugs (`e-process.md`, `gro-criterion.md`).
- Links between wiki pages are relative markdown links, not wikilinks.
- Source pages carry YAML frontmatter; `scripts/build_list.py` reads it to
  generate `e-world.md`. Fields: see `wiki/templates/source.md`. Only pages
  with `public: true` appear in the list.
- The `note:` field is the one-line human-facing annotation. Keep it to a
  sentence. Everything longer belongs in the body.
- In chat, name a paper by its title (citekey optional). The human reads
  titles, not keys.
- Write claims with the citekey attached, e.g. "GRO e-variables maximise
  expected log growth under the alternative [grunwaldSafeTesting2024]".
- `wiki/log.md` is append-only. Entry headers are
  `## [YYYY-MM-DD] ingest|query|lint | <subject>` so `grep "^## \["` works.

## Public list

`e-world.md` is generated. Edit the `note:` and link fields in the source
page, then run `make list`; do not hand-edit `e-world.md`. The header text
of the list lives in `scripts/build_list.py`.
