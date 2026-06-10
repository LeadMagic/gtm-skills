#!/usr/bin/env python3
"""Validate JOLT / buyer indecision deliverables."""

import re
import sys
from pathlib import Path

REQUIRED = [
    r"j(?:udge)?|indecision|fomu",
    r"offer|recommend",
    r"limit|option|path",
    r"take risk|risk off|de-risk|phased|pilot|success plan",
]
MIN_CHARS = 200


def check(content: str) -> list[str]:
    if len(content.strip()) < MIN_CHARS:
        return [f"Deliverable too short (<{MIN_CHARS} chars)"]
    lower = content.lower()
    errs = []
    for pattern in REQUIRED:
        if not re.search(pattern, lower, re.I):
            errs.append(f"Missing JOLT element: {pattern}")
    if re.search(r"more roi|additional deck|full menu|unlimited poc", lower):
        errs.append("Avoid ROI-piling — use Limit + Take risk for indecision")
    return errs


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    errs = check(path.read_text(encoding="utf-8", errors="replace"))
    if errs:
        print("FAIL — buyer indecision deliverable:")
        for err in errs:
            print(f"  - {err}")
        return 1

    print("PASS — buyer indecision deliverable meets JOLT checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
