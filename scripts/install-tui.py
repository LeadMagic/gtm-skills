#!/usr/bin/env python3
"""Preview-first installer for the LeadMagic GTM Agent Skills catalog.

The zero-dependency interactive flow selects targets, scope, and exact skill
groups. Existing folders are skipped by default. ``--force`` is the only path
that replaces an installed folder.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SHARED_REFERENCES = ROOT / "references"

BUNDLES: dict[str, tuple[str, ...]] = {
    "buyer-insight": ("customer-research", "win-loss-analysis", "competitive-intel", "positioning-messaging"),
    "outbound-stack": ("cold-email-strategy", "cold-email-copywriting", "domain-infrastructure", "email-deliverability", "inbox-setup", "sending-platforms", "reply-handling"),
    "prospecting-stack": ("lead-finding", "lead-enrichment", "email-finding", "contact-verification", "list-building", "signal-scoring"),
    "sales-revops-stack": ("pipeline-management", "revenue-forecasting", "meeting-prep", "deal-desk", "sales-enablement", "demo-scripts", "objection-handling"),
    "founder-gtm": ("founder-sales", "solo-founder-gtm", "pricing-strategy", "positioning-messaging", "pitch-deck-builder", "fundraising-strategy", "financial-modeling"),
    "inbound-stack": ("content-marketing", "inbound-triage", "landing-pages", "seo-strategy", "social-selling", "linkedin-algorithm"),
    "customer-success": ("customer-onboarding", "cs-playbooks", "sla-management", "headless-support", "qbr-planning"),
    "analytics-stack": ("gtm-metrics", "attribution", "campaign-analytics", "tracking-plan", "a-b-testing"),
    "automation-stack": ("clay-automation", "n8n-automation", "crm-integration", "api-enrichment", "waterfall-enrichment", "mcp-setup"),
    "abm-stack": ("abm-strategy", "account-selection", "multi-thread-orchestration", "strategic-gifting"),
    "startup-essentials": ("gtm-context-bootstrap", "gtm-context", "icp-scoring", "customer-research", "positioning-messaging", "pricing-strategy", "founder-sales", "saas-metrics-calculator"),
}


@dataclass(frozen=True)
class Target:
    key: str
    label: str
    gh_agent: str | None
    project_path: str
    user_path: str
    notes: str
    aliases: tuple[str, ...] = ()


TARGETS: tuple[Target, ...] = (
    Target("claude", "Claude Code", "claude-code", ".claude/skills", "~/.claude/skills", "Official Claude skill discovery folders.", ("claude-code",)),
    Target("copilot", "GitHub Copilot", "github-copilot", ".github/skills", "~/.copilot/skills", "GitHub's Agent Skills installer.", ("github-copilot", "vscode")),
    Target("codex", "Codex", "codex", ".agents/skills", "~/.codex/skills", "GitHub's Agent Skills installer."),
    Target("cursor", "Cursor", "cursor", ".agents/skills", "~/.agents/skills", "Shared Agent Skills directory."),
    Target("gemini", "Gemini CLI", "gemini-cli", ".agents/skills", "~/.agents/skills", "Shared Agent Skills directory.", ("gemini-cli",)),
    Target("opencode", "OpenCode", "opencode", ".agents/skills", "~/.agents/skills", "Shared Agent Skills directory."),
    Target("windsurf", "Windsurf", "windsurf", ".agents/skills", "~/.agents/skills", "Shared Agent Skills directory."),
    Target("goose", "Goose", "goose", ".agents/skills", "~/.agents/skills", "GitHub's Agent Skills installer."),
    Target("hermes", "Hermes", "universal", ".agents/skills", "~/.agents/skills", "Universal Agent Skills directory."),
    Target("jesse", "Jesse", None, ".jesse/skills", "~/.jesse/skills", "Jesse's local skills directory."),
)


def discover_catalog() -> dict[str, list[Path]]:
    catalog: dict[str, list[Path]] = {}
    for skill_file in sorted(SKILLS.glob("*/*/SKILL.md")):
        catalog.setdefault(skill_file.parent.parent.name, []).append(skill_file.parent)
    return catalog


def all_skills(catalog: dict[str, list[Path]]) -> list[Path]:
    return [skill for category in sorted(catalog) for skill in catalog[category]]


def parse_csv(values: list[str] | None) -> list[str]:
    return [item.strip() for value in (values or []) for item in value.split(",") if item.strip()]


def resolve_skill_names(names: list[str], catalog: dict[str, list[Path]]) -> list[Path]:
    lookup = {path.name: path for path in all_skills(catalog)}
    unknown = sorted(set(names) - set(lookup))
    if unknown:
        raise SystemExit("Unknown skill(s): " + ", ".join(unknown))
    return [lookup[name] for name in names]


def dedupe(paths: list[Path]) -> list[Path]:
    return list(dict.fromkeys(paths))


def parse_multi_choice(raw: str, labels: list[str]) -> list[str]:
    if raw.strip().lower() == "all":
        return labels
    selected: list[str] = []
    for value in re.split(r"[\s,]+", raw.strip().lower()):
        if not value:
            continue
        if value.isdigit() and 1 <= int(value) <= len(labels):
            label = labels[int(value) - 1]
        else:
            label = next((item for item in labels if item.lower() == value), "")
        if not label:
            raise SystemExit(f"Unknown selection: {value}")
        if label not in selected:
            selected.append(label)
    return selected


def checkbox_menu(title: str, labels: list[str], details: dict[str, str] | None = None) -> list[str]:
    print(f"\n{title} (comma-separated numbers or names; 'all' selects everything)\n")
    for index, label in enumerate(labels, 1):
        suffix = f"  {details[label]}" if details and label in details else ""
        print(f"  [ ] {index:2d}. {label}{suffix}")
    try:
        raw = input("\nSelect: ").strip()
    except (EOFError, KeyboardInterrupt):
        raise SystemExit("\nCancelled.")
    if not raw:
        raise SystemExit("Nothing selected.")
    return parse_multi_choice(raw, labels)


def choose_targets() -> list[Target]:
    details = {target.key: target.notes for target in TARGETS}
    keys = checkbox_menu("1/3 Choose agent targets", [target.key for target in TARGETS], details)
    return [target for target in TARGETS if target.key in keys]


def choose_scope() -> str:
    print("\n2/3 Choose installation scope\n")
    print("  [x] 1. project  Install only in this project (recommended, default)")
    print("  [ ] 2. user     Install for all of your projects")
    raw = input("\nScope [1]: ").strip().lower()
    if raw in ("", "1", "project"):
        return "project"
    if raw in ("2", "user"):
        return "user"
    raise SystemExit(f"Unknown scope: {raw}")


def choose_skills(catalog: dict[str, list[Path]]) -> list[Path]:
    total = len(all_skills(catalog))
    print("\n3/3 Choose what to install\n")
    print("  [x] 1. bundles     Curated, task-oriented groups (recommended)")
    print("  [ ] 2. categories  One or more complete GTM categories")
    print("  [ ] 3. skills      Individual skills by exact name")
    print(f"  [ ] 4. all         Complete catalog ({total} skills)")
    mode = input("\nMode [1]: ").strip().lower() or "1"
    if mode in ("4", "all"):
        return all_skills(catalog)
    if mode in ("1", "bundles", "bundle"):
        details = {name: f"({len(BUNDLES[name])} skills)" for name in BUNDLES}
        names = checkbox_menu("Choose bundles", sorted(BUNDLES), details)
        return dedupe(resolve_skill_names([skill for name in names for skill in BUNDLES[name]], catalog))
    if mode in ("2", "categories", "category"):
        details = {name: f"({len(catalog[name])} skills)" for name in catalog}
        names = checkbox_menu("Choose categories", sorted(catalog), details)
        return [skill for name in names for skill in catalog[name]]
    if mode in ("3", "skills", "skill"):
        names = input("Exact skill names, comma-separated: ").strip().split(",")
        return resolve_skill_names([name.strip() for name in names if name.strip()], catalog)
    raise SystemExit(f"Unknown mode: {mode}")


def resolve_requested_targets(values: list[str] | None) -> list[Target]:
    if not values:
        return []
    if "all" in values:
        return list(TARGETS)
    selected: list[Target] = []
    for value in values:
        target = next((item for item in TARGETS if value in (item.key, *item.aliases)), None)
        if not target:
            raise SystemExit(f"Unknown target: {value}")
        if target not in selected:
            selected.append(target)
    return selected


def resolve_requested_skills(args: argparse.Namespace, catalog: dict[str, list[Path]]) -> list[Path]:
    requested = any((args.all, args.bundle, args.category, args.skill))
    if not requested:
        return []
    selected: list[Path] = []
    if args.all:
        selected.extend(all_skills(catalog))
    bundles = parse_csv(args.bundle)
    unknown_bundles = sorted(set(bundles) - set(BUNDLES))
    if unknown_bundles:
        raise SystemExit("Unknown bundle(s): " + ", ".join(unknown_bundles))
    selected.extend(resolve_skill_names([skill for name in bundles for skill in BUNDLES[name]], catalog))
    categories = parse_csv(args.category)
    unknown_categories = sorted(set(categories) - set(catalog))
    if unknown_categories:
        raise SystemExit("Unknown category(s): " + ", ".join(unknown_categories))
    selected.extend(skill for name in categories for skill in catalog[name])
    selected.extend(resolve_skill_names(parse_csv(args.skill), catalog))
    return dedupe(selected)


def destination_root(target: Target, project: Path, scope: str) -> Path:
    template = target.project_path if scope == "project" else target.user_path
    base = Path(template).expanduser()
    return base if base.is_absolute() else project / base


def print_plan(targets: list[Target], selected: list[Path], project: Path, scope: str, force: bool) -> None:
    print("\nInstallation plan")
    print(f"  Selection: {len(selected)} skills across {len({path.parent.name for path in selected})} categories")
    print(f"  Scope: {scope}")
    print(f"  Existing folders: {'replace (--force)' if force else 'skip (safe default)'}")
    for target in targets:
        destination = destination_root(target, project, scope)
        collisions = sum((destination / skill.name).exists() for skill in selected)
        print(f"  [ ] {target.label}: {destination} ({collisions} existing)")


def run(command: list[str], *, cwd: Path, dry_run: bool) -> int:
    print("$ " + " ".join(command))
    return 0 if dry_run else subprocess.run(command, cwd=cwd, check=False).returncode


def referenced_shared_files(source_skill: Path) -> set[str]:
    referenced: set[str] = set()
    for markdown in source_skill.rglob("*.md"):
        referenced.update(re.findall(r"(?<![A-Za-z0-9_./-])references/([A-Za-z0-9._-]+\.md)", markdown.read_text(encoding="utf-8", errors="replace")))
    return referenced


def copy_shared_references(destination: Path, sources: list[Path], dry_run: bool) -> int:
    copied = 0
    for source_skill in sources:
        for filename in sorted(referenced_shared_files(source_skill)):
            source = SHARED_REFERENCES / filename
            local_source = source_skill / "references" / filename
            if not source.exists() or local_source.exists():
                continue
            target = destination / source_skill.name / "references" / filename
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            copied += 1
    if copied:
        print(f"  materialize {copied} shared reference file(s)")
    return copied


def copy_skills(destination: Path, selected: list[Path], dry_run: bool, force: bool) -> tuple[int, int, int]:
    if dry_run and len(selected) > 20:
        print(f"  COPY {len(selected)} selected skill folders -> {destination}")
        copy_shared_references(destination, selected, dry_run=True)
        return len(selected), 0, 0
    installed = skipped = failed = 0
    installed_sources: list[Path] = []
    for source in selected:
        target_dir = destination / source.name
        if target_dir.exists() and not force:
            print(f"  SKIP {source.name}: already exists")
            skipped += 1
            continue
        if dry_run:
            print(f"  COPY {source.parent.name}/{source.name} -> {target_dir}")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.copytree(source, target_dir, ignore=shutil.ignore_patterns(".DS_Store", "*.pyc", "__pycache__"))
        installed += 1
        installed_sources.append(source)
    copy_shared_references(destination, installed_sources, dry_run)
    return installed, skipped, failed


def install_target(target: Target, selected: list[Path], project: Path, scope: str, dry_run: bool, force: bool) -> tuple[int, int, int]:
    destination = destination_root(target, project, scope)
    missing = [skill for skill in selected if force or not (destination / skill.name).exists()]
    skipped = len(selected) - len(missing)
    for skill in selected:
        if skill not in missing:
            print(f"  SKIP {skill.name}: already exists")
    if not missing:
        return 0, skipped, 0

    if target.gh_agent and shutil.which("gh"):
        installed: list[Path] = []
        failed = 0
        use_all = len(missing) == len(all_skills(discover_catalog())) and skipped == 0
        commands = [(None, ["gh", "skill", "install", str(ROOT), "--from-local", "--all", "--agent", target.gh_agent, "--scope", scope])] if use_all else [
            (skill, ["gh", "skill", "install", str(ROOT), f"{skill.parent.name}/{skill.name}", "--from-local", "--agent", target.gh_agent, "--scope", scope]) for skill in missing
        ]
        for skill, command in commands:
            if force:
                command.append("--force")
            code = run(command, cwd=project, dry_run=dry_run)
            if code == 0:
                installed.extend(missing if skill is None else [skill])
            else:
                failed += len(missing) if skill is None else 1
        copy_shared_references(destination, installed, dry_run)
        return len(installed), skipped, failed

    print("  GitHub CLI skill installer unavailable; using the built-in copy path.")
    installed, copy_skipped, failed = copy_skills(destination, missing, dry_run, force)
    return installed, skipped + copy_skipped, failed


def main() -> int:
    keys = sorted({"all", *(target.key for target in TARGETS), *(alias for target in TARGETS for alias in target.aliases)})
    parser = argparse.ArgumentParser(description="Interactively install exact GTM skill groups with a preview-first, non-invasive flow.")
    parser.add_argument("--target", action="append", choices=keys, help="Target agent; repeatable. Omit for the interactive wizard.")
    parser.add_argument("--scope", choices=("project", "user"), help="Install scope. Interactive default: project.")
    parser.add_argument("--project", default=os.getcwd(), help="Project directory for project-scoped installs (default: cwd).")
    parser.add_argument("--bundle", action="append", help="Curated bundle; repeatable or comma-separated.")
    parser.add_argument("--category", action="append", help="Category; repeatable or comma-separated.")
    parser.add_argument("--skill", action="append", help="Exact skill name; repeatable or comma-separated.")
    parser.add_argument("--all", action="store_true", help="Install every skill in the current catalog.")
    parser.add_argument("--force", action="store_true", help="Explicitly replace existing skill folders.")
    parser.add_argument("--yes", action="store_true", help="Apply a non-interactive plan without confirmation.")
    parser.add_argument("--dry-run", action="store_true", help="Print the exact plan without changing files.")
    parser.add_argument("--list-bundles", action="store_true", help="List curated bundle names and exact contents.")
    args = parser.parse_args()

    catalog = discover_catalog()
    if not catalog:
        raise SystemExit(f"No skills found under {SKILLS}")
    if args.list_bundles:
        for name in sorted(BUNDLES):
            print(f"{name} ({len(BUNDLES[name])}): {', '.join(BUNDLES[name])}")
        return 0

    interactive = not args.target and not any((args.all, args.bundle, args.category, args.skill))
    targets = choose_targets() if interactive else resolve_requested_targets(args.target) or [TARGETS[0]]
    scope = choose_scope() if interactive and args.scope is None else args.scope or "project"
    selected = choose_skills(catalog) if interactive else resolve_requested_skills(args, catalog) or all_skills(catalog)
    project = Path(args.project).expanduser().resolve()

    print_plan(targets, selected, project, scope, args.force)
    if not args.dry_run and not args.yes:
        answer = input("\nApply this plan? [y/N]: ").strip().lower()
        if answer not in ("y", "yes"):
            print("Cancelled. Nothing changed.")
            return 0
    if scope == "project" and not args.dry_run:
        project.mkdir(parents=True, exist_ok=True)

    installed = skipped = failed = 0
    for target in targets:
        print(f"\n==> {target.label}")
        result = install_target(target, selected, project, scope, args.dry_run, args.force)
        installed += result[0]
        skipped += result[1]
        failed += result[2]

    print(f"\nDone: selected={len(selected)}, targets={len(targets)}, installed={installed}, skipped={skipped}, failed={failed}, catalog={len(all_skills(catalog))}.")
    if args.dry_run:
        print("Dry run only; nothing changed.")
    elif any(target.key == "claude" for target in targets):
        print("Claude Code discovers project skills in .claude/skills and user skills in ~/.claude/skills.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
