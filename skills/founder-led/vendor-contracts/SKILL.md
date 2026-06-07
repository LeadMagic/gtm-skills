---
name: vendor-contracts
description: >-
  Vendor contracts, MSAs, DPAs, and procurement for B2B SaaS — master service
  agreements, service level agreements, data processing agreements, order
  forms, vendor security assessments, and contract negotiation playbooks.
  Use when selling to enterprise (inbound contracts), buying from vendors
  (outbound procurement), negotiating terms, or building standard agreement
  templates. Triggers on: "MSA", "SLA agreement", "data processing agreement",
  "order form", "vendor security review", "enterprise contract", "procurement".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [contracts, msa, sla, dpa, procurement, vendor-management, enterprise-sales]
  related_skills: [legal-for-founders, data-privacy-compliance, security-assessments, soc2-compliance, deal-desk, business-insurance]
  frameworks:
    - "YC — Standard commercial terms for B2B SaaS"
    - "SaaS Capital — B2B SaaS contract benchmarks"
    - "Jason Lemkin (SaaStr) — Enterprise contract negotiation"
    - "David Skok (Matrix Partners) — B2B contract structure"
---

# Vendor Contracts & Procurement

## Overview

Contracts are the skeleton of enterprise sales. A clean MSA + Order Form +
DPA + SLA package closes deals in weeks. A messy, non-standard contract gets
stuck in legal review for months. The mistake: letting every enterprise
customer dictate terms from scratch. You need standard templates that cover
80% of deals, with red-line boundaries for the remaining 20%. This skill
covers the complete contract stack: MSA, Order Form, SLA, DPA — for both
selling to customers (inbound) and buying from vendors (outbound).

## When to Use

Trigger phrases: "MSA template", "master service agreement", "order form",
"SLA agreement", "data processing agreement template", "enterprise contract",
"vendor contract", "procurement process", "contract negotiation",
"commercial terms for SaaS", "standard contract"

## Step-by-Step Process

### Phase 1: Inbound Contracts (Selling to Customers)

**The standard contract stack:**

```
CONTRACT STACK (4 documents):

1. MSA (Master Services Agreement)
   - The "umbrella" contract. Signed once. Governs the entire relationship.
   - Covers: service description, payment terms, term/termination, IP,
     confidentiality, limitation of liability, warranties, indemnification,
     governing law, dispute resolution

2. Order Form
   - Each purchase gets its own Order Form.
   - Covers: products purchased, quantity (seats/volume), price, term length,
     billing frequency, renewal terms, special terms
   - References the MSA

3. SLA (Service Level Agreement)
   - Can be part of MSA or separate.
   - Covers: uptime commitment, response times, credits for downtime,
     support hours, escalation paths

4. DPA (Data Processing Agreement)
   - Required for GDPR compliance and enterprise deals.
   - Covers: data processed, purpose, sub-processors, security measures,
     breach notification, data subject rights, SCCs
```

**MSA — Key clauses and negotiation positions:**

| Clause | Standard Position | Fallback | Non-Negotiable |
|---|---|---|---|
| **Limitation of Liability** | 12 months of fees paid | 24 months | Never unlimited |
| **Indemnification** | Mutual for IP claims. Customer indemnifies for their data. | Customer indemnifies for their use only | Never indemnify for customer's data misuse |
| **Warranty Disclaimer** | "AS IS" — no warranties beyond what's explicitly stated | Accept limited warranties (performance, security) | Never warranty "error-free" or "uninterrupted" |
| **Termination for Convenience** | 30 days written notice | 60 days | Must include — don't lock into perpetual |
| **Governing Law** | Your state (or Delaware) | Their state | Not international (costly to litigate) |
| **Payment Terms** | Net 30, annual upfront | Net 45, quarterly | Never Net 90+ (cash flow killer) |

**Order Form — standard fields:**
- Company name, address, billing contact
- Products/services purchased
- Quantity (seats, volume, API calls)
- Term (monthly / annual / multi-year) — push for annual
- Price per unit, total contract value
- Billing frequency
- Start date, end date, auto-renewal terms
- Special terms (discounts, pilot terms, custom features)
- Signed by both parties

**SLA — standard commitments:**
- Uptime: 99.5% (standard) to 99.9% (enterprise). 99.99% is unreasonable
  for a startup.
- Credits: 5-10% of monthly fee per X% downtime. Cap at 100% of monthly fee.
- Exclusions: planned maintenance (48 hours notice), force majeure,
  customer-caused issues, third-party services
- Response times: P1 (15-60 min), P2 (1-4 hours), P3 (4-24 hours)

**DPA — key elements:**
- See: `data-privacy-compliance` skill for full DPA details
- Must include: data types, processing purpose, sub-processor list,
  security measures, breach notification (72 hours), data subject rights,
  SCCs for international transfers
- Have a standard DPA ready. Enterprise customers WILL ask for one.

### Phase 2: Contract Negotiation Playbook

**The enterprise legal review gauntlet:**

1. **Week 1:** Customer's procurement team receives your MSA.
2. **Week 2-3:** Their legal team red-lines the MSA (30-50 changes).
3. **Week 4:** Back-and-forth negotiation. Compromise on minor. Hold on major.
4. **Week 5-6:** Final review. Signatures.

**Your goal:** Get from MSA sent → signed in under 4 weeks. Every week of
delay is a week your revenue isn't starting.

**Negotiation rules:**

1. **Protect liability cap at all costs.** "We can be flexible on [X], but
   our liability cap of 12 months' fees is standard for SaaS companies at
   our stage."
