# GTM Automation Expert Playbook — RevOps Workflow Maturity

*Workflow design, human+machine division, and automation maturity — distinct from outbound copy/infra experts.*

**Canonical expert:** Jen Igartua (Go Nimbly) — RevOps automation roadmap, agentic GTM, data-first orchestration.  
**Tool playbooks:** `references/automation-playbook-index.md` (38 playbooks).  
**Outbound experts (do not duplicate here):** Justin Michael (Sales Borg / Pattern 23), Eric Nowoslawski (infra / Pattern 15c), Pat Spielmann (enrichment copy / Pattern 17).

---

## When to load this playbook

| Trigger | Load |
|---|---|
| Design RevOps automation strategy | Pattern 30 · this playbook · `gtm-operations` |
| Clay vs n8n vs Cargo vs MCP | `tool-selection-stack` + Section below |
| Fix automation sprawl / broken CRM sync | Jen Igartua maturity model |
| AI agents in GTM stack | `ai-sdr-setup`, `mcp-setup` — with guardrails here |
| Scale from agency to in-house | Pattern 7 + `hiring-agencies` |

---

## Jen Igartua (Go Nimbly) — RevOps automation

**Role:** CEO, Go Nimbly — "OG RevOps agency"; fractional RevOps for Twilio, Zendesk, Intercom, Rippling.  
**Domain:** GTM systems integration, automation roadmap, AI-ready architecture, RevOps as product team.

**Public channels**
- 💼 [LinkedIn](https://www.linkedin.com/in/jen-igartua/)
- 🔗 [gonimbly.com](https://www.gonimbly.com/)
- 🎙 [Revenue Hotline — efficient GTM engine](https://www.recapped.io/blog/revenue-hotline-how-to-build-a-more-efficient-gtm-engine-with-go-nimblys-ceo-jen-igartua)
- ▶ [GTM Innovators — RevOps & silo syndrome](https://www.gtminnovators.com/2058133/episodes)

**Key frameworks**

| Framework | Meaning | GTM action |
|---|---|---|
| **Must-have basics** | Clean data, integrations, opportunity tracking | Fix CRM hygiene before Clay/n8n |
| **Performance boosters** | MEDDPICC auto-fill, mutual action plans, routing | `crm-integration`, `revops-tech-stack` |
| **Delighters** | AI summaries, signal alerts, rep time saved | `ai-sdr-setup` with human-in-loop |
| **Data before AI** | AI fails on dirty CRM | Enrichment QA → `waterfall-enrichment` |
| **RevOps as product** | Roadmap, intake, prioritization | `gtm-operations` + RevOps Co-op PM patterns |
| **Automate backstage; careful frontstage** | Internal sync aggressive; customer-facing cautious | No auto-send without verify gate |

**Contrast matrix — automation experts**

| Expert | Owns | Does not own |
|---|---|---|
| **Jen Igartua** | RevOps maturity, stack orchestration, CRM automation roadmap | Cold email copy, domain infra |
| **Justin Michael** | Sales Borg, SEP human+machine outbound | CRM hygiene, finance approvals |
| **Eric Nowoslawski** | Deliverability, inbox scale, Clay crawl-walk-run campaigns | Enterprise RevOps architecture |
| **Pat Spielmann** | Verify-before-send, Hook-Line-Sinker copy | n8n error handling, MCP guardrails |
| **Matthew Volm** | RevOps Co-op PM, intake prioritization | Tool-specific column design |

---

## Automation maturity model (0–4)

| Level | State | Next action |
|---|---|---|
| **0 — Manual** | Spreadsheets, rep copy-paste | CRM single source of truth |
| **1 — Point tools** | Zapier sprawl, no ownership | `revops-tech-stack` audit |
| **2 — Orchestrated** | Clay or n8n with documented flows | `automation-playbook-index` load order |
| **3 — Governed** | Verify gates, error handling, runbooks | `crm-integration` conflict rules |
| **4 — Agentic** | MCP/agents → approved batch jobs only | `mcp-setup`, `skills-lock` |

**Gate:** Do not jump to Level 4 without Level 2 data quality — Justin Michael's semi-automation ceiling for enterprise applies.

---

## Human + machine division of labor

| Machine owns | Human owns |
|---|---|
| Enrichment, scoring, routing, CRM field updates | Discovery, negotiation, relationship |
| SLA timers, round-robin, dedupe | Manager coaching, deal strategy |
| Draft personalization (reviewed) | Sent emails that need judgment |
| Questionnaire pre-fill from trust center | Security exceptions, legal redlines |

**AI SDR guardrails:** `ai-sdr-setup` — no autonomous send without Pat Spielmann verify gate + Eric Nowoslawski infra check at scale.

---

## Tool selection (orchestration layer)

| Tool | Best for | Pair with |
|---|---|---|
| **Clay** | Enrichment tables, research, waterfall QA | `clay-toolkit`, `leadmagic-waterfall` |
| **n8n** | Event-driven INB/OUT/LIF flows, error retry | `tools/n8n-toolkit/gtm-flow-catalog.md` |
| **Cargo** | Persistent multi-agent routing at scale | RevOps engineer FTE; CRM-native upsert |
| **CRM native** (HubSpot/SF flows) | Lifecycle, simple routing | `hubspot-setup`, `salesforce-setup` |

**Decision rule:** If pain is **data in CRM** → evaluate Cargo/orchestration. If pain is **finding emails** → Clay + LeadMagic. If pain is **message** → outbound experts index, not this playbook.

---

## Load order (new automation build)

1. `revops-tech-stack` — inventory
2. `gtm-automation-expert-playbook.md` (this doc) — maturity + human/machine map
3. `tool-selection-stack` — build vs buy
4. `waterfall-enrichment` + `contact-verification` — data quality
5. Motion toolkit per `automation-playbook-index.md`
6. `gtm-metrics` — measure pipeline impact, not automation vanity metrics

---

## Cross-links

- `references/automation-playbook-index.md` — 38 playbooks
- `references/gtm-experts-outbound-index.md` — outbound expert router
- `gtm-ops/gtm-operations/references/gtm-ops-skill-index.md`
- `foundation/using-gtm-skills` — Pattern 6, 6b, 30
