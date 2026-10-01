# Instantly Sequences — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **Instantly Help Center** — Connect sending accounts, enable warmup, and set per-account daily limits and campaign schedules before launch.
- **Eric Nowoslawski — Cold email infrastructure** — Cold email infra at scale — 2 inboxes/domain, backup inboxes, Creative Ideas testing.
- **Google and Yahoo — Bulk sender requirements (2024)** — Authenticate with SPF, DKIM, and DMARC, keep spam complaints below 0.3%, and honor unsubscribes quickly.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/clay-enrollment-handoff.md` | Instantly Sequences reference | Extended clay enrollment handoff detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
