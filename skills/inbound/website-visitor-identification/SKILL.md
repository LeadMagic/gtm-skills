---
name: website-visitor-identification
description: >-
  Design website visitor identification and deanonymization programs — company
  vs person-level ID, vendor selection (Clearbit/Breeze, RB2B, 6sense, etc.),
  privacy guardrails (GDPR/CCPA operational), Slack alert triage, and ICP routing
  to MQL or outbound triggers. Use when implementing visitor ID, reverse-IP reveal,
  intent data, or person-level LinkedIn visitor tracking. Triggers on: "visitor
  identification", "deanonymization", "website intent", "Clearbit Reveal", "RB2B",
  "who visited our website", "reverse IP", "WebSights", "Leadfeeder", "visitor ID
  privacy".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [inbound, visitor-id, intent, deanonymization, privacy, abm, clearbit, rb2b]
  related_skills:
    - inbound-triage
    - icp-scoring
    - 1p-tagging-pixels
    - revops-tech-stack
    - gtm-spend-management
    - cold-email-strategy
    - lead-enrichment
    - campaign-governance
    - attribution
  frameworks:
    - "HubSpot Breeze Intelligence (Clearbit heritage) — Reveal & enrichment"
    - "Dharmesh Shah (HubSpot) — Inbound Attract + measurable intent"
    - "Chris Walker (Refine Labs) — Measurable demand vs dark social"
    - "Scott Brinker — MarTech consolidation before new intent vendors"
    - "Winning by Design — Bowtie acquisition stage instrumentation"
    - "SiriusDecisions Demand Waterfall — MQL definitions from intent"
---

# Website Visitor Identification

## Overview

Most B2B sites convert 2–3% of traffic to forms — the rest looks like dark
traffic. Visitor identification (deanonymization) recovers **company** or
**person** signals from anonymous sessions. The mistake: buying RB2B or 6sense
before deciding identification **level**, running person-level ID on EU traffic
without privacy review, or routing every alert to SDRs without an ICP filter.

This skill is the **canonical home** for visitor ID strategy: person vs business
decision tree, vendor comparison (Clearbit/Breeze, RB2B, 6sense, Demandbase,
ZoomInfo WebSights, Leadfeeder/Dealfront, Warmly, Koala, Factors.ai, Albacross),
privacy operational checklist (not legal advice), and GTM workflows from
website visit → MQL or guardrailed outbound trigger.

## Frameworks Referenced

- **HubSpot Breeze Intelligence (Clearbit heritage).** Company Reveal on visit;
  form enrichment for person + firmographics in HubSpot-native stacks.
- **Dharmesh Shah (HubSpot).** Visitor ID instruments the **Attract** stage of
  the inbound flywheel — permission-based follow-up after self-directed research.
  `references/dharmesh-shah-hubspot-inbound.md` · Pattern 20 + 27.
- **Chris Walker (Refine Labs).** Visitor ID is the **measurable** counterpart
  to dark social — pair with `content-marketing` and `attribution`, not replace them.
  Pattern 26 + 20.
- **Scott Brinker — MarTech consolidation.** One company-ID owner + at most one
  person-ID vendor until utilization proves ROI (`revops-tech-stack`).
- **Winning by Design Bowtie.** Visitor ID instruments the **acquisition** stage.
- **SiriusDecisions Demand Waterfall.** Intent signals feed MQL definitions —
  coordinate with `inbound-triage`.

## When to Use

- "Identify companies visiting our website"
- "Set up Clearbit Reveal / Breeze Intelligence"
- "RB2B vs Warmly vs Koala"
- "Person-level vs company-level visitor ID"
- "Website intent data program"
- "GDPR / CCPA for visitor deanonymization" (operational — not legal counsel)
- "Slack alerts for website visitors"
- "Route visitor intent to sales"

## Prerequisites

- ICP defined (`icp-scoring`)
- CRM with account + contact model
- Consent management for EU traffic (`1p-tagging-pixels`)
- UTM taxonomy (`campaign-governance`) for source attribution

## Step-by-Step Process

### Phase 1: Choose Identification Level

Load `references/person-vs-business-identification.md`.

1. Map primary motion: ABM account prioritization → **company**; authenticated
   PLG → **person (1P)**; SDR outbound trigger → **person (guardrailed)**.
2. Run privacy go/no-go (`references/visitor-id-privacy-gtm.md`) before person ID.
3. Document decision: level, lawful basis note (counsel confirms), geo scope.

### Phase 2: Vendor Selection

Load `references/visitor-id-vendor-comparison.md` and
`templates/visitor-id-vendor-eval-scorecard.md`.

| Need | Directional pick |
|---|---|
| HubSpot stack | Breeze Intelligence / Clearbit Reveal |
| Enterprise ABM | 6sense OR Demandbase (one) |
| SMB company ID | Leadfeeder/Dealfront or Albacross (EU) |
| Person LinkedIn ID | RB2B (US-primary, privacy review) |
| PLG sales-assist | Koala or Warmly |
| Analytics + firm ID | Factors.ai |

