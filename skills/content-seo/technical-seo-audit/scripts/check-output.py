#!/usr/bin/env python3
"""Validate a completed technical SEO audit."""

import re
import sys
from pathlib import Path

REQUIRED = (
    "audit metadata",
    "executive status",
    "crawl and index funnel",
    "issue register",
    "canonical signal matrix",
    "rendered metadata and structured data",
    "core web vitals",
    "prioritized remediation backlog",
    "release verification and monitoring",
)
PLACEHOLDER = re.compile(r"\[(?:site|url|scope|yyyy|type|count|source|issue|reproduction|fix|owner|template|delta|result|action|ms|score|cause|change|impact|size|dependency|test)[^\]]*\]", re.I)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check-output.py path/to/technical-seo-audit.md")
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
    for metric in ("lcp", "inp", "cls"):
        if metric not in lower:
            errors.append(f"missing Core Web Vital: {metric.upper()}")
    if not re.search(r"\b(field|crux|search console)\b", lower):
        errors.append("field-data evidence or limitation is not stated")

    if errors:
        print("FAIL — technical SEO audit:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("PASS — technical SEO audit includes evidence, prioritization, and verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
