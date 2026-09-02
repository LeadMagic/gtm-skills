# GitHub Repository Topics

GitHub allows 20 topics per repository. These topics balance Agent Skills runtime discovery with the catalog's highest-value GTM use cases.

## Canonical topics (20)

| Topic | Discovery intent |
|---|---|
| `agent-skills` | Canonical Agent Skills phrase |
| `agentskills` | Common unhyphenated marketplace query |
| `claude-code` | Claude Code installation and discovery |
| `codex` | OpenAI Codex compatibility |
| `github-copilot` | GitHub Copilot compatibility |
| `ai-agents` | Broader agent ecosystem |
| `go-to-market` | Full GTM category phrase |
| `gtm` | Short GTM discovery term |
| `b2b-saas` | Primary company and buyer context |
| `sales` | Revenue workflows |
| `marketing` | Demand and content workflows |
| `outbound` | Outbound system design |
| `cold-email` | High-intent outbound query |
| `revops` | Revenue operations workflows |
| `seo` | Content and technical SEO skills |
| `customer-success` | Customer-success and support workflows |
| `plg` | Product-led growth workflows |
| `lead-generation` | Lead acquisition and enrichment |
| `prospecting` | Account and contact discovery |
| `sales-enablement` | Sales collateral and playbooks |

## Update via CLI

```bash
gh api repos/LeadMagic/gtm-skills/topics -X PUT --input - <<'EOF'
{"names":["agent-skills","agentskills","claude-code","codex","github-copilot","ai-agents","go-to-market","gtm","b2b-saas","sales","marketing","outbound","cold-email","revops","seo","customer-success","plg","lead-generation","prospecting","sales-enablement"]}
EOF
```
