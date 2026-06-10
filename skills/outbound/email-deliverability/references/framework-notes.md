# Email Deliverability — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/bounce-complaint-procedures.md` | Google Bulk Sender Guidelines | Bounce/complaint handling |
| `references/deliverability-primer.md` | Operator primer | SPF/DKIM/DMARC fundamentals |
| `references/output-artifacts.md` | Skill tables | Authentication audit fields |
| `references/sending-limits-reference.md` | Provider docs | Per-mailbox and per-domain limits |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
