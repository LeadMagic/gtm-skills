<!-- AUTO-GENERATED shared reference: references/automation-playbook-index.md; run npm run regenerate. -->

# Automation Playbook Index

Master index of **every** GTM automation skill and toolkit playbook. Load `using-gtm-skills` Pattern 6 / 6b / 17 for orchestration order.

**Rule:** Process skills (`automation/`) define *when and why*. Tool skills (`tools/`, `leadmagic/`) define *how to configure*. Never skip data quality (`waterfall-enrichment`, `contact-verification`, `leadmagic-waterfall`) before routing automation.

---

## Category: `automation/` (12 playbooks)

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 1 | `clay-automation` | Clay rollout, table governance, enrichment QA | `skills/automation/clay-automation/references/framework-notes.md`, `skills/automation/clay-automation/templates/output-template.md` |
| 2 | `n8n-automation` | n8n vs Clay vs MCP decision, error handling | `skills/automation/n8n-automation/references/framework-notes.md`, `skills/automation/n8n-automation/references/gtm-flow-catalog.md` |
| 3 | `mcp-setup` | MCP agents → approved batch jobs | `skills/automation/mcp-setup/references/framework-notes.md` |
| 4 | `waterfall-enrichment` | Provider order, match rates, cost caps | `skills/automation/waterfall-enrichment/references/framework-notes.md` |
| 5 | `api-enrichment` | Direct API enrichment pipelines | `skills/automation/api-enrichment/references/framework-notes.md` |
| 6 | `crm-integration` | Sync rules, field mapping, conflict resolution | `skills/automation/crm-integration/references/framework-notes.md` |
| 7 | `ai-sdr-setup` | AI SDR guardrails, human-in-loop | `skills/automation/ai-sdr-setup/references/framework-notes.md`, `skills/outbound/cold-email-strategy/references/justin-michael-sales-borg.md` |
| 8 | `salesforce-setup` | SFDC automation objects, flows | `skills/automation/salesforce-setup/references/framework-notes.md` |
| 9 | `hubspot-setup` | HubSpot workflows, lifecycle | `skills/automation/hubspot-setup/references/framework-notes.md` |
| 10 | `attio-setup` | Attio automation patterns | `skills/automation/attio-setup/references/framework-notes.md` |
| 11 | `tool-selection-stack` | Build vs buy, stack consolidation | `skills/automation/tool-selection-stack/references/framework-notes.md` |
| 12 | `skills-lock` | Skill integrity verification | `skills/automation/skills-lock/references/framework-notes.md` |

---

## Category: `tools/` (15 playbooks — 9 toolkits + 6 sequencer platforms)

Cross-platform toolkits and platform-specific sequencer skills live in the same category. Use `sequencing-toolkit` for architecture and comparison; use a platform skill (`instantly-sequences`, `smartlead-workflows`, etc.) for deep setup. Upstream with `leadmagic-waterfall` + `clay-toolkit` before enrollment.

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 13 | `clay-toolkit` | Table blueprints, waterfall columns | `skills/tools/clay-toolkit/references/gtm-table-blueprints.md`, `skills/tools/clay-toolkit/templates/waterfall-config.md` |
| 14 | `clay-loops-toolkit` | Signal loops (funding, hiring, job change) | `skills/tools/clay-loops-toolkit/references/loop-catalog.md`, `skills/tools/clay-loops-toolkit/references/leadmagic-waterfall.md`, `skills/tools/clay-loops-toolkit/templates/loop-blueprint.md` |
| 15 | `n8n-toolkit` | Flow IDs: INB / OUT / SIG / LIF / REV / MCP | `skills/tools/n8n-toolkit/references/gtm-flow-catalog.md`, `skills/tools/n8n-toolkit/templates/workflow-blueprint.md` |
| 16 | `ai-prompts-toolkit` | Claygent / LLM prompt loops P01–P10 | `skills/tools/ai-prompts-toolkit/references/prompt-library.md`, `skills/tools/ai-prompts-toolkit/templates/prompt-spec.md` |
| 17 | `sequencing-toolkit` | Multi-channel sequence architecture (router) | `skills/tools/sequencing-toolkit/references/platform-comparison.md`, `skills/tools/sequencing-toolkit/templates/sequence-architecture.md` |
| 18 | `crm-toolkit` | CRM selection, blueprints, land-expand | `skills/tools/crm-toolkit/references/salesforce-blueprint.md`, `skills/tools/crm-toolkit/references/hubspot-blueprint.md` |
| 19 | `leadmagic-toolkit` | Find → Verify → Enrich column patterns | `skills/tools/leadmagic-toolkit/references/framework-notes.md` |
| 20 | `analytics-toolkit` | Stack by stage, event taxonomy | `skills/tools/analytics-toolkit/references/analytics-stack-by-stage.md` |
| 21 | `support-toolkit` | Headless support automation | `skills/tools/support-toolkit/references/platform-comparison.md` |
| 22 | `instantly-sequences` | Warmup pool, rotation, unified inbox | `skills/tools/instantly-sequences/references/clay-enrollment-handoff.md`, `skills/tools/instantly-sequences/references/framework-notes.md` |
| 23 | `smartlead-workflows` | Unlimited mailboxes, AI reply labels, Eric-scale infra | `skills/tools/smartlead-workflows/references/clay-enrollment-handoff.md`, `skills/tools/smartlead-workflows/references/framework-notes.md` |
| 24 | `lemlist-setup` | lemwarm, Guillaume multichannel, personalization | `skills/tools/lemlist-setup/references/clay-enrollment-handoff.md`, `skills/tools/lemlist-setup/references/framework-notes.md` |
| 25 | `salesloft-cadences` | Rhythm cadences, CRM verify gate | `skills/tools/salesloft-cadences/references/enrichment-enrollment-gate.md`, `skills/tools/salesloft-cadences/references/framework-notes.md` |
| 26 | `outreach-sequences` | Enterprise triggers, Clay→CRM→Outreach | `skills/tools/outreach-sequences/references/enrichment-enrollment-gate.md`, `skills/tools/outreach-sequences/references/framework-notes.md` |
| 27 | `hubspot-sequences` | Workflow enrollment, rep-triggered sequences | `skills/tools/hubspot-sequences/references/enrichment-enrollment-gate.md`, `skills/tools/hubspot-sequences/references/framework-notes.md` |

