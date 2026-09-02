#!/usr/bin/env python3
"""Validate a completed win-loss program pack."""
from pathlib import Path
import sys

required = [
    "## Context", "## Framework Basis", "## Recommendation",
    "## Sample and Limitations", "## Decision Timeline",
    "## Decision Drivers and Sentiment", "## Findings and Counterexamples",
    "## Implementation Steps", "## Metrics", "## Quality Check",
]
path = Path(sys.argv[1]) if len(sys.argv) == 2 else None
if not path or not path.is_file():
    print("Usage: check-output.py path/to/win-loss-pack.md")
    raise SystemExit(2)
text = path.read_text(encoding="utf-8", errors="replace")
missing = [section for section in required if section not in text]
placeholders = [token for token in ("[decision]", "[segment]", "[finding]", "[artifact]") if token in text]
if missing or placeholders:
    if missing:
        print("Missing sections:", ", ".join(missing))
    if placeholders:
        print("Unfilled placeholders:", ", ".join(placeholders))
    raise SystemExit(1)
print("OK: win-loss pack contains the required evidence, decisions, and actions")
