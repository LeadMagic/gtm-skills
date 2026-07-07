#!/usr/bin/env python3
"""cc-gtm — Smart Claude installer for LeadMagic GTM Skills.

Pick exactly which skills to install — not all 205.
Zero dependencies. Installs only what you choose.

Supports:
  - Claude Code CLI (.claude/skills/)
  - Claude Desktop (Claude Projects instructions)
  - Chunked loading (categories, skills, or curated bundles)

Usage:
  python3 scripts/cc-gtm.py                          # interactive menu
  python3 scripts/cc-gtm.py --category outbound      # install one category
  python3 scripts/cc-gtm.py --category outbound,sales-revops
  python3 scripts/cc-gtm.py --skills cold-email-strategy,domain-infrastructure
  python3 scripts/cc-gtm.py --list                    # list all skills
  python3 scripts/cc-gtm.py --list --category outbound
  python3 scripts/cc-gtm.py --dry-run --category tools
  python3 scripts/cc-gtm.py --project /path/to/project --category foundation
  python3 scripts/cc-gtm.py --desktop --category outbound  # Claude Desktop
  python3 scripts/cc-gtm.py --bundle outbound-stack   # curated bundle
  python3 scripts/cc-gtm.py --all                     # install everything
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REFERENCES_DIR = ROOT / "references"
DEFAULT_REL = ".claude/skills/gtm-skills"

LM_URL = "https://leadmagic.io/?utm_source=github&utm_medium=organic&utm_campaign=gtm-skills"
GH_URL = "https://github.com/LeadMagic/gtm-skills"

_NO_COLOR = os.environ.get("NO_COLOR") or not sys.stderr.isatty()

if _NO_COLOR:
    def c(code, text):
        return text
else:
    def c(code, text):
        return f"\033[{code}m{text}\033[0m"

def bold(t): return c("1", t)
def dim(t):  return c("2", t)
def red(t):  return c("31", t)
def green(t): return c("32", t)
def yellow(t): return c("33", t)
def blue(t):  return c("34", t)
def magenta(t): return c("35", t)
def cyan(t):  return c("36", t)
def gray(t):  return c("90", t)

def banner():
    top = "=" * 62
    bot = "=" * 62
    print(f"\n+{top}+")
    print(f"|{bold(cyan('  LeadMagic GTM Skills')):<62}|")
    print(f"|{dim('  Smart Claude Installer'):<62}|")
    print(f"+{bot}+\n")

def sep(char="-", w=62):
    return char * w

BUNDLES = {
    "outbound-stack": ["cold-email-strategy", "cold-email-copywriting", "domain-infrastructure",
                       "email-deliverability", "inbox-setup", "sending-platforms", "reply-handling"],
    "outbound-phone": ["cold-calling"],
    "prospecting-stack": ["lead-finding", "lead-enrichment", "email-finding", "contact-verification",
                          "list-building", "signal-scoring"],
    "sales-revops-stack": ["pipeline-management", "meeting-prep", "deal-desk", "sales-enablement",
                           "demo-scripts", "objection-handling", "buyer-indecision", "transparency-selling"],
    "founder-gtm": ["founder-sales", "solo-founder-gtm", "pricing-strategy", "positioning-messaging",
                    "pitch-deck-builder", "fundraising-strategy", "financial-modeling"],
    "inbound-stack": ["content-marketing", "inbound-triage", "landing-pages", "seo-strategy",
                      "social-selling", "linkedin-algorithm"],
    "cs-stack": ["customer-onboarding", "cs-playbooks", "sla-management", "headless-support", "qbr-planning"],
    "analytics-stack": ["gtm-metrics", "attribution", "campaign-analytics", "tracking-plan", "a-b-testing"],
    "automation-stack": ["clay-automation", "n8n-automation", "crm-integration", "api-enrichment",
                         "waterfall-enrichment", "mcp-setup"],
    "abm-stack": ["abm-strategy", "account-selection", "multi-thread-orchestration", "strategic-gifting"],
    "tools-stack": ["clay-toolkit", "sequencing-toolkit", "n8n-toolkit", "ai-prompts-toolkit", "crm-toolkit"],
    "startup-essentials": ["gtm-context", "icp-scoring", "positioning-messaging", "pricing-strategy",
                           "founder-sales", "pitch-deck-builder", "financial-modeling", "saas-metrics-calculator"],
}

def discover_skills():
    result = {}
    if not SKILLS_DIR.exists():
        return result
    for cat_dir in sorted(SKILLS_DIR.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith("."):
            continue
        skills = sorted(d.name for d in cat_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists())
        if skills:
            result[cat_dir.name] = skills
    return result

def get_skill_description(skill_path):
    try:
        text = skill_path.read_text("utf-8")
        if not text.startswith("---"):
            return ""
        end = text.find("\n---\n", 4)
        if end == -1:
            return ""
        fm = text[4:end]
        for line in fm.split("\n"):
            if line.startswith("description:"):
                val = line.split(":", 1)[1].strip()
                if val in (">-", ">", "|", "|-"):
                    lines = []
                    idx = fm.split("\n").index(line)
                    for cl in fm.split("\n")[idx + 1:]:
                        if cl.startswith("  ") or cl.strip() == "":
                            lines.append(cl.strip())
                        else:
                            break
                    return " ".join(lines).strip()
                return val.strip("'\"")
        return ""
    except Exception:
        return ""

def parse_list(arg):
    return [s.strip() for s in arg.split(",") if s.strip()]

def resolve_skill_paths(cats, skill_names, catalog):
    paths = []
    seen = set()
    for cat in cats:
        actual = next((k for k in catalog if k.lower() == cat.lower()), None)
        if not actual:
            print(f"  {yellow('!')}  Category {red(cat)} not found. Use {cyan('--list')}.")
            continue
        for skill in catalog[actual]:
            p = SKILLS_DIR / actual / skill
            if p not in seen:
                paths.append(p)
                seen.add(p)
    for name in skill_names:
        found = False
        for cat, skills in catalog.items():
            for skill in skills:
                if skill.lower() == name.lower():
                    p = SKILLS_DIR / cat / skill
                    if p not in seen:
                        paths.append(p)
                        seen.add(p)
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"  {yellow('!')}  Skill {red(name)} not found.")
    return paths

def resolve_bundle(name, catalog):
    bundle = BUNDLES.get(name.lower())
    if not bundle:
        print(f"  {yellow('!')}  Bundle {red(name)} not found. Available: {cyan(', '.join(BUNDLES.keys()))}")
        return []
    return resolve_skill_paths([], bundle, catalog)

def verify_skill(skill_dir):
    required = ["SKILL.md", "references/framework-notes.md", "templates/output-template.md", "scripts/check-output.py"]
    return all((skill_dir / f).exists() for f in required)

def copy_skill(src, dst, dry):
    if not verify_skill(src):
        print(f"  {red('X')} {src.name}: missing artifacts, skipping")
        return False
    if dry:
        print(f"  {gray('[dry]')} {blue('copy')} {src.relative_to(ROOT)} -> {dst}")
        return True
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".git"))
    return True

def copy_shared_references(dst_root, dry):
    if not REFERENCES_DIR.exists():
        return 0
    dst_refs = dst_root / "references"
    count = 0
    for ref_file in sorted(REFERENCES_DIR.iterdir()):
        if not ref_file.is_file() or not ref_file.name.endswith(".md"):
            continue
        target = dst_refs / ref_file.name
        if dry:
            print(f"  {gray('[dry]')} {blue('copy')} references/{ref_file.name}")
        else:
            dst_refs.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ref_file, target)
        count += 1
    return count

def generate_claude_md(installed, catalog, dst_root, dry):
    lines = [
        "# GTM Skills",
        "",
        f"{len(installed)} go-to-market skills installed from LeadMagic/gtm-skills.",
        "Skills are self-contained folders with instructions, scripts, references, and templates.",
        "",
        "## Operating Model",
        "",
        "- Discovery loads skill name + description from frontmatter.",
        "- Activation loads SKILL.md when a task matches.",
        "- Execution loads references/, templates/, scripts/ on demand.",
        "- Use the narrowest skill that matches the task; chain skills for full GTM workflows.",
        "",
        "## Installed Skills",
        "",
    ]
    by_cat = {}
    for p in installed:
        by_cat.setdefault(p.parent.name, []).append(p)
    for cat in sorted(by_cat):
        lines.append(f"### {cat} ({len(by_cat[cat])})")
        for sd in sorted(by_cat[cat], key=lambda x: x.name):
            desc = get_skill_description(sd / "SKILL.md")
            if len(desc) > 120:
                desc = desc[:117] + "..."
            lines.append(f"- **{sd.name}** -- {desc}")
        lines.append("")
    lines += [
        "## Full Catalog",
        "",
        f"To browse all 205 skills: {GH_URL}",
        f"LeadMagic enrichment platform: {LM_URL}",
        "",
    ]
    content = "\n".join(lines) + "\n"
    target = dst_root / "CLAUDE.md"
    if dry:
        print(f"  {gray('[dry]')} {blue('write')} {target} ({len(installed)} skills)")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, "utf-8")

def generate_desktop_instructions(installed, catalog, dst_root, dry):
    lines = [
        "# GTM Skills -- Claude Desktop Instructions",
        "",
        f"You have access to {len(installed)} go-to-market skills from LeadMagic.",
        "Each skill has a SKILL.md with instructions. When asked to help with a task,",
        "check if any skill matches and use its framework.",
        "",
        "## Skills Available",
        "",
    ]
    by_cat = {}
    for p in installed:
        by_cat.setdefault(p.parent.name, []).append(p)
    for cat in sorted(by_cat):
        lines.append(f"### {cat}")
        for sd in sorted(by_cat[cat], key=lambda x: x.name):
            desc = get_skill_description(sd / "SKILL.md")
            if len(desc) > 100:
                desc = desc[:97] + "..."
            lines.append(f"- **{sd.name}**: {desc}")
        lines.append("")
    lines += [
        "## How to Use",
        "",
        "When asked for help with a task, check the skill descriptions above.",
        "If a skill matches, read its SKILL.md file and follow its framework.",
        "Skills produce artifacts (templates, scorecards, playbooks) -- not just advice.",
        "",
        f"Full catalog: {GH_URL}",
        f"LeadMagic: {LM_URL}",
    ]
    content = "\n".join(lines) + "\n"
    target = dst_root / "claude-desktop-instructions.md"
    if dry:
        print(f"  {gray('[dry]')} {blue('write')} {target}")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, "utf-8")

def interactive_select(catalog):
    banner()
    total = sum(len(v) for v in catalog.values())
    print(f"  {bold(str(total))} skills across {bold(str(len(catalog)))} categories.\n")
    print(f"  {bold('Categories:')}\n")
    cats = sorted(catalog.keys())
    for i, cat in enumerate(cats, 1):
        print(f"    {gray(f'{i:2d}.')} {bold(f'{cat:<25s}')} {gray(f'({len(catalog[cat])})')}")
    print()
    print(f"  {bold('Options:')}")
    print(f"    {gray('*')} Category numbers (comma-separated): {cyan('1,5,12')}")
    print(f"    {gray('*')} {green('all')} -- install everything ({total} skills)")
    print(f"    {gray('*')} Skill name to search: {cyan('cold-email-strategy')}")
    print(f"    {gray('*')} Bundle: {cyan('--bundle outbound-stack')} (see --list-bundles)")
    print(f"    {gray('*')} {red('q')} to quit\n")
    try:
        choice = input(f"  {bold('Your choice:')} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print(f"\n  {gray('Cancelled.')}")
        sys.exit(0)
    if choice in ("q", "quit", "exit"):
        print(f"  {gray('Cancelled.')}")
        sys.exit(0)
    if choice == "all":
        print(f"\n  {green('v')} Selected {bold('all')} {total} skills\n")
        return resolve_skill_paths(cats, [], catalog)
    if "," in choice or choice.isdigit():
        try:
            nums = [int(n.strip()) for n in choice.split(",")]
            selected_cats = []
            for n in nums:
                if 1 <= n <= len(cats):
                    selected_cats.append(cats[n - 1])
                else:
                    print(f"  {yellow('!')}  Invalid: {red(str(n))}")
            if selected_cats:
                count = sum(len(catalog[c]) for c in selected_cats)
                print(f"\n  {green('v')} {bold(', '.join(selected_cats))} ({count} skills)\n")
                return resolve_skill_paths(selected_cats, [], catalog)
        except ValueError:
            pass
    matches = []
    for cat, skills in catalog.items():
        for skill in skills:
            if choice in skill.lower():
                matches.append(SKILLS_DIR / cat / skill)
    if matches:
        print(f"\n  {green('v')} Found {bold(str(len(matches)))} matching {cyan(choice)}:")
        for m in matches:
            print(f"    {gray('*')} {m.parent.name}/{magenta(m.name)}")
        try:
            confirm = input(f"\n  {bold('Install all?')} [{green('y')}/{red('N')}]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return []
        if confirm in ("y", "yes"):
            return matches
        return []
    print(f"  {yellow('!')}  No match for {red(choice)}.")
    return []

def cmd_list(catalog, args):
    total = sum(len(v) for v in catalog.values())
    if args.list_bundles:
        print(f"\n  {bold('Curated Bundles:')}\n")
        for name, skills in sorted(BUNDLES.items()):
            print(f"  {cyan(name):<25s} {gray(f'({len(skills)} skills)')}")
            for s in skills:
                print(f"    {gray('*')} {s}")
            print()
        return 0
    if args.category:
        cats = parse_list(args.category)
        for cat in cats:
            actual = next((k for k in catalog if k.lower() == cat.lower()), None)
            if actual:
                print(f"\n{bold(actual)} {gray(f'({len(catalog[actual])})')}:")
                for s in catalog[actual]:
                    desc = get_skill_description(SKILLS_DIR / actual / s / "SKILL.md")
                    if len(desc) > 80:
                        desc = desc[:77] + "..."
                    print(f"  {cyan(s):<30s} {gray(desc)}")
            else:
                print(f"\n  {yellow('!')}  Category {red(cat)} not found")
        return 0
    print(f"\n  {bold(str(total))} skills across {bold(str(len(catalog)))} categories:\n")
    for cat in sorted(catalog.keys()):
        print(f"  {bold(cat)} {gray(f'({len(catalog[cat])})')}")
        for s in catalog[cat]:
            print(f"    {cyan(s)}")
    print()
    print(f"  {gray('Bundles:')} {cyan('--list-bundles')} to see curated stacks")
    print(f"  {gray('Install:')} {cyan('--category outbound')} or {cyan('--skills cold-email-strategy')} or {cyan('--bundle outbound-stack')}")
    print()
    return 0

def main():
    parser = argparse.ArgumentParser(prog="cc-gtm", description="Smart Claude installer for LeadMagic GTM Skills.")
    parser.add_argument("--list", action="store_true", help="List all available skills")
    parser.add_argument("--list-bundles", action="store_true", help="List curated skill bundles")
    parser.add_argument("--category", type=str, help="Install category (comma-separated)")
    parser.add_argument("--skills", type=str, help="Install specific skills (comma-separated)")
    parser.add_argument("--bundle", type=str, help="Install a curated bundle")
    parser.add_argument("--all", action="store_true", help="Install all 205 skills")
    parser.add_argument("--project", type=str, help="Target project directory (default: cwd)")
    parser.add_argument("--desktop", action="store_true", help="Generate Claude Desktop instructions")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without copying")
    parser.add_argument("--no-shared-refs", action="store_true", help="Skip shared references/")
    args = parser.parse_args()

    catalog = discover_skills()
    if not catalog:
        print(f"{red('X')} No skills found. Run from the gtm-skills repo root.")
        return 1

    if args.list or args.list_bundles:
        return cmd_list(catalog, args)

    if args.all:
        selected = resolve_skill_paths(sorted(catalog.keys()), [], catalog)
    elif args.bundle:
        selected = resolve_bundle(args.bundle, catalog)
    elif args.category:
        selected = resolve_skill_paths(parse_list(args.category), [], catalog)
    elif args.skills:
        selected = resolve_skill_paths([], parse_list(args.skills), catalog)
    else:
        selected = interactive_select(catalog)

    if not selected:
        print(f"\n  {gray('Nothing selected. Use')} {cyan('--list')} {gray('to browse,')} {cyan('--bundle')} {gray('for stacks,')}")
        print(f"  {cyan('--category')} {gray('for categories,')} {cyan('--skills')} {gray('for specific skills.')}")
        return 0

    project = Path(args.project) if args.project else Path.cwd()
    install_root = project / DEFAULT_REL

    print(sep("="))
    target_label = "Claude Desktop" if args.desktop else "Claude Code"
    print(f"  {bold('Installing')} {green(str(len(selected)))} {bold('skill(s)')} -> {cyan(target_label)}")
    print(f"  {gray('->')} {install_root}")
    print(sep("="))
    print()

    installed_count = 0
    for skill_dir in selected:
        dst = install_root / skill_dir.parent.name / skill_dir.name
        if copy_skill(skill_dir, dst, args.dry_run):
            installed_count += 1
            if not args.dry_run:
                print(f"  {green('v')} {skill_dir.parent.name}/{bold(skill_dir.name)}")

    if not args.no_shared_refs:
        ref_count = copy_shared_references(install_root, args.dry_run)
        if ref_count:
            if args.dry_run:
                print(f"\n  {gray('Would copy')} {bold(str(ref_count))} {gray('shared refs')}")
            else:
                print(f"\n  {blue('books')} {bold(str(ref_count))} shared reference files -> {install_root / 'references'}")

    if selected:
        generate_claude_md(selected, catalog, install_root, args.dry_run)
        if not args.dry_run:
            print(f"  {blue('doc')} {bold('CLAUDE.md')} generated ({len(selected)} skills indexed)")

    if args.desktop:
        generate_desktop_instructions(selected, catalog, install_root, args.dry_run)
        if not args.dry_run:
            print(f"  {blue('desktop')} {bold('claude-desktop-instructions.md')} generated")
            print(f"     {gray('Paste into Claude.ai -> Settings -> Project Instructions')}")

    print()
    print(sep("-"))
    if installed_count == len(selected):
        print(f"  {green('OK')} {bold(f'{installed_count}/{len(selected)}')} skills installed")
    else:
        print(f"  {yellow('!')}  {bold(f'{installed_count}/{len(selected)}')} skills installed (some skipped)")
    if args.dry_run:
        print(f"  {gray('[DRY RUN -- nothing copied]')}")
    else:
        print(f"  {gray('Location:')} {install_root}")
        print()
        if args.desktop:
            print(f"  {bold('Claude Desktop:')}")
            print(f"    {gray('1.')} Open {bold('claude.ai')} -> New Project")
            print(f"    {gray('2.')} Upload skill folders to the project")
            print(f"    {gray('3.')} Paste {cyan('claude-desktop-instructions.md')} into Project Instructions")
            print(f"    {gray('4.')} Ask: {green('\"what GTM skills are available?\"')}")
        else:
            print(f"  {bold('Claude Code:')}")
            print(f"    {gray('1.')} Open project in {bold('Claude Code')}")
            print(f"    {gray('2.')} Claude discovers skills in {cyan(DEFAULT_REL)}/")
            print(f"    {gray('3.')} Ask: {green('\"what GTM skills are available?\"')}")
        print()
        print(f"  {gray('Full catalog:')} {GH_URL}")
        print(f"  {gray('LeadMagic:')} {LM_URL}")
    print(sep("-"))
    print()

    return 0 if installed_count == len(selected) else 1

if __name__ == "__main__":
    sys.exit(main())
