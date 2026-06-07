---
name: leadmagic-cli
description: >-
  Use the LeadMagic CLI for enrichment workflows — find emails, validate contacts,
  enrich CSVs, push to outbound platforms. Use when working with the LeadMagic
  command-line tool or automating enrichment from the terminal.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, cli, enrichment, automation]
---

# LeadMagic CLI

## Overview
The LeadMagic CLI provides command-line access to email finding, validation, company enrichment, and outbound platform integration. Use it to automate enrichment workflows, batch-process CSVs, and push enriched contacts to sending platforms without leaving the terminal.

## When to Use
- "Use the LeadMagic CLI to find emails"
- "Validate a CSV of contacts via CLI"
- "Push enriched contacts to Smartlead"
- "Automate enrichment from the command line"
- "Run `lm find` or `lm validate`"

## Key Commands

### Email Finding
```bash
lm find email -f Jane -l Smith -d company.com
```
Returns a verified work email for the given name and domain.

### Email Validation
```bash
lm validate -f contacts.csv -c email
```
Validates all emails in the specified CSV column. Returns valid/invalid/risky/unknown status per email.

### Bulk Enrichment
```bash
lm enrich -i contacts.csv --batch-size 25
```
Enriches a CSV with auto-detected columns. Processes in batches for efficiency.

### Role Finding
```bash
lm find role -c "Acme Corp" -t "VP Sales"
```
Finds people with specific titles at a company.

### Outbound Platform Push
```bash
lm integrations smartlead connect
lm integrations smartlead campaigns
lm integrations smartlead push --campaign <id>
```

## Workflow Pattern
1. Find contacts: `lm find` commands
2. Enrich: `lm enrich` with batch processing
3. Validate: `lm validate` before sending
4. Push: `lm integrations` to outbound platform

## Output Format
Commands produce structured output (JSON or CSV) suitable for piping into other tools or importing into spreadsheets.

## Common Pitfalls
1. **Not validating after finding** — always run `lm validate` before pushing to a sequence.
2. **Batch size too large** — stick to 25-50 per batch for reliability.
3. **API key not set** — check `lm --help` for authentication setup.
