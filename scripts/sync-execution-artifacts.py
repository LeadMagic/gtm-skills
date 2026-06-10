#!/usr/bin/env python3
"""Ensure every SKILL.md Execution Artifacts section lists the standard artifact triad."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

STANDARD = [
    ("references/framework-notes.md", "- `references/framework-notes.md` — Framework index and authority routing"),
    ("templates/output-template.md", "- `templates/output-template.md` — Primary deliverable shell"),
    ("scripts/check-output.py", "- `scripts/check-output.py` — Lightweight deliverable validator"),
]


def sync_skill(skill_md: Path) -> bool:
    content = skill_md.read_text(encoding="utf-8")
    m = re.search(r"## Execution Artifacts\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not m:
        return False

    body = m.group(1).strip()
    lines = [ln for ln in body.splitlines() if ln.strip()]

    ordered: list[str] = []
    for _key, std_line in STANDARD:
        hit = next((ln for ln in lines if _key in ln), None)
        ordered.append(hit or std_line)

    for ln in lines:
        if not any(key in ln for key, _ in STANDARD):
            ordered.append(ln)

    new_body = "\n".join(ordered) + "\n"
    if new_body.strip() == body.strip():
        return False

    new_content = content[: m.start(1)] + new_body + content[m.end(1) :]
    skill_md.write_text(new_content, encoding="utf-8")
    return True


def main() -> int:
    updated = 0
    for skill_md in sorted(SKILLS.rglob("SKILL.md")):
        if sync_skill(skill_md):
            updated += 1
            print(f"  synced: {skill_md.parent.relative_to(SKILLS)}")
    print(f"\nUpdated {updated} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
