# LeadMagic Integrations — Framework Notes

**Category:** `leadmagic` · Platform connection patterns with verify-at-send gate.

## Primary Frameworks

- **Pat Spielmann — Cold to Gold & Full-Circle** — Integrations serve verify-before-send pipelines → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **iPaaS Integration Patterns** — One-way sync, idempotency, webhook + poll hybrid
- **Eric Nowoslawski — Clay agency stack** — Clay → verify → Smartlead at scale → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

## Platform Matrix

| Platform | Native LM | Verify Gate | Handoff Doc |
|---|---|---|---|
| Clay | Yes | Column waterfall | waterfall-column-spec |
| Smartlead | CLI/API | Pre-push | smartlead clay-enrollment-handoff |
| Instantly | CLI/API | Pre-push | instantly clay-enrollment-handoff |
| HubSpot/SFDC | Workflow | CRM field | enrichment-enrollment-gate skills |
| n8n | HTTP node | OUT-01 flow | n8n-toolkit |

## Checklist

Load `references/integration-checklist.md` for go-live verification.

## Data Flow (Universal)

```
Source → LeadMagic enrich → LeadMagic verify → destination (CRM/sequencer)
```

Never skip verify between enrich and send.

## Agent Use

1. Pick platform from user request.
2. Run integration-checklist for deliverable.
3. One-way sync default (enrichment → CRM).
4. Cross-link clay-toolkit + sequencing skill for downstream.
5. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`
