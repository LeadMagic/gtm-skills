# Target-State RevOps Architecture

**ARR band:** _____________ **Effective date:** _____________

## Category owners (one per row)

| Category | Bowtie stage | Owner tool | Integrates to CRM | Data owner |
|---|---|---|---|---|
| CRM | All | | Hub | |
| Enrichment | Acquire | | → CRM | |
| Sequencing | Acquire → Close | | ↔ CRM | |
| Conversation intel | Close | | → CRM | |
| Forecasting | Close | | ← CRM | |
| Warehouse / BI | All (analytics) | | ← CRM + tools | |
| iPaaS | All | | Orchestration | |

## Integration contracts

| Source | Destination | Objects | Frequency | Owner |
|---|---|---|---|---|
| | CRM | | | |

## New vendor gate

Before purchase: stack overlap check · bowtie stage assignment · spend approval (`gtm-spend-management`)

Cross-ref: Scott Brinker consolidation · WbD bowtie
