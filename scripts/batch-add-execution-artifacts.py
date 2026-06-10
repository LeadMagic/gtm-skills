#!/usr/bin/env python3
"""Batch-add Execution Artifacts sections and supporting files to skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

ARTIFACT_REQUIRED_CATEGORIES = {
    "analytics",
    "automation",
    "design",
    "leadmagic",
    "sequencing-tools",
    "tools",
}


def parse_frontmatter(content: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    fm = m.group(1)
    data: dict = {}
    meta: dict = {}
    in_meta = False
    for line in fm.splitlines():
        if line.startswith("metadata:"):
            in_meta = True
            continue
        if in_meta:
            if re.match(r"^\S", line):
                in_meta = False
            else:
                mm = re.match(r"^\s+(\w+):\s*(.*)$", line)
                if mm:
                    key, val = mm.group(1), mm.group(2).strip()
                    if val.startswith("[") and val.endswith("]"):
                        items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
                        meta[key] = items
                    else:
                        meta[key] = val.strip('"').strip("'")
                continue
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            key, val = mm.group(1), mm.group(2).strip()
            if val.startswith(">"):
                continue
            data[key] = val.strip('"').strip("'")
    if meta:
        data["metadata"] = meta
    return data


def extract_section(content: str, heading: str) -> str:
    pattern = rf"^{re.escape(heading)}\n\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_tables(content: str, max_tables: int = 2) -> list[str]:
    tables: list[str] = []
    lines = content.splitlines()
    i = 0
    while i < len(lines) and len(tables) < max_tables:
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|", lines[i + 1]):
            start = i
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            tables.append("\n".join(lines[start:i]))
        else:
            i += 1
    return tables


def extract_process_phases(content: str) -> list[str]:
    proc = extract_section(content, "## Step-by-Step Process")
    if not proc:
        return []
    phases = re.findall(r"^### (Phase \d+[^:\n]*|Step \d+[^:\n]*)", proc, re.MULTILINE)
    if not phases:
        phases = re.findall(r"^### ([^\n]+)", proc, re.MULTILINE)
    return phases[:8]


def humanize(name: str) -> str:
    return name.replace("-", " ").title()


def skill_terms(name: str, category: str, tags: list[str]) -> list[str]:
    parts = set(re.split(r"[-_]", name))
    parts.update(re.split(r"[-_]", category))
    for t in tags[:5]:
        parts.update(re.split(r"[-_]", t))
    stop = {"the", "and", "for", "gtm", "skill", "tool", "tools"}
    terms = [p.lower() for p in parts if len(p) > 2 and p.lower() not in stop]
    if name.replace("-", " ") not in terms:
        terms.insert(0, name.replace("-", " "))
    return terms[:6]


def make_framework_notes(skill_name: str, category: str, content: str, fm: dict) -> str:
    meta = fm.get("metadata", {})
    frameworks = meta.get("frameworks", [])
    if isinstance(frameworks, str):
        frameworks = [frameworks]

    title = humanize(skill_name)
    lines = [f"# {title} — Framework Notes", "", "Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.", ""]

    if frameworks:
        lines.extend(["## Primary frameworks", ""])
        for fw in frameworks[:8]:
            lines.append(f"- **{fw}**")
        lines.append("")

    auth = extract_section(content, "## Authoritative Foundations") or extract_section(content, "## Frameworks Referenced")
    if auth:
        lines.extend(["## Authoritative foundations", "", auth[:1200], ""])
        if len(auth) > 1200:
            lines.append("*(See SKILL.md for full detail.)*")
            lines.append("")

    phases = extract_process_phases(content)
    if phases:
        lines.extend(["## Process phases", ""])
        for p in phases:
            lines.append(f"- {p}")
        lines.append("")

    tables = extract_tables(content)
    if tables:
        lines.extend(["## Key reference tables", ""])
        for t in tables:
            lines.extend([t, ""])

    lines.extend([
        "## Agent routing",
        "",
        "| Question | Action |",
        "|---|---|",
        f"| Build deliverable | Use `templates/output-template.md` |",
        f"| Validate output | Run `scripts/check-output.py` |",
        f"| Full process | Follow `SKILL.md` step-by-step |",
        "",
    ])
    return "\n".join(lines)


def clean_output_format(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^```(?:markdown|md)?\n?", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def make_output_template(skill_name: str, category: str, content: str) -> str:
    title = humanize(skill_name)
    out_fmt = extract_section(content, "## Output Format")
    body = clean_output_format(out_fmt) if out_fmt else ""

    lines = [f"# {title} — Deliverable", ""]

    if body and len(body) > 80 and not body.startswith("The agent"):
        if body.startswith("#"):
            lines.append(body)
        else:
            lines.extend(["## Deliverable spec", "", body, ""])
    else:
        lines.extend([
            "## Context",
            "- Company / product:",
            "- ICP / segment:",
            "- Owner:",
            "- Date:",
            "",
            "## Summary",
            "[One paragraph: what this deliverable decides or enables]",
            "",
            "## Core output",
            "[Fill per SKILL.md Output Format]",
            "",
        ])

    qc = extract_section(content, "## Quality Check")
    if qc and "- [" in qc:
        lines.extend(["## Quality check", ""])
        for line in qc.splitlines():
            if line.strip().startswith("- ["):
                lines.append(line.strip())
        lines.append("")

    lines.extend([
        "## Next steps",
        "1. ",
        "2. ",
        "3. ",
        "",
    ])
    return "\n".join(lines)


def make_check_script(skill_name: str, category: str, fm: dict) -> str:
    meta = fm.get("metadata", {})
    tags = meta.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    terms = skill_terms(skill_name, category, tags)
    terms_literal = repr(terms)
    title = humanize(skill_name)
    return f'''#!/usr/bin/env python3
"""Validate {title} deliverables."""

import sys
from pathlib import Path

TERMS = {terms_literal}


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace").lower()
    if len(text.strip()) < 200:
        print("FAIL — deliverable too short (<200 chars)")
        return 1

    missing = [t for t in TERMS if t not in text]
    if missing:
        print("FAIL — missing terms:", ", ".join(missing))
        return 1

    print("PASS — {title} deliverable meets minimum checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def artifact_description(path: Path, skill_dir: Path) -> str:
    rel = path.relative_to(skill_dir)
    name = path.stem.replace("-", " ")
    parent = rel.parts[0] if len(rel.parts) > 1 else ""

    custom = {
        "framework-notes.md": "Named frameworks and reference tables",
        "output-template.md": "Deliverable shell for agent output",
        "check-output.py": "Lightweight deliverable validator",
        "email-frameworks.md": "Cold email copy frameworks and rules",
        "subject-line-patterns.md": "Subject line pattern library",
        "sequence-touch-library.md": "Multi-touch email templates",
        "deliverability-primer.md": "Deliverability fundamentals",
        "provider-decision-matrix.md": "Mailbox provider comparison",
        "output-artifacts.md": "Extended output tables and inventories",
        "platform-comparison.md": "Sending platform evaluation matrix",
        "reply-taxonomy.md": "Reply classification taxonomy",
        "reply-funnel-reference.md": "Reply routing funnel reference",
        "bounce-complaint-procedures.md": "Bounce and complaint handling SOP",
        "sending-limits-reference.md": "Provider sending limits reference",
    }
    if path.name in custom:
        return custom[path.name]

    if parent == "references":
        return f"{name.title()} reference material"
    if parent == "templates":
        return f"{name.title()} template"
    if parent == "scripts":
        return f"{name.title()} script"
    return f"{rel} — local artifact"


def insert_execution_artifacts(content: str, artifact_lines: list[str]) -> str:
    section = "## Execution Artifacts\n\n" + "\n".join(artifact_lines) + "\n\n"

    for anchor in ["## Related Skills", "## ⚠️ Disclaimer", "## Disclaimer"]:
        if anchor in content:
            return content.replace(anchor, section + anchor, 1)

    if content.endswith("\n"):
        return content + "\n" + section
    return content + "\n\n" + section


def process_skill(skill_dir: Path, scripts_only: bool = False) -> dict:
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    if "## Execution Artifacts" in content and not scripts_only:
        return {"skipped": True}

    fm = parse_frontmatter(content)
    meta = fm.get("metadata", {})
    skill_name = fm.get("name", skill_dir.name)
    category = meta.get("category", skill_dir.parts[-2] if len(skill_dir.parts) >= 2 else "unknown")
    if isinstance(category, list):
        category = category[0]

    refs_dir = skill_dir / "references"
    tmpl_dir = skill_dir / "templates"
    scripts_dir = skill_dir / "scripts"

    created: list[str] = []
    artifacts: list[Path] = []

    existing_refs = sorted(refs_dir.glob("*")) if refs_dir.exists() else []
    existing_tmpls = sorted(tmpl_dir.glob("*")) if tmpl_dir.exists() else []
    existing_scripts = sorted(scripts_dir.glob("*")) if scripts_dir.exists() else []

    has_framework_notes = any(p.name == "framework-notes.md" for p in existing_refs)
    need_framework_notes = not existing_refs or (not has_framework_notes and len(existing_refs) == 0)

    if not existing_refs:
        refs_dir.mkdir(parents=True, exist_ok=True)
        fn_path = refs_dir / "framework-notes.md"
        fn_path.write_text(make_framework_notes(skill_name, category, content, fm), encoding="utf-8")
        created.append(str(fn_path.relative_to(ROOT)))
        existing_refs = sorted(refs_dir.glob("*"))

    if not existing_tmpls:
        tmpl_dir.mkdir(parents=True, exist_ok=True)
        ot_path = tmpl_dir / "output-template.md"
        ot_path.write_text(make_output_template(skill_name, category, content), encoding="utf-8")
        created.append(str(ot_path.relative_to(ROOT)))
        existing_tmpls = sorted(tmpl_dir.glob("*"))

    need_script = (
        category in ARTIFACT_REQUIRED_CATEGORIES
        or existing_scripts
        or (tmpl_dir.exists() and existing_tmpls)
        or scripts_only
    )
    has_check = any(p.name == "check-output.py" for p in existing_scripts)
    if need_script and not has_check:
        scripts_dir.mkdir(parents=True, exist_ok=True)
        script_path = scripts_dir / "check-output.py"
        script_path.write_text(make_check_script(skill_name, category, fm), encoding="utf-8")
        script_path.chmod(0o755)
        created.append(str(script_path.relative_to(ROOT)))
        existing_scripts = sorted(scripts_dir.glob("*"))

    for p in existing_refs + existing_tmpls + existing_scripts:
        if p.is_file():
            artifacts.append(p)

    artifact_lines = []
    for p in artifacts:
        rel = p.relative_to(skill_dir)
        desc = artifact_description(p, skill_dir)
        artifact_lines.append(f"- `{rel}` — {desc}")

    if not scripts_only:
        new_content = insert_execution_artifacts(content, artifact_lines)
        if new_content != content:
            skill_md.write_text(new_content, encoding="utf-8")
            created.append(str(skill_md.relative_to(ROOT)))
    elif created and "scripts/check-output.py" in [Path(c).name for c in created]:
        if "check-output.py" not in content:
            rel_script = "scripts/check-output.py"
            desc = artifact_description(scripts_dir / "check-output.py", skill_dir)
            line = f"- `{rel_script}` — {desc}"
            if "## Execution Artifacts" in content:
                skill_md.write_text(content.replace("## Execution Artifacts\n\n", f"## Execution Artifacts\n\n{line}\n", 1), encoding="utf-8")
                created.append(str(skill_md.relative_to(ROOT)))

    return {"skill": str(skill_dir.relative_to(SKILLS_DIR)), "created": created}


def fix_stray_backticks():
    fixes = []
    path = SKILLS_DIR / "outbound/domain-infrastructure/references/output-artifacts.md"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if text.rstrip().endswith("```"):
            path.write_text(text.rstrip()[:-3].rstrip() + "\n", encoding="utf-8")
            fixes.append(str(path.relative_to(ROOT)))
    path2 = SKILLS_DIR / "outbound/email-deliverability/references/output-artifacts.md"
    if path2.exists():
        text = path2.read_text(encoding="utf-8")
        if text.rstrip().endswith("```"):
            path2.write_text(text.rstrip()[:-3].rstrip() + "\n", encoding="utf-8")
            fixes.append(str(path2.relative_to(ROOT)))
    return fixes


def main() -> int:
    scripts_only = "--scripts-only" in sys.argv
    fixes = fix_stray_backticks()
    results = []
    for skill_md in sorted(SKILLS_DIR.rglob("SKILL.md")):
        r = process_skill(skill_md.parent, scripts_only=scripts_only)
        if not r.get("skipped"):
            results.append(r)

    updated = len(results)
    created_files = sum(len(r["created"]) for r in results)
    print(f"Updated skills: {updated}")
    print(f"Files touched/created: {created_files}")
    if fixes:
        print(f"Fixed stray backticks: {fixes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
