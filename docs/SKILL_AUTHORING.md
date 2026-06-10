# Skill Authoring Standard

This is the quality bar for every skill in GTM Skills.

## Frontmatter

```yaml
---
name: skill-name
description: >-
  Use when the user asks for specific outcome, mentions specific trigger phrases,
  or needs a concrete GTM artifact. Include what the skill produces.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: category-name
  tags: [gtm, sales, marketing]
  related_skills: [related-skill]
  frameworks:
    - "Named Authority — Framework"
---
```

Rules:

- `name` must match the directory.
- `description` must be under 1024 characters.
- `compatibility` must be under 500 characters.
- Descriptions must include trigger language so agents know when to load the skill.
- Every skill must cite named authorities, frameworks, vendor docs, or primary sources.
- Source coverage must pass the rubric in [SOURCE_STANDARDS.md](SOURCE_STANDARDS.md): no anonymous "best practices", no placeholder framework names, no internal/private sources.

## Body Structure

Use this order:

1. Overview — what mistake this skill prevents.
2. When to Use — trigger phrases and situations.
3. Authoritative Foundations — named sources and frameworks.
4. Prerequisites — inputs, access, constraints.
5. Step-by-Step Process — phases the agent follows.
6. Output Format — exactly what the user receives.
7. Quality Check — verifiable acceptance criteria.
8. Common Pitfalls — mistake, why it fails, fix.
9. Related Skills — cross-links.

## Artifact Pattern

Use support files when the skill includes long references, reusable templates, or deterministic checks:

```text
skill-name/
├── SKILL.md
├── references/framework-notes.md
├── templates/output-template.md
└── scripts/check-output.py
```

Keep `SKILL.md` focused. Move long tables and libraries into `references/`.

## Reference Paths

When linking to support files, follow one convention so validation passes:

- **Skill-local files** (this skill's own `references/`, `templates/`, `scripts/`, `assets/`) are referenced relative to the skill directory: `` `references/framework-notes.md` `` or `[notes](references/framework-notes.md)`.
- **Shared catalogs** at the repo root are referenced by their root path: `` `references/experts.md` ``.
- **Files owned by another skill** are referenced by their full repo path: `` `skills/<category>/<skill>/references/<file>.md` `` — never as a bare `references/<file>.md`, which would be read as skill-local.
- Inside a skill subdirectory (e.g. a file under `references/`), a link to another category must climb to the repo root: `../../../<category>/<skill>/references/<file>.md`.

`scripts/validate-skills.js` and `scripts/audit-references.py` require every reference target to resolve relative to the skill directory or the repo root.

## Anti-Fluff Rules

Replace vague claims with named sources and operational detail.

Bad:

```text
Use best practices to improve conversion.
```

Good:

```text
Use Joanna Wiebe's message-mining pattern to extract customer language, then write a hero with one quantified pain, one differentiated mechanism, and one CTA.
```

Avoid:

- "in today's fast-paced world"
- "game-changer"
- "unlock your potential"
- "best-in-class"
- "seamless"
- "actionable insights"
- unsupported "data-driven" claims

## Validation

`scripts/validate-skills.js` enforces the [agentskills.io specification](https://agentskills.io/specification) plus the GTM quality bar:

| Check | Standard |
|---|---|
| `name` | Lowercase `a-z0-9` + hyphens; matches directory; max 64 chars |
| `description` | 40–1024 chars; includes trigger language |
| `compatibility` | Exact repo string; max 500 chars |
| Authority | `Authoritative Foundations` or `Frameworks Referenced` with ≥3 named sources |
| Process | `Step-by-Step`, `Implementation Checklist`, or documented workflow section |
| Artifacts | Every skill: `references/framework-notes.md`, `templates/output-template.md`, `scripts/check-output.py` |
| Execution Artifacts | SKILL.md lists all three artifacts above |
| Hygiene | No decoration filler, AI-slop phrases, or broken reference paths |
| Length | ≤500 lines unless ≥5 reference files (move detail to `references/`) |

Maintenance scripts:

```bash
npm run fix:authority   # replace generic authority filler in SKILL.md
npm run fix:artifacts   # add missing framework-notes / output templates
npm run sync:artifacts  # align Execution Artifacts sections
```

Release gate:

```bash
npm run build
npm run verify          # check + generated-artifact drift
gh skill publish --dry-run
```

A skill is not ready unless all three pass.
