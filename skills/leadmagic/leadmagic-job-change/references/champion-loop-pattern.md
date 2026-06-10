# LeadMagic Job Change — Champion Loop Pattern

Operational pattern for routing job-change signals. Pairs with clay-loops-toolkit **L03 — Job Change / Champion**.

## Signal Types → Routes

| Scenario | Detection | Route | Play Skill |
|---|---|---|---|
| Champion → new company | Job change + past buyer | AE expansion task | expansion-selling |
| Champion left open opp | Job change + open deal | Risk alert → multi-thread | multi-thread-orchestration |
| Target contact new role | Job change + ICP account | Sequencer (verified) | job-change-play |
| Former user at new logo | Job change + product usage history | CSM + AE joint | customer-marketing |

## Clay Loop Architecture (L03)

4-table pattern from clay-loops-toolkit:

| Table | Purpose |
|---|---|
| SOURCE | CRM contacts with linkedin_url |
| MONITOR | LeadMagic Job Change column on schedule |
| ENRICH | Find → Verify → Enrich at new company |
| ACTION | Route by scenario matrix above |

Load full spec: `../../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md` (Job Change section)

## LeadMagic Column Sequence

| Order | Column | Run If |
|---:|---|---|
| 1 | Job Change | linkedin_url present |
| 2 | signal_detected | change within 30 days |
| 3 | Find Email | new company context |
| 4 | Verify Email | email found |
| 5 | Enrich Person | verify = valid |

Credits: ~4-6 per signal row.

## CRM Routing Rules

```
IF past_opportunity_won AND new_company in ICP
  → assign AE (expansion)
ELIF open_opportunity AND contact = champion
  → create risk task + flag deal
ELIF new_company in TAM AND verify = valid
  → enroll job-change-play sequence
ELSE
  → log signal, no auto-outreach
```

## Message Guardrails (ColdIQ Trigger Selling)

- Reference **specific** role change + business implication
- Never generic "congrats on new role" without problem hook
- Champion variant: reference prior relationship explicitly
- Risk variant: internal alert first — do not email new company from automated seq

Cross-ref Pat (data before copy): `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Verify Gate

Same as all LeadMagic outbound: no sequence without Verify = valid at new email.

## Metrics

| Metric | Target |
|---|---:|
| Signal-to-meeting (champion) | >15% |
| False positive (wrong person) | <5% |
| Open opp risk flagged <24h | 100% |
| Credit per routed meeting | track monthly |

Expert router: `references/gtm-experts-outbound-index.md`
