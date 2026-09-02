#!/usr/bin/env python3
"""Exercise every skill-local deliverable checker against its own blank template."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TIMEOUT_SECONDS = 5


def main() -> int:
    failures: list[str] = []
    checkers = sorted(SKILLS.glob("*/*/scripts/check-output.py"))

    for checker in checkers:
        skill_dir = checker.parents[1]
        template = skill_dir / "templates" / "output-template.md"
        rel = checker.relative_to(ROOT)

        try:
            compile(checker.read_text(encoding="utf-8"), str(rel), "exec")
        except SyntaxError as error:
            failures.append(f"{rel}: syntax error: {error}")
            continue

        if not checker.stat().st_mode & 0o100:
            failures.append(f"{rel}: is not executable")

        try:
            usage = subprocess.run(
                [sys.executable, str(checker)],
                cwd=skill_dir,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
            if usage.returncode != 2:
                failures.append(f"{rel}: no-argument usage exit was {usage.returncode}, expected 2")

            blank = subprocess.run(
                [sys.executable, str(checker), str(template)],
                cwd=skill_dir,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
            if blank.returncode != 1:
                failures.append(
                    f"{rel}: unfilled output-template exit was {blank.returncode}, expected 1"
                )
        except subprocess.TimeoutExpired:
            failures.append(f"{rel}: exceeded {TIMEOUT_SECONDS}s timeout")

    if failures:
        print(f"Checker audit failed: {len(failures)} issue(s)")
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"Checker audit passed: {len(checkers)} executable checkers reject usage errors and unfilled templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
