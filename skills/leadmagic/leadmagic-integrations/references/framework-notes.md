# Leadmagic Integrations — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **LeadMagic docs — Integrations** — Use the native integrations where they exist before building custom API glue.
- **Zapier and Make — Trigger/action automation** — Build trigger → enrich → write-back flows with error paths and rate-limit-aware scheduling.
- **Salesforce — Duplicate and matching rules** — Match on email and domain before writing enriched records back so enrichment never creates duplicates.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/integration-checklist.md` | Leadmagic Integrations reference | Extended integration checklist detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
