# Automation Playbook Index

Master index of **every** GTM automation skill and toolkit playbook. Load `using-gtm-skills` Pattern 6 / 6b / 17 for orchestration order.

**Rule:** Process skills (`automation/`) define *when and why*. Tool skills (`tools/`, `sequencing-tools/`, `leadmagic/`) define *how to configure*. Never skip data quality (`waterfall-enrichment`, `contact-verification`, `leadmagic-waterfall`) before routing automation.

---

## Category: `automation/` (12 playbooks)

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 1 | `clay-automation` | Clay rollout, table governance, enrichment QA | `references/framework-notes.md`, `templates/output-template.md` |
| 2 | `n8n-automation` | n8n vs Clay vs MCP decision, error handling | `references/framework-notes.md`, `references/gtm-flow-catalog.md` |
| 3 | `mcp-setup` | MCP agents → approved batch jobs | `references/framework-notes.md` |
| 4 | `waterfall-enrichment` | Provider order, match rates, cost caps | `references/framework-notes.md` |
| 5 | `api-enrichment` | Direct API enrichment pipelines | `references/framework-notes.md` |
| 6 | `crm-integration` | Sync rules, field mapping, conflict resolution | `references/framework-notes.md` |
| 7 | `ai-sdr-setup` | AI SDR guardrails, human-in-loop | `references/framework-notes.md`, `../../outbound/cold-email-strategy/references/justin-michael-sales-borg.md` |
| 8 | `salesforce-setup` | SFDC automation objects, flows | `references/framework-notes.md` |
| 9 | `hubspot-setup` | HubSpot workflows, lifecycle | `references/framework-notes.md` |
| 10 | `attio-setup` | Attio automation patterns | `references/framework-notes.md` |
| 11 | `tool-selection-stack` | Build vs buy, stack consolidation | `references/framework-notes.md` |
| 12 | `skills-lock` | Skill integrity verification | `references/framework-notes.md` |

---

## Category: `tools/` (9 toolkits)

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 13 | `clay-toolkit` (`tools/clay-toolkit`) | Table blueprints, waterfall columns | `references/gtm-table-blueprints.md`, `templates/waterfall-config.md` |
| 14 | `clay-loops-toolkit` | Signal loops (funding, hiring, job change) | `references/loop-catalog.md`, `references/leadmagic-waterfall.md`, `templates/loop-blueprint.md` |
| 15 | `n8n-toolkit` | Flow IDs: INB / OUT / SIG / LIF / REV / MCP | `references/gtm-flow-catalog.md`, `templates/workflow-blueprint.md` |
| 16 | `ai-prompts-toolkit` | Claygent / LLM prompt loops P01–P10 | `references/prompt-library.md`, `templates/prompt-spec.md` |
| 17 | `sequencing-toolkit` | Multi-channel sequence architecture | `references/platform-comparison.md`, `templates/sequence-architecture.md` |
| 18 | `crm-toolkit` | CRM selection, blueprints, land-expand | `references/salesforce-blueprint.md`, `references/hubspot-blueprint.md` |
| 19 | `leadmagic-toolkit` | Find → Verify → Enrich column patterns | `references/framework-notes.md` |
| 20 | `analytics-toolkit` | Stack by stage, event taxonomy | `references/analytics-stack-by-stage.md` |
| 21 | `support-toolkit` | Headless support automation | `references/platform-comparison.md` |

---

## Category: `sequencing-tools/` (6 platform playbooks)

Platform-specific sequencer configuration. Pair with `sequencing-toolkit` for architecture; upstream with `leadmagic-waterfall` + `clay-toolkit`.

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 22 | `instantly-sequences` | Warmup pool, rotation, unified inbox | `references/clay-enrollment-handoff.md`, `references/framework-notes.md` |
| 23 | `smartlead-workflows` | Unlimited mailboxes, AI reply labels, Eric-scale infra | `references/clay-enrollment-handoff.md`, `references/framework-notes.md` |
| 24 | `lemlist-setup` | lemwarm, Guillaume multichannel, personalization | `references/clay-enrollment-handoff.md`, `references/framework-notes.md` |
| 25 | `salesloft-cadences` | Rhythm cadences, CRM verify gate | `references/enrichment-enrollment-gate.md`, `references/framework-notes.md` |
| 26 | `outreach-sequences` | Enterprise triggers, Clay→CRM→Outreach | `references/enrichment-enrollment-gate.md`, `references/framework-notes.md` |
| 27 | `hubspot-sequences` | Workflow enrollment, rep-triggered sequences | `references/enrichment-enrollment-gate.md`, `references/framework-notes.md` |

**Expert cross-refs:** Eric Nowoslawski (infra scale — Smartlead/Instantly) · Pat Spielmann (verify-before-send) · Guillaume Moubeche (lemlist) → `references/gtm-experts-outbound-index.md`

---

## Category: `leadmagic/` (6 playbooks)

