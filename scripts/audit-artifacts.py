#!/usr/bin/env python3
"""Audit the complete packaged artifact surface under skills/."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
RESOURCE_DIRS = {"references", "templates", "scripts", "assets"}
JUNK_NAMES = {".DS_Store", "Thumbs.db"}
JUNK_SUFFIXES = {".orig", ".rej", ".swp", ".tmp", "~"}
MIN_SIZES = {"references": 300, "templates": 200, "scripts": 100}


def kind(path: Path) -> str:
    relative = path.relative_to(SKILLS_DIR)
    if path.name == "SKILL.md":
        return "entrypoints"
    for candidate in RESOURCE_DIRS:
        if candidate in relative.parts[2:]:
            return candidate
    return "other"


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    skill_roots = {path.parent for path in skill_files}
    package_files = sorted(path for path in SKILLS_DIR.rglob("*") if path.is_file())

    for skill_file in skill_files:
        relative = skill_file.relative_to(SKILLS_DIR)
        if len(relative.parts) != 3:
            errors.append(f"non-discoverable skill path: {relative}")
            continue
        root = skill_file.parent
        required = (
            root / "references" / "framework-notes.md",
            root / "templates" / "output-template.md",
            root / "scripts" / "check-output.py",
        )
        for required_file in required:
            if not required_file.is_file():
                errors.append(f"missing required artifact: {required_file.relative_to(ROOT)}")

    for path in package_files:
        relative = path.relative_to(SKILLS_DIR)
        if path.is_symlink():
            errors.append(f"symlink is not portable: {relative}")
        if path.name in JUNK_NAMES or "__pycache__" in relative.parts or path.suffix == ".pyc":
            errors.append(f"cache or platform junk file: {relative}")
        if any(path.name.endswith(suffix) for suffix in JUNK_SUFFIXES):
            errors.append(f"temporary or merge-residue file: {relative}")
        if path.stat().st_size == 0:
            errors.append(f"empty packaged file: {relative}")

        owners = [root for root in skill_roots if root == path or root in path.parents]
        if len(owners) != 1:
            errors.append(f"file does not belong to exactly one skill: {relative}")

        file_kind = kind(path)
        if path.name != "SKILL.md" and file_kind == "other":
            errors.append(f"artifact outside references/templates/scripts/assets: {relative}")
        minimum = MIN_SIZES.get(file_kind)
        if minimum and path.stat().st_size < minimum:
            errors.append(
                f"thin {file_kind} artifact ({path.stat().st_size} < {minimum} bytes): {relative}"
            )
        if file_kind == "scripts" and path.suffix in {".py", ".sh"} and not (path.stat().st_mode & 0o111):
            errors.append(f"script is not executable: {relative}")

    counts = Counter(kind(path) for path in package_files)
    expected_entrypoints = len(skill_files)
    if counts["entrypoints"] != expected_entrypoints:
        errors.append(
            f"entrypoint count {counts['entrypoints']} != discovered skills {expected_entrypoints}"
        )

    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        print(f"Artifact audit failed: {len(errors)} error(s)")
        return 1

    ordered = ("entrypoints", "references", "templates", "scripts", "assets", "other")
    breakdown = ", ".join(f"{name}={counts[name]}" for name in ordered)
    print(f"Artifact audit passed: {len(skill_files)} skills, {len(package_files)} files ({breakdown})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
