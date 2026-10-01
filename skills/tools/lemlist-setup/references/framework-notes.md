# Lemlist Setup — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **lemlist Help Center** — Build multichannel sequences (email, LinkedIn, calls) with conditions, and use lemwarm and custom tracking domains before sending.
- **Guillaume Moubeche — lemlist outbound** — Multichannel sequences — email, LinkedIn, calls in one enrollment; personalization should earn the reply, not decorate the email.
- **Google and Yahoo — Bulk sender requirements (2024)** — Authenticate with SPF, DKIM, and DMARC, keep spam complaints below 0.3%, and honor unsubscribes quickly.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/clay-enrollment-handoff.md` | Lemlist Setup reference | Extended clay enrollment handoff detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
