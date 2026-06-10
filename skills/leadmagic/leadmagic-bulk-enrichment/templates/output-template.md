# LeadMagic Bulk Enrichment Deliverable

## Context
- Input CSV size:
- Job types: find / validate / enrich
- CRM export? Y/N
- Sequencer export? Y/N

## Framework Basis
- DAMA data quality stages
- Pat Spielmann — valid-only export to send

## Pipeline Stages
| Stage | Output File | Row Count |
|---|---|---:|
| Intake |  |  |
| Dedupe |  |  |
| ICP filter |  |  |
| Enrich |  |  |
| Verify |  |  |
| Send-ready |  |  |

Full spec: `references/batch-pipeline-spec.md`

## Status Routing
| Status | Destination |
|---|---|
| valid | send-ready |
| invalid | suppress |
| risky | catch_all_queue |
| unknown | manual review |

## CRM Upsert Map
| LM Field | CRM Field | Overwrite Rule |
|---|---|---|

## QA Sample
- [ ] 50-row spot check complete
- [ ] Credit burn reconciled

## Quality Check
- [ ] ICP filter before enrich
- [ ] Idempotent CRM upsert rules
- [ ] No invalid rows in sequencer export
