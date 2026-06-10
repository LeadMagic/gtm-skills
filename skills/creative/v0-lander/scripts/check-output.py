#!/usr/bin/env python3
"""Validate V0 Lander deliverables."""

import sys
from pathlib import Path

TERMS = ['v0 lander', 'vercel', 'lander', 'creative', 'page', 'generative']


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace").lower()
    if len(text.strip()) < 200:
        print("FAIL — deliverable too short (<200 chars)")
        return 1

    missing = [t for t in TERMS if t not in text]
    if missing:
        print("FAIL — missing terms:", ", ".join(missing))
        return 1

    print("PASS — V0 Lander deliverable meets minimum checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
