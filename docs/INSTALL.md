# AI System Install Guide

GTM Blueprints follow the [Agent Skills open standard](https://agentskills.io/specification). Every skill is a `SKILL.md` file with YAML frontmatter and Markdown body. Skills work anywhere the standard is supported.

## Supported Systems — 11 Platforms

These are the systems in the repo compatibility string. The TUI installer supports all of them.

| # | System | TUI Key | Install Method | Path / Behavior |
|---|---|---|---|---|
| 1 | **Claude Code** | `claude` | `claude plugins add LeadMagic/gtm-skills` | Preferred plugin install |
| 2 | **Cursor** | `cursor` | Project-local copy | `.cursor/skills/gtm-skills/` |
| 3 | **Codex** | `codex` | `codex skills install LeadMagic/gtm-skills` or local copy | `~/.codex/skills/gtm-skills/` fallback |
| 4 | **Hermes** | `hermes` | `hermes skills install LeadMagic/gtm-skills` or local copy | `~/.hermes/skills/gtm-skills/` fallback |
| 5 | **Windsurf** | `windsurf` | Project-local copy | `.windsurf/skills/gtm-skills/` |
| 6 | **OpenCode** | `opencode` | Project-local copy | `.opencode/skills/gtm-skills/` |
| 7 | **Gemini CLI** | `gemini` | Project-local copy | `.gemini/skills/gtm-skills/` |
| 8 | **GitHub Copilot** | `copilot` | Copy + instructions | `.github/skills/gtm-skills/` and `.github/copilot-instructions.md` |
| 9 | **Zed** | `zed` | AGENTS.md + local copy | `AGENTS.md` and `.zed/skills/gtm-skills/` |
| 10 | **VS Code** | `vscode` | Copy + instructions | same path as Copilot agent mode |
| 11 | **Goose** | `goose` | Local copy | `~/.config/goose/skills/gtm-skills/` |

## How Skills Get Discovered

Each system reads `name` and `description` from every skill's YAML frontmatter at startup. When your request matches a skill's description, the system loads the full skill body. You don't invoke skills by name — describe what you need and the right skill activates automatically.

**Progressive disclosure:** Level 1 loads metadata (~100 tokens per skill). Level 2 loads the full SKILL.md body. Level 3 loads references, templates, scripts, and assets on demand.

## Quick Install — TUI

```bash
git clone https://github.com/LeadMagic/gtm-skills.git
cd gtm-skills
./install.sh

# Non-interactive examples
./install.sh --target hermes
./install.sh --target cursor --project /path/to/project
./install.sh --target all --dry-run
```

The installer is dependency-free Python. It uses official CLIs when available and safe local-copy fallbacks when they are not.

## Quick Install — Manual

```bash
# Claude Code
claude plugins add LeadMagic/gtm-skills

# Hermes Agent
hermes skills install LeadMagic/gtm-skills

# Project-local systems
cp -R . .cursor/skills/gtm-skills
cp -R . .windsurf/skills/gtm-skills
cp -R . .opencode/skills/gtm-skills
cp -R . .gemini/skills/gtm-skills
```

## Per-System Detail

### Claude Code

Preferred path:

```bash
claude plugins add LeadMagic/gtm-skills
```

### Cursor

Use the installer or copy the repo into `.cursor/skills/gtm-skills/` for project-local discovery.

```bash
./install.sh --target cursor --project /path/to/project
```

### Codex

Use the Codex CLI if available. The installer falls back to a local copy under `~/.codex/skills/gtm-skills/`.

```bash
./install.sh --target codex
```

### Hermes

Use the Hermes CLI if available. The installer falls back to a local copy under `~/.hermes/skills/gtm-skills/`.

```bash
./install.sh --target hermes
```

### Windsurf / OpenCode / Gemini CLI

Use project-local copies:

```bash
./install.sh --target windsurf --project /path/to/project
./install.sh --target opencode --project /path/to/project
./install.sh --target gemini --project /path/to/project
```

### Copilot / VS Code

The installer copies the skills under `.github/skills/gtm-skills/` and writes `.github/copilot-instructions.md` pointing the agent to the repo index.

```bash
./install.sh --target copilot --project /path/to/project
./install.sh --target vscode --project /path/to/project
```

### Zed

The installer writes `AGENTS.md` and copies the full skill repo under `.zed/skills/gtm-skills/`.

```bash
./install.sh --target zed --project /path/to/project
```

### Goose

The installer copies the full repo under `~/.config/goose/skills/gtm-skills/`.

```bash
./install.sh --target goose
```

## Category Quick Reference

Run this to regenerate the complete category index from the current repository state:

```bash
node scripts/generate-indexes.js
```

The generated `AGENTS.md`, `CLAUDE.md`, `taxonomy.csv`, and `skills.lock` are the source of truth for the complete 189-skill catalog.
