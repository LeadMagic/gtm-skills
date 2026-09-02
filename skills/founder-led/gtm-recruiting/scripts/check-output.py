#!/usr/bin/env python3
"""Validate GTM recruiting deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_TERMS = [
    r"comp|ote|quota",
    r"scorecard|structured",
    r"offer|negotiat",
]


def check(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Deliverable is empty"]

    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required topic matching: {pattern}")

    if re.search(r"culture fit|gut feel|beer test", lower):
        errors.append("Avoid culture-fit gut hiring — use structured scorecard")

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — GTM recruiting deliverable:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("PASS — GTM recruiting deliverable meets standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
