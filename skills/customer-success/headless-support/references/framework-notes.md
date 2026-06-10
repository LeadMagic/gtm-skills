# Headless Support — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Plain — API-first headless support and BYOAI via MCP** — composable stack with Attio + agent IDE; see `byoai-headless-stack.md`
- **Intercom — Fin AI Agent** — vendor-locked AI when CS lives in Messenger
- **Amazon — Working Backwards** — deflection reduces cost and improves CSAT

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **Plain — API-first headless support and BYOAI via MCP.** Use for embedded portals and Cursor/Claude thread triage — see `byoai-headless-stack.md`.
- **Intercom — Fin AI Agent and Resolution Bot.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Zendesk — AI Agents and Answer Bot.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Ada — Conversational AI for Support.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Forethought — AI-First Customer Support.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Amazon — Working Backwards (deflection reduces cost and improves CSAT).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## Process phases

- Phase 1 — Knowledge base architecture (30+ articles)
- Phase 2 — AI deployment (Path A: vendor AI / Path B: Plain BYOAI + MCP)
- Phase 3 — In-product self-serve (Level 0 deflection)
- Phase 4 — Automated triage and routing
- Phase 5 — Deflection metrics dashboard

## Key reference tables

| Category | Articles | Examples |
|---|---|---|
| Getting Started | 5-10 | Account setup, team invites, first campaign |
| Core Features | 15-20 | Step-by-step guides for every major feature |
| Billing & Account | 5-8 | Plans, invoices, upgrade/downgrade, cancel |
| Troubleshooting | 10-15 | Common errors, workarounds, fixes |
| Integrations | 5-10 | Setup guides for each integration |
| Best Practices | 5-8 | Pro tips, workflows, customer examples |
| FAQ | 10-15 | Short answers to most common questions |

| Surface | Method | Example |
|---|---|---|
| Empty states | Explain what goes here + link to setup guide | "No campaigns yet. Start your first →" |
| Hover tooltips | 1-sentence explanation of each field | "Bounce rate: % of emails that couldn't be delivered" |
| Feature announcement | In-app modal with 3-step walkthrough | "New: Auto-rotate mailboxes. Here's how →" |
| Error messages | What happened + how to fix + link to article | "Domain not verified. 2-min fix →" |
| Setup wizard | Step-by-step onboarding flow | 1. Connect inbox 2. Add team 3. Send first campaign |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
