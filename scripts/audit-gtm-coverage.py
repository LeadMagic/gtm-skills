#!/usr/bin/env python3
"""Validate the curated GTM capability map against skills and expert entries."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "references" / "gtm-capability-map.json"
EXPERTS_PATH = ROOT / "references" / "experts.md"


def main() -> int:
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    capabilities = data.get("capabilities", [])
    skill_files = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
    skill_names = {path.parent.name for path in skill_files}
    expert_headings = {
        line[4:].split(" — ")[0].strip()
        for line in EXPERTS_PATH.read_text(encoding="utf-8").splitlines()
        if line.startswith("### ")
    }
    errors: list[str] = []
    ids: set[str] = set()
    mapped_skills: set[str] = set()
    mapped_experts: set[str] = set()

    for capability in capabilities:
        capability_id = capability.get("id", "")
        if not capability_id or capability_id in ids:
            errors.append(f"invalid or duplicate capability id: {capability_id!r}")
        ids.add(capability_id)
        skills = capability.get("skills", [])
        experts = capability.get("experts", [])
        if not skills or not experts:
            errors.append(f"{capability_id}: must name at least one skill and expert")
        for skill in skills:
            mapped_skills.add(skill)
            if skill not in skill_names:
                errors.append(f"{capability_id}: missing skill {skill}")
        for expert in experts:
            mapped_experts.add(expert)
            if expert not in expert_headings:
                errors.append(f"{capability_id}: missing expert heading {expert}")

    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        print(f"GTM coverage audit failed: {len(errors)} error(s)")
        return 1
    print(
        "GTM coverage audit passed: "
        f"{len(capabilities)} capabilities, {len(mapped_skills)} mapped skills, "
        f"{len(mapped_experts)} mapped experts, {len(skill_names)} catalog skills"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
