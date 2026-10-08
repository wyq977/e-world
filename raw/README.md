# raw/ — human-owned sources

One directory per bib citekey:

    raw/<citekey>/
      paper.pdf      the primary file (see version policy in AGENTS.md)
      meta.yaml      citekey, version, arxiv (with vN), doi, url, added, added_by
      paper.txt      text layer, copied from Zotero's .zotero-ft-cache at staging

Folders arrive here only via `make approve KEY=<citekey>` run by a human
after reviewing inbox/<citekey>/. The agent reads and never writes.
Example meta.yaml:

    citekey: grunwaldSafeTesting2024
    zotero_item: VAHZTSP7
    zotero_attachment: 4K227MXX
    version: publisher-oa        # publisher-oa | arxiv | other
    arxiv: 1906.07801v4
    doi: 10.1093/jrsssb/qkae011
    url: https://academic.oup.com/jrsssb/article/86/5/1091/7630123
    added: 2026-10-08
    added_by: yongqi
