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
# Keep in sync with scripts/lib/compatibility.js
STANDARD_COMPATIBILITY = (
    "Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, "
    "Goose, Hermes, Jesse, Windsurf, Zed"
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
    ".github/workflows/regenerate.yml",
    "scripts/generated-artifacts.txt",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
]
ALLOWED_URL_HOSTS = {
    "github.com",
    "img.shields.io",
    "leadmagic.io",
    "www.leadmagic.io",
    "agentskills.io",
    "agent-skills.md",
    "agenticskills.io",
    "skills.re",
    "skillindex.dev",
    "theskills.directory",
    "claude.ai",
    "support.claude.com",
    "code.claude.com",
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

PACKAGE_KINDS = ("entrypoints", "references", "templates", "scripts", "assets", "other")


def discover_package_files() -> list[Path]:
    return sorted(
        path
        for path in (ROOT / "skills").rglob("*")
        if path.is_file()
        and path.name != ".DS_Store"
        and path.suffix != ".pyc"
        and "__pycache__" not in path.parts
    )


def package_file_kind(path: Path) -> str:
    relative = path.relative_to(ROOT / "skills")
    if path.name == "SKILL.md":
        return "entrypoints"
    for kind in ("references", "templates", "scripts", "assets"):
        if kind in relative.parts[2:]:
            return kind
    return "other"


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
        package_files = discover_package_files()
        package_paths = {path.relative_to(ROOT).as_posix() for path in package_files}
        expected_file_counts = {
            kind: sum(package_file_kind(path) == kind for path in package_files)
            for kind in PACKAGE_KINDS
        }
        if lock.get("version") != "2.0.0":
            fail(f"skills.lock version {lock.get('version')!r} != '2.0.0'", failures)
        if lock.get("total_skills") != len(skills):
            fail(f"skills.lock total {lock.get('total_skills')} != skill count {len(skills)}", failures)
        if lock.get("total_files") != len(package_files):
            fail(f"skills.lock file total {lock.get('total_files')} != packaged file count {len(package_files)}", failures)
        if lock.get("file_counts") != expected_file_counts:
            fail(f"skills.lock file counts {lock.get('file_counts')} != {expected_file_counts}", failures)
        readme_text = read(ROOT / "README.md")
        readme_inventory = {
            "Marketplace-discoverable skills": len(skills),
            "Skill entrypoint files": expected_file_counts["entrypoints"],
            "Reference files": expected_file_counts["references"],
            "Template files": expected_file_counts["templates"],
            "Script files": expected_file_counts["scripts"],
            "Asset files": expected_file_counts["assets"],
            "Other packaged files": expected_file_counts["other"],
            "Total packaged skill files": len(package_files),
        }
        for label, value in readme_inventory.items():
            row = f"| {label} | {value} |"
            if row not in readme_text:
                fail(f"README exact inventory row missing or stale: {row}", failures)
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
        lock_artifacts = lock.get("artifacts", {})
        lock_paths = set(lock_artifacts)
        if lock_paths != package_paths:
            missing = sorted(package_paths - lock_paths)[:5]
            extra = sorted(lock_paths - package_paths)[:5]
            fail(
                f"skills.lock artifact paths != packaged files (missing sample: {missing}, extra sample: {extra})",
                failures,
            )
        for relative_path, meta in lock_artifacts.items():
            if relative_path not in package_paths:
                continue
            artifact_path = ROOT / relative_path
            if not artifact_path.is_file():
                continue
            digest = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
            if digest != meta.get("sha256"):
                fail(f"skills.lock artifact hash drift for {relative_path}", failures)
            if artifact_path.stat().st_size != meta.get("size_bytes"):
                fail(f"skills.lock artifact size drift for {relative_path}", failures)
            if package_file_kind(artifact_path) != meta.get("kind"):
                fail(f"skills.lock artifact kind drift for {relative_path}", failures)

    count = len(skills)
    count_surfaces = {
        "README.md": read(ROOT / "README.md") if (ROOT / "README.md").exists() else "",
        "AGENTS.md": read(ROOT / "AGENTS.md") if (ROOT / "AGENTS.md").exists() else "",
        "CLAUDE.md": read(ROOT / "CLAUDE.md") if (ROOT / "CLAUDE.md").exists() else "",
        "package.json": read(ROOT / "package.json") if (ROOT / "package.json").exists() else "",
        "CITATION.cff": read(ROOT / "CITATION.cff") if (ROOT / "CITATION.cff").exists() else "",
        "references/skill-index-master.md": read(ROOT / "references/skill-index-master.md") if (ROOT / "references/skill-index-master.md").exists() else "",
        "skills/foundation/using-gtm-skills/SKILL.md": read(ROOT / "skills/foundation/using-gtm-skills/SKILL.md") if (ROOT / "skills/foundation/using-gtm-skills/SKILL.md").exists() else "",
        ".claude-plugin/plugin.json": read(ROOT / ".claude-plugin/plugin.json") if (ROOT / ".claude-plugin/plugin.json").exists() else "",
        ".claude-plugin/marketplace.json": read(ROOT / ".claude-plugin/marketplace.json") if (ROOT / ".claude-plugin/marketplace.json").exists() else "",
    }
    for surface, text in count_surfaces.items():
        if str(count) not in text:
            fail(f"{surface} does not mention current skill count {count}", failures)

    readme = count_surfaces.get("README.md", "")
    if f"skills-{count}-blue" not in readme or f"**{count} go-to-market (GTM) agent skills" not in readme:
        fail("README.md skill badge and lead inventory must match the on-disk count", failures)
    stale_install_patterns = {
        "codex skills install": "Codex has no direct skills-install subcommand; use gh skill",
        "claude plugins add": "Claude plugin installation uses marketplace add plus plugin install",
        "gh skill install LeadMagic/gtm-skills --category": "gh skill has no --category flag",
    }
    install_surfaces = [
        "README.md",
        "docs/INSTALL.md",
        "AGENTS.md",
        "CLAUDE.md",
        "skills/foundation/using-gtm-skills/SKILL.md",
    ]
    for rel in install_surfaces:
        text = read(ROOT / rel) if (ROOT / rel).exists() else ""
        for pattern, reason in stale_install_patterns.items():
            if pattern in text:
                fail(f"stale install command in {rel}: {pattern!r} ({reason})", failures)

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

    manifest_path = ROOT / "scripts/generated-artifacts.txt"
    manifest_entries: list[str] = []
    if manifest_path.exists():
        for raw in read(manifest_path).splitlines():
            line = raw.split("#", 1)[0].strip()
            if line:
                manifest_entries.append(line)
    if len(manifest_entries) < 8:
        fail("scripts/generated-artifacts.txt must list all generated catalog paths", failures)
    if "README.md" not in manifest_entries:
        fail("README.md must be generated from the on-disk skill catalog", failures)

    package_path = ROOT / "package.json"
    if package_path.exists() and manifest_entries:
        package_text = read(package_path)
        if "scripts/check-generated.sh" not in package_text:
            fail("package.json check:generated must use scripts/check-generated.sh", failures)
        if "scripts/regenerate.sh" not in package_text:
            fail("package.json build/regenerate must use scripts/regenerate.sh", failures)

    workflow_path = ROOT / ".github/workflows/validate.yml"
    if workflow_path.exists():
        workflow = read(workflow_path)
        if "permissions:\n      contents: read" not in workflow:
            fail("validate workflow must use least-privilege contents: read permissions", failures)
        if "gh skill publish --dry-run" not in workflow:
            fail("validate workflow must run gh skill publish --dry-run", failures)
        if "check:generated" not in workflow:
            fail("validate workflow must run npm run check:generated", failures)
        if "audit-checkers.py" not in read(ROOT / "package.json"):
            fail("npm verification must execute every skill-local output checker", failures)
        if "concurrency:" not in workflow:
            fail("validate workflow missing concurrency guard", failures)

    regen_path = ROOT / ".github/workflows/regenerate.yml"
    if regen_path.exists():
        regen = read(regen_path)
        if "permissions:\n  contents: write" not in regen:
            fail("regenerate workflow must request contents: write", failures)
        if "scripts/regenerate.sh" not in regen:
            fail("regenerate workflow must run scripts/regenerate.sh", failures)
        if "workflow_dispatch" not in regen:
            fail("regenerate workflow must support workflow_dispatch", failures)
        if "generated-artifacts.txt" not in regen:
            fail("regenerate workflow must read scripts/generated-artifacts.txt", failures)

    plugin_path = ROOT / ".claude-plugin/plugin.json"
    if plugin_path.exists():
        plugin = json.loads(read(plugin_path))
        skill_roots = plugin.get("skills", [])
        if skill_roots != ["./skills"]:
            fail(f"plugin.json must expose the validated recursive skill root ['./skills'], got {skill_roots}", failures)

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