Run 30-day pilot: ICP-qualified rate, false positive sample (n=50), cost per
qualified ID. Register vendor in `gtm-spend-management` → `GTM-Data` class.

### Phase 3: Privacy & Consent (Operational)

Load `references/visitor-id-privacy-gtm.md`.

**Disclaimer:** Not legal advice — involve privacy counsel for person-level ID.

- Update privacy policy disclosures
- Fire visitor ID scripts after consent in EU
- Sign vendor DPA (`vendor-contracts`)
- Wire suppression list to CRM + sequencer
- Document security questionnaire triggers

Cross-links: `references/gtm-data-exchange-playbook.md`,
`references/gtm-security-hygiene-basics.md`,
`references/security-questionnaire-deal-guide.md`

### Phase 4: Build Workflows

Load `references/visitor-identification-playbook.md`.

**Company ID → MQL path:**
```
Visit → vendor ID → enrich → ICP filter → intent score → inbound-triage routing
```

**Person ID → outbound trigger (if approved):**
```
Person match → privacy gate → ICP + confidence High → enrich email →
cold-email-strategy trigger branch (≤2 touches) → human on reply
```

Integrations: CRM account/contact, Slack (`templates/visitor-alert-triage-checklist.md`),
Clay/n8n webhooks, SEP enrollment rules.

### Phase 5: Measurement & Governance

| Metric | Purpose |
|---|---|
| ICP-qualified ID rate | Quality over raw volume |
| Alert → meeting | ROI on person ID |
| False positive rate (sampled) | Vendor renewal input |
| Opt-out / complaint rate | Kill switch for person ID |

Quarterly: stack overlap audit (`revops-tech-stack`), spend review
(`gtm-spend-management`).

## Output Format

Visitor identification program document:
- Identification level decision + rationale
- Vendor selection with eval scorecard
- Privacy operational checklist status
- Workflow diagrams (company MQL + person trigger)
- Slack channel design + triage SOP
- CRM field map + integration contracts
- Anti-pattern acknowledgments

See `templates/output-template.md`.

## Quality Check

- [ ] Person vs business decision documented with decision tree
- [ ] ICP filter runs before CRM write or sequence enrollment
- [ ] Privacy checklist complete; person ID has counsel review if EU traffic
- [ ] Vendor comparison includes identification level column
- [ ] Slack triage checklist assigned to owners
- [ ] UTM/source attribution wired (`campaign-governance`)
- [ ] Vendor in spend register with owner + renewal
- [ ] Anti-patterns addressed: no spam-all, opt-outs honored

## Common Pitfalls

1. **Person ID without privacy review.** GDPR/CCPA exposure. Fix: company ID
   default; person ID only after `visitor-id-privacy-gtm.md` gates + counsel.

2. **No ICP filter.** SDRs chase ISPs, agencies, and universities. Fix:
   automate `icp-scoring` before any alert or CRM create.

3. **Duplicate intent vendors.** Clearbit + 6sense + Leadfeeder + RB2B all
   firing. Fix: Brinker consolidation — one company + one person max.

4. **Creepy outbound copy.** "I saw you on our pricing page" destroys trust.
   Fix: signal-anchored relevance via `cold-email-strategy` — not surveillance tone.

5. **Ignoring opt-outs.** Visitor ID contact opts out on email but stays in
   RB2B alerts. Fix: suppression sync across CRM, sequencer, Slack enrollment.

6. **EU scripts before consent.** Non-essential tags fire on page load. Fix:
   `1p-tagging-pixels` consent-first deployment.

## Execution Artifacts

- `references/framework-notes.md` — frameworks and cross-links
- `templates/output-template.md` — deliverable shell
- `scripts/check-output.py` — deliverable validator
- `references/visitor-identification-playbook.md` — **master guide**
- `references/person-vs-business-identification.md` — decision matrix
- `references/visitor-id-privacy-gtm.md` — GDPR/CCPA operational checklist
- `references/visitor-id-vendor-comparison.md` — Clearbit, RB2B, 6sense, etc.
- `templates/visitor-alert-triage-checklist.md` — Slack triage SOP
- `templates/visitor-id-vendor-eval-scorecard.md` — vendor pilot scorecard

## Related Skills

- **inbound-triage** — MQL routing after company ID + form fills
- **cold-email-strategy** — person ID → trigger-based outbound branch
- **icp-scoring** — filter before sales routing
- **1p-tagging-pixels** — consent, pixels, identity resolution context
- **revops-tech-stack** — vendor selection and stack consolidation
- **gtm-spend-management** — `GTM-Data` vendor roster and renewals
- **lead-enrichment** — verify person match before outreach
- **campaign-governance** — UTM + visitor source attribution
- **attribution** — measurable demand layer alongside dark social
