# AI System Install Guide

GTM Blueprints follow the [Agent Skills open standard](https://agentskills.io/specification). Every skill is a `SKILL.md` file with YAML frontmatter and Markdown body. Skills work anywhere the standard is supported.

## Supported Systems — 15 Platforms

| # | System | Install Method | Skill Path | Auto-Discovery |
|---|---|---|---|---|
| 1 | **Claude Code** | `claude plugins add leadmagic/gtm-skills` | `.claude/skills/` or `~/.claude/skills/` | Yes — reads all descriptions at startup |
| 2 | **Cursor** | Copy to `.cursor/skills/` or reads `.claude/skills/` | `.cursor/skills/` | Yes — Cursor 0.46+ supports Agent Skills |
| 3 | **OpenAI Codex** | Copy to `.agents/skills/` or `~/.agents/skills/` | `.agents/skills/` | Yes — reads `AGENTS.md` at project root |
| 4 | **Hermes Agent** | `hermes skills install leadmagic/gtm-skills` | `~/.hermes/skills/` or `.hermes/skills/` | Yes — full spec compliance |
| 5 | **Windsurf** | Copy to `.windsurf/skills/` | `.windsurf/skills/` | Yes |
| 6 | **OpenCode** | Copy to `.opencode/skills/` or `~/.config/opencode/skills/` | `.opencode/skills/` | Yes |
| 7 | **GitHub Copilot** | Copy to `.github/copilot/skills/` | `.github/copilot/skills/` | Yes |
| 8 | **Gemini CLI** | Copy to `.claude/skills/` (standard path) | `.claude/skills/` | Yes |
| 9 | **Zed** | Reads `AGENTS.md` at project root | Project root | Partial — reads AGENTS.md index |
| 10 | **VS Code (Copilot)** | Copy to `.github/copilot/skills/` | `.github/copilot/skills/` | Yes — via Copilot extension |
| 11 | **Goose (Block)** | Copy to `.goose/skills/` | `.goose/skills/` | Yes |
| 12 | **Antigravity (Google)** | Copy to `.agent/skills/` or `~/.gemini/antigravity/skills/` | `.agent/skills/` | Yes |
| 13 | **Claude.ai (Projects)** | Upload `skills/` directory into project knowledge | Project → Add content | Manual — upload per project |
| 14 | **Junie (JetBrains)** | Copy to `.claude/skills/` | `.claude/skills/` | Yes |
| 15 | **Amp (Sourcegraph)** | Copy to `.claude/skills/` | `.claude/skills/` | Yes |

## How Skills Get Discovered

Each system reads `name` and `description` from every skill's YAML frontmatter at startup. When your request matches a skill's description, the system loads the full skill body. You don't invoke skills by name — describe what you need and the right skill activates automatically.

**Progressive disclosure:** Level 1 loads metadata (~100 tokens per skill). Level 2 loads the full SKILL.md body (<5K tokens). Level 3 loads references, scripts, and assets on demand.

## Quick Install

```bash
# Clone the repo
git clone https://github.com/leadmagic/gtm-skills.git
cd gtm-skills

# === Claude Code (recommended) ===
claude plugins add leadmagic/gtm-skills
claude skills install leadmagic/gtm-skills
# Install a specific category
claude skills install leadmagic/gtm-skills --category outbound

# === Claude Code (manual) ===
cp -r skills/* .claude/skills/

# === Cursor ===
cp -r skills/* .cursor/skills/

# === Codex ===
cp -r skills/* .agents/skills/

# === Hermes Agent ===
hermes skills install leadmagic/gtm-skills

# === Windsurf ===
cp -r skills/* .windsurf/skills/

# === OpenCode ===
cp -r skills/* .opencode/skills/

# === GitHub Copilot ===
cp -r skills/* .github/copilot/skills/

# === Gemini CLI ===
cp -r skills/* .claude/skills/

# === Goose ===
cp -r skills/* .goose/skills/

# === Antigravity ===
cp -r skills/* .agent/skills/
```

## Per-System Detail

### Claude Code (Anthropic)
The primary target. Marketplace install is the cleanest path. Claude Code auto-discovers all skills at session start. Use natural language — the right skill activates based on your request.

```bash
claude plugins add leadmagic/gtm-skills
# Then just ask:
# "Build a cold email sequence for VP Sales at Series B SaaS companies"
# "Score this company list against our ICP"
# "Set up a Clay waterfall enrichment workflow"
```

### Cursor (Anysphere)
Cursor 0.46+ supports the Agent Skills spec natively. Place skills in `.cursor/skills/` or Cursor will read from `.claude/skills/` if present. Works with Cursor's Agent mode.

### OpenAI Codex
Codex discovers skills via `AGENTS.md` at the project root. This repo's `AGENTS.md` points to the `skills/` directory. Global install: `~/.agents/skills/`. Project install: `./.agents/skills/`.

### Hermes Agent (Nous Research)
Full spec compliance. Install via `hermes skills install` or copy to `~/.hermes/skills/`. Hermes reads frontmatter at session start and loads skills on trigger match.

### Windsurf
Copy skills to `.windsurf/skills/`. Windsurf's agent mode respects the Agent Skills spec.

### OpenCode
Copy to `.opencode/skills/` (project) or `~/.config/opencode/skills/` (global). OpenCode auto-discovers at session start.

### GitHub Copilot
Copy to `.github/copilot/skills/`. Works in VS Code and JetBrains via the Copilot extension.

### Gemini CLI (Google)
Uses the standard `.claude/skills/` directory. Copy skills there. Gemini CLI supports the full Agent Skills spec.

### Zed
Zed reads `AGENTS.md` at the project root. The repo's `AGENTS.md` provides the skill index. Full skill loading is partial — Claude Code or Cursor are recommended for full skill execution.

### VS Code with Copilot
Copy skills to `.github/copilot/skills/`. The Copilot extension discovers and loads skills automatically.

### Goose (Block)
Copy to `.goose/skills/`. Full spec compliance.

### Antigravity (Google)
Copy to `.agent/skills/` (project) or `~/.gemini/antigravity/skills/` (global). Google's IDE with full Agent Skills support.

### Claude.ai Projects
Upload the `skills/` directory into a Claude.ai Project via "Add content." Skills are available within that project's conversations. No auto-install — manual upload per project.

### Junie (JetBrains)
JetBrains' AI agent. Copy to `.claude/skills/`. Full spec compliance.

### Amp (Sourcegraph)
Copy to `.claude/skills/`. Full spec compliance.

## Category Quick Reference

| Category | Skills | For when you need to... |
|---|---|---|
| `foundation` | 5 | Define ICP, positioning, pricing, competitive intel |
| `prospecting` | 7 | Find leads, enrich data, verify contacts, score signals |
| `outbound` | 9 | Cold email, cold calling, deliverability, domains, inbox setup, platforms |
| `inbound` | 4 | Triage inbound, content marketing, social selling, landing pages |
| `sales-revops` | 6 | Enablement, meeting prep, pipeline, objections, demos, deal desk |
| `analytics` | 8 | Campaign analytics, GTM metrics, A/B testing, experimentation, alerts, tagging |
| `automation` | 8 | Clay, AI SDR, API enrichment, CRM, MCP, n8n, waterfall, tool stack selection |
| `design` | 7 | Pitch decks, one-pagers, battlecards, ROI calculators, case studies, UI/UX |
| `growth` | 4 | Churn prevention, expansion, referrals, customer marketing |
| `founder-led` | 13 | Solo founder, brand, launches, lead magnets, sales team, metrics, SaaS building, SOC2, exit, hiring |
| `leadmagic` | 6 | CLI, waterfall, MCP, integrations, bulk enrichment, job change |
| `management-leadership` | 2 | Sales coaching, team management |
| `customer-success` | 2 | CS playbooks, QBR planning |
| `product-led-growth` | 2 | PLG strategy, freemium optimization |
| `creative` | 3 | Copywriting, social media, graphic design |
