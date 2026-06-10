#!/usr/bin/env python3
"""Validate GTM leadership deliverables (hire, coach, PIP, fire, resignation, crisis)."""

import re
import sys
from pathlib import Path

DELIVERABLE_MARKERS = [
    r"hire|scorecard|candidate|vp sales|cro",
    r"coach|reks|difficult conversation|radical candor",
    r"pip|performance improvement|milestone|quota",
    r"terminat|fire|exit|handoff",
    r"resign|counter-offer|exit interview",
    r"crisis|holding statement|war room|severity",
]
LEADERSHIP_ANCHORS = [
    r"comp|compensation|quota:ote|bridge group",
    r"care.*challenge|document|feedback",
]
MIN_CHARS = 200


def check(content: str) -> list[str]:
    if len(content.strip()) < MIN_CHARS:
        return [f"Deliverable too short (<{MIN_CHARS} chars)"]
    lower = content.lower()
    errs = []

    if sum(1 for p in DELIVERABLE_MARKERS if re.search(p, lower, re.I)) < 1:
        errs.append("Missing deliverable type (hire, coach, PIP, fire, resignation, or crisis)")

    for pattern in LEADERSHIP_ANCHORS:
        if not re.search(pattern, lower, re.I):
            errs.append(f"Missing leadership anchor: {pattern}")

    if re.search(r"hit your number harder|yell louder|no documentation", lower):
        errs.append("Avoid results-only leadership — document facts and use Radical Candor structure")

    return errs


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    errs = check(path.read_text(encoding="utf-8", errors="replace"))
    if errs:
        print("FAIL — GTM leadership deliverable:")
        for err in errs:
            print(f"  - {err}")
        return 1

    print("PASS — GTM leadership deliverable meets minimum checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
