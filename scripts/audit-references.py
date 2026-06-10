#!/usr/bin/env python3
"""Audit cross-skill references and skill layout for LeadMagic/gtm-skills.

Walks every skills/<category>/<skill>/SKILL.md and reports:
  (a) reference targets that resolve neither skill-locally nor at the repo root,
  (b) SKILL.md files not at the exact depth skills/<category>/<skill>/SKILL.md,
  (c) frontmatter name that does not equal the skill directory name.

Extraction mirrors scripts/validate-skills.js: markdown link targets plus
backtick-quoted repo paths. A target is valid if it exists relative to the
skill directory (skill-local artifact) OR relative to the repo root (shared
catalog such as references/experts.md, or a full skills/<cat>/<skill>/... path).

Exit non-zero on any finding.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

CHECKABLE_EXT = re.compile(r"\.(?:md|py|js|csv|json)$")
BACKTICK_PATH = re.compile(
    r"^(?:references|templates|scripts|assets|skills)/[A-Za-z0-9._/-]+\.(?:md|py|js|csv|json)$"
)
MD_LINK = re.compile(r"\]\(([^)]+)\)")
BACKTICK = re.compile(r"`([^`]+)`")


def extract_targets(content: str) -> list[str]:
    targets: set[str] = set()
    for raw in MD_LINK.findall(content):
        target = raw.strip()
        parts = target.split()
        if parts:
            target = parts[0]
        if not target or re.match(r"^(?:https?:|mailto:|#)", target, re.I):
            continue
        target = target.split("#", 1)[0]
        if CHECKABLE_EXT.search(target):
            targets.add(target)
    for raw in BACKTICK.findall(content):
        target = raw.strip()
        if BACKTICK_PATH.match(target):
            targets.add(target)
    return sorted(targets)


def target_resolves(target: str, skill_dir: Path) -> bool:
    if (skill_dir / target).exists():
        return True
    if (ROOT / target).exists():
        return True
    return False


def frontmatter_name(content: str) -> str | None:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    fm = content[4:end]
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("'\"") if m else None


def main() -> int:
    bad_depth: list[str] = []
    bad_name: list[str] = []
    bad_refs: list[str] = []

    skills = sorted(SKILLS_DIR.rglob("SKILL.md"))
    checked = 0
    for path in skills:
        rel_parts = path.relative_to(ROOT).parts
        flat = len(rel_parts) == 4 and rel_parts[0] == "skills" and rel_parts[3] == "SKILL.md"
        rel = path.relative_to(ROOT).as_posix()
        if not flat:
            bad_depth.append(rel)
            continue
        checked += 1
        skill_dir = path.parent
        dir_name = rel_parts[2]
        content = path.read_text(encoding="utf-8", errors="replace")

        name = frontmatter_name(content)
        if name != dir_name:
            bad_name.append(f"{rel}: name {name!r} != directory {dir_name!r}")

        for target in extract_targets(content):
            if not target_resolves(target, skill_dir):
                bad_refs.append(f"{rel}: {target}")

    findings = len(bad_depth) + len(bad_name) + len(bad_refs)
    if bad_depth:
        print(f"\nSKILL.md not at depth skills/<category>/<skill>/SKILL.md ({len(bad_depth)}):")
        for item in bad_depth:
            print(f"  - {item}")
    if bad_name:
        print(f"\nfrontmatter name != directory name ({len(bad_name)}):")
        for item in bad_name:
            print(f"  - {item}")
    if bad_refs:
        print(f"\nunresolvable reference targets ({len(bad_refs)}):")
        for item in bad_refs:
            print(f"  - {item}")

    if findings:
        print(f"\nReference audit FAILED: {findings} finding(s) across {len(skills)} SKILL.md files.")
        return 1

    print(
        f"Reference audit passed: {checked} skills, all reference targets resolve, "
        "layout and frontmatter names clean."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
