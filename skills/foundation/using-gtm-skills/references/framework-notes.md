# Using Gtm Skills — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **LeadMagic/gtm-skills — master router.** Category tables, skill maps, and subsidiary index links in `SKILL.md`.
- **references/pitfalls-index.md** — Auto-generated aggregator of every skill's `## Common Pitfalls` section.
- **references/experts.md** — Named practitioner catalog with public channels.

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **LeadMagic/gtm-skills — the full GTM Skills catalog.** Skill maps in this guide route tasks to the right playbook.
- **Jacco van der Kooij (Winning by Design).** SPICED discovery, Bowtie lifecycle, GTM Index, REKS coaching — primary WbD cite.
- **Sam Jacobs (Pavilion).** CRO Council exec comp; multi-gate variable (ARR + NRR + efficiency).
- **Mark Roberge — The Sales Acceleration Formula.** Data-driven hiring, training, demand gen, and sales process design — the science behind scaling a B2B sales org.
- **Jason Lemkin & Mark Roberge — From Survival to Thrival.** Two-phase SaaS GTM: Survival ($0–$2M ARR, founder sells) → Thrival ($2M–$10M+, build the machine) → enterprise upmarket motion.
- **April Dunford — Obviously Awesome Positioning.** Positioning before messaging and channel selection.
- **Winning by Design — GTM Operating Model.** SPICED, Bowtie, POD structures, and revenue architecture.

## Key reference tables

| If You Need To... | Load These Categories |
|---|---|
| **Raise money, manage equity, run a board** | `founder-led/` (fundraising-strategy, financial-modeling, board-meeting-prep, equity-management) |
| **Sell as a founder or build a sales team** | `founder-led/` (founder-sales, sales-team-building), `sales-revops/` (sales-enablement, pipeline-management, demo-scripts, deal-desk) |
| **Enterprise sales / upmarket motion** | `foundation/` (icp-targeting-tiers, gtm-context), `abm/` (abm-strategy, multi-thread-orchestration), `sales-revops/` (meeting-prep, deal-desk, roi-calculator), `founder-led/` (soc2-compliance) |
| **Mark Roberge / Survival to Thrival journey** | See skill maps below — routes by ARR stage and motion |
| **Build outbound / cold email** | `outbound/` (cold-email-strategy, cold-email-copywriting, email-deliverability, domain-infrastructure) |
| **Find and enrich leads** | `prospecting/` (lead-finding, lead-enrichment, email-finding, contact-verification) |
| **Automate GTM workflows** | `automation/` (clay-automation, n8n-automation, mcp-setup, waterfall-enrichment) + `tools/` (clay-toolkit, clay-loops-toolkit, ai-prompts-toolkit, n8n-toolkit) |
| **n8n flows (inbound/outbound/signals)** | `tools/n8n-toolkit` (flow catalog, MCP patterns) → motion skill (`inbound-triage`, `reply-handling`, signal plays) |
| **Clay + AI prompts (tools)** | `tools/clay-toolkit`, `tools/clay-loops-toolkit`, `tools/ai-prompts-toolkit`, `tools/sequencing-toolkit` |
| **Content, social, creative** | `creative/` (vibe-marketing, ai-content-creation, copywriting, social-media-strategy), `content-seo/` |
| **Customer success and support** | `customer-success/` (cs-playbooks, customer-onboarding, sla-management, headless-support) |
| **Analytics and metrics** | `analytics/` (gtm-metrics, event-analytics, campaign-analytics, attribution) |
| **AI-native GTM (vibe coding/marketing)** | `creative/` (vibe-coding, vibe-marketing, v0-lander, ai-content-creation, ai-video-creation) |
| **Legal, compliance, security** | `founder-led/` (legal-for-founders, soc2-compliance, data-privacy-compliance, security-assessments, business-insurance) |
| **Hiring and team building** | `founder-led/` (gtm-role-descriptions, gtm-recruiting, job-posting-strategy, hiring-by-role, sales-team-building) + `management-leadership/gtm-leadership` |
| **GTM leadership (hire/fire/hard talks)** | `management-leadership/gtm-leadership`, `gtm-role-descriptions` (comp templates), `employment-compliance` |
| **Buyer indecision / stuck deals** | `sales-revops/buyer-indecision` (JOLT), `pipeline-management`, `deal-desk` |
| **Sales process design (Winning by Design)** | See WbD skill map below — `pipeline-management` is the anchor |
| **Outsource GTM / work with agencies** | `founder-led/` (hiring-agencies, hiring-contractors), `automation/` (clay-automation) |
| **Design and brand** | `design/` (pitch-deck-builder, roi-calculator, design-system-gtm, brand-kit) |

| WbD Component | What It Covers | Load These Skills |
|---|---|---|
| **GTM Index (6 models)** | Revenue, Data, Math, Operating, Growth, GTM — score 1–10 | `gtm-system-architecture`, `gtm-metrics` |
| **GTM Playbook Kit** | Goal + Actions + Exit Criteria per stage | `pipeline-management` (anchor) |
| **SPICED** | Situation, Pain, Impact, Critical Event, Decision (discovery) | `pipeline-management`, `meeting-prep`, `founder-sales` |
| **MEDDICC** | Metrics, EB, Decision Criteria/Process, Pain, Champion, Competition (deal scoring) | `pipeline-management`, `meeting-prep`, `sales-coaching`, `multi-thread-orchestration` |
| **Bowtie** | Acquire → retain → expand (revenue doesn't end at Closed Won) | `gtm-system-architecture`, `customer-onboarding`, `expansion-selling` |
| **POD structures** | SDR:AE:CSM ratios by complexity | `sales-team-building` |
| **REKS coaching** | Results → Efforts → Knowledge → Skills | `sales-coaching`, `sales-team-building` |
| **Enablement layer** | Playbook, battlecards, talk tracks per stage | `sales-enablement`, `demo-scripts`, `objection-handling` |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
