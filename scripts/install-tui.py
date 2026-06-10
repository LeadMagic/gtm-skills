#!/usr/bin/env python3
"""Interactive installer for LeadMagic GTM Skills.

No dependencies. Supports every system in the repo compatibility string.
Run:
  python3 scripts/install-tui.py
  python3 scripts/install-tui.py --target hermes --dry-run
  python3 scripts/install-tui.py --target jesse --project /path/to/project
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = "LeadMagic/gtm-skills"
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
AGENTS = ROOT / "AGENTS.md"
CLAUDE = ROOT / "CLAUDE.md"


@dataclass
class Target:
    key: str
    label: str
    kind: str  # cli, copy, instructions
    command: list[str] | None = None
    path_template: str | None = None
    notes: str = ""


TARGETS: list[Target] = [
    Target("claude", "Claude Code", "cli", ["claude", "plugins", "add", REPO], notes="Preferred path: Claude plugin install."),
    Target("jesse", "Jesse", "copy", path_template="{project}/.jesse/skills/gtm-skills", notes="Project-local skills directory."),
    Target("codex", "Codex", "cli", ["codex", "skills", "install", REPO], path_template="{home}/.codex/skills/gtm-skills", notes="Uses Codex CLI when available; falls back to local copy."),
    Target("hermes", "Hermes", "cli", ["hermes", "skills", "install", REPO], path_template="{home}/.hermes/skills/gtm-skills", notes="Uses Hermes CLI when available; falls back to local copy."),
    Target("windsurf", "Windsurf", "copy", path_template="{project}/.windsurf/skills/gtm-skills", notes="Project-local Windsurf skill directory."),
    Target("opencode", "OpenCode", "copy", path_template="{project}/.opencode/skills/gtm-skills", notes="Project-local OpenCode skill directory."),
    Target("gemini", "Gemini CLI", "copy", path_template="{project}/.gemini/skills/gtm-skills", notes="Project-local Gemini skills directory."),
    Target("copilot", "GitHub Copilot", "instructions", path_template="{project}/.github/copilot-instructions.md", notes="Writes an instructions file that points Copilot at AGENTS.md and the copied skills."),
    Target("zed", "Zed", "instructions", path_template="{project}/AGENTS.md", notes="Zed reads AGENTS.md from the project root."),
    Target("vscode", "VS Code", "instructions", path_template="{project}/.github/copilot-instructions.md", notes="Same install path as Copilot agent mode."),
    Target("goose", "Goose", "copy", path_template="{home}/.config/goose/skills/gtm-skills", notes="Local Goose skills directory."),
]


def run(cmd: list[str], dry: bool) -> int:
    print("$ " + " ".join(cmd))
    if dry:
        return 0
    return subprocess.call(cmd)


def copy_tree(src: Path, dst: Path, dry: bool) -> None:
    print(f"copy {src} -> {dst}")
    if dry:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    ignore = shutil.ignore_patterns(".git", "node_modules", "*.pyc", "__pycache__")
    shutil.copytree(src, dst, ignore=ignore)


def write_file(path: Path, content: str, dry: bool) -> None:
    print(f"write {path}")
    if dry:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def expand(template: str, project: Path) -> Path:
    return Path(template.format(home=str(Path.home()), project=str(project))).expanduser()


def install(target: Target, project: Path, dry: bool) -> None:
    print(f"\n==> {target.label}")
    print(target.notes)

    if target.kind == "cli" and target.command:
        if dry:
            run(target.command, dry)
            print(f"OK (dry-run): {target.label} installs via `{target.command[0]}` when the CLI is available.")
            if target.path_template:
                print("Fallback if the CLI is unavailable:")
                copy_tree(ROOT, expand(target.path_template, project), dry)
            return
        if shutil.which(target.command[0]):
            code = run(target.command, dry)
            if code == 0:
                print(f"OK: {target.label} installed via CLI")
                return
            print(f"CLI install failed with exit code {code}; trying fallback copy if available.")
        else:
            print(f"{target.command[0]} not found; trying fallback copy if available.")

    if target.kind in {"copy", "cli"} and target.path_template:
        copy_tree(ROOT, expand(target.path_template, project), dry)
        print("OK: copied repository with all skills and artifacts")
        return

    if target.kind == "instructions":
        if target.path_template is None:
            raise RuntimeError(f"No instruction path configured for {target.key}")
        if target.key in {"copilot", "vscode"}:
            skills_dst = project / ".github" / "skills" / "gtm-skills"
            copy_tree(ROOT, skills_dst, dry)
            content = """# GTM Skills for Copilot / VS Code Agent Mode

Use the skills in `.github/skills/gtm-skills/skills/` when the user asks for GTM,
sales, marketing, customer success, RevOps, prospecting, outbound, PLG, analytics,
or founder-led SaaS work.

Start with `.github/skills/gtm-skills/AGENTS.md` for the full skill index.
Load individual `SKILL.md` files only when they match the task.
"""
            write_file(expand(target.path_template, project), content, dry)
            print("OK: copied skills and wrote Copilot instructions")
            return
        if target.key == "zed":
            source = AGENTS.read_text() if AGENTS.exists() else "# GTM Skills\n"
            content = source + "\n\nInstalled by scripts/install-tui.py from LeadMagic/gtm-skills.\n"
            write_file(expand(target.path_template, project), content, dry)
            copy_tree(ROOT, project / ".zed" / "skills" / "gtm-skills", dry)
            print("OK: wrote AGENTS.md and copied skills under .zed/skills")
            return

    raise RuntimeError(f"No install strategy for {target.key}")


def choose_targets() -> list[Target]:
    print("\nLeadMagic GTM Skills Installer")
    print("Select targets. Use comma-separated numbers, 'all', or Enter for Hermes + Claude + Jesse.\n")
    for i, t in enumerate(TARGETS, 1):
        print(f"{i:2d}. {t.label:18} {t.notes}")
    raw = input("\nInstall targets: ").strip().lower()
    if not raw:
        wanted = {"hermes", "claude", "jesse"}
        return [t for t in TARGETS if t.key in wanted]
    if raw == "all":
        return TARGETS
    selected = []
    for part in raw.split(','):
        part = part.strip()
        if not part:
            continue
        if part.isdigit():
            selected.append(TARGETS[int(part) - 1])
        else:
            match = next((t for t in TARGETS if t.key == part), None)
            if not match:
                raise SystemExit(f"Unknown target: {part}")
            selected.append(match)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Install LeadMagic GTM Skills into supported AI agent systems.")
    parser.add_argument("--target", action="append", choices=[t.key for t in TARGETS] + ["all"], help="Target system. Repeatable. Omit for interactive TUI.")
    parser.add_argument("--project", default=os.getcwd(), help="Project directory for project-local installs. Default: cwd.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files or running install commands.")
    args = parser.parse_args()

    if not SKILLS.exists():
        raise SystemExit(f"Cannot find skills directory at {SKILLS}")

    project = Path(args.project).expanduser().resolve()
    if args.target:
        keys = {k for item in args.target for k in ([t.key for t in TARGETS] if item == "all" else [item])}
        selected = [t for t in TARGETS if t.key in keys]
    else:
        selected = choose_targets()

    for target in selected:
        install(target, project, args.dry_run)

    print("\nDone. Verification prompt: ask your agent to list available GTM skills, then load `foundation/using-gtm-skills`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
