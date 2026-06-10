#!/usr/bin/env python3
"""Validate pipeline-management / GTM sales process deliverables."""
from pathlib import Path
import sys

REQUIRED = [
    "## Context",
    "## Framework Basis",
    "## Stage Map",
    "## MEDDICC Scorecard",
    "## Conversion Targets",
    "## Handoffs",
    "## Quality Check",
]

STAGE_HEADERS = ["Goal", "Exit Criteria"]

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path or not path.exists():
    print("Usage: check-output.py path/to/deliverable.md")
    raise SystemExit(2)

text = path.read_text()
missing = [s for s in REQUIRED if s not in text]
if missing:
    print("Missing sections:", ", ".join(missing))
    raise SystemExit(1)

stage_section = text.split("## Stage Map", 1)
if len(stage_section) < 2:
    print("Stage Map section empty")
    raise SystemExit(1)

for header in STAGE_HEADERS:
    if header not in stage_section[1]:
        print(f"Stage Map missing column: {header}")
        raise SystemExit(1)

print("OK: sales process deliverable contains required sections")
