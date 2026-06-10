# Website Visitor Identification Playbook

*GTM operational guide — not legal advice. Privacy section defers to counsel for binding decisions.*

---

## What this covers

Website visitor identification (deanonymization) turns anonymous traffic into actionable GTM signals. Two levels matter:

| Level | What you get | Primary method |
|---|---|---|
| **Business (company)** | Firm name, size, industry, sometimes technographics | Reverse-IP → company graph |
| **Person (contact)** | Named individual, often LinkedIn profile | Cookie/device graph, form identity, vendor identity networks |

**Canonical decision guide:** `person-vs-business-identification.md`  
**Vendor selection:** `visitor-id-vendor-comparison.md`  
**Privacy go/no-go:** `visitor-id-privacy-gtm.md`

---

## Confidence tiers (operate with tiers, not binary truth)

| Tier | Company ID | Person ID | GTM action |
|---|---|---|---|
| **High** | IP + multiple corroborating signals (ASN, firmographic match, repeat visits) | Form fill, login, or vendor with disclosed match method + ICP fit | Route to sales or enroll in trigger sequence |
| **Medium** | Single IP match, shared office building risk | Vendor person match without corroboration | Slack alert + SDR research before outreach |
| **Low** | VPN, ISP residential, mobile carrier | Stale profile, wrong persona at right company | Log for ABM account list only — no person outreach |

**False positives:** Company ID confuses co-located tenants, VPN egress, and agency traffic. Person ID confuses shared devices, family members on home IP, and stale LinkedIn employment.

---

## When each level fits the GTM motion

| Motion | Level | Why |
|---|---|---|
| ABM account prioritization | Company | Account-level intent without contact risk |
| Inbound MQL routing | Company + form identity | Form is lawful 1P identity; IP adds firm context |
| SDR speed-to-lead | Company alert → research contact | Research beats guessing person from IP |
| PLG product signals | Person (logged-in user) | Authenticated identity only |
| Outbound trigger sequence | Person (high confidence only) | Requires privacy review + ICP gate |
| Enterprise procurement-heavy | Company | Security questionnaires favor firm-level intent |

---

## Workflow 1: Company ID → MQL path

```
Anonymous visit
  → Reverse-IP / intent vendor (Clearbit Reveal, 6sense, Leadfeeder, etc.)
  → Firmographic enrichment (employee count, industry, geo)
  → ICP filter (icp-scoring)
  → IF ICP + engagement threshold:
        Create/update account in CRM
        Score intent (pages, frequency, recency)
        IF score > MQL threshold → route SDR/AE (inbound-triage SLAs)
      ELSE:
        ABM nurture audience only
  → Log source: visitor_id_vendor + confidence tier
```

**UTM + source:** Pass `utm_*` and referrer into CRM via `campaign-governance` so visitor intent is attributed to channel, not mislabeled "direct."

**Integration points:**
- CRM: account + intent score fields
- Slack: `#intent-alerts` with ICP badge (template: `templates/visitor-alert-triage-checklist.md`)
- Marketing automation: account-based nurture, not bulk person email from IP alone

---

## Workflow 2: Person ID → outbound trigger (guardrailed)

```
Person-level match (RB2B, Warmly person mode, etc.)
  → Privacy go/no-go checklist (visitor-id-privacy-gtm.md)
  → ICP filter (company + title + geo)
  → Confidence tier = High only for automated sequence
  → Enrich email (lead-enrichment waterfall)
  → Verify contact still at company
  → Enroll cold-email-strategy trigger branch (1–2 touches max on first signal)
  → Log lawful basis + opt-out path in CRM
```

**Do not:** Auto-enroll every LinkedIn visitor. **Do:** Treat as Tier 3 trigger in `cold-email-strategy` — signal-anchored, short branch, human review on reply.

---

## Slack alert triage playbook

Load `templates/visitor-alert-triage-checklist.md`.

**Channel design:**
- `#intent-company` — all company ID hits passing minimum engagement
- `#intent-priority` — ICP Tier 1 accounts only
- `#intent-person` — person ID (restricted membership: SDR lead + RevOps)

**Triage SLA:** 4 business hours for ICP Tier 1 person alerts; 24 hours for company-only.

**Alert payload (minimum):**
- Company name, domain, employee band
- Pages viewed + visit count (7d)
- UTM / referrer
- ICP tier + confidence tier
- Suggested owner (territory rules)

---

## ICP filter before sales routing

Non-negotiable gates (from `icp-scoring`):

1. Employee count / revenue band in range
2. Industry / tech stack fit
3. Geo / regulatory fit (EU person ID stricter)
4. Engagement threshold (≥2 high-intent pages OR ≥3 visits in 14d)
5. Not existing customer in active onboarding (check CRM)

**Anti-patterns:**
- Spam every visitor with generic outbound
- No ICP filter — SDRs chase ISPs and universities
- Ignoring opt-outs / unsubscribes from any channel
- Person-level outreach on EU traffic without legal review
- Routing agency/consultant traffic as target accounts

---

## Stack placement

| Function | Owner skill | Tool category |
|---|---|---|
| Visitor ID vendor selection | `revops-tech-stack` | Intent / deanonymization |
| Spend / renewal | `gtm-spend-management` | `GTM-Data` class |
| Tracking + consent | `1p-tagging-pixels` | Consent before pixels |
| Inbound routing | `inbound-triage` | MQL path |
| Outbound trigger | `cold-email-strategy` | Person ID branch |
| Data boundaries | `revops-tech-stack` Phase 4b | PII in sequences |

---

## Measurement

| Metric | Target direction |
|---|---|
| Identified visit rate | Track — don't optimize blindly |
| ICP-qualified ID rate | ↑ (quality over volume) |
| Alert → research → meeting | Primary funnel for person ID |
| False positive rate (sampled quarterly) | ↓ |
| Opt-out / complaint rate | → 0; kill person ID if elevated |

Pair with `attribution` + `gtm-metrics` — visitor ID is **measurable demand** complement to Chris Walker dark social (unmeasurable influence).

---

## Related artifacts

- `person-vs-business-identification.md` — decision matrix
- `visitor-id-privacy-gtm.md` — GDPR/CCPA operational checklist
- `visitor-id-vendor-comparison.md` — Clearbit, RB2B, 6sense, etc.
- `templates/visitor-alert-triage-checklist.md`
- `templates/visitor-id-vendor-eval-scorecard.md`
- `references/gtm-data-exchange-playbook.md` — customer data boundaries
- `references/gtm-security-hygiene-basics.md` — rep access to person-level alerts
