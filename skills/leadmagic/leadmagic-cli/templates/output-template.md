# LeadMagic CLI Workflow Deliverable

## Context
- Input file:
- Target action: find / validate / push
- Destination platform:

## Framework Basis
- Pat Spielmann — validate before push
- CLI pipeline patterns

## Selected Pattern
- [ ] A: CSV scrub (find → validate → filter)
- [ ] B: Push to sequencer
- [ ] C: Role-based find
- [ ] D: Scheduled re-verify
- [ ] E: Clay export post-process

Spec: `references/cli-workflow-patterns.md`

## Command Sequence
```bash
# Document actual commands
```

## Output Files
| Stage | File | Row Count |
|---|---|---:|
| Input |  |  |
| Verified |  |  |
| Send-ready |  |  |

## Verify Gate
- [ ] Every send-ready row has verify_status = valid
- [ ] Invalid rows suppressed

## Quality Check
- [ ] ICP filter before find (large lists)
- [ ] Sequencer handoff doc cross-referenced
- [ ] Error handling documented
