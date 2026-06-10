# SaaS Vendor Roster — SOP

The **vendor spend register** is the operational source of truth — not Ramp alone,
not the CRM. Ramp shows transactions; the roster shows **intent, owner, renewal**.

---

## Roster vs other systems

| System | Role |
|---|---|
| **vendor-spend-register** | Owner, renewal, ACV, seats, bowtie stage |
| **Ramp** | Actual charges, cards, receipts |
| **gtm-tool-cost-model** | Planned TCO, scenarios |
| **vendor-contracts** | Legal PDFs, MSA, DPA |
| **revops-tech-stack** | Process fit, consolidation |

---

## Required fields (every GTM vendor)

| Field | Example |
|---|---|
| `vendor_id` | V-042 |
| `vendor_name` | Gong |
| `category` | Conversation intel |
| `owner_email` | revops@company.com |
| `department` | Sales |
| `cost_model` | Per seat |
| `annual_budget_usd` | 48000 |
| `payment_method` | Ramp virtual card GONG-001 |
| `contract_start` | 2025-03-01 |
| `renewal_date` | 2026-03-01 |
| `auto_renew` | Y |
| `notice_days` | 30 |
| `seats_paid` | 12 |
| `seats_active` | 9 |
| `bowtie_stage` | Close |
| `crm_integration` | Y — HubSpot |
| `status` | Active / Trial / Sunset |

Template: `templates/vendor-spend-register.md`

---

## Lifecycle

### New vendor

1. Stack overlap check (`revops-tech-stack`)
2. TCO row (`gtm-tool-cost-model`)
3. Approval (`spend-approval-matrix`)
4. Issue Ramp card or bill pay
5. Add roster row **before** first charge
6. Calendar renewal reminders

### Active vendor

- Monthly: active vs paid seats
- Quarterly: utilization review
- Annually: negotiate before auto-renew

### Sunset vendor

- [ ] Migration complete
- [ ] Card terminated
- [ ] Roster status = Sunset
- [ ] Export data per DPA
- [ ] Remove from stack diagram

---

## Zombie detection rules

Flag vendor if **any**:

- Charge in Ramp, no roster owner
- Roster owner left company
- `seats_active / seats_paid` < 50% for 2 quarters
- No bowtie stage mapping
- Duplicate category without migration plan

---

## Renewal workflow (T-90 days)

| Day | Action |
|---|---|
| T-90 | Owner receives alert; usage report pulled |
| T-60 | True-down proposal; negotiate (`vendor-contracts`) |
| T-30 | Finance approves renewal amount |
| T-7 | Bill pay scheduled or card limit updated |
| T-0 | Confirm charge matches approved ACV |

---

## RACI

| Activity | RevOps | Finance | Dept head |
|---|---|---|---|
| Maintain roster | R/A | C | I |
| Ramp admin | C | R/A | I |
| Approve new vendor | R | C | A |
| Renewal negotiate | R | C | A |
| Quarterly review | R/A | R | C |

R = responsible, A = accountable, C = consulted, I = informed
