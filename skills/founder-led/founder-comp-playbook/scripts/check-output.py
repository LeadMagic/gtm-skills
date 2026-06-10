#!/usr/bin/env python3
"""Validate founder comp deliverables."""
import re, sys
from pathlib import Path

TERMS = [r"ote|quota|5:1|5 to 1", r"equity|fd%|vest", r"founder|runway|arr", r"ramp|attainment|negotiat"]

def check(content: str) -> list[str]:
    if not content.strip():
        return ["Empty deliverable"]
    lower = content.lower()
    errs = []
    for p in TERMS:
        if not re.search(p, lower, re.I):
            errs.append(f"Missing: {p}")
    if re.search(r"\$200k ote.*\$400k quota", lower.replace(",", "")):
        errs.append("Quota may not match 5:1 — verify math")
    return errs

def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2
    errs = check(path.read_text(encoding="utf-8", errors="replace"))
    if errs:
        for e in errs:
            print(f"  - {e}")
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
