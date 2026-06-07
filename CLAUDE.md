# GTM Blueprints

67 go-to-market skills for AI agents. Install into Claude Code, then ask for anything: build an ICP scorecard, write a cold email sequence, create a battlecard, set up a Clay waterfall, design a pricing model, or plan a product launch.

## Skills Index

See README.md for the full catalog. Skills are organized under `skills/<category>/<skill-name>/SKILL.md`.

## How Skills Work

The agent reads the `name` and `description` from each skill's YAML frontmatter. When your request matches a skill's description, the agent loads the full skill body and follows its instructions.

You don't need to invoke skills by name — just describe what you need and the agent matches the right skill automatically.

## Skill Categories

- **foundation** — GTM context, ICP, positioning, competitive intel, pricing
- **prospecting** — Lead finding, enrichment, email discovery, verification, list building, signals
- **outbound** — Cold email strategy, copywriting, deliverability, domains, sending platforms, replies
- **inbound** — Inbound triage, content marketing, social selling, landing pages
- **sales-revops** — Sales enablement, meeting prep, pipeline, objections, demos, deal desk
- **analytics** — Campaign analytics, deliverability, GTM metrics, A/B testing, attribution, alerts
- **automation** — Clay, AI SDR, API enrichment, CRM, MCP, n8n, waterfall enrichment
- **design** — Pitch decks, one-pagers, battlecards, ROI calculators, case studies, design systems, UI/UX
- **growth** — Churn prevention, expansion, referrals, customer marketing
- **founder-led** — Solo founder GTM, brand, launches, lead magnets, sales team building, metrics
- **leadmagic** — CLI workflows, waterfall enrichment, MCP, integrations, bulk enrichment, job change
