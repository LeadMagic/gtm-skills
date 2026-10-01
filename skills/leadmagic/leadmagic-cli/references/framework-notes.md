# Leadmagic Cli — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **LeadMagic docs — CLI installation and commands** — Install lm-tui, authenticate with `lm login` (browser OAuth), and check `lm --help` rather than pasting API keys into config.
- **LeadMagic docs — Credits** — Check the credit balance and estimate cost before bulk runs; failed lookups and credit rules are documented per endpoint.
- **Command Line Interface Guidelines (clig.dev)** — Prefer machine-readable output, meaningful exit codes, and non-interactive flags when scripting the CLI in pipelines.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/cli-workflow-patterns.md` | Leadmagic Cli reference | Extended cli workflow patterns detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.
