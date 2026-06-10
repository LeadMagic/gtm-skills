#!/usr/bin/env python3
import sys
from pathlib import Path

terms = ["utm", "campaign", "naming", "hierarchy"]
path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path or not path.exists():
    print("Usage: check-output.py path/to/deliverable.md")
    raise SystemExit(2)
t = path.read_text().lower()
missing = [x for x in terms if x not in t]
if missing:
    print("Missing:", ", ".join(missing))
    raise SystemExit(1)
print("OK")
