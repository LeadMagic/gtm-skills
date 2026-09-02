# Repository Maintenance Scripts

Dependency-free tooling (Node >= 24 and Python 3). All scripts are wired into `package.json`; prefer the npm aliases.

| Script | npm alias | Purpose |
|---|---|---|
| `generate-indexes.js` | `npm run generate-indexes` | Regenerate `README.md`, `AGENTS.md`, `CLAUDE.md`, `taxonomy.csv`, and `.claude-plugin/*` from skills on disk |
| `generate-pitfalls-index.js` | `npm run generate-pitfalls` | Aggregate every skill's Common Pitfalls into `references/pitfalls-index.md` |
| `generate-skills-lock.py` | `npm run check:lock` (`--check`) | Generate or verify the SHA-256 inventory for every packaged skill file |
| `validate-skills.js` | `npm run validate` | Agent Skills + GTM quality bar: frontmatter, strict 500-line limit, authority, process, artifacts, hygiene |
| `audit-artifacts.py` | `npm run check:artifacts` | Verify exact artifact ownership, required files, minimum substance, portability, and executable scripts |
| `fix-decoration-authority.py` | `npm run fix:authority` | Replace generic authority filler with substantive `Authoritative Foundations` bullets |
| `fix-weak-skill-artifacts.py` | `npm run fix:artifacts` | Add missing `framework-notes.md`, `output-template.md`, expand thin indexes |
| `sync-execution-artifacts.py` | `npm run sync:artifacts` | Ensure `## Execution Artifacts` lists the standard artifact triad |
| `public-repo-audit.py` | `npm run check:public` | Public hygiene checks: count drift, required community files, allowed URL domains, CI hygiene |
| `install-tui.py` | `npm run install:tui` | Scoped installer for 10 agent targets using `gh skill`, Claude plugins, or safe local-copy fallbacks |
| `audit-checkers.py` | `npm run check:checkers` | Executes every deliverable checker and rejects unfilled-template false positives |
| `harden-check-output.py` | `npm run harden:checkers` | Idempotently repairs legacy checkers that accept their own templates |
| `materialize-shared-references.py` | `npm run check:portable` | Generates and verifies skill-local copies of shared references for portable one-skill installs |
| `batch-add-execution-artifacts.py` | — | Maintenance batch tool for adding Execution Artifacts sections to skills |
| `generate-skills-lock.sh` | — | Shell wrapper for the lock generator |

## Common Workflows

Regenerate everything after changing skills:

```bash
npm run build    # generate-indexes + generate-pitfalls + skills.lock
```

Validate before a PR or release:

```bash
npm run check    # validate + lock check + installer dry-run + public audit
```

## Rules

- Generated files must never be hand-edited; rerun `npm run build` instead.
- No runtime dependencies and no telemetry. Scripts must work from a fresh clone with only Node and Python installed.
