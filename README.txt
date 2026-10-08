e-world — an ongoing, human-curated collection of literature on e-values.

Public output
  e-world.md / index.html   annotated list, generated from wiki/sources frontmatter
                            build:  make list      (pandoc + csl/custom.csl)

Layers
  e-world.bib     canonical metadata, human-edited
  raw/<citekey>/  approved sources (paper.pdf, meta.yaml, paper.txt); human creates
  inbox/          staging for review; never read as a source; git-ignored
  wiki/           agent-maintained notes: index.md, log.md, gaps.md,
                  sources/<citekey>.md, concepts/<slug>.md
  scripts/        build_list.py (wiki -> e-world.md), pdf2txt.sh (gs fallback)
  AGENTS.md       rules and workflows for the agent (ingest / query / lint)

Adding a paper
  1. file it in Zotero (Better BibTeX key = citekey) and export e-world.bib
  2. ask the agent:  stage <citekey>    -> inbox/<citekey>/ (pdf, txt, meta.yaml)
  3. review the staging report; say "go" in chat -> agent runs make approve -> raw/<citekey>/
  4. agent ingests
  The agent never edits the bib and never writes to the Zotero library.

Requirements: pandoc, python3, ghostscript (only for PDFs not in Zotero).
CSL: https://www.zotero.org/styles/
