# Sla Management — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- ****

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **ITIL 4 — Service Level Management practice.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Zendesk — SLA Policy Design Guide.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Intercom — SLA and Business Hours Configuration.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **HDI — Support Center Certification Standards.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4
- Phase 5

## Key reference tables

| Priority | Definition | Examples | FRT | Resolution |
|---|---|---|---|---|
| **P1 — Critical** | System down, security incident, data loss, revenue blocked | Can't log in, billing failed for all users, API down | 15 min | 2 hours |
| **P2 — High** | Major feature broken, workflow blocked, no workaround | Export failing, campaign can't send, integration down | 1 hour | 8 hours |
| **P3 — Normal** | Question, minor bug, configuration help, workaround exists | "How do I set up X?", report looks wrong | 4 hours | 24 hours |
| **P4 — Low** | Feature request, cosmetic bug, nice-to-have | "Add dark mode", typo on page | 8 hours | 5 days or "Deferred" |

| Plan | P1 FRT | P2 FRT | P3 FRT | Channels | Dedicated CSM |
|---|---|---|---|---|---|
| **Free** | Best-effort | Best-effort | 24 hours | Email, KB | No |
| **Starter** | 1 hour | 4 hours | 8 hours | Email, Chat | No |
| **Growth** | 30 min | 2 hours | 4 hours | Email, Chat, Phone | No |
| **Enterprise** | 15 min | 1 hour | 2 hours | All + Slack | Yes |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
