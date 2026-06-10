#!/usr/bin/env python3
"""Remove agent/tool co-author trailers from a git commit message file."""

from __future__ import annotations

import re
import sys
from pathlib import Path

def is_blocked_trailer(line: str) -> bool:
    stripped = line.strip()
    return bool(
        re.match(r"^co-authored-by:\s*cursor\b", stripped, re.I)
        or re.match(r"^made with \[cursor\]", stripped, re.I)
    )


def strip_message(text: str) -> str:
    lines = text.splitlines()
    kept = [line for line in lines if not is_blocked_trailer(line)]
    while kept and not kept[-1].strip():
        kept.pop()
    return "\n".join(kept).rstrip() + ("\n" if kept else "")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: strip-commit-trailers.py <commit-msg-file>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8", errors="replace")
    cleaned = strip_message(original)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
