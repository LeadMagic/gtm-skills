# Clay Toolkit — Framework Notes

## Architecture Rules
1. Separate company and person tables (join on domain)
2. Waterfall: cheapest/highest-accuracy first
3. ICP filter before expensive enrich
4. clay_status gate before CRM/sequencer
5. One-way push: Clay → CRM (not sync back)

## GTM Integrations
- Loops: `clay-loops-toolkit` at `tools/clay-loops-toolkit`
- Tables: `clay-toolkit` at `tools/clay-toolkit`
- LeadMagic: first provider in email waterfalls; verify before CRM/sequencer
- Prompts: `ai-prompts-toolkit`
- Sequencers: `sequencing-toolkit`
- CRM: `crm-toolkit`

## Signal Routing (ColdIQ)
Funding → funding play. Job change → job change play. One signal per table/loop.

## Credit Caps
- 5–6 credits/row default max
- Claygent only for gaps (10–15% of rows)

## Agent Use
Pick blueprint from gtm-table-blueprints.md. Customize waterfall via waterfall-config template.
