#!/usr/bin/env python3
"""Audit skill layout and link resolvability across LeadMagic/gtm-skills.

Checks every skills/<category>/<skill>/ tree:
  (a) SKILL.md at flat depth skills/<category>/<skill>/SKILL.md
  (b) frontmatter name equals directory name
  (c) resolvable reference targets in SKILL.md plus references/*.md and templates/*.md

Extraction mirrors scripts/validate-skills.js: markdown link targets plus
backtick-quoted repo paths. Resolution order:
  - skills/...           → repo root
  - references|templates|scripts|assets/... → skill directory, then repo root
  - ../...               → relative to the containing file
  - other relative paths → containing file dir, then skill dir, then repo root

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
    r"^(?:\.\./|references|templates|scripts|assets|skills)/[A-Za-z0-9._/-]+\.(?:md|py|js|csv|json)$"
)
MD_LINK = re.compile(r"\]\(([^)]+)\)")
BACKTICK = re.compile(r"`([^`]+)`")
SKILL_LOCAL_PREFIX = ("references/", "templates/", "scripts/", "assets/")


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


def skill_dir_for(path: Path) -> Path | None:
    try:
        rel = path.relative_to(SKILLS_DIR)
    except ValueError:
        return None
    if len(rel.parts) < 2:
        return None
    return SKILLS_DIR / rel.parts[0] / rel.parts[1]


def target_resolves(target: str, file_path: Path, skill_dir: Path) -> bool:
    candidates: list[Path] = []

    if target.startswith("skills/"):
        candidates.append(ROOT / target)
    elif target.startswith("../"):
        cur = file_path.parent
        rel = target
        while rel.startswith("../"):
            rel = rel[3:]
            cur = cur.parent
        candidates.append(cur / rel)
    elif target.startswith(SKILL_LOCAL_PREFIX):
        candidates.append(skill_dir / target)
        candidates.append(ROOT / target)
    else:
        candidates.append(file_path.parent / target)
        candidates.append(skill_dir / target)
        candidates.append(ROOT / target)

    return any(p.exists() for p in candidates)


def frontmatter_name(content: str) -> str | None:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    fm = content[4:end]
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("'\"") if m else None


def scannable_files(skill_dir: Path) -> list[Path]:
    files = [skill_dir / "SKILL.md"]
    for sub in ("references", "templates"):
        d = skill_dir / sub
        if d.is_dir():
            files.extend(sorted(d.glob("*.md")))
    return files


def main() -> int:
    bad_depth: list[str] = []
    bad_name: list[str] = []
    bad_refs: list[str] = []

    skills = sorted(SKILLS_DIR.rglob("SKILL.md"))
    checked = 0
    files_scanned = 0

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

        for scan_path in scannable_files(skill_dir):
            files_scanned += 1
            scan_content = scan_path.read_text(encoding="utf-8", errors="replace")
            for target in extract_targets(scan_content):
                if not target_resolves(target, scan_path, skill_dir):
                    bad_refs.append(f"{scan_path.relative_to(ROOT).as_posix()}: {target}")

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
        print(
            f"\nReference audit FAILED: {findings} finding(s) across "
            f"{checked} skills ({files_scanned} files scanned)."
        )
        return 1

    print(
        f"Reference audit passed: {checked} skills, {files_scanned} files scanned, "
        "all reference targets resolve, layout and frontmatter names clean."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
