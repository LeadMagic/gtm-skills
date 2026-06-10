# Inbound Triage — Deliverable

## Deliverable spec

Inbound triage workflow diagram + SLA document:
```
# Inbound Triage Workflow

Form Fill → Enrich (15s) → ICP Filter → Score → Route → SLA Enforcement

Routing rules:
- Demo request + ICP fit → AE calendar hold (5 min)
- MQL + score >60 → SDR (15 min)
- MQL + score 40-60 → Nurture track
- Non-ICP → Marketing nurture
- No enrichment data → Manual review queue

SLA dashboard:
- Response time by rep
- MQL→SQL conversion rate
- SQL→Opportunity conversion rate
- Lead leakage (where leads drop out)

## Quality check

- [ ] Lead stages defined with clear qualification criteria
- [ ] Enrichment completes within 15 seconds of form fill
- [ ] SLAs defined and tracked for every touch
- [ ] Routing rules documented and automated
- [ ] Escalation paths for exceptions
- [ ] Weekly SLA review cadence established

## Next steps
1. 
2. 
3. 
