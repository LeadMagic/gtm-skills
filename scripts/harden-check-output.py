#!/usr/bin/env python3
"""Make legacy check-output scripts reject their own unfilled templates."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MARKER = "# Reject unresolved fields from the shipped output template."
GUARD = (
    f"{MARKER}\n"
    "{indent}if any(marker in {variable}.lower() for marker in "
    "('[field]', '[value]', '[company]', '[one paragraph:', '[fill per')):\n"
    "{indent}    print('FAIL — unresolved output-template placeholders remain')\n"
    "{indent}    return 1"
)


def template_passes(checker: Path) -> bool:
    template = checker.parents[1] / "templates" / "output-template.md"
    result = subprocess.run(
        [sys.executable, str(checker), str(template)],
        cwd=checker.parents[1],
        capture_output=True,
        timeout=5,
        check=False,
    )
    return result.returncode == 0


def harden(checker: Path) -> bool:
    text = checker.read_text(encoding="utf-8")
    if MARKER in text or not template_passes(checker):
        return False

    read_line = re.search(
        r"^(?P<indent>\s*)(?P<variable>text|t) = path\.read_text\([^\n]*\)(?:\.lower\(\))?\s*$",
        text,
        re.M,
    )
    if read_line:
        indent = read_line.group("indent")
        variable = read_line.group("variable")
        guard = GUARD.format(indent=indent, variable=variable)
        if not indent:
            guard = guard.replace("    return 1", "    raise SystemExit(1)")
        text = text[: read_line.end()] + "\n" + guard + text[read_line.end() :]
    else:
        check_fn = re.search(r"^def check\(content: str\) -> list\[str\]:\s*$", text, re.M)
        if not check_fn:
            raise RuntimeError(f"Cannot locate safe hardening point in {checker.relative_to(ROOT)}")
        guard = GUARD.format(indent="    ", variable="content")
        text = text[: check_fn.end()] + "\n" + guard + text[check_fn.end() :]

    checker.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    updated = []
    for checker in sorted(SKILLS.glob("*/*/scripts/check-output.py")):
        if harden(checker):
            updated.append(checker.relative_to(ROOT))

    print(f"Hardened {len(updated)} checker(s).")
    for path in updated:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
