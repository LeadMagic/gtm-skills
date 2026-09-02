#!/usr/bin/env python3
"""Materialize repository-level references inside the skills that use them.

Agent Skills installers copy one skill directory at a time. This generator makes
references to the root ``references/`` catalog portable while retaining one
canonical source file. Generated copies are checked for drift in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SHARED = ROOT / "references"
MARKER_PREFIX = "<!-- AUTO-GENERATED shared reference: "
REMOTE_REFERENCE_BASE = "https://github.com/LeadMagic/gtm-skills/blob/main/references/"
ROOT_REFERENCE = re.compile(r"(?<![A-Za-z0-9_./-])references/([A-Za-z0-9._/-]+\.md)")
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")


def generated_text(relative: str) -> str:
    source = SHARED / relative
    marker = f"{MARKER_PREFIX}references/{relative}; run npm run regenerate. -->\n\n"
    content = source.read_text(encoding="utf-8")
    content = ROOT_REFERENCE.sub(
        lambda match: REMOTE_REFERENCE_BASE + match.group(1),
        content,
    )

    def rewrite_relative_link(match: re.Match[str]) -> str:
        raw = match.group(1)
        target = raw.strip().split()[0].split("#", 1)[0] if raw.strip() else ""
        if not target or re.match(r"^(?:https?:|mailto:|#)", target, re.IGNORECASE):
            return match.group(0)
        resolved = safe_shared((PurePosixPath(relative).parent / target).as_posix())
        return f"]({REMOTE_REFERENCE_BASE}{resolved})" if resolved else match.group(0)

    content = MARKDOWN_LINK.sub(rewrite_relative_link, content)
    # Generated copies should be portable and pass Git whitespace checks even
    # when a canonical Markdown source uses trailing spaces for hard breaks.
    content = "\n".join(line.rstrip() for line in content.rstrip().splitlines()) + "\n"
    return marker + content


def is_generated(path: Path) -> bool:
    try:
        return path.read_text(encoding="utf-8", errors="replace").startswith(MARKER_PREFIX)
    except OSError:
        return False


def safe_shared(relative: str) -> str | None:
    clean = PurePosixPath(relative)
    if clean.is_absolute() or ".." in clean.parts or clean.suffix != ".md":
        return None
    candidate = SHARED.joinpath(*clean.parts)
    return clean.as_posix() if candidate.is_file() else None


def referenced_shared(content: str, *, shared_parent: PurePosixPath | None = None) -> set[str]:
    found = {value for raw in ROOT_REFERENCE.findall(content) if (value := safe_shared(raw))}
    if shared_parent is None:
        return found

    for raw in MARKDOWN_LINK.findall(content):
        target = raw.strip().split()[0].split("#", 1)[0] if raw.strip() else ""
        if not target or re.match(r"^(?:https?:|mailto:|#)", target, re.IGNORECASE):
            continue
        if target.startswith("references/"):
            target = target[len("references/") :]
        else:
            target = (shared_parent / target).as_posix()
        if value := safe_shared(target):
            found.add(value)
    return found


def expected_for_skill(skill_dir: Path) -> dict[Path, str]:
    original_files = [
        path
        for path in skill_dir.rglob("*.md")
        if path.is_file() and not is_generated(path)
    ]
    original_local_refs = {
        path.relative_to(skill_dir / "references").as_posix()
        for path in original_files
        if (skill_dir / "references") in path.parents
    }

    required: set[str] = set()
    for path in original_files:
        required.update(referenced_shared(path.read_text(encoding="utf-8", errors="replace")))
    required.difference_update(original_local_refs)

    return {
        skill_dir / "references" / relative: generated_text(relative)
        for relative in sorted(required)
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when generated copies are missing or stale.")
    args = parser.parse_args()

    skill_dirs = sorted(path.parent for path in SKILLS.glob("*/*/SKILL.md"))
    expected: dict[Path, str] = {}
    for skill_dir in skill_dirs:
        expected.update(expected_for_skill(skill_dir))

    existing = {
        path
        for skill_dir in skill_dirs
        for path in skill_dir.rglob("*.md")
        if is_generated(path)
    }

    if args.check:
        missing = sorted(set(expected) - existing)
        unexpected = sorted(existing - set(expected))
        stale = sorted(path for path in set(expected) & existing if path.read_text(encoding="utf-8") != expected[path])
        for label, paths in (("missing", missing), ("unexpected", unexpected), ("stale", stale)):
            for path in paths:
                print(f"{label}: {path.relative_to(ROOT)}")
        if missing or unexpected or stale:
            print("Shared-reference materialization FAILED. Run: npm run regenerate")
            return 1
        print(f"Shared references verified: {len(expected)} generated copies across {len(skill_dirs)} skills.")
        return 0

    for path in existing:
        path.unlink()
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Materialized {len(expected)} shared-reference copies across {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
