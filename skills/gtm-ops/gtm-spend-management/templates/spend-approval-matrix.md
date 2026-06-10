# GTM Spend Approval Matrix

**Company:** ___ **Effective:** ___ **Owner:** Finance + RevOps

---

## Thresholds

| Annual contract value (ACV) | Required approvers | SLA | Required artifacts |
|---|---|---|---|
| **< $2,000** | Manager + RevOps | 2 business days | Business case (3 bullets) |
| **$2,000 – $9,999** | Dept head (Sales/Marketing) + Finance | 5 business days | Stack overlap note + TCO row |
| **$10,000 – $49,999** | CRO or CMO + Finance | 10 business days | `tool-cost-sheet` line + security review |
| **≥ $50,000** | CEO (+ board if >1% ARR) | 15 business days | `vendor-contracts` procurement pack |

---

## Request template (copy for Slack / Notion)

```
Vendor: [name]
ACV: $[annual]
Cost model: [seat / credit / platform]
Owner: [email]
Bowtie stage: [acquisition / close / expand]
Overlap check: [no overlap / replaces X]
TCO row updated: [Y/N]
Ramp payment: [virtual card / bill pay]
Trial end date (if trial): [date]
```

---

## Category-specific rules

| Category | Extra approver | Notes |
|---|---|---|
| CRM change | CRO + RevOps | Migration plan required |
| Enrichment API | RevOps | Credit cap + 80% alert |
| Intent data | CMO + RevOps | Overlap with existing intent |
| Gifting platform | Marketing + Finance | `strategic-gifting` budget |
| Paid ads | Marketing | `campaign-governance` caps |
| AI / LLM in stack | RevOps + Eng | Token budget |

---

## Deny criteria (auto-reject)

- [ ] No stack overlap review
- [ ] No assigned owner
- [ ] Duplicate category without sunset plan
- [ ] Personal card reimbursement request for ongoing SaaS
- [ ] Auto-renew with no notice period in contract

---

## Emergency exceptions

| Scenario | Approver | Post-mortem |
|---|---|---|
| Conference sponsorship <7d | CMO + Finance verbal → written 48h | Required |
| Production outage fix tool | CTO + RevOps | Required |

---

## Ramp issuance after approval

| ACV | Ramp action |
|---|---|
| < $10K monthly SaaS | Issue / raise virtual card limit |
| ≥ $10K annual invoice | Bill pay workflow |
| Trial | $500 cap card, 14-day expiry |

Policy: `references/spend-governance.md`
