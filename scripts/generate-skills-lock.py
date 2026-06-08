#!/usr/bin/env python3
"""Generate or verify skills.lock for gtm-skills.

Source of truth: every marketplace-discoverable SKILL.md under skills/.

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
        if len(rel) != 3 or rel[-1] != "SKILL.md":
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


def build_lock() -> dict:
    skills = {}
    for path in discover_skills():
        rel = path.relative_to(ROOT).as_posix()
        category, slug, _ = path.relative_to(SKILLS_DIR).parts
        key = f"{category}/{slug}"
        skills[key] = {
            "path": rel,
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
    return {
        "version": "1.0.0",
        "repository": "LeadMagic/gtm-skills",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "total_skills": len(skills),
        "skills": dict(sorted(skills.items())),
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
            print(f"expected {new_lock['total_skills']} skills")
            return 1
        print(f"skills.lock verified: {new_lock['total_skills']} skills")
        return 0

    if LOCK_PATH.exists():
        old_lock = json.loads(LOCK_PATH.read_text())
        if stable(old_lock) == stable(new_lock):
            new_lock["generated_at"] = old_lock.get("generated_at", new_lock["generated_at"])

    LOCK_PATH.write_text(json.dumps(new_lock, indent=2) + "\n")
    print(f"skills.lock generated: {new_lock['total_skills']} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
