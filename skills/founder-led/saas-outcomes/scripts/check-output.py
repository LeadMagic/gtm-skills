#!/usr/bin/env python3
"""Validate SaaS outcomes deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_TERMS = [
    r"bootstrap|venture|cash.?flow",
    r"multiple|valuation|arr",
    r"end.?goal|path|outcome",
]


def check(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Deliverable is empty"]

    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required topic matching: {pattern}")

    if re.search(r"guaranteed \d+x|will sell for", lower):
        errors.append("Avoid guaranteed valuation claims — use ranges and assumptions")

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — SaaS outcomes deliverable:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("OK: SaaS outcomes deliverable passes checklist")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
