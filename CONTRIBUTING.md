# Contributing to GTM Skills

Thanks for improving GTM Skills. This repo is a public, operator-grade skill library for AI agents. Contributions are welcome when they make the library more useful, more accurate, or easier to install.

## What We Accept

- New skills that produce concrete artifacts: playbooks, templates, workflows, scorecards, scripts, dashboards, or QA checklists.
- Improvements to existing skills: clearer triggers, stronger frameworks, better output formats, better failure modes.
- Documentation fixes: install paths, compatibility notes, troubleshooting, examples.
- Validator, installer, CI, and lockfile improvements.
- Public vendor/tool guidance that works without requiring one paid platform.

## What We Reject

- Generic "best practice" content without named sources or real operating detail.
- Thin skills that duplicate existing coverage.
- Vendor-only docs that read like a catalog entry.
- Private/internal implementation details, credentials, customer data, private infrastructure, or private community references.
- Analytics/tracking SDK additions. This repo has no runtime telemetry.

## Skill Quality Bar

Every skill must include:

1. `SKILL.md` with valid YAML frontmatter.
2. `name` matching the directory name.
3. `description` under 1024 characters that says what the skill does and when to use it.
4. Named authorities/frameworks in metadata or the body.
5. Trigger phrases under "When to Use".
6. Step-by-step process.
7. Output format the agent can actually produce.
8. Quality checks and common pitfalls.
9. Related skills.
10. Support files in `references/`, `templates/`, `scripts/`, or `assets/` when the skill has long tables, reusable artifacts, or deterministic checks.

See `docs/SKILL_AUTHORING.md` for the full standard.

## Local Validation

Run all checks before opening a PR:

```bash
npm run regenerate   # or: npm run build
npm run verify       # check + generated drift gate
gh skill publish --dry-run
```

`npm run check` runs the skill validator, the reference audit (`scripts/audit-references.py`, which confirms every reference target resolves, skill paths are flat, and frontmatter `name` matches the directory), the lock check, the installer dry-run, and the public-repo hygiene audit.

Expected result (count matches the current catalog):

```text
203 skills checked. 0 errors, 0 warnings.
Reference audit passed: 203 skills, all reference targets resolve, layout and frontmatter names clean.
skills.lock verified: 203 skills
npm run check:generated — no drift in files listed in scripts/generated-artifacts.txt
```

After merge to `main`, `.github/workflows/regenerate.yml` auto-commits catalog updates if anything drifted. On PRs, drift fails CI — run `npm run regenerate` locally first.

## Adding a Skill

Use this structure:

```text
skills/<category>/<skill-name>/
├── SKILL.md
├── references/
├── templates/
├── scripts/
└── assets/
```

Do not nest deeper than `skills/<category>/<skill-name>/SKILL.md`. Agentskills marketplace discovery only sees that layout.

## Pull Request Checklist

- [ ] `npm run check` passes.
- [ ] `gh skill publish --dry-run` passes.
- [ ] New/changed skills cite named authorities.
- [ ] Generated files are current: README.md, AGENTS.md, CLAUDE.md, taxonomy.csv, skills.lock, `.claude-plugin/*`.
- [ ] No private/internal details or secrets.
- [ ] No new runtime dependencies unless justified.
- [ ] No telemetry, analytics SDKs, crash-reporting SDKs, or hidden network calls.

## Security and Privacy

Never include secrets, tokens, private customer data, private infrastructure details, or internal operating metrics. If you find sensitive content, report it privately through the process in `SECURITY.md`.
