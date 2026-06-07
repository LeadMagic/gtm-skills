# AI System Support

GTM Blueprints follow the [Agent Skills open standard](https://agentskills.io/specification). Every skill is a `SKILL.md` file with YAML frontmatter and Markdown body. Skills work anywhere the standard is supported.

## Supported Systems

| System | Install Method | Path |
|---|---|---|
| **Claude Code** | `claude plugins add leadmagic/gtm-skills` | `.claude/skills/` |
| **Claude.ai (Projects)** | Upload `skills/` directory into project knowledge | Project → Add content |
| **Cursor** | Git clone or copy into `.cursor/skills/` | `.cursor/skills/` or read from `.claude/skills/` |
| **OpenAI Codex** | Git clone, point at `.agents/skills/` | `.agents/skills/` |
| **Hermes Agent** | `hermes skills install leadmagic/gtm-skills` | `~/.hermes/skills/` |
| **Windsurf** | Copy skills to `.windsurf/skills/` | `.windsurf/skills/` |
| **OpenCode** | Copy skills to `.opencode/skills/` or `~/.config/opencode/skills/` | `.opencode/skills/` |
| **GitHub Copilot** | Copy skills to `.github/copilot/skills/` | `.github/copilot/skills/` |
| **Gemini CLI** | Copy skills to `.claude/skills/` (yes, that path) | `.claude/skills/` |
| **Zed** | Reads `AGENTS.md` at project root — points to `skills/` | Project root |
| **VS Code (Copilot)** | Copy skills to `.github/copilot/skills/` | `.github/copilot/skills/` |
| **Goose (Block)** | Copy skills to `.goose/skills/` | `.goose/skills/` |

## Quick Install

```bash
# Clone the repo
git clone https://github.com/leadmagic/gtm-skills.git

# Claude Code (marketplace)
claude plugins add leadmagic/gtm-skills
claude skills install leadmagic/gtm-skills

# Claude Code (manual)
cp -r gtm-skills/skills/* .claude/skills/

# Cursor
cp -r gtm-skills/skills/* .cursor/skills/

# Codex
cp -r gtm-skills/skills/* .agents/skills/

# Hermes
hermes skills install leadmagic/gtm-skills
```

## How Skills Get Discovered

Each system reads `name` and `description` from every skill's YAML frontmatter at startup. When your request matches a skill's description, the system loads the full skill body. You don't invoke skills by name — describe what you need and the right skill activates automatically.

## Category Quick Reference

| Category | Skills | For when you need to... |
|---|---|---|
| `foundation` | 5 | Define ICP, positioning, pricing, competitive intel |
| `prospecting` | 7 | Find leads, enrich data, verify contacts, score signals |
| `outbound` | 8 | Cold email, cold calling, deliverability, domains, platforms, replies |
| `inbound` | 4 | Triage inbound, content marketing, social selling, landing pages |
| `sales-revops` | 6 | Enablement, meeting prep, pipeline, objections, demos, deal desk |
| `analytics` | 6 | Campaign analytics, deliverability, GTM metrics, A/B testing, alerts |
| `automation` | 7 | Clay, AI SDR, API enrichment, CRM, MCP, n8n, waterfall enrichment |
| `design` | 7 | Pitch decks, one-pagers, battlecards, ROI calculators, case studies, UI/UX |
| `growth` | 4 | Churn prevention, expansion, referrals, customer marketing |
| `founder-led` | 8 | Solo founder GTM, brand, launches, lead magnets, sales team, metrics |
| `leadmagic` | 6 | CLI, waterfall, MCP, integrations, bulk enrichment, job change |