**Expert cross-refs:** Eric Nowoslawski (infra scale — Smartlead/Instantly) · Pat Spielmann (verify-before-send) · Guillaume Moubeche (lemlist) → `https://github.com/LeadMagic/gtm-skills/blob/main/references/gtm-experts-outbound-index.md`

---

## Category: `leadmagic/` (6 playbooks)

LeadMagic-specific enrichment, integration, and agent tooling. Default upstream provider for `clay-toolkit` and `clay-loops-toolkit`.

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 28 | `leadmagic-waterfall` | Clay waterfall: Find → Verify → Enrich | `skills/leadmagic/leadmagic-waterfall/references/waterfall-column-spec.md`, `skills/leadmagic/leadmagic-waterfall/references/framework-notes.md` |
| 29 | `leadmagic-integrations` | Clay, CRM, sequencer, n8n connections | `skills/leadmagic/leadmagic-integrations/references/integration-checklist.md`, `skills/leadmagic/leadmagic-integrations/references/framework-notes.md` |
| 30 | `leadmagic-cli` | Terminal find/validate/push pipelines | `skills/leadmagic/leadmagic-cli/references/cli-workflow-patterns.md`, `skills/leadmagic/leadmagic-cli/references/framework-notes.md` |
| 31 | `leadmagic-bulk-enrichment` | CSV batch INTAKE → VERIFY → EXPORT | `skills/leadmagic/leadmagic-bulk-enrichment/references/batch-pipeline-spec.md`, `skills/leadmagic/leadmagic-bulk-enrichment/references/framework-notes.md` |
| 32 | `leadmagic-mcp` | Agent tool guardrails, MCP→n8n batch | `skills/leadmagic/leadmagic-mcp/references/agent-tool-guardrails.md`, `skills/leadmagic/leadmagic-mcp/references/framework-notes.md` |
| 33 | `leadmagic-job-change` | Champion routing, clay-loops L03 | `skills/leadmagic/leadmagic-job-change/references/champion-loop-pattern.md`, `skills/leadmagic/leadmagic-job-change/references/framework-notes.md` |

**Expert cross-ref:** Pat Spielmann — Cold to Gold → `outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

---

## Category: `gtm-ops/` (automation-adjacent, 5 playbooks)

| # | Skill | Playbook focus | Key artifacts |
|---|---|---|---|
| 34 | `revops-tech-stack` | Target architecture, consolidation | `skills/gtm-ops/revops-tech-stack/templates/stack-audit-scorecard.md`, `skills/gtm-ops/revops-tech-stack/templates/target-state-architecture.md` |
| 35 | `gtm-operations` | Operating cadence, RevOps maturity | `skills/gtm-ops/gtm-operations/templates/operating-cadence-calendar.md` |
| 36 | `gtm-spend-management` | Vendor cards, approvals | `skills/gtm-ops/gtm-spend-management/references/ramp-playbook.md`, `skills/gtm-ops/gtm-spend-management/templates/vendor-spend-register.md` |
| 37 | `gtm-tool-cost-model` | TCO per automation tool | `skills/gtm-ops/gtm-tool-cost-model/templates/tool-cost-sheet.md` |
| 38 | `campaign-governance` | UTM + campaign hierarchy for automation triggers | `skills/gtm-ops/campaign-governance/templates/utm-parameter-sheet.md` |

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
6. Platform skill (`tools/instantly-sequences`, `tools/smartlead-workflows`, etc., or `leadmagic-integrations`)
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
- Outbound expert router: `https://github.com/LeadMagic/gtm-skills/blob/main/references/gtm-experts-outbound-index.md` (Pat Spielmann, Eric Nowoslawski, Guillaume)
- Pat Spielmann playbook: `outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- Eric Nowoslawski playbook: `outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`
- Automation strategy: `https://github.com/LeadMagic/gtm-skills/blob/main/references/gtm-automation-expert-playbook.md` (Jen Igartua — Pattern 30)
- Master router: `foundation/using-gtm-skills` → Pattern 6, 6b, 17, 30

**Total indexed playbooks: 38** (12 automation + 15 tools + 6 leadmagic + 5 gtm-ops) + 8 motion consumer skills
