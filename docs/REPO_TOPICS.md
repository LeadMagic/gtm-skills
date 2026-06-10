# GitHub Repository Topics

GitHub allows **20 topics** per repository. These are the canonical topics for [LeadMagic/gtm-skills](https://github.com/LeadMagic/gtm-skills).

## Current topics (20)

| Topic | Why |
|---|---|
| `agent-skills` | Core agentskills.io / Anthropic pattern |
| `agentskills` | Marketplace discovery alias |
| `claude-code` | Primary Claude Code marketplace install |
| `jesse` | Jesse agent compatibility |
| `codex` | OpenAI Codex / agent IDE |
| `copilot` | GitHub Copilot agent surface |
| `go-to-market` | Full GTM scope |
| `gtm` | Short discovery term |
| `b2b-saas` | ICP and buyer context |
| `sales` | Revenue motion |
| `outbound` | Cold outbound cluster |
| `cold-email` | High-intent search term |
| `revops` | RevOps / ops cluster |
| `customer-success` | CS / support skills |
| `plg` | Product-led growth skills |
| `lead-generation` | Prospecting discovery |
| `prospecting` | SDR motion |
| `marketing` | Demand / content cluster |
| `sales-enablement` | Enablement + playbooks |
| `mcp` | Model Context Protocol / agent tools |

## Removed (redundant at 20-cap)

- `ai-agents` — covered by `agent-skills`
- `claude-skills` — covered by `claude-code`
- `revenue-operations` — covered by `revops`
- `github-copilot` — covered by `copilot`

## Update via CLI

```bash
gh api repos/LeadMagic/gtm-skills/topics -X PUT --input - <<'EOF'
{"names":["agent-skills","agentskills","claude-code","jesse","codex","copilot","go-to-market","gtm","b2b-saas","sales","outbound","cold-email","revops","customer-success","plg","lead-generation","prospecting","marketing","sales-enablement","mcp"]}
EOF
```
