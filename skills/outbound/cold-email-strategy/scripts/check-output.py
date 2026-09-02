#!/usr/bin/env python3
"""Validate cold-email strategy deliverables."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = (
    "campaign context",
    "campaign cell",
    "contact thesis",
    "touch map",
    "reply and exception routing",
    "sending and governance",
    "experiment plan",
    "measurement funnel",
    "implementation handoff",
)
PLACEHOLDERS = re.compile(r"\[(?:fill|todo|tbd)\]|<[^>]+>", re.IGNORECASE)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL — file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    normalized = text.lower()
    if len(text.strip()) < 800:
        print("FAIL — deliverable is too short for an executable sequence strategy")
        return 1

    missing = [heading for heading in REQUIRED_HEADINGS if f"## {heading}" not in normalized]
    if missing:
        print("FAIL — missing sections: " + ", ".join(missing))
        return 1
    if PLACEHOLDERS.search(text):
        print("FAIL — unresolved template placeholders remain")
        return 1
    if text.count("|") < 35:
        print("FAIL — expected populated campaign, touch, routing, experiment, and measurement tables")
        return 1

    print("PASS — cold-email strategy includes required decisions and no placeholders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
