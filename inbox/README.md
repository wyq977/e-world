# inbox/ — staging, not a source

The agent stages papers here on request (`stage <citekey>`): one folder per
citekey with paper.pdf, paper.txt and a draft meta.yaml, copied from your
Zotero library. Nothing in here is read for ingestion.

Review a folder, then promote it:

    make approve KEY=<citekey>

Contents other than this README are git-ignored.
