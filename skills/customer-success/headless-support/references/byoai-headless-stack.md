# BYOAI + Headless CRM/Support Stack

Composable GTM stack for technical teams: **API-first CRM**, **API-first support**, and **bring-your-own AI (BYOAI)** via MCP — instead of monolithic suites with vendor-locked AI agents.

---

## When to use this pattern

| Signal | Headless + BYOAI fit |
|---|---|
| Engineering-led product (dev tools, API, infra) | High — team builds UIs and automations |
| Attio or programmable CRM already chosen | High — same composable philosophy |
| Jesse / Claude Code / Codex in daily workflow | High — MCP connects agent to CRM + support |
| Need embedded support portal in your app | High — Plain headless + custom UI |
| Want Fin / Zendesk AI only, no custom build | Low — use `support-tool-stack` UI-first platforms |
| Non-technical CS team, no RevOps builder | Low — Intercom or Help Scout faster to operate |

**Rule:** BYOAI is not "skip the knowledge base." Deflection still requires 30+ help center articles and tested escalation paths (`SKILL.md` Phase 1–2).

---

## Reference stack (seed → Series A)

| Layer | Tool | Role | AI connection |
|---|---|---|---|
| **CRM** | Attio | Programmable objects, lists as queues, webhooks | API + n8n; optional CRM MCP when available |
| **Support** | Plain | Threads, customers, tenants, help center, headless portal | **Plain MCP** (`https://mcp.plain.com/mcp`) |
| **Orchestration** | n8n | Routing, enrichment sync, SLA timers | Webhooks from Attio + Plain |
| **Enrichment** | Clay + LeadMagic | Waterfall, verify-before-send | `leadmagic-mcp` for agent research |
| **Agent IDE** | Jesse / Claude Code | Draft replies, triage, account research | `mcp-setup` guardrails |

**Contrast — suite stack:** HubSpot CRM + Intercom (Fin AI locked to Intercom). Works faster for non-technical teams; harder to embed support in-product or wire your agent across CRM + support + code.

---

## Plain — headless support infrastructure

Plain is **API-first support**: GraphQL API parity with UI, native MCP server, headless customer portal, Slack/email/chat channels into one queue.

**BYOAI primitives (via MCP):**
- **Read:** search threads, customer/tenant details, help center articles
- **Draft:** `addGeneratedReply` for human review before send
- **Write (confirm first):** assign, label, priority, internal notes, mark done
- **Auth:** OAuth via Plain account — same permissions as the user; no separate API key rotation for MCP

**Setup:** Load `mcp-setup` → add Plain MCP server → read-only tools first → enable reply/assign only with confirmation gates.

**Headless portal:** Embed support in your product (custom components, your design system). Customers submit and track threads without leaving your app. Pair with in-app contextual help (Level 0 deflection in `SKILL.md`).

Sources: [Plain headless support](https://www.plain.com/support/headless-support) · [Plain MCP server](https://help.plain.com/article/mcp-server) · [API-first support definition](https://www.plain.com/blog/what-is-api-first-customer-support)

---

## Attio + Plain integration map

| Event | Flow |
|---|---|
| New support thread (enterprise tier) | Plain webhook → n8n → upsert Attio Person/Company → flag Account tier |
| Deal closed-won | Attio workflow → create Plain tenant field / label for onboarding priority |
| Churn risk thread | Plain label `churn-risk` → n8n → Attio Deal or CS object note |
| Agent researches account | MCP: Plain thread history + Attio list membership in one agent session |

CRM setup: `attio-setup` · Support MCP: `mcp-setup` · Full platform compare: `support-tool-stack`

---

## BYOAI operating rules

1. **Human-in-loop for customer-facing sends** — agents draft; humans approve (`mcp-setup` write gates).
2. **No autonomous billing/security promises** — same escalation triggers as Fin/Zendesk AI (`SKILL.md` Phase 2).
3. **Thread context + CRM context together** — agent should load Plain thread + Attio record before replying.
4. **Batch work in n8n** — do not loop 100 CRM writes in chat; use MCP-01 pattern (`n8n-toolkit`).
5. **Measure deflection per channel** — KB self-serve, MCP-assisted drafts, human — separate CSAT where possible.

---

## Decision: Plain vs Intercom Fin

| Need | Choose |
|---|---|
| In-app Messenger + Fin out of the box | Intercom |
| Embedded portal + your UI + MCP in Jesse | Plain |
| Phone + ITIL + workforce management | Zendesk |
| Email shared inbox only | Front or Help Scout |

Plain does not replace product tours or marketing automation — pair with `customer-onboarding` and in-app help for Level 0 deflection.

---

## Load order

1. `crm-toolkit` → `crm-selection.md` (confirm Attio)
2. `attio-setup` — objects, lists, webhooks
3. `headless-support` — KB + deflection funnel
4. `mcp-setup` + Plain MCP — agent tool scope
5. `support-tool-stack` — channel + SLA design
6. `n8n-toolkit` — cross-system routing