2. **Push back on IP indemnity expansion.** "We'll indemnify for our IP
   infringement. We can't indemnify for your use of our product with your
   data — that's your domain."
3. **Accept minor redlines gracefully.** "Sure, we can accept Net 45 instead
   of Net 30." Small concessions build goodwill for the big ones.
4. **Have a line you won't cross.** Unlimited liability. Non-standard IP
   assignment (they want YOUR IP). Perpetual, irrevocable licenses. Walk
   away if they insist on these.

**When to bring in your lawyer:**
- Contract value > $50K and heavily red-lined
- Customer wants custom indemnity beyond IP
- International jurisdiction (their country's law)
- Data processing terms outside standard DPA
- Any clause that seems like it creates material risk

### Phase 3: Outbound Procurement (Buying from Vendors)

**Vendor evaluation framework:**

1. **Security Review:** DPA signed? SOC2 report obtained? Sub-processors
   documented?
2. **Commercial Terms:** Annual vs monthly? Auto-renewal? Price lock?
   Termination for convenience?
3. **Data Processing:** What data do they access? Where is it stored? Who
   are their sub-processors?
4. **Integration Risk:** How critical is this vendor to your product? What
   happens if they go down or sunset the feature?

**Vendor contract red flags (when YOU are the buyer):**
- Auto-renewal with no notice period ("you're locked in for another year")
- Unilateral price increases ("we can raise your price by 20% at any time")
- No termination for convenience (you're stuck even if the product degrades)
- "We can use your data to improve our models" — for any vendor with access
  to customer data, this is a hard NO
- No SLA or uptime commitment (they go down, you have no recourse)

**Vendor procurement process:**
1. Business case: why do we need this? alternatives considered?
2. Security review: DPA + SOC2 + sub-processors
3. Commercial review: pricing, terms, auto-renewal
4. Legal review: MSA, DPA, any red flags
5. Approval: based on spend threshold ($1K: manager. $10K: VP. $50K: CEO)

### Phase 4: Contract Management

**Store contracts somewhere you can find them:**

- Contract repository: DocuSign, PandaDoc, Ironclad, or at minimum — a
  shared Google Drive folder with naming convention
- Key metadata per contract: counterparty, start date, end date, renewal
  terms, contract value, auto-renewal (Y/N), termination notice deadline
- Calendar reminders: 90 days before auto-renewal or expiration

**Contract tools:**
- DocuSign ($10-40/mo): e-signatures, templates, basic management
- PandaDoc ($19-49/mo): proposals, contracts, e-signatures
- Ironclad ($$$): enterprise contract lifecycle management
- Common Paper: open-source standard contracts for B2B SaaS

## Output Format

```
CONTRACT STACK — [Company]

STANDARD DOCUMENTS:
- [ ] MSA — [template ready / needs lawyer review / pending]
- [ ] Order Form — [template ready]
- [ ] SLA — [template ready. Uptime: X%]
- [ ] DPA — [template ready. SCCs: Yes/No]

CONTRACT PROCESS:
- Sales → Legal handoff: [when does legal get involved? $X threshold?]
- Average cycle time: [weeks from MSA sent → signed]
- Non-standard terms log: [what we've accepted and why]

VENDOR PROCUREMENT:
- [ ] Vendor security review checklist
- [ ] Procurement approval thresholds: $X / $Y / $Z
- Contract repository: [tool / folder]
```

## Quality Checklist

- [ ] MSA template reviewed by startup lawyer
- [ ] Order Form template ready — clean, simple, one page
- [ ] SLA with realistic uptime commitment (not 99.99%)
- [ ] DPA template ready for enterprise customers
- [ ] Liability cap: 12 months of fees (standard, defensible)
- [ ] Contract repository organized (DocuSign / PandaDoc / Ironclad)
- [ ] Vendor security review process documented
- [ ] Auto-renewal dates tracked with calendar reminders

## Common Pitfalls

1. **No standard MSA.** Every enterprise customer sends you THEIR contract.
   You're negotiating from their paper. Every time. Every deal takes months.
   Fix: Have your own MSA template. "We use our standard MSA. Our customers
   find it fair."

2. **Unlimited liability.** You signed a contract with no liability cap. A
   customer sues for $5M in damages from your $10K/year SaaS product. Your
   company is dead. Fix: Liability cap = 12 months of fees. Non-negotiable
   for early-stage companies.

3. **Custom contracts for every deal.** "This customer wants their own MSA."
   Now you're managing 50 unique contracts with different terms. Legal risk
   per contract. Fix: 80/20 rule. 80% of deals use standard contract. 20%
   negotiate minor terms. 0% get fully custom.

4. **No auto-renewal tracking.** Contract auto-renews at 3x the price.
   You didn't notice. Customer is furious. Fix: Calendar reminders 90 days
   before every renewal. Review terms before auto-renewal triggers.

5. **Ignoring vendor security review.** You bought a tool without checking
   its security. It gets breached. Your customer data is exposed. Your
   customer sues YOU — not the vendor. Fix: Security review every vendor
   that touches customer data. DPA + SOC2 minimum.

## Related Skills

- `legal-for-founders` — Foundational contracts, ToS, Privacy Policy
- `data-privacy-compliance` — DPA details, SCCs, GDPR requirements
- `security-assessments` — Vendor security questionnaires, pen testing
- `soc2-compliance` — SOC2 that every enterprise vendor review asks for
- `deal-desk` — Deal structuring, pricing, proposals