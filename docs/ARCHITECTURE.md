# Architecture

GTM Skills is a static, portable agent-skills repository. It is designed for agents to discover skills cheaply, load instructions on demand, and read supporting artifacts only when needed.

## Repository Shape

```text
gtm-skills/
├── skills/                         # Marketplace-discoverable skills
│   └── <category>/<skill>/
│       ├── SKILL.md                # Required activation file
│       ├── references/             # Deep background, tables, methodology
│       ├── templates/              # Copy-paste output formats
│       ├── scripts/                # Deterministic local checks/helpers
│       └── assets/                 # Static artifacts
├── references/                     # Cross-repo catalogs (experts, pitfalls index)
│   ├── templates/                  # Shared, cross-skill output templates
│   └── artifacts/                  # Shared, cross-skill reference artifacts
├── scripts/                        # Repo maintenance tools
├── docs/                           # Human documentation
├── .claude-plugin/                 # Claude Code marketplace metadata
├── AGENTS.md                       # Agent-facing index
├── CLAUDE.md                       # Claude-focused index
├── README.md                       # Human-facing index
├── taxonomy.csv                    # Generated catalog
└── skills.lock                     # SHA256 integrity manifest
```

## Discovery Contract

All skills must live at exactly:

```text
skills/<category>/<skill-name>/SKILL.md
```

Do not use deeper nesting for skills. Support files may be nested inside a skill directory, but there must not be another `SKILL.md` below it.

## Progressive Disclosure

Agents load the repo in stages:

1. Discovery: read `name` and `description` from frontmatter.
2. Activation: load the selected skill's `SKILL.md`.
3. Execution: load `references/`, `templates/`, `scripts/`, and `assets/` only when required.

This keeps context use low while preserving deep operating detail.

## Generated Files

These files are generated from the actual skills on disk:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `taxonomy.csv`
- `references/pitfalls-index.md`
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `skills.lock`

Hand-maintained cross-repo catalogs:

- `references/README.md` — browsable index of the shared reference library
- `references/skill-index-master.md` — one-page map of every category and skill
- `references/experts.md` — master expert/practitioner index
- `references/gtm-experts-outbound-index.md` — outbound + discovery expert router
- `references/cold-calling-experts-index.md` — phone-first expert router
- `references/automation-playbook-index.md` — 38 automation/toolkit playbooks
- `references/lifecycle-skill-index.md` — lifecycle stage skill router
- `references/gtm-glossary.md` — shared GTM terminology
- `references/saas-metrics-reference.md` — metric formulas (churn, LTV, NRR)
- `references/meritech-saas-benchmarks.md` — public SaaS index (Meritech Capital)
- `references/benchmark-reconciliation.md` — canonical thresholds when sources differ
- `references/dharmesh-shah-hubspot-inbound.md` — HubSpot inbound flywheel (canonical)
- Subsidiary maps inside skills (`coaching-experts.md`, `interview-experts.md`, `expert-frameworks.md`, `gtm-ops-skill-index.md`) link back to `foundation/using-gtm-skills` and the master catalogs above

Run:

```bash
npm run build
```

`npm run build` runs `generate-indexes.js`, `generate-pitfalls-index.js`, and `generate-skills-lock.py`.

Then verify no drift:

```bash
npm run check
gh skill publish --dry-run
```

## Integrity Model

`skills.lock` stores SHA256 hashes for every marketplace-discoverable `SKILL.md`. Consumers and CI can detect unexpected changes by verifying the lock.

## CI Model

GitHub Actions validates:

- JavaScript/Python syntax.
- Skill metadata and body quality.
- Marketplace discovery depth (flat `skills/<category>/<skill>/SKILL.md` only).
- Reference audit (`scripts/audit-references.py`): every reference target resolves, skill depth is flat, and frontmatter `name` matches the directory.
- `skills.lock` consistency.
- Installer dry-run.
- Public repository hygiene audit.
- Generated file drift (`npm run build` followed by `git diff --exit-code` on generated catalogs).
- `gh skill publish --dry-run`.

## Reference Path Convention

Skills reference two kinds of files:

- **Skill-local artifacts** (this skill's own `references/`, `templates/`, `scripts/`, `assets/`) are referenced relative to the skill directory, e.g. `references/framework-notes.md`.
- **Shared catalogs and cross-skill files** are referenced as repo-root paths — either a top-level catalog like `references/experts.md`, or the full skill path `skills/<category>/<skill>/references/<file>.md`.

A reference target is valid if it resolves relative to the skill directory **or** relative to the repository root. Files inside a skill subdirectory (e.g. `references/*.md`) that point at another category must climb to the repo root first (`../../../<category>/...`) or use a full `skills/...` path. This convention is enforced by `scripts/validate-skills.js` and `scripts/audit-references.py`.

## Release Model

Releases are created through `gh skill publish --tag vX.Y.Z`, not by hand-tagging first. The publish command creates the tag and release metadata expected by the marketplace tooling.
