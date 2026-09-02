# Skills Lock Integrity Report

## Context

- Repository: `[owner/repository]`
- Revision: `[commit or release]`
- Scope: `[skills directory and exclusions]`
- Checked at: `[ISO-8601 timestamp]`

## Framework Basis

- Agent Skills packaging rule: `[how self-contained artifacts are discovered]`
- Digest standard: `[algorithm and reference]`
- Reproducibility rule: `[sorting and volatile-field policy]`

## Recommendation

`[Pass, fail, or remediation recommendation with the reason]`

## Artifact Inventory

| Kind | Exact count |
|---|---:|
| Skill entrypoints | `[count]` |
| References | `[count]` |
| Templates | `[count]` |
| Scripts | `[count]` |
| Assets | `[count]` |
| Other | `[count]` |
| Total packaged files | `[count]` |

## Implementation Steps

1. `[Generate or repair the complete manifest]`
2. `[Verify path-set, size, and hash equality]`
3. `[Add or update the CI drift gate]`

## Metrics

- Discoverable skills: `[count]`
- Locked packaged files: `[count]`
- Missing records: `[count]`
- Extra records: `[count]`
- Hash or size mismatches: `[count]`

## Failures and Residual Risks

- `[Failure, exclusion, or security boundary]`

## Quality Check

- [ ] Every packaged path is represented exactly once.
- [ ] Counts were derived from disk.
- [ ] Hashes and byte sizes were verified.
- [ ] No-op regeneration is stable.
- [ ] Integrity is not presented as proof of trust.
