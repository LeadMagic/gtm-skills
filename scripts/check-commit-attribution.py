#!/usr/bin/env python3
"""Fail CI when commits include agent co-author trailers (e.g. Cursor)."""

from __future__ import annotations

import re
import subprocess
import sys

BLOCKED = (
    re.compile(r"co-authored-by:\s*cursor\b", re.I),
    re.compile(r"made with \[cursor\]", re.I),
)


def commits_to_check() -> list[tuple[str, str]]:
    """Check commits on this branch not on origin/main, else HEAD only."""
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        capture_output=True,
        text=True,
        check=False,
    )
    if base.returncode == 0 and base.stdout.strip():
        rev_range = f"{base.stdout.strip()}..HEAD"
    else:
        rev_range = "HEAD"
    log = subprocess.run(
        ["git", "log", rev_range, "--format=%H%x09%s"],
        capture_output=True,
        text=True,
        check=True,
    )
    rows: list[tuple[str, str]] = []
    for line in log.stdout.splitlines():
        if "\t" not in line:
            continue
        sha, subject = line.split("\t", 1)
        body = subprocess.run(
            ["git", "log", "-1", "--format=%B", sha],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        rows.append((sha[:7], body))
    return rows or [(
        subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=True).stdout.strip(),
        subprocess.run(["git", "log", "-1", "--format=%B"], capture_output=True, text=True, check=True).stdout,
    )]


def main() -> int:
    violations: list[str] = []
    for short_sha, body in commits_to_check():
        for line in body.splitlines():
            stripped = line.strip()
            if any(p.search(stripped) for p in BLOCKED):
                violations.append(f"{short_sha}: {stripped}")
    if violations:
        print("FAIL — agent co-author trailers found in commit message(s):", file=sys.stderr)
        for item in violations:
            print(f"  - {item}", file=sys.stderr)
        print(
            "\nCursor is fine in skill compatibility docs; do not add Co-authored-by: Cursor on commits.",
            file=sys.stderr,
        )
        print("Fix: git commit --amend, or run scripts/strip-commit-trailers.py on .git/COMMIT_EDITMSG", file=sys.stderr)
        return 1
    print("PASS — no agent co-author trailers in checked commits")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
