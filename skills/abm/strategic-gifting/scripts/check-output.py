#!/usr/bin/env python3
"""Validate strategic gifting deliverables."""
import re, sys
from pathlib import Path

TERMS = [r"gift|giftology|sendoso|personal", r"policy|compliance|limit", r"tier|abm|story"]

def check(content: str) -> list[str]:
    if not content.strip():
        return ["Empty"]
    lower = content.lower()
    errs = [f"Missing: {p}" for p in TERMS if not re.search(p, lower, re.I)]
    if re.search(r"logo swag|unstick.*deal|bribe", lower) and not re.search(r"do not|never|jolt", lower):
        errs.append("Address bribery/unstick — use JOLT not gifts")
    return errs

def main() -> int:
    path = Path(Path(sys.argv[1]) if len(sys.argv) > 1 else "")
    if not path.exists():
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
