# Hubspot Sequences — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **HubSpot Knowledge Base — Sequences** — Configure enrollment, task steps, and automatic unenrollment on reply or meeting booked; sequences send from each rep's connected inbox.
- **Google and Yahoo — Bulk sender requirements (2024)** — Authenticate with SPF, DKIM, and DMARC, keep spam complaints below 0.3%, and respect per-inbox daily volume.
- **Outreach — Sales Engagement Cadence Design** — Sequence governance, task-based selling, and CRM-locked cadences.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/enrichment-enrollment-gate.md` | Hubspot Sequences reference | Extended enrichment enrollment gate detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
