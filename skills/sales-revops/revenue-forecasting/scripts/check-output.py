#!/usr/bin/env python3
"""Validate a completed revenue forecast pack."""
from pathlib import Path
import sys

required = [
    "## Context", "## Framework Basis", "## Recommendation",
    "## Category Definitions", "## Forecast Bridge",
    "## Opportunity Evidence and Risk", "## Historical Assumptions",
    "## Implementation Steps", "## Metrics", "## Quality Check",
]
path = Path(sys.argv[1]) if len(sys.argv) == 2 else None
if not path or not path.is_file():
    print("Usage: check-output.py path/to/revenue-forecast-pack.md")
    raise SystemExit(2)
text = path.read_text(encoding="utf-8", errors="replace")
missing = [section for section in required if section not in text]
placeholders = [token for token in ("[period]", "[amount]", "[deal]", "[action]") if token in text]
if missing or placeholders:
    if missing:
        print("Missing sections:", ", ".join(missing))
    if placeholders:
        print("Unfilled placeholders:", ", ".join(placeholders))
    raise SystemExit(1)
print("OK: revenue forecast pack contains the required model, evidence, and actions")
