#!/usr/bin/env python3
"""Validate GTM prompt specs and loop blueprints."""
from pathlib import Path
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path or not path.exists():
    print("Usage: check-output.py path/to/prompt-spec.md|prompt-loop-blueprint.md")
    raise SystemExit(2)

text = path.read_text()
is_loop = "Prompt Loop Blueprint" in text
required = (
    ["## Context", "## Steps", "## Gates", "## Quality Check"]
    if is_loop
    else ["## Context", "## Variables", "## Prompt Text", "## Output Schema", "## Quality Gate"]
)
missing = [s for s in required if s not in text]
if missing:
    print("Missing sections:", ", ".join(missing))
    raise SystemExit(1)
print("OK: prompt deliverable valid")
