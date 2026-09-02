#!/usr/bin/env python3
"""Validate a completed skills-lock integrity report."""
from pathlib import Path
import sys

required = ["## Context", "## Framework Basis", "## Recommendation", "## Implementation Steps", "## Metrics", "## Quality Check"]
path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path or not path.exists():
    print("Usage: check-output.py path/to/deliverable.md")
    raise SystemExit(2)
text = path.read_text()
missing = [section for section in required if section not in text]
if missing:
    print("Missing sections:", ", ".join(missing))
    raise SystemExit(1)
placeholders = ("[owner/repository]", "[count]", "[Pass, fail", "[Generate or repair")
present = [placeholder for placeholder in placeholders if placeholder in text]
if present:
    print("Unfilled placeholders:", ", ".join(present))
    raise SystemExit(1)
print("OK: deliverable contains required sections")
