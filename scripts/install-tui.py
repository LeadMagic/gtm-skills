#!/usr/bin/env python3
"""Install LeadMagic GTM Skills into supported agent runtimes.

The preferred portable path is GitHub CLI's ``gh skill install`` command. The
installer uses the checked-out repository as its source, so a local audit and
the installed content refer to the same files. Claude Code uses the repository's
native plugin marketplace. A dependency-free copy fallback installs each skill
at the discovery root instead of nesting the repository above the SKILL.md files.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

REPO = "LeadMagic/gtm-skills"
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SHARED_REFERENCES = ROOT / "references"


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
    Target(
        "claude", "Claude Code", None, ".claude/skills", "~/.claude/skills",
        "Uses the native Claude plugin marketplace; local-copy fallback is available.",
        ("claude-code",),
    ),
    Target(
        "copilot", "GitHub Copilot", "github-copilot", ".github/skills", "~/.copilot/skills",
        "Uses GitHub's Agent Skills installer.", ("github-copilot", "vscode"),
    ),
    Target("codex", "Codex", "codex", ".agents/skills", "~/.codex/skills", "Uses GitHub's Agent Skills installer."),
    Target("cursor", "Cursor", "cursor", ".agents/skills", "~/.agents/skills", "Uses the shared Agent Skills directory."),
    Target("gemini", "Gemini CLI", "gemini-cli", ".agents/skills", "~/.agents/skills", "Uses the shared Agent Skills directory.", ("gemini-cli",)),
    Target("opencode", "OpenCode", "opencode", ".agents/skills", "~/.agents/skills", "Uses the shared Agent Skills directory."),
    Target("windsurf", "Windsurf", "windsurf", ".agents/skills", "~/.agents/skills", "Uses the shared Agent Skills directory."),
    Target("goose", "Goose", "goose", ".agents/skills", "~/.agents/skills", "Uses GitHub's Agent Skills installer."),
    Target("hermes", "Hermes", "universal", ".agents/skills", "~/.agents/skills", "Uses the universal Agent Skills directory."),
    Target("jesse", "Jesse", None, ".jesse/skills", "~/.jesse/skills", "Uses Jesse's local skills directory."),
)


def run(command: list[str], *, cwd: Path, dry_run: bool) -> int:
    print("$ " + " ".join(command))
    if dry_run:
        return 0
    return subprocess.run(command, cwd=cwd, check=False).returncode


def discover_skills() -> list[Path]:
    return sorted(path.parent for path in SKILLS.glob("*/*/SKILL.md"))


def destination_root(target: Target, project: Path, scope: str) -> Path:
    template = target.project_path if scope == "project" else target.user_path
    base = Path(template).expanduser()
    return base if base.is_absolute() else project / base


def copy_referenced_shared_files(
    destination: Path,
    dry_run: bool,
    skill_sources: list[Path] | None = None,
) -> int:
    """Materialize repo-level references so every installed skill is self-contained."""
    copied = 0
    for source_skill in skill_sources if skill_sources is not None else discover_skills():
        referenced: set[str] = set()
        for markdown in source_skill.rglob("*.md"):
            referenced.update(
                re.findall(
                    r"(?<![A-Za-z0-9_./-])references/([A-Za-z0-9._-]+\.md)",
                    markdown.read_text(encoding="utf-8", errors="replace"),
                )
            )
        for filename in sorted(referenced):
            source = SHARED_REFERENCES / filename
            if not source.exists() or (source_skill / "references" / filename).exists():
                continue
            target = destination / source_skill.name / "references" / filename
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            copied += 1
    if copied:
        print(f"copy {copied} referenced shared files into installed skill folders")
    return copied


def copy_skills(target: Target, project: Path, scope: str, dry_run: bool, force: bool) -> int:
    destination = destination_root(target, project, scope)
    skills = discover_skills()
    print(f"copy {len(skills)} individual skill folders -> {destination}")
    if dry_run:
        return len(skills)

    destination.mkdir(parents=True, exist_ok=True)
    installed = 0
    installed_sources: list[Path] = []
    for source in skills:
        target_dir = destination / source.name
        if target_dir.exists():
            if not force:
                print(f"SKIP: {target_dir} already exists (pass --force to replace it)")
                continue
            shutil.rmtree(target_dir)
        shutil.copytree(
            source,
            target_dir,
            ignore=shutil.ignore_patterns(".DS_Store", "*.pyc", "__pycache__"),
        )
        installed += 1
        installed_sources.append(source)
    copy_referenced_shared_files(destination, dry_run=False, skill_sources=installed_sources)
    return installed


def install_claude(target: Target, project: Path, scope: str, dry_run: bool, force: bool) -> bool:
    if shutil.which("claude"):
        run(
            ["claude", "plugin", "marketplace", "add", REPO, "--scope", scope],
            cwd=project,
            dry_run=dry_run,
        )
        install_code = run(
            ["claude", "plugin", "install", "gtm-skills@gtm-skills", "--scope", scope, "--yes"],
            cwd=project,
            dry_run=dry_run,
        )
        if install_code == 0:
            print("OK: Claude Code plugin installed")
            return True
        print("Claude plugin install failed; using the local skill-copy fallback.")
    else:
        print("Claude CLI not found; using the local skill-copy fallback.")

    installed = copy_skills(target, project, scope, dry_run, force)
    print(f"OK: {installed} Claude skill folders copied")
    return installed == len(discover_skills())


def install_agent(target: Target, project: Path, scope: str, dry_run: bool, force: bool) -> bool:
    if target.gh_agent and shutil.which("gh"):
        command = [
            "gh", "skill", "install", str(ROOT), "--from-local", "--all",
            "--agent", target.gh_agent, "--scope", scope,
        ]
        if force:
            command.append("--force")
        if run(command, cwd=project, dry_run=dry_run) == 0:
            copy_referenced_shared_files(destination_root(target, project, scope), dry_run)
            print(f"OK: {target.label} skills installed with GitHub CLI")
            return True
        print("GitHub CLI skill install failed; using the local-copy fallback.")

    installed = copy_skills(target, project, scope, dry_run, force)
    print(f"OK: {installed} {target.label} skill folders copied")
    return installed == len(discover_skills())


def choose_targets() -> list[Target]:
    print("\nLeadMagic GTM Skills Installer")
    print("Select targets by number or key, comma-separated; press Enter for Claude + Codex.\n")
    for index, target in enumerate(TARGETS, 1):
        print(f"{index:2d}. {target.label:18} {target.notes}")
    raw = input("\nInstall targets: ").strip().lower()
    if not raw:
        return [target for target in TARGETS if target.key in {"claude", "codex"}]
    if raw == "all":
        return list(TARGETS)

    selected: list[Target] = []
    for value in (part.strip() for part in raw.split(",")):
        if value.isdigit() and 1 <= int(value) <= len(TARGETS):
            target = TARGETS[int(value) - 1]
        else:
            target = next((item for item in TARGETS if value in (item.key, *item.aliases)), None)
        if target is None:
            raise SystemExit(f"Unknown target: {value}")
        if target not in selected:
            selected.append(target)
    return selected


def resolve_requested_targets(values: list[str] | None) -> list[Target]:
    if not values:
        return choose_targets()
    if "all" in values:
        return list(TARGETS)
    selected: list[Target] = []
    for value in values:
        target = next((item for item in TARGETS if value in (item.key, *item.aliases)), None)
        if target and target not in selected:
            selected.append(target)
    return selected


def main() -> int:
    keys = sorted({"all", *(target.key for target in TARGETS), *(alias for target in TARGETS for alias in target.aliases)})
    parser = argparse.ArgumentParser(description="Install LeadMagic GTM Skills into supported AI agents.")
    parser.add_argument("--target", action="append", choices=keys, help="Target agent. Repeatable; omit for the interactive picker.")
    parser.add_argument("--scope", choices=("project", "user"), default="project", help="Install scope (default: project).")
    parser.add_argument("--project", default=os.getcwd(), help="Project directory for project-scoped installs (default: cwd).")
    parser.add_argument("--force", action="store_true", help="Replace existing skill folders.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands and destinations without changing files.")
    args = parser.parse_args()

    if not SKILLS.exists():
        raise SystemExit(f"Cannot find skills directory at {SKILLS}")

    project = Path(args.project).expanduser().resolve()
    if args.scope == "project" and not args.dry_run:
        project.mkdir(parents=True, exist_ok=True)

    selected = resolve_requested_targets(args.target)
    failures = 0
    for target in selected:
        print(f"\n==> {target.label} ({args.scope} scope)")
        print(target.notes)
        ok = (
            install_claude(target, project, args.scope, args.dry_run, args.force)
            if target.key == "claude"
            else install_agent(target, project, args.scope, args.dry_run, args.force)
        )
        failures += int(not ok)

    total = len(discover_skills())
    print(f"\nDone. Catalog source contained exactly {total} skills.")
    print("Verify with `gh skill list` when installed through GitHub CLI, then ask the agent to load `using-gtm-skills`.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
