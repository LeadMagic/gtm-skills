# Website Visitor Identification — Deliverable Template

## Executive summary

- **Identification strategy:** Company / Person / Hybrid
- **Primary vendor:** 
- **Privacy status:** Checklist complete Y/N · Counsel review Y/N
- **ICP filter:** Automated Y/N

---

## 1. Identification level decision

*Load `person-vs-business-identification.md` decision tree result.*

| Question | Answer |
|---|---|
| Primary GTM motion | |
| Chosen ID level | |
| Rationale | |

---

## 2. Vendor selection

*Load `visitor-id-vendor-comparison.md` + eval scorecard.*

| Vendor | ID level | Role in stack | Annual cost |
|---|---|---|---|
| | | | |

---

## 3. Privacy & compliance (operational)

*Load `visitor-id-privacy-gtm.md` — not legal advice.*

- [ ] Privacy policy updated
- [ ] Consent banner (EU)
- [ ] DPA signed
- [ ] Suppression list wired
- [ ] Person ID gates (if applicable)

---

## 4. Workflows

### Company ID → MQL

```
[diagram or bullet flow from visitor-identification-playbook.md]
```

### Person ID → outbound trigger (if applicable)

```
[guardrailed flow]
```

---

## 5. Slack alert design

| Channel | Audience | SLA |
|---|---|---|
| | | |

Triage checklist: `templates/visitor-alert-triage-checklist.md`

---

## 6. CRM & integration map

| Source | Destination | Fields | Frequency |
|---|---|---|---|
| | | | |

---

## 7. Measurement plan

| Metric | Baseline | Target | Review cadence |
|---|---|---|---|
| ICP-qualified ID rate | | | |
| Alert → meeting | | | |
| False positive (sampled) | | | |

---

## 8. Anti-patterns acknowledged

- [ ] No spam-every-visitor policy
- [ ] ICP filter before routing
- [ ] Opt-out honored

---

## Related skills

`inbound-triage` · `cold-email-strategy` · `revops-tech-stack` · `gtm-spend-management` · `1p-tagging-pixels` · `icp-scoring`
