#!/usr/bin/env python3
"""Validate a completed GTM context pack."""

import re
import sys
from pathlib import Path

REQUIRED = (
    "context metadata",
    "company and product facts",
    "icp and buying situations",
    "positioning chain",
    "customer language",
    "voice and claims",
    "gtm operating constraints",
    "contradictions and open questions",
)
PLACEHOLDER = re.compile(r"\[(?:company|owner|scope|date|claim|source|segment|role|event|alternative|job|metric|traits|terms|proof|issue|skill)[^\]]*\]", re.I)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check-output.py path/to/gtm-context-pack.md")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL — file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()
    errors = [f"missing section: {section}" for section in REQUIRED if section not in lower]
    if PLACEHOLDER.search(text):
        errors.append("unresolved template placeholders remain")
    if not re.search(r"\b(verified|owner-confirmed|assumption|contradicted|unknown)\b", lower):
        errors.append("claim states are missing")
    if not re.search(r"\b(?:19|20)\d{2}-\d{2}-\d{2}\b", text):
        errors.append("no ISO freshness date found")

    if errors:
        print("FAIL — GTM context pack:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("PASS — GTM context pack includes the required evidence and decision fields")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
