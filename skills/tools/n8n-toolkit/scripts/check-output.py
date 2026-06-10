#!/usr/bin/env python3
"""Validate n8n GTM workflow deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Context",
    "## Framework Basis",
    "## Workflow Blueprint",
    "## Node Configuration",
    "## Error Handling",
    "## Quality Check",
]

FLOW_ID_PATTERN = re.compile(
    r"\b(INB|OUT|SIG|LIF|REV|MCP)-\d{2}\b", re.I
)

REQUIRED_QUALITY_ITEMS = [
    r"idempotency",
    r"error",
    r"credential|webhook auth|HMAC",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def check_deliverable(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Deliverable file is empty or missing"]

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing section: {section}")

    if not FLOW_ID_PATTERN.search(content):
        errors.append(
            "Missing flow ID (INB-01, OUT-01, SIG-01, LIF-03, REV-01, MCP-01, etc.)"
        )

    quality_block = ""
    if "## Quality Check" in content:
        quality_block = content.split("## Quality Check", 1)[1].lower()

    for pattern in REQUIRED_QUALITY_ITEMS:
        if not re.search(pattern, quality_block, re.I):
            errors.append(f"Quality Check missing item matching: {pattern}")

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    errors = check_deliverable(read_text(path))
    if errors:
        print("FAIL — n8n workflow deliverable validation:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PASS — n8n GTM workflow deliverable meets standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
