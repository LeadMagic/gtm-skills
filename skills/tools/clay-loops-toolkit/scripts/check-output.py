#!/usr/bin/env python3
"""Validate Clay Loop blueprint deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Context",
    "## 4-Table Architecture",
    "## Monitor Logic",
    "## LeadMagic",
    "## Routing",
    "## Quality Check",
]

REQUIRED_TERMS = [
    r"signal_detected",
    r"leadmagic|LeadMagic",
    r"verify",
    r"source_url|why_now",
]


def check(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Blueprint file is empty"]

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing section: {section}")

    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required term matching: {pattern}")

    if re.search(r"claygent.*find.*email|guess.*email", lower):
        errors.append("Do not use Claygent for email find in loops — use LeadMagic")

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/loop-blueprint.md")
        return 2

    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — Clay loop blueprint validation:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("PASS — Clay loop blueprint meets tools/clay-loops-toolkit standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