LeadMagic-specific enrichment, integration, and agent tooling. Default upstream provider for `clay-toolkit` and `clay-loops-toolkit`.

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 28 | `leadmagic-waterfall` | Clay waterfall: Find → Verify → Enrich | `references/waterfall-column-spec.md`, `references/framework-notes.md` |
| 29 | `leadmagic-integrations` | Clay, CRM, sequencer, n8n connections | `references/integration-checklist.md`, `references/framework-notes.md` |
| 30 | `leadmagic-cli` | Terminal find/validate/push pipelines | `references/cli-workflow-patterns.md`, `references/framework-notes.md` |
| 31 | `leadmagic-bulk-enrichment` | CSV batch INTAKE → VERIFY → EXPORT | `references/batch-pipeline-spec.md`, `references/framework-notes.md` |
| 32 | `leadmagic-mcp` | Agent tool guardrails, MCP→n8n batch | `references/agent-tool-guardrails.md`, `references/framework-notes.md` |
| 33 | `leadmagic-job-change` | Champion routing, clay-loops L03 | `references/champion-loop-pattern.md`, `references/framework-notes.md` |

**Expert cross-ref:** Pat Spielmann — Cold to Gold → `outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

---

## Category: `gtm-ops/` (automation-adjacent, 5 playbooks)

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 34 | `revops-tech-stack` | Target architecture, consolidation | `templates/stack-audit-scorecard.md`, `templates/target-state-architecture.md` |
| 35 | `gtm-operations` | Operating cadence, RevOps maturity | `templates/operating-cadence-calendar.md` |
| 36 | `gtm-spend-management` | Vendor cards, approvals | `references/ramp-playbook.md`, `templates/vendor-spend-register.md` |
| 37 | `gtm-tool-cost-model` | TCO per automation tool | `templates/tool-cost-sheet.md` |
| 38 | `campaign-governance` | UTM + campaign hierarchy for automation triggers | `templates/utm-parameter-sheet.md` |

---

## Motion Skills (automation consumers)

These skills **consume** automation outputs — pair with toolkits above:

| Motion | Skills | Typical automation stack |
|---|---|---|
| Inbound routing | `inbound-triage`, `landing-pages` | n8n INB-01 → CRM → Slack |
| Outbound enrichment | `lead-enrichment`, `list-building` | leadmagic-waterfall + clay-toolkit |
| Reply handling | `reply-handling` | n8n LIF-03 + ai-prompts-toolkit |
| Signal plays | `funding-signal-play`, `social-intent-monitoring` | clay-loops-toolkit + leadmagic-job-change |
| Lifecycle | `mql-nurture`, `onboarding-sequences` | n8n + hubspot-sequences / sequencing-toolkit |
| Prospecting | `email-finding`, `contact-verification` | leadmagic-toolkit + leadmagic-waterfall |
| Cold email send | `cold-email-strategy`, `cold-email-copywriting` | leadmagic-waterfall → smartlead/instantly/lemlist |
| Champion / job change | `job-change-play`, `expansion-selling` | leadmagic-job-change + clay-loops L03 |

---

## Load Order by Use Case

### New automation build
1. `revops-tech-stack` — inventory
2. `tool-selection-stack` — Clay vs n8n vs MCP
3. `leadmagic-waterfall` + `contact-verification` — data quality
4. Motion toolkit (clay / n8n / prompts)
5. `crm-integration` — sync rules
6. Platform skill (`sequencing-tools/*` or `leadmagic-integrations`)
7. `gtm-metrics` — measure pipeline impact

### Enrichment → sequencer (Pat Spielmann Cold to Gold)
1. `leadmagic-waterfall` OR `clay-toolkit` — Find → Verify → Enrich
2. `cold-email-copywriting` — Hook-Line-Sinker (pat-spielmann-outbound-copy.md)
3. `instantly-sequences` / `smartlead-workflows` / `lemlist-setup` — verify gate + enroll
4. `email-deliverability` — Eric Nowoslawski infra before scale

### Agency → in-house handoff
1. `hiring-agencies` — pilot scorecard
2. `clay-automation` or `n8n-automation` — document workflows
3. `skills-lock` — verify playbook integrity

---

## Cross-References

- GTM Ops index: `gtm-ops/gtm-operations/references/gtm-ops-skill-index.md`
- n8n flow catalog: `tools/n8n-toolkit/references/gtm-flow-catalog.md`
- Clay loop catalog: `tools/clay-loops-toolkit/references/loop-catalog.md`
- Clay LeadMagic waterfall: `tools/clay-loops-toolkit/references/leadmagic-waterfall.md`
- Outbound expert router: `references/gtm-experts-outbound-index.md` (Pat Spielmann, Eric Nowoslawski, Guillaume)
- Pat Spielmann playbook: `outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- Eric Nowoslawski playbook: `outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`
- Automation strategy: `references/gtm-automation-expert-playbook.md` (Jen Igartua — Pattern 30)
- Master router: `foundation/using-gtm-skills` → Pattern 6, 6b, 17, 30

**Total indexed playbooks: 38** (12 automation + 9 tools + 6 sequencing-tools + 6 leadmagic + 5 gtm-ops) + 8 motion consumer skills
