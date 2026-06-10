#!/usr/bin/env python3
"""Validate sales coaching deliverables."""
import re, sys
from pathlib import Path

REQUIRED = [
    r"reks|efforts|knowledge|skills",
    r"meddicc|deal review|scorecard",
    r"1:1|cadence|coaching",
]
OPTIONAL_BONUS = [r"jacco|winning by design", r"jolt|indecision", r"call coaching|one keep"]

def check(content: str) -> list[str]:
    if not content.strip():
        return ["Empty deliverable"]
    lower = content.lower()
    errs = []
    for p in REQUIRED:
        if not re.search(p, lower, re.I):
            errs.append(f"Missing required topic: {p}")
    if re.search(r"hit your number|close harder|send more roi", lower):
        errs.append("Avoid results-only coaching — use REKS/MEDDICC/JOLT")
    return errs

def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2
    errs = check(path.read_text(encoding="utf-8", errors="replace"))
    if errs:
        print("FAIL — sales coaching deliverable:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("OK: sales coaching deliverable passes checklist")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
