#!/usr/bin/env bash
# PreToolUse hook for Bash: refuse commands that would write under ~/Zotero.
# Reading (ls, cat, head, grep, cp FROM Zotero) is allowed.
set -euo pipefail
HOOK_INPUT=$(cat)
export HOOK_INPUT
exec python3 - <<'PY'
import json, os, re, shlex, sys
try:
    cmd = json.loads(os.environ.get("HOOK_INPUT", "{}")).get("tool_input", {}).get("command", "")
except json.JSONDecodeError:
    sys.exit(0)
if "Zotero" not in cmd:
    sys.exit(0)
def block(why):
    print(f"Blocked: {why}. Zotero is read-only for the agent (AGENTS.md).", file=sys.stderr)
    sys.exit(2)
# redirections into Zotero
if re.search(r'>>?\s*["\']?[^\s"\']*Zotero', cmd):
    block("redirect writes under ~/Zotero")
for seg in re.split(r'[;&|]+|\n', cmd):
    try:
        toks = shlex.split(seg)
    except ValueError:
        toks = seg.split()
    if not toks:
        continue
    # skip env assignments
    while toks and ("=" in toks[0] and not toks[0].startswith("-")):
        toks = toks[1:]
    if not toks:
        continue
    prog = toks[0].rsplit("/", 1)[-1]
    args = toks[1:]
    if not any("Zotero" in a for a in args):
        continue
    if prog in {"rm", "rmdir", "truncate", "chmod", "chown", "ln", "mkdir", "touch",
                "sqlite3", "tee", "shred", "unlink", "rsync", "dd"}:
        block(f"'{prog}' on a ~/Zotero path")
    if prog in {"sed", "perl"} and any(a.startswith("-i") for a in args):
        block(f"in-place '{prog}' on a ~/Zotero path")
    if prog == "mv":
        block("'mv' of a ~/Zotero path")
    if prog in {"cp", "install"}:
        nonopt = [a for a in args if not a.startswith("-")]
        if nonopt and "Zotero" in nonopt[-1]:
            block(f"'{prog}' with a ~/Zotero destination")
    if prog in {"python", "python3", "node", "ruby", "osascript"} and "-c" in args:
        block(f"inline '{prog}' script mentioning ~/Zotero")
sys.exit(0)
PY
