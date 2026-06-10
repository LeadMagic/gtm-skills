#!/usr/bin/env python3
"""Validate hiring-by-role deliverables."""

import sys

REQUIRED_SECTIONS = [
    "Interview Plan",
    "Process",
    "Scorecard",
    "Quality check",
]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: check-output.py <markdown-file>")
        return 1

    text = open(sys.argv[1], encoding="utf-8").read()
    missing = [s for s in REQUIRED_SECTIONS if s not in text]

    if missing:
        print("FAIL: missing sections:", ", ".join(missing))
        return 1

    print("OK: hiring-by-role deliverable sections present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
