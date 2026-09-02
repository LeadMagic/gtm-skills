#!/usr/bin/env python3
"""Validate Clay table blueprint deliverables."""
from pathlib import Path
import sys

REQUIRED = ["## Context", "## Table Architecture", "## Waterfall", "## Output", "## Quality Check"]

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path or not path.exists():
    print("Usage: check-output.py path/to/deliverable.md")
    raise SystemExit(2)

text = path.read_text()
missing = [s for s in REQUIRED if s not in text]
if missing:
    print("Missing sections:", ", ".join(missing))
    raise SystemExit(1)
print("OK: Clay blueprint valid")
