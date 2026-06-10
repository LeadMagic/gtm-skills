# N8N Automation — Framework Notes

Use these references to ground outputs in named, repeatable methodology.

## Primary Frameworks

- **Jen Igartua (Go Nimbly) — RevOps automation maturity** — Must-have basics (CRM hygiene) → performance boosters (routing, scoring) → delighters (AI signals). Data before AI. Canonical → `references/gtm-automation-expert-playbook.md` (Pattern 30).
- **n8n Workflow Automation Framework** — Error handling, retry policies, idempotent CRM writes.
- **iPaaS Integration Patterns** — Event-driven vs batch; never duplicate CRM as system of record.
- **HubSpot Academy — CRM Automation** — Lifecycle workflows; pair with `hubspot-setup`.

## Operating Assumptions

- Load `references/gtm-automation-expert-playbook.md` for strategy before building flows.
- Flow catalog: `tools/n8n-toolkit/references/gtm-flow-catalog.md` (INB / OUT / SIG / LIF / REV / MCP).
- Adapt recommendations by ICP tier: small business, mid-market, and enterprise.
- Separate strategy from execution: define the decision rule before creating assets.
- Prefer measurable outputs: fields, templates, scores, dashboards, or checklists.
- MCP agents → approved batch jobs only (`mcp-setup`); no autonomous customer-facing send.

## Contrast (do not merge experts)

| Expert | Owns |
|---|---|
| Jen Igartua | Orchestration roadmap, maturity 0–4 |
| Eric Nowoslawski | Email infra, Clay crawl-walk-run campaigns |
| Justin Michael | Sales Borg outbound human+machine |
| Pat Spielmann | Verify-before-send enrichment copy |

## Agent Use

Before final output, cite which framework shaped the recommendation and identify any assumptions that need user confirmation.
