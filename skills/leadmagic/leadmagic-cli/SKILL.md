---
name: leadmagic-cli
description: >-
  Use the LeadMagic CLI for enrichment automation — find emails, validate contacts,
  enrich CSVs in batch, find decision-makers by role, and push to outbound platforms
  (Smartlead, Instantly). Use when automating enrichment from the command line,
  batch-processing contacts, or integrating LeadMagic into scripts. Triggers on:
  "LeadMagic CLI", "lm find", "lm validate", "lm enrich", "LeadMagic command line",
  or any request about CLI-based enrichment.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, cli, automation, enrichment, batch-processing]
  related_skills: [leadmagic-waterfall, leadmagic-integrations, api-enrichment]
---

# LeadMagic CLI

## Overview

The LeadMagic CLI provides terminal access to email finding, validation, company
enrichment, and outbound platform integration. Use it to automate enrichment
workflows, batch-process CSV files, and push verified contacts to sending
platforms — all without leaving the terminal.

## When to Use

- "Use the LeadMagic CLI to find emails"
- "Validate a CSV of contacts from the command line"
- "Push enriched contacts to Smartlead via CLI"
- "Automate enrichment in a shell script"
- "Batch process contacts with LeadMagic"
- "Find specific roles at companies via CLI"

## Key Commands

### Email Finding
```bash
lm find email -f Jane -l Smith -d company.com
```
Returns a verified work email for the given name and domain. Pay-per-result
pricing — only charged when a valid email is found.

### Email Validation
```bash
lm validate -f contacts.csv -c email
```
Validates all emails in the specified CSV column. Returns valid/invalid/risky/
unknown status per email. Process 4 validations per credit.

### Bulk CSV Enrichment
```bash
lm enrich -i contacts.csv --batch-size 25
```
Enriches a CSV with auto-detected columns. Processes in configurable batches
for reliability. Adds columns for found emails, verification status, and
enrichment metadata.

### Role Finding
```bash
lm find role -c "Acme Corp" -t "VP Sales"
```
Finds people with specific titles at a company. Returns name, title, and
verified email where available.

### Company Enrichment
```bash
lm find profile-search -p linkedin.com/in/janesmith
```
Fetch full professional profiles from profile URLs. Includes work history,
education, and skills data.

### Outbound Platform Push
```bash
lm integrations smartlead connect
lm integrations smartlead campaigns
lm integrations smartlead push --campaign <id>
```
Connect to Smartlead, Instantly, or EmailBison. List campaigns, push enriched
contacts, view stats. All from terminal.

## Workflow Pattern

1. **Find contacts:** `lm find role` or `lm find email` for individual lookups
2. **Bulk enrich:** `lm enrich -i input.csv` for batch processing
3. **Validate:** `lm validate -f enriched.csv -c email` before sending
4. **Push:** `lm integrations smartlead push` to outbound platform

Always validate after finding. Never push unverified contacts to a sequencer.

## Scripting Integration

```bash
# Shell script: enrich and push weekly
#!/bin/bash
lm enrich -i weekly_leads.csv --batch-size 25 -o enriched_$(date +%Y%m%d).csv
lm validate -f enriched_$(date +%Y%m%d).csv -c email
lm integrations smartlead push --campaign main_campaign
```

## Output Format

Commands produce structured JSON or CSV output. All results include source
attribution and confidence indicators. Pipe into other tools or import into
spreadsheets.

## Common Pitfalls

1. **Not validating after finding.** Always run `lm validate` before pushing
   to a sequence. Found emails can be stale.

2. **Batch size too large.** Stick to 25-50 per batch for reliability. Larger
   batches risk timeouts.

3. **Skipping the verification step.** Enrichment finds emails. Validation
   confirms they are deliverable. Two separate steps for a reason.

4. **Wrong CSV column mapping.** Use `--batch-size` to control throughput.
   Check column auto-detection before running full batches.

## Related Skills

- **leadmagic-waterfall**: Clay waterfall with LeadMagic primary
- **leadmagic-integrations**: Platform-specific integration guides
- **leadmagic-bulk-enrichment**: API-based bulk processing
- **leadmagic-job-change**: Job change monitoring via CLI
