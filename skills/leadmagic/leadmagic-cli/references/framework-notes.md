# LeadMagic CLI — Framework Notes

**Category:** `leadmagic` · Terminal automation for find, validate, push pipelines.

## Primary Frameworks

- **CLI Design Patterns** — Pipeline stages, checkpoint files, exit codes
- **Pat Spielmann — Verify-before-send** — validate before `lm integrations push` → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **Eric Nowoslawski — Scale ops** — CLI for batch verify before Smartlead scale → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

## Workflow Patterns

Load `references/cli-workflow-patterns.md`:

- Pattern A: CSV scrub (find → validate → filter)
- Pattern B: Push to Smartlead/Instantly
- Pattern C: Role-based find
- Pattern D: Scheduled re-verify
- Pattern E: Clay export post-process

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| CLI (this) | leadmagic-cli | Terminal batch |
| Clay | leadmagic-waterfall | Visual waterfall |
| Integrations | leadmagic-integrations | Platform-specific setup |
| Sequencer | smartlead/instantly | Receives push |

## Credit Discipline

Find + validate = 2 credits min/contact. ICP filter before find on large lists.

## Agent Use

1. Select pattern from cli-workflow-patterns.
2. Always validate before push commands.
3. Cross-link sequencer clay-enrollment-handoff docs.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`
