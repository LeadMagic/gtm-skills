#!/usr/bin/env python3
"""Generate or verify the complete packaged-file skills.lock for gtm-skills.

Source of truth: every marketplace-discoverable skill and packaged file under skills/.

Usage:
  python3 scripts/generate-skills-lock.py          # rewrite skills.lock
  python3 scripts/generate-skills-lock.py --check  # verify skills.lock is current
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
LOCK_PATH = ROOT / "skills.lock"


def discover_skills() -> list[Path]:
    skills = sorted(SKILLS_DIR.rglob("SKILL.md"))
    missed = []
    for p in skills:
        rel = p.relative_to(SKILLS_DIR).parts
        if rel[-1] != "SKILL.md" or len(rel) != 3:
            missed.append(str(p.relative_to(ROOT)))
    if missed:
        raise SystemExit("Non-marketplace-discoverable skill paths:\n" + "\n".join(missed))
    return skills


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def discover_package_files() -> list[Path]:
    ignored_names = {".DS_Store"}
    return sorted(
        path
        for path in SKILLS_DIR.rglob("*")
        if path.is_file()
        and path.name not in ignored_names
        and path.suffix != ".pyc"
        and "__pycache__" not in path.parts
    )


def file_kind(path: Path) -> str:
    relative = path.relative_to(SKILLS_DIR)
    if path.name == "SKILL.md":
        return "entrypoints"
    for kind in ("references", "templates", "scripts", "assets"):
        if kind in relative.parts[2:]:
            return kind
    return "other"


def build_lock() -> dict:
    skills = {}
    for path in discover_skills():
        rel_parts = path.relative_to(SKILLS_DIR).parts
        key = "/".join(rel_parts[:-1])  # e.g. tools/clay-loops-toolkit
        skills[key] = {
            "path": list(rel_parts),
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
    package_files = discover_package_files()
    file_counts = {
        kind: sum(file_kind(path) == kind for path in package_files)
        for kind in ("entrypoints", "references", "templates", "scripts", "assets", "other")
    }
    artifacts = {
        path.relative_to(ROOT).as_posix(): {
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
            "kind": file_kind(path),
        }
        for path in package_files
    }
    return {
        "version": "2.0.0",
        "repository": "LeadMagic/gtm-skills",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "total_skills": len(skills),
        "total_files": len(package_files),
        "file_counts": file_counts,
        "skills": dict(sorted(skills.items())),
        "artifacts": artifacts,
    }


def stable(lock: dict) -> dict:
    clone = dict(lock)
    clone["generated_at"] = "<ignored>"
    return clone


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify skills.lock without writing")
    args = parser.parse_args()

    new_lock = build_lock()
    if args.check:
        if not LOCK_PATH.exists():
            print("skills.lock missing")
            return 1
        old_lock = json.loads(LOCK_PATH.read_text())
        if stable(old_lock) != stable(new_lock):
            print("skills.lock is stale; run python3 scripts/generate-skills-lock.py")
            print(
                f"expected {new_lock['total_skills']} skills and "
                f"{new_lock['total_files']} packaged files"
            )
            return 1
        print(
            f"skills.lock verified: {new_lock['total_skills']} skills, "
            f"{new_lock['total_files']} packaged files"
        )
        return 0

    if LOCK_PATH.exists():
        old_lock = json.loads(LOCK_PATH.read_text())
        if stable(old_lock) == stable(new_lock):
            new_lock["generated_at"] = old_lock.get("generated_at", new_lock["generated_at"])

    LOCK_PATH.write_text(json.dumps(new_lock, indent=2) + "\n")
    print(
        f"skills.lock generated: {new_lock['total_skills']} skills, "
        f"{new_lock['total_files']} packaged files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
