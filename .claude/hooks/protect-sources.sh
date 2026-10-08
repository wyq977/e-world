#!/usr/bin/env bash
# PreToolUse hook: block Write/Edit into human-owned source layers.
set -euo pipefail
input=$(cat)
path=$(printf '%s' "$input" | python3 -c '
import json,sys
d=json.load(sys.stdin)
print(d.get("tool_input",{}).get("file_path",""))
' 2>/dev/null || true)
[ -z "$path" ] && exit 0
root=$(cd "$(dirname "$0")/../.." && pwd)
case "$path" in
  "$root"/raw/*|raw/*|"$root"/e-world.bib|e-world.bib)
    echo "Blocked: '$path' is human-owned (raw/ or e-world.bib). Ask the human to change it. See AGENTS.md." >&2
    exit 2 ;;
esac
exit 0
