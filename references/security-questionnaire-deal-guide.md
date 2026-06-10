# Security Questionnaire Deal Guide

*When security review enters the enterprise deal — GTM framing for AEs, deal desk, and founders.*

Implementation (pen tests, SOC 2 controls, SIG/CAIQ answers) → `security-assessments`, `soc2-compliance`. Customer data handling → `gtm-data-exchange-playbook.md`.

---

## When security review typically appears

| ACV / segment | Typical trigger | Who owns the relationship |
|---|---|---|
| **<$10K SMB** | Rarely formal; may ask "are you SOC 2?" | AE sends trust page link |
| **$10K–$50K mid-market** | Questionnaire after verbal yes | AE + founder/ops |
| **$50K+ enterprise** | Parallel track once EB engaged | Deal desk + security lead |
| **Regulated buyer** (finance, health, gov) | Security before commercial terms finalize | Legal + security from day one of eval |

**G2 / SaaStr context:** A large share of B2B buyers require a security assessment before purchase, often *after* shortlisting — so late surprises stall deals. Front-load trust materials in evaluation, not at signature. Source: [Jason Lemkin — Just Do The SOC-2](https://www.saastr.com/just-do-the-soc-2/) (citing G2 buyer research).

---

## Deal-stage playbook

### Stage 1 — Discovery / early eval

**Do:**

- Share public trust center / security page
- Ask: "Does your procurement team require a security review? When does it usually start?"
- Offer synthetic POC data

**Don't:**

- Send SOC 2 report without NDA
- Promise specific certifications you don't have yet
- Request production customer data

### Stage 2 — Active evaluation / POC

**Do:**

- Confirm POC data scope in writing (email or mutual doc)
- Introduce your security contact as *partner*, not blocker
- If questionnaire arrives, log receipt date and SLA (target: 5 business days with trust center)

**Don't:**

- Let AE solo-fill technical architecture questions
- Extend POC on production data without review complete

### Stage 3 — Commercial / procurement

**Do:**

- Run DPA in parallel with order form (legal)
- Provide bridge letter or readiness report if SOC 2 in progress
- Track security review as a **MEDDICC** line item (paper process / procurement)

**Don't:**

- Discount because "security is taking too long" without executive alignment
- Sign customer paper that adds unlimited liability without legal review

### Stage 4 — Closed-won

**Do:**

- Archive which artifacts were shared (trust center access log)
- Hand off to CS: security contacts, data boundaries, retention

**Don't:**

- Re-open security review because CS asked for new data class via email

---

## Artifact menu (what to send when)

| Buyer ask | GTM response | Owner |
|---|---|---|
| "Are you SOC 2?" | Yes/No + report via trust center under NDA | Security / ops |
| "Send your pen test" | Summary or full report per policy | Security |
| "Fill this 300-row spreadsheet" | Trust center first; questionnaire automation if still required | Security + deal desk |
| "We need a DPA" | Standard DPA + subprocessors list | Legal |
| "Where is data stored?" | Trust center FAQ — don't improvise regions | Security |

Methodology refs: [Vanta Trust Center implementation](https://help.vanta.com/en/articles/11487960-vanta-trust-center-implementation-guide) · [Vanta — proactive sales partnership](https://www.vanta.com/resources/building-a-comprehensive-trust-center)

---

## Roles

| Role | Responsibility |
|---|---|
| **AE** | Surface timing early; never fabricate answers; keep deal moving |
| **Deal desk** | Track review status; coordinate legal + security; no rogue concessions |
| **Security / ops** | Accurate answers; trust center; SOC 2 / pen test artifacts |
| **Legal** | DPA, customer paper, liability caps |
| **CS (post-sale)** | No new data classes without same review path |

Assign a **Trust Collaborator** or sales-facing security liaison so AEs aren't DMing engineers for every question.

---

## SLA targets (internal)

| Item | Target |
|---|---|
| Acknowledge questionnaire receipt | 1 business day |
| First draft responses | 5 business days (with trust center + prior answers) |
| DPA turn | Legal queue — flag at commit if >2 weeks |
| Trust center link after request | Same day |

---

## Stalled deal diagnostics

| Symptom | Likely cause | GTM fix |
|---|---|---|
| Security ghosted us | Wrong thread — IT not copied | Multi-thread to CISO delegate via champion |
| Same questions repeated | No trust center / stale answers | Central FAQ + questionnaire KB |
| Review started before EB buy-in | Procurement running early | Pause; align with `pipeline-management` stage gates |
| We missed deadline | AE hid questionnaire 2 weeks | Deal desk intake rule: forward same day |

---

## Related skills

- `deal-desk` — commercial structure + security track coordination
- `pipeline-management` — MEDDICC paper process
- `customer-onboarding` — post-sale data handoff
- `soc2-compliance`, `security-assessments` — building artifacts
- `data-privacy-compliance` — DPA substance
- `references/gtm-data-exchange-playbook.md` — what data to exchange when
