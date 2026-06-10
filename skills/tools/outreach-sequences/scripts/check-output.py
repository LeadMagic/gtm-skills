#!/usr/bin/env python3
"""Validate outreach-sequences deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Context",
    "## Framework Basis",
    "## CRM Field Map",
    "## Enrollment Gate",
    "## Trigger Architecture",
    "## Quality Check",
]

REQUIRED_TERMS = [r"verify|trigger|enroll", r"outreach|sequence"]


def check(content: str) -> list[str]:
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing section: {section}")
    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required term matching: {pattern}")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2
    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — outreach-sequences validation:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS — outreach-sequences deliverable meets standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
