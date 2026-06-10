# Legal GTM Playbook — Commercial Counsel for SaaS Sales

*GTM practitioner lens for AEs, deal desk, founders, and RevOps — not legal advice.*

**Canonical expert:** Eunice Buhler (G2 General Counsel) — sales-legal alignment, commercial velocity.  
**CLM methodology:** Ironclad — deal desk swimlanes, template library, CRM-native workflows.  
**Security timing:** `references/security-questionnaire-deal-guide.md` · `references/gtm-data-exchange-playbook.md`.  
**Implementation:** `soc2-compliance`, `security-assessments` (founder-led).

**Disclaimer:** Templates and process guidance only. Binding terms, employment law, and regulatory conclusions require qualified counsel.

---

## When to load this playbook

| Trigger | Load |
|---|---|
| Enterprise MSA / order form redlines | Pattern 29 · this playbook · `deal-desk` |
| When to sign DPA | Section below + `gtm-data-exchange-playbook.md` |
| Security questionnaire in deal | `security-questionnaire-deal-guide.md` |
| Discount + custom terms approval | `deal-desk` discount authority + Ironclad swimlanes |
| SDR commission / contractor classification | `employment-compliance` (not deal desk) |
| Hire first sales counsel | a16z commercial counsel framing — section below |

---

## Eunice Buhler (G2) — Sales + Legal alignment

**Role:** SVP, General Counsel & Corporate Secretary, G2.  
**Domain:** Commercial velocity, sales partnership, SLA commitments, "get to yes" mindset.

**Public channels**
- 💼 [LinkedIn](https://www.linkedin.com/in/eunice-g-buhler-37880277/)
- 🔗 [G2 — Legal team growth](https://company.g2.com/news/celebrating-g2-legal-team)
- ▶ [SaaStr — Align Sales & Legal to Close Faster](https://www.saastr.com/how-to-align-sales-legal-to-close-more-deals-faster-with-g2/)
- 📊 [SlideShare deck](https://www.slideshare.net/slideshow/how-to-align-sales-legal-to-close-more-deals-faster-with-g2/261000327)

**Key frameworks**

| Framework | GTM action |
|---|---|
| **True north star (CEO)** | Legal and sales share customer-outcome goal — not "legal wins" vs "sales wins" |
| **Availability** | Legal reachable on Slack/standups; monthly 1:1 with segment leaders |
| **Respect as internal clients** | Sales escalates early; legal commits to published SLA (G2: 5-day → 1-day SLA turnaround) |
| **Commercially focused attorneys** | M&A-style "how do we get to yes" — document the rare hard **no** |
| **Balance short-term gain vs long-term risk** | Trade concessions in negotiation, not in security/compliance posture |

**Contrast:** Buhler = **relationship + velocity** between revenue and legal. Vanta/Drata = **trust center artifacts**. Lemkin = **do SOC 2 early** — complementary, not contradictory.

---

## Ironclad — Deal desk & CLM (methodology)

**Role:** AI contract lifecycle management — sales-facing workflows, not infosec.  
**Domain:** Template library, approval routing, Salesforce/HubSpot-native contract generation.

**Public channels**
- 🔗 [ironcladapp.com](https://ironcladapp.com/) · [Sales teams](https://ironcladapp.com/solutions/team/sales)
- 📰 [Running a Deal Desk on Ironclad](https://ironcladapp.com/resources/articles/how-to-run-a-deal-desk-on-ironclad)
- 📰 [Salesforce integration — deal velocity](https://ironcladapp.com/resources/customer-stories/ironclad-salesforce-integration)

**Deal desk swimlanes (GTM)**

| Term type | Typical approval | AE autonomy |
|---|---|---|
| List price, standard MSA | None | Full |
| Discount 0–10% | Rep discretion | `deal-desk` template |
| Discount 10–30% | Manager → VP/CRO | Document trade |
| Non-standard liability / indemnity | Legal + deal desk | Never verbal promise |
| Custom DPA exhibits | Legal | Use pre-approved template |
| Multi-year uplift / usage hybrid | Finance + deal desk | Ironclad workflow |

**Artifacts to maintain (legal-pre-approved):**
- Standard MSA, enterprise MSA, security-strict variant (finserv/health)
- Order form + DPA bundle
- SLA matrix, subprocessors list, insurance certificates

---

## MSA, DPA, security — phase gates (canonical)

*Aligned with `security-questionnaire-deal-guide.md` and `gtm-data-exchange-playbook.md`.*

| Deal stage | Legal / GTM action | Do not |
|---|---|---|
| **Discovery** | Ask when procurement runs legal/security; share trust center link | Send full SOC 2 without NDA |
| **Evaluation / POC** | Mutual NDA; **synthetic data** default | Production export pre-contract |
| **Security review** | Route questionnaire to owner; 5-day SLA target | AE invents encryption answers |
| **Commercial negotiation** | **DPA + order form in parallel** | "Sign later" on DPA for enterprise |
| **Closed-won** | Archive executed pack; CS handoff of data boundaries | Re-request same customer data via email |

**When to sign DPA (canonical):**
- **Enterprise / regulated / production data:** DPA executed **before** production data intake — during negotiation, not post-signature onboarding.
- **SMB click-through:** Standard online terms + DPA available on request; no production PII until contract active.
- **POC with real data:** Active POC agreement + NDA minimum; DPA if customer segment requires (see go/no-go tree in `gtm-data-exchange-playbook.md`).

---

## Employment & commission (GTM-adjacent)

| Topic | Guidance | Skill |
|---|---|---|
| SDR as contractor | High misclassification risk if full-time, your tools, your hours | `employment-compliance` — default **W-2** |
| Commission plan changes | Written plan + acknowledgment; clawback in offer | `gtm-role-descriptions` comp templates |
| Draw / ramp guarantees | Document recoverable vs non-recoverable | `founder-comp-playbook` |

---

## When to hire commercial counsel (a16z framing)

| Stage | Model |
|---|---|
| **<$30M ARR** | Fractional GC + CLM (Ironclad/Juro) + deal desk playbook |
| **$30–50M ARR** | 1 FTE **sales counsel** (velocity) + corporate legal (policy) |
| **$50M+ ARR** | Dedicated commercial team when MSA turnaround >48h or >300 contracts/qtr |

Sales counsel reports to **VP Sales or COO** for velocity; dotted line to GC for policy (SaaStr/Pulse RevOps knowledge base pattern).

---

## 5-clause cap & batching (velocity tactics)

1. Cap **custom legal asks** per deal (e.g., five non-standard clauses) — escalate rest to strategic deal review.
2. **Weekly legal batch** for non-urgent redlines vs interrupt-driven daily chaos.
3. **Pre-approved fallback ladder** for liability cap, indemnity, DPA subprocessors — AE knows floor before escalation.

---

## Cross-links

- `references/benchmark-reconciliation.md` — legal/security timing
- `references/experts.md` — Eunice Buhler, Ironclad, Vanta, Lemkin
- `deal-desk/SKILL.md` — discount authority, business case
- `vendor-contracts` — vendor MSAs/DPAs (procurement side)
