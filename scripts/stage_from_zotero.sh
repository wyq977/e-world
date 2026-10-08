#!/usr/bin/env bash
# Stage one paper from local Zotero storage into inbox/<citekey>/ (agent step; see AGENTS.md "Stage").
# Usage: scripts/stage_from_zotero.sh <citekey> <zotero_item_key> <zotero_attachment_key> <version> [arxiv_id_with_vN]
# Reads ~/Zotero only. Never writes to raw/ or Zotero.
set -euo pipefail
key=$1; item=$2; att=$3; version=$4; arxiv=${5:-}
root=$(cd "$(dirname "$0")/.." && pwd); Z=$HOME/Zotero/storage/$att; d=$root/inbox/$key
mkdir -p "$d"; pdf=$(ls "$Z"/*.pdf | head -1)
cp "$pdf" "$d/paper.pdf"
if [ -f "$Z/.zotero-ft-cache" ]; then cp "$Z/.zotero-ft-cache" "$d/paper.txt"; else : > "$d/paper.txt"; fi
pages=$(gs -q -dNODISPLAY -dNOSAFER -c "($d/paper.pdf) (r) file runpdfbegin pdfpagecount = quit" 2>/dev/null || echo 0)
ff=$(tr -cd '\f' < "$d/paper.txt" | wc -c | tr -d ' ')
if [ "$ff" -lt $((pages-1)) ]; then gs -q -sDEVICE=txtwrite -o "$d/paper.txt" "$d/paper.pdf"; textnote="regenerated with gs (cache had $ff of $pages pages)"; else textnote="zotero cache, $pages pages"; fi
# bib fields from this entry only (stop at the next @)
entry=$(awk -v k="{$key," 'index($0,k){f=1} f&&/^@/&&!index($0,k){exit} f' "$root/e-world.bib")
doi=$(printf '%s\n' "$entry" | grep -m1 -iE '^\s*doi\s*=' | sed -E 's/.*= *[{"]?([^}",]*).*/\1/' || true)
url=""; [ -n "$doi" ] && url="https://doi.org/$doi"
cat > "$d/meta.yaml" <<YAML
citekey: $key
zotero_item: $item
zotero_attachment: $att
version: $version
arxiv: $arxiv
doi: $doi
url: $url
source_file: $(basename "$pdf")
text: $textnote
added: $(date +%F)
added_by: $(git -C "$root" config user.name 2>/dev/null || echo human)
YAML
echo "$key: $(basename "$pdf") | $textnote | $(wc -c < "$d/paper.txt") chars | doi=${doi:-none}"
