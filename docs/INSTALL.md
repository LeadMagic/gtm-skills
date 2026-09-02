# Install GTM Agent Skills

GTM Skills follows the [Agent Skills specification](https://agentskills.io/specification). The generated README and `skills.lock` contain the exact current catalog count; installation commands discover skills from the folders on disk. Repository-level reference sources are materialized into the skills that use them, so an installed skill does not depend on the rest of the checkout.

GitHub CLI skill commands are currently in public preview and require GitHub CLI 2.90.0 or later. Check with `gh --version`, preview the requested skill before installation, and review executable scripts before granting a skill user-wide scope.

## Recommended path: GitHub CLI

Recent GitHub CLI releases include `gh skill`, which discovers, previews, installs, lists, updates, and publishes Agent Skills.

### 1. Review before installing

Skills can contain instructions and executable scripts. Preview the exact skill and inspect its files before granting it access to a trusted project or user-wide scope.

```bash
gh skill preview LeadMagic/gtm-skills foundation/gtm-context-bootstrap
```

### 2. Install the narrowest useful scope

Project scope keeps the skill inside the current repository. User scope makes it available across projects and should be reserved for sources you intentionally trust.

```bash
# One skill in the current project
gh skill install LeadMagic/gtm-skills foundation/gtm-context-bootstrap \
  --agent codex --scope project

# Every skill for the current user
gh skill install LeadMagic/gtm-skills --all \
  --agent codex --scope user
```

Supported `--agent` values include `github-copilot`, `claude-code`, `cursor`, `codex`, `gemini-cli`, `opencode`, `windsurf`, `goose`, and `universal`. Run `gh skill install --help` for the authoritative list in your installed GitHub CLI version.

### 3. Pin reproducible installs

Use a release tag or commit SHA when repeatability matters:

```bash
gh skill install LeadMagic/gtm-skills foundation/gtm-context-bootstrap \
  --agent codex --scope project --pin <release-tag-or-commit>
```

Without a pin, GitHub CLI resolves the latest tagged release and then the default branch. Do not assume an untagged package version is installable as a release.

### 4. Verify and update

```bash
gh skill list
gh skill update --all
```

After installation, ask the target agent to list available GTM skills and load `using-gtm-skills`. For a single-skill test, ask it to load the installed skill by name and identify its execution artifacts.

## Claude Code plugin

The native plugin install exposes the complete repository:

```text
/plugin marketplace add LeadMagic/gtm-skills
/plugin install gtm-skills@gtm-skills
```

Non-interactive CLI equivalent:

```bash
claude plugin marketplace add LeadMagic/gtm-skills --scope user
claude plugin install gtm-skills@gtm-skills --scope user --yes
```

## Audited local checkout

Use the repository installer when you want to inspect the exact files first or when GitHub CLI skill installation is unavailable:

```bash
gh repo clone LeadMagic/gtm-skills
cd gtm-skills

# Show commands and destinations without changing anything
./install.sh --target all --dry-run

# Install into one project
./install.sh --target codex --scope project --project /path/to/project

# Replace an existing install only when explicitly intended
./install.sh --target codex --scope project --project /path/to/project --force
```

The local installer copies each skill directly under the target discovery root. It does not silently replace existing skills unless `--force` is supplied.

Available local target keys:

| Target | Project discovery root | Preferred mechanism |
|---|---|---|
| `claude` | `.claude/skills/` | Claude plugin; direct-copy fallback |
| `copilot` / `vscode` | `.github/skills/` | `gh skill --agent github-copilot` |
| `codex` | `.agents/skills/` | `gh skill --agent codex` |
| `cursor` | `.agents/skills/` | `gh skill --agent cursor` |
| `gemini` | `.agents/skills/` | `gh skill --agent gemini-cli` |
| `opencode` | `.agents/skills/` | `gh skill --agent opencode` |
| `windsurf` | `.agents/skills/` | `gh skill --agent windsurf` |
| `goose` | `.agents/skills/` | `gh skill --agent goose` |
| `hermes` | `.agents/skills/` | Universal Agent Skills directory |
| `jesse` | `.jesse/skills/` | Direct local copy |

## Curated Claude installer

The repository also includes a selector for categories, bundles, or individual skills:

```bash
python3 scripts/cc-gtm.py --list
python3 scripts/cc-gtm.py --bundle startup-essentials --dry-run
python3 scripts/cc-gtm.py --skills gtm-context-bootstrap,technical-seo-audit
```

Selected skills are installed directly under `.claude/skills/<skill-name>/`. Generated skill-local reference copies keep each selected installation independent of the repository checkout.

## Maintainer verification

```bash
npm run regenerate
npm run verify
gh skill publish --dry-run
```

`npm run verify` validates every skill and reference, executes every deliverable checker against its unfilled template, verifies the integrity manifest, exercises installer dry-runs, audits public metadata, and confirms generated catalogs have no drift.
