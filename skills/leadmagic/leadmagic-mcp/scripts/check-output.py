#!/usr/bin/env python3
"""Validate leadmagic-mcp deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Context",
    "## Framework Basis",
    "## Enabled Tool Categories",
    "## Agent Rules",
    "## Test Workflows",
    "## Quality Check",
]

REQUIRED_TERMS = [r"mcp|agent|tool", r"confirm|verify|guardrail"]


def check(content: str) -> list[str]:
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing section: {section}")
    lower = content.lower()
    for pattern in REQUIRED_TERMS:
        if not re.search(pattern, lower, re.I):
            errors.append(f"Missing required term matching: {pattern}")
    if re.search(r"api[_-]?key\s*[:=]\s*['\"]?[a-z0-9]{20}", lower):
        errors.append("Do not include API keys in deliverable")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2
    errors = check(path.read_text(encoding="utf-8", errors="replace"))
    if errors:
        print("FAIL — leadmagic-mcp validation:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS — leadmagic-mcp deliverable meets standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
