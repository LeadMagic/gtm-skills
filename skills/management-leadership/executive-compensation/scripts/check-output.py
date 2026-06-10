#!/usr/bin/env python3
"""Validate executive compensation deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_TERMS = [
    r"ote|variable|base",
    r"equity|vest|cliff",
    r"nrr|arr|revenue",
    r"severance|clawback|cause",
]


def check(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Deliverable is empty"]
    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required topic matching: {pattern}")
    if re.search(r"bookings.?only|single.?gate", lower) and not re.search(r"nrr|efficiency|rule of 40", lower):
        errors.append("CRO/VP packages should include revenue quality gates (NRR or efficiency)")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2
    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — executive compensation deliverable:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: executive compensation deliverable passes checklist")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
