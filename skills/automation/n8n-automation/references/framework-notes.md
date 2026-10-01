# N8N Automation — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **n8n docs — Workflows, webhooks, and HTTP Request node** — Build GTM glue with webhook triggers, HTTP nodes, and a dedicated error workflow for failed runs.
- **Jen Igartua (Go Nimbly) — RevOps automation maturity** — Automate stable, well-defined processes first; automating a broken process only makes it fail faster.
- **HubSpot developer docs — API limits and webhooks** — Batch requests and back off on rate-limit responses when n8n writes to the CRM.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/gtm-flow-catalog.md` | N8N Automation reference | Extended gtm flow catalog detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
