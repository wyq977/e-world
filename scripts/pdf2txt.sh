#!/usr/bin/env bash
# Fallback text extraction for PDFs that are not in Zotero (no .zotero-ft-cache).
# Usage: scripts/pdf2txt.sh in.pdf out.txt     (uses ghostscript)
set -euo pipefail
gs -q -sDEVICE=txtwrite -o "$2" "$1"
echo "wrote $2 ($(wc -c < "$2") bytes)"
