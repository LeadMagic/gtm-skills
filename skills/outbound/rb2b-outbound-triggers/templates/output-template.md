# RB2B Outbound Triggers — Deliverable

## Context

- Company / product:
- ICP definition:
- Current RB2B setup (yes/no):
- SDR team size:
- Sequencer (Smartlead/Instantly/Outreach/Salesloft):
- Date:

## Summary

[One paragraph: what this deliverable decides — the RB2B-to-outbound pipeline]

## 1. Visitor Routing Matrix

| Tier             | ICP Score | Title Match                        | Page Engagement   | Action                             | SLA      |
| ---------------- | --------- | ---------------------------------- | ----------------- | ---------------------------------- | -------- |
| Tier 1 — Hot     | ≥80       | Decision-maker/influencer          | Pricing/docs/demo | Immediate Slack + 7-touch sequence | <15 min  |
| Tier 2 — Warm    | 50-79     | Any match                          | Any page          | Enrich + 5-touch sequence          | <4 hours |
| Tier 3 — Monitor | <50       | Junior/irrelevant                  | Low engagement    | Log in CRM, no outbound            | None     |
| Tier 4 — Exclude | N/A       | Competitor/vendor/customer/partner | N/A               | Suppress                           | N/A      |

## 2. Enrichment Waterfall

| Step | Tool                | Input           | Output                         | Fallback              |
| ---- | ------------------- | --------------- | ------------------------------ | --------------------- |
| 1    | RB2B payload        | Visitor session | Name, title, company, LinkedIn | —                     |
| 2    | Clay enrichment     | Company name    | Firmographics, tech stack      | Apollo                |
| 3    | LeadMagic           | Name + company  | Verified email                 | → Apollo → Hunter     |
| 4    | Email verification  | Email address   | Valid/invalid/risky            | Never send unverified |
| 5    | Phone (Tier 1 only) | Name + company  | Direct/mobile                  | Lusha → ZoomInfo      |
| 6    | ICP scoring         | Full enrichment | Score 0-100                    | Custom scoring model  |

## 3. Sequence Designs

### Tier 1 — Hot Visitor Sequence (7 touches, 10 business days)

| Touch | Day | Channel  | Content Goal                                   |
| ----- | --- | -------- | ---------------------------------------------- |
| 1     | 0   | LinkedIn | Connection request — reference visit context   |
| 2     | 0   | Email    | Personalized — "noticed you exploring [topic]" |
| 3     | 2   | Email    | Value drop — relevant case study               |
| 4     | 4   | LinkedIn | Engage with their recent post                  |
| 5     | 6   | Email    | Question tied to their role                    |
| 6     | 8   | Phone    | Cold call referencing visit                    |
| 7     | 10  | Email    | Breakup — "closing the loop"                   |

### Tier 2 — Warm Visitor Sequence (5 touches, 14 business days)

| Touch | Day | Channel  | Content                     |
| ----- | --- | -------- | --------------------------- |
| 1     | 0   | Email    | Soft reference + value prop |
| 2     | 3   | LinkedIn | Connection request          |
| 3     | 7   | Email    | Resource share (no ask)     |
| 4     | 11  | Email    | Question + soft CTA         |
| 5     | 14  | Email    | Breakup                     |

## 4. Slack Alert Template

```
🔥 RB2B Hot Visitor Alert
Name: [Visitor Name]
Title: [Job Title]
Company: [Company]
LinkedIn: [URL]
Pages visited: [list]
Session: [duration] | [pageviews]
ICP Score: [score]/100
Action: Enrich → Sequence "Tier 1 Hot Visitor"
SDR Owner: [assignment]
SLA: Contact within 15 minutes
```

## 5. Clay Workflow Spec

1. Trigger: RB2B webhook fires
2. Filter: ICP score ≥50
3. Enrich: LeadMagic → Apollo → Hunter (email waterfall)
4. Verify: Email verification gate
5. Score: Update ICP score with enrichment data
6. Route: Round-robin SDR assignment
7. Enroll: Push to sequencer with correct cadence
8. Log: CRM record with source = "RB2B Visitor"

## 6. Measurement Dashboard

| Metric                       | Target     | Source          |
| ---------------------------- | ---------- | --------------- |
| Visitors identified / week   | [baseline] | RB2B dashboard  |
| ICP fit rate                 | 30-50%     | Clay scoring    |
| Enrichment success rate      | ≥70%       | Clay waterfall  |
| SDR response within SLA      | ≥80%       | CRM timestamps  |
| Meeting booked rate (Tier 1) | 5-10%      | CRM source tag  |
| Meeting booked rate (Tier 2) | 2-5%       | CRM source tag  |
| Pipeline sourced from RB2B   | [monthly]  | CRM attribution |

## 7. Privacy Guardrails

- [ ] US-only visitor identification (RB2B default)
- [ ] CCPA opt-out mechanism published
- [ ] Existing customer suppression via CRM matching
- [ ] Competitor/vendor suppression list
- [ ] No exact page-level behavior in outreach copy
- [ ] Person-level data retained per data retention policy
- [ ] SDR access limited to assigned visitors only

## Quality check

- [ ] Routing tiers have clear, unambiguous criteria
- [ ] Tier 1 SLA is 15 minutes
- [ ] Enrichment includes verification before sending
- [ ] Sequences reference visit context naturally
- [ ] Tier 4 exclusions cover competitors, vendors, customers, partners
- [ ] Measurement tracks RB2B-sourced pipeline separately
- [ ] Privacy guardrails address CCPA
- [ ] Clay workflow has error handling for enrichment failures
- [ ] Breakup emails are professional
- [ ] Phone is Tier 1 only
