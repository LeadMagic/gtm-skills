# LeadMagic CLI — Workflow Patterns

Use the [current command reference](https://leadmagic.io/docs/cli/commands) and `lm --help` to check installed command syntax. Authenticate with `lm login` (OAuth), not a committed API key.

## Pattern A: Inspect a CSV before enrichment

```bash
lm enrich -i contacts.csv --dry-run
```

Check column mapping and the planned operations, estimate cost, and obtain authorization before removing `--dry-run`.

## Pattern B: Find a missing work email

```bash
lm find email -f "Jane" -l "Smith" -d example.com
```

This is a placeholder input, not a live customer fixture. Use authorized real inputs for a paid request. A returned Email Finder address is already validated; do not chain it into validation.

## Pattern C: Validate externally sourced email

```bash
lm validate -f external-contacts.csv -c email
```

Use this for CRM exports and other external sources. Preserve consent, suppression, and provenance when selecting the final audience.

## Pattern D: Refresh stale CRM addresses

Select stale records using the CRM's verification timestamp, export only the selected rows, and run validation. Merge the result by a stable record ID; never clear opt-outs or overwrite a good address with a null result.

## Pattern E: Sequencer handoff

Review the cleaned output, campaign identifier, and authorization to send. Run `lm integrations --help` and the selected provider's help for current connect and push flags. Do not invent `lm filter`, `lm find-roles`, or unsupported `--input` options.

## Error Handling

| Error | Action |
| --- | --- |
| Rate limit | Back off; respect shared account rate limits |
| Expired session | Reauthenticate with `lm login`; never log tokens |
| Partial job failure | Inspect failed rows before replaying paid work |
| Empty finder result | Mark unresolved; do not guess an address |

## Credit Discipline

Email Finder costs 1 credit for a found result; Email Validation costs 0.25 credits per validation. They are separate workflows, not a mandatory combined charge. Confirm [current pricing](https://leadmagic.io/docs/v1/credits) and account entitlement before running a large list.
