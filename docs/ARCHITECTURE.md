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
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `skills.lock`

Run:

```bash
npm run build
```

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
- Marketplace discovery depth.
- `skills.lock` consistency.
- Installer dry-run.
- Generated file drift.
- `gh skill publish --dry-run`.

## Release Model

Releases are created through `gh skill publish --tag vX.Y.Z`, not by hand-tagging first. The publish command creates the tag and release metadata expected by the marketplace tooling.
