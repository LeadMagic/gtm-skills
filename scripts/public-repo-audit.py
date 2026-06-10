#!/usr/bin/env python3
"""Public-facing repository hygiene checks for LeadMagic/gtm-skills.

This script intentionally avoids embedding private denylist terms. It enforces
public, generic controls only: generated-count drift, marketplace-discoverable
skill paths, required community/security files, allowed public URL domains,
lockfile integrity, and dependency/CI hygiene.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
STANDARD_COMPATIBILITY = (
    "Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, "
    "Copilot, Zed, VS Code, Goose"
)
REQUIRED_PUBLIC_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "CITATION.cff",
    "AGENTS.md",
    "CLAUDE.md",
    "skills.lock",
    "taxonomy.csv",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/dependabot.yml",
    ".github/workflows/validate.yml",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
]
ALLOWED_URL_HOSTS = {
    "github.com",
    "img.shields.io",
    "leadmagic.io",
    "www.leadmagic.io",
    "agentskills.io",
}
JUNK_SUFFIXES = (".orig", ".rej", "~")
JUNK_NAMES = {".DS_Store"}
TELEMETRY_PACKAGES = {
    "@sentry/",
    "sentry",
    "posthog",
    "posthog-js",
    "segment",
    "@segment/",
    "mixpanel",
    "statsig",
    "amplitude-js",
    "@amplitude/",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter(path: Path) -> str:
    text = read(path)
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) >= 3 else ""


def yaml_scalar(fm: str, key: str) -> str:
    block = re.search(rf"^{re.escape(key)}:\s*>-?\n((?:\s{{2}}.+\n?)+)", fm, re.M)
    if block:
        return " ".join(line.strip() for line in block.group(1).splitlines() if line.strip())
    inline = re.search(rf"^{re.escape(key)}:\s*\"?(.+?)\"?\s*$", fm, re.M)
    return inline.group(1).strip() if inline else ""


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_PUBLIC_FILES:
        if not (ROOT / rel).exists():
            fail(f"missing required public file: {rel}", failures)

    junk = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name in JUNK_NAMES or path.name.endswith(JUNK_SUFFIXES) or path.name.startswith("_TEMPLATE"):
            junk.append(str(path.relative_to(ROOT)))
    if junk:
        fail(f"junk/stale files present: {', '.join(junk[:20])}", failures)

    skills = sorted((ROOT / "skills").rglob("SKILL.md"))
    if not skills:
        fail("no skills found", failures)

    # Marketplace discovery: skills/<category>/<skill>/SKILL.md only (flat depth).
    bad_paths = []
    for path in skills:
        rel_parts = path.relative_to(ROOT).parts
        flat = len(rel_parts) == 4 and rel_parts[0] == "skills" and rel_parts[3] == "SKILL.md"
        if not flat:
            bad_paths.append(str(path.relative_to(ROOT)))
    if bad_paths:
        fail(f"non-marketplace-discoverable skill paths: {', '.join(bad_paths[:20])}", failures)

    bad_skills = []
    category_counts: dict[str, int] = {}
    for path in skills:
        rel = path.relative_to(ROOT)
        category = rel.parts[1]
        category_counts[category] = category_counts.get(category, 0) + 1
        fm = frontmatter(path)
        name = yaml_scalar(fm, "name")
        compatibility = yaml_scalar(fm, "compatibility")
        rel_skill_parts = path.relative_to(ROOT / "skills").parts
        skill_dir = rel_skill_parts[1]  # skills/<category>/<skill>/SKILL.md
        name_ok = name == skill_dir
        if not name_ok:
            bad_skills.append(f"{rel}: name {name!r} does not match directory {skill_dir!r}")
        if compatibility != STANDARD_COMPATIBILITY:
            bad_skills.append(f"{rel}: non-standard compatibility")
        if re.search(r"^\s*frameworks:\s*\[\s*\]\s*$", fm, re.M):
            bad_skills.append(f"{rel}: empty frameworks array")
        if "frameworks:" not in fm and "## Authoritative" not in read(path):
            bad_skills.append(f"{rel}: missing frameworks/authoritative foundations")
    if bad_skills:
        fail("skill metadata failures:\n  " + "\n  ".join(bad_skills[:30]), failures)

    taxonomy_path = ROOT / "taxonomy.csv"
    if taxonomy_path.exists():
        with taxonomy_path.open(newline="", encoding="utf-8") as handle:
            taxonomy_rows = list(csv.DictReader(handle))
        if len(taxonomy_rows) != len(skills):
            fail(f"taxonomy count {len(taxonomy_rows)} != skill count {len(skills)}", failures)
        disk_slugs = {
            f"{p.relative_to(ROOT / 'skills').parts[0]}/{p.relative_to(ROOT / 'skills').parts[1]}"
            for p in skills
        }
        csv_slugs: set[str] = set()
        for row in taxonomy_rows:
            slug = row.get("slug", "").strip()
            name = row.get("name", "").strip()
            category = row.get("category", "").strip()
            path = row.get("path", "").strip()
            expected_path = f"skills/{category}/{slug}/SKILL.md"
            key = f"{category}/{slug}"
            if slug != name:
                fail(f"taxonomy.csv slug != name for {key}: {slug!r} vs {name!r}", failures)
            if path != expected_path:
                fail(f"taxonomy.csv path mismatch for {key}: {path!r} != {expected_path!r}", failures)
            if not (ROOT / path).exists():
                fail(f"taxonomy.csv path missing on disk: {path}", failures)
            csv_slugs.add(key)
        if csv_slugs != disk_slugs:
            missing = sorted(disk_slugs - csv_slugs)[:5]
            extra = sorted(csv_slugs - disk_slugs)[:5]
            fail(
                f"taxonomy.csv keys != disk skills (missing sample: {missing}, extra sample: {extra})",
                failures,
            )

    lock_path = ROOT / "skills.lock"
    if lock_path.exists():
        lock = json.loads(read(lock_path))
        if lock.get("total_skills") != len(skills):
            fail(f"skills.lock total {lock.get('total_skills')} != skill count {len(skills)}", failures)
        lock_skills = lock.get("skills", {})
        if len(lock_skills) != len(skills):
            fail(f"skills.lock entries {len(lock_skills)} != skill count {len(skills)}", failures)
        for name, meta in lock_skills.items():
            raw_path = meta.get("path", "")
            if isinstance(raw_path, list):
                skill_path = ROOT / "skills" / Path(*raw_path)
            else:
                skill_path = ROOT / str(raw_path)
            if not skill_path.exists():
                fail(f"skills.lock missing path for {name}: {meta.get('path')}", failures)
                continue
            digest = hashlib.sha256(skill_path.read_bytes()).hexdigest()
            if digest != meta.get("sha256"):
                fail(f"skills.lock hash drift for {name}", failures)

    count = len(skills)
    count_surfaces = {
        "README.md": read(ROOT / "README.md") if (ROOT / "README.md").exists() else "",
        "AGENTS.md": read(ROOT / "AGENTS.md") if (ROOT / "AGENTS.md").exists() else "",
        "CLAUDE.md": read(ROOT / "CLAUDE.md") if (ROOT / "CLAUDE.md").exists() else "",
        "package.json": read(ROOT / "package.json") if (ROOT / "package.json").exists() else "",
        "references/skill-index-master.md": read(ROOT / "references/skill-index-master.md") if (ROOT / "references/skill-index-master.md").exists() else "",
        ".claude-plugin/plugin.json": read(ROOT / ".claude-plugin/plugin.json") if (ROOT / ".claude-plugin/plugin.json").exists() else "",
        ".claude-plugin/marketplace.json": read(ROOT / ".claude-plugin/marketplace.json") if (ROOT / ".claude-plugin/marketplace.json").exists() else "",
    }
    for surface, text in count_surfaces.items():
        if str(count) not in text:
            fail(f"{surface} does not mention current skill count {count}", failures)

    # URL policy: public docs should only link to the repo, LeadMagic, badges, and the spec.
    url_files = ["README.md", "docs/INSTALL.md", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "CITATION.cff"]
    for rel in url_files:
        path = ROOT / rel
        if not path.exists():
            continue
        for url in sorted(set(re.findall(r"https?://[^\s)\]\"<>]+", read(path)))):
            host = urlparse(url).netloc.lower()
            if host.startswith("www.") and host[4:] in ALLOWED_URL_HOSTS:
                host = host[4:]
            if host not in ALLOWED_URL_HOSTS:
                fail(f"unapproved public URL in {rel}: {url}", failures)

    package_path = ROOT / "package.json"
    if package_path.exists():
        package = json.loads(read(package_path))
        package_blob = json.dumps({
            "dependencies": package.get("dependencies", {}),
            "devDependencies": package.get("devDependencies", {}),
            "optionalDependencies": package.get("optionalDependencies", {}),
        }).lower()
        for name in TELEMETRY_PACKAGES:
            if name.lower() in package_blob:
                fail(f"telemetry dependency present in package.json: {name}", failures)

    workflow_path = ROOT / ".github/workflows/validate.yml"
    if workflow_path.exists():
        workflow = read(workflow_path)
        if "permissions:\n      contents: read" not in workflow:
            fail("validate workflow must use least-privilege contents: read permissions", failures)
        if "gh skill publish --dry-run" not in workflow:
            fail("validate workflow must run gh skill publish --dry-run", failures)
        if "references/skill-index-master.md" not in workflow:
            fail("validate workflow must verify references/skill-index-master.md drift", failures)
        if "concurrency:" not in workflow:
            fail("validate workflow missing concurrency guard", failures)

    plugin_path = ROOT / ".claude-plugin/plugin.json"
    if plugin_path.exists():
        plugin = json.loads(read(plugin_path))
        globs = plugin.get("skills", [])
        if globs != ["skills/*/*/SKILL.md"]:
            fail(f"plugin.json skills globs must be flat-only ['skills/*/*/SKILL.md'], got {globs}", failures)

    if failures:
        print(f"\nPublic repo audit failed: {len(failures)} issue(s).")
        return 1

    print(
        f"Public repo audit passed: {count} skills, {len(category_counts)} categories, "
        "generated artifacts current, public metadata clean."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
