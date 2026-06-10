# LeadMagic Integration Checklist

Platform-by-platform verification gate before go-live. Pat Spielmann rule: **enrich → verify → send**.

## Universal Pre-Flight

- [ ] LeadMagic API key in env/secret store (never committed)
- [ ] Verify endpoint fires before any sequencer/CRM send automation
- [ ] `lm_email_status` (or equivalent) field exists in destination system
- [ ] Suppression list synced (customers, unsub, competitors)
- [ ] Test batch: 50 rows end-to-end with status logging

Cross-ref Pat stack: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Clay

- [ ] Native LeadMagic integration (not raw HTTP) for credit billing
- [ ] Waterfall: LM Find → fallbacks → LM Verify → Enrich
- [ ] Conditional run on fallbacks (empty previous only)
- [ ] COALESCE + email_valid formula columns
- [ ] Sequencer push gated on email_valid
- [ ] Load: leadmagic-waterfall/references/waterfall-column-spec.md

## Smartlead / Instantly

- [ ] Verify via LM before push (`lm integrations push` or Clay gate)
- [ ] Custom variables mapped: why_now, verify_status, signal_url
- [ ] Duplicate detection enabled in sequencer
- [ ] Clay handoff doc loaded for platform
- [ ] Eric infra: secondary domains, warmup complete

## Salesforce / HubSpot

- [ ] One-way sync: enrichment → CRM (not bidirectional on email)
- [ ] Workflow: stale email (>90d) → re-verify
- [ ] Custom fields: lm_email_status, last_verified, personalization_snippet
- [ ] Sequence enrollment rule checks lm_email_status = valid
- [ ] Pair: hubspot-setup or salesforce-setup for workflow limits

## Zapier / Make / n8n

- [ ] Idempotent webhook (dedupe by email + CRM ID)
- [ ] Error branch: verify fail → Slack alert, not silent drop
- [ ] Batch size ≤500 for rate limits
- [ ] n8n: use OUT-01 pattern from n8n-toolkit

## MCP Agent Path

- [ ] Agent read-only for lookup; confirm gate for CRM write
- [ ] Batch calls for lists (not per-row in chat loop)
- [ ] Pair: leadmagic-mcp + mcp-setup

## Post-Launch Monitoring

| Metric | Threshold | Action |
|---|---|---|
| Bounce rate | >3% | Pause send, audit verify gate |
| Invalid rate post-verify | >5% | Re-order waterfall providers |
| CRM sync conflicts | any | Switch to one-way push |

Expert router: `references/gtm-experts-outbound-index.md` (Pat = data/copy, Eric = infra scale)
