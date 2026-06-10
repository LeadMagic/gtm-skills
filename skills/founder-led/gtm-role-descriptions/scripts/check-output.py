#!/usr/bin/env python3
"""Validate GTM role description deliverables."""

import re
import sys
from pathlib import Path

REQUIRED_JD_SECTIONS = [
    r"why this role exists",
    r"what you.ll own|what you'll own",
    r"success",
    r"who you are",
    r"compensation|ote|salary",
    r"apply|how to apply",
]

ANTI_PATTERNS = [
    r"\brockstar\b",
    r"\bninja\b",
    r"\bguru\b",
    r"\bhustle culture\b",
    r"\bfast[- ]paced environment\b",
]

REQUIRED_COMP_FIELDS = [
    r"ote|target cash|salary",
    r"quota|okr",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace").lower()


def check_jd(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["JD file is empty or missing"]

    for pattern in REQUIRED_JD_SECTIONS:
        if not re.search(pattern, content, re.I):
            errors.append(f"JD missing section matching: {pattern}")

    for pattern in ANTI_PATTERNS:
        if re.search(pattern, content, re.I):
            errors.append(f"JD contains anti-pattern: {pattern}")

    if not re.search(r"\$\d", content):
        errors.append("JD should include compensation dollar range")

    if re.search(r"\b\d+\+?\s*years?\s+(of\s+)?experience\b", content, re.I):
        if not re.search(r"not required|instead", content, re.I):
            errors.append("JD has years-only requirement without alternative criteria")

    return errors


def check_comp(content: str) -> list[str]:
    errors = []
    if not content.strip():
        return ["Comp plan file is empty or missing"]

    for pattern in REQUIRED_COMP_FIELDS:
        if not re.search(pattern, content, re.I):
            errors.append(f"Comp plan missing: {pattern}")

    return errors


def main() -> int:
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    jd_path = base / "job-description.md"
    comp_path = base / "comp-plan.md"

    all_errors = []
    all_errors.extend(check_jd(read_text(jd_path)))
    all_errors.extend(check_comp(read_text(comp_path)))

    if all_errors:
        print("FAIL — GTM role description validation:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("PASS — JD and comp plan meet GTM role description standards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
