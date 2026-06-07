---
name: legal-for-founders
description: >-
  Complete legal playbook for SaaS founders — incorporation (Delaware C-Corp
  vs LLC), IP assignment, Terms of Service, Privacy Policy, NDAs, consulting
  agreements, co-founder IP, fundraising legal (SAFE, priced round, board
  consents), and when to hire a lawyer. Step-by-step checklists with YC,
  CooleyGO, Clerky, and Orrick resources. Triggers on: "legal for startup",
  "incorporate", "Terms of Service", "Privacy Policy", "NDA", "SAFE",
  "startup legal", "founder legal basics".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [legal, incorporation, terms-of-service, privacy-policy, nda, safe, ip, contracts, compliance, startup-law]
  related_skills: [soc2-compliance, data-privacy-compliance, equity-management, vendor-contracts, employment-compliance, business-insurance, co-founder-dynamics, fundraising-strategy]
  frameworks:
    - "YC Startup Documents (YC SAFE, Series Seed, incorporation docs)"
    - "Clerky — Standard incorporation, equity, and fundraising docs"
    - "CooleyGO — Free startup legal resources (Cooley LLP)"
    - "Orrick — Startup legal toolkit"
    - "Fenwick & West — Startup legal guides"
    - "Alex Macgillivray (Twitter, Google GC) — Platform legal"
---

# Legal for Founders

## Overview

Legal mistakes are the most expensive mistakes in startups — because you don't
discover them until years later, during fundraising, acquisition, or a lawsuit.
The mistake: "we'll fix the legal stuff later." A missing IP assignment can
kill a $100M acquisition. A handshake co-founder deal becomes a lawsuit at
$10M ARR. A copied Terms of Service gets you sued under GDPR. This skill
covers every legal foundation a SaaS founder needs: incorporation, IP,
contracts, privacy, and fundraising legal — with resources to do it right
without spending $50K on lawyers.

## When to Use

Trigger phrases: "incorporate startup", "Delaware C-Corp", "startup legal",
"Terms of Service template", "Privacy Policy for SaaS", "NDA template",
"SAFE agreement", "IP assignment", "founder legal checklist", "when to
hire a startup lawyer", "Clerky vs lawyer"

## When to Hire a Lawyer (and When Not To)

**Use standardized docs + AI review (don't need lawyer):**
- Incorporation (Clerky, Stripe Atlas, Firstbase.io)
- SAFE / convertible note (YC templates)
- Terms of Service (generator + review)
- Privacy Policy (generator + review)
- NDA (standard templates)
- Independent contractor agreements
- Offer letters (standard templates)

**Hire a lawyer for:**
- Priced equity rounds (Series A+)
- Acquisition / exit
- Complex IP situations (university IP, prior employer IP)
- Regulatory issues (fintech, healthcare, defense)
- Litigation or threats of litigation
- International entity setup
- Co-founder separation disputes

**How to hire a startup lawyer:**
- Look for: "emerging companies" or "venture capital" practice group
- Good signs: knows what a SAFE is without explanation, bills flat fees
  for standard work, has done 50+ Series Seed/A rounds
- Bad signs: suggests an LLC for a VC-backed startup, talks you out of
  Delaware, bills hourly for incorporation, has never heard of Clerky
- Top firms for startups: Cooley, Fenwick & West, Gunderson, Wilson Sonsini,
  Orrick, Goodwin Procter (they're expensive but venture-standard)
- Boutique options: many ex-Cooley/Fenwick partners at lower rates

## Step-by-Step Process

### Phase 1: Incorporation

**Delaware C-Corp (the startup standard):**

WHY Delaware C-Corp:
- Every VC requires it (SAFEs convert to C-Corp preferred stock)
- Best-developed corporate law in the US (predictable outcomes)
- Standard for 409A valuations and option plans
- Simple to convert to public company (IPO)

ALTERNATIVE: LLC (rare for VC-backed startups):
- OK for bootstrapped, lifestyle businesses
- Can convert to C-Corp later ($5-10K cost, 4-6 weeks)
- Tax-efficient for profit distributions (pass-through)
- NOT OK for VC funding — investors won't invest in LLCs

**Incorporation checklist (use Clerky, Stripe Atlas, or Firstbase.io):**
1. [ ] Choose company name (check Delaware availability + trademark)
2. [ ] File Certificate of Incorporation (Delaware)
3. [ ] Appoint registered agent in Delaware ($50-300/yr)
4. [ ] Adopt Bylaws (Clerky generates these)
5. [ ] Board consent: elect officers, authorize share issuance, set up bank
6. [ ] Issue founder shares (with vesting — 4-year, 1-year cliff)
7. [ ] File 83(b) election within 30 days of share issuance (CRITICAL —
   missing this can cost millions in taxes later)
8. [ ] Get EIN from IRS
9. [ ] Open business bank account
10. [ ] Qualify to do business in your home state (foreign qualification)
11. [ ] Set up cap table (Carta, Pulley, or Clerky)

**83(b) Election — do NOT miss this:**
- Without 83(b): you're taxed as shares vest. If your company grows, you owe
  tax on phantom income for shares you can't sell.
- With 83(b): you're taxed on the full grant value at grant date (usually $0
  — zero tax), and future appreciation is capital gains.
- Must be filed within 30 days of share issuance. No exceptions. No extensions.
  If you miss it, you can't fix it.
- Send certified mail with return receipt. Keep proof forever.

### Phase 2: IP Assignment

**The most important legal docs you'll sign:**

1. **Founder IP Assignment:** Every founder assigns ALL IP they create for the
   company to the company. Without this, the founder owns the IP personally
   and can walk away with it.

2. **Proprietary Information and Inventions Assignment Agreement (PIIA):**
   Every employee and contractor signs this. It says: "Everything you create
   for the company belongs to the company."

3. **Prior Inventions Disclosure:** If a founder or employee has prior IP (side
   projects, open source work), it must be listed on Schedule A. Everything NOT
   listed is assigned to the company.

**The "side project" problem:**
- If you don't disclose your side projects, the company can claim them
- If your side project is related to the company's business, it's theirs
- Rule: disclose everything on Schedule A. Better to over-disclose than lose
  your side projects in a due diligence nightmare.

### Phase 3: Terms of Service (ToS)

**Don't copy-paste from another startup. Their ToS was written for THEIR
product, risk profile, and jurisdiction. Yours needs to match YOUR business.**

**Essential ToS clauses for SaaS:**

| Clause | What It Does |
|---|---|
| **Acceptance** | How users agree (click-through, browse-wrap) |
| **Service Description** | What you provide, SLAs if any |
| **User Obligations** | What users can't do (reverse engineer, resell, spam) |
| **Payment Terms** | Pricing, billing, refunds, cancellations |
| **Intellectual Property** | Who owns what — you own the platform, they own their data |
| **Data & Privacy** | Reference to Privacy Policy. Data handling, DPA availability |
| **Limitation of Liability** | Cap your exposure (typically fees paid in last 12 months) |
| **Disclaimer of Warranties** | "AS IS" — no guarantees beyond what you explicitly offer |
| **Indemnification** | User indemnifies you for their misuse |
| **Termination** | How either party can end the relationship |
| **Governing Law** | Delaware (or your jurisdiction). Arbitration clause? |

**ToS generation resources:**
- CooleyGO Terms of Service Generator (free — best starting point)
- Termly.io ($10-20/mo — auto-generated, monitored for legal changes)
- Iubenda ($9-29/mo — international, multilingual)
- Basecamp's open-source ToS policies (start from theirs, adapt)

### Phase 4: Privacy Policy

**Legally required in almost every jurisdiction.** GDPR, CCPA, CalOPPA all
require a published privacy policy.

**Essential Privacy Policy sections:**

1. **What data you collect:** Email, name, company, payment info, usage data,
   cookies, IP address — be specific, not vague.

2. **How you use it:** Provide service, improve product, communicate, billing.
   Don't say "and other purposes" — that's a GDPR violation.

3. **Who you share it with:** Sub-processors (AWS, Stripe, Intercom — name
   them), analytics, legal requirements.

4. **Cookies and tracking:** What cookies you use, what they do, how to opt
   out. Required under ePrivacy Directive in EU.

5. **Data retention:** How long you keep data. "As long as account is active"
   + "30 days after account deletion" (or similar — be specific).

6. **User rights:** Right to access, correct, delete, export data. Required
   under GDPR, CCPA, and similar laws.

7. **International transfers:** If you transfer data from EU to US, you need
   Standard Contractual Clauses (SCCs) or a valid transfer mechanism.

8. **Children's privacy:** COPPA compliance if under 13 (most B2B SaaS can
   say "not for children under 13" — but you must say it).

9. **Changes to policy:** How you'll notify users. "We'll email you 30 days
   before changes take effect."

10. **Contact:** Privacy email address. privacy@[company].com

**Privacy Policy generation resources:**
- Termly.io Privacy Policy Generator (free for basic)
- Iubenda Privacy and Cookie Policy Generator
- CooleyGO Privacy Policy Generator
- Have a lawyer review before launch (seriously — this is the one doc that
  can get you in trouble if it's wrong)

### Phase 5: NDAs and Consulting Agreements

**NDA (Non-Disclosure Agreement) — when to use:**
- Sharing proprietary information with a potential partner or contractor
- M&A discussions (your lawyer will handle this)
- Employee/contractor onboarding (but the PIIA covers this already)

**NDA — when NOT to use:**
- Pitching VCs (they won't sign — and you don't need them to)
- Talking to customers about their problems (they'll walk away)
- Standard sales conversations (it's weird — don't do it)

**Template:** YC has a free mutual NDA template. Use it.

**Consulting/Contractor Agreement — essentials:**
1. Scope of work (specific deliverables, timeline)
2. Payment terms (rate, invoicing, payment schedule)
3. IP assignment (work product belongs to you — CRITICAL)
4. Confidentiality
5. Independent contractor relationship (not employee — important for tax)
6. Termination (either party, X days notice)
7. Non-solicitation (can't poach your employees — typically 12 months)

### Phase 6: Fundraising Legal

**SAFE (Simple Agreement for Future Equity):**
- YC standard SAFE — use the template. Don't modify it unless your lawyer
  has a VERY good reason.
- 4 flavors: Cap, No Cap, Discount, MFN (Cap is most common)
- No board seat, no governance rights, no maturity date, no interest
- Converts at next priced round (with Cap or Discount)
- Post-money SAFE (since 2018): dilution is clear at time of signing
- YC SAFE docs: free at ycombinator.com/documents

**Series Seed / Series A:**
- Hire a lawyer. This is not DIY territory.
- Key documents: Stock Purchase Agreement, Amended Certificate of Incorporation,
  Investor Rights Agreement, Right of First Refusal, Voting Agreement
- Board composition: typically 2 founders + 1 lead investor + 1 independent
- Protective provisions: list of things investors can veto. Standard set is
  fine. Avoid veto on budget or hiring.

## Output Format

```
LEGAL FOUNDATIONS — [Company]

INCORPORATION:
- Entity: [DE C-Corp / LLC]
- Filing Date: [date]
- Registered Agent: [name]
- EIN: [obtained / pending]
- Foreign Qualification: [states]
- 83(b) Filed: [YES / PENDING — DO NOT MISS THIS]

IP ASSIGNMENT:
- Founder PIIAs: [signed by all founders?]
- Employee/Contractor PIIAs: [standard form in place?]
- Prior Inventions Disclosures: [complete for all founders?]

KEY DOCUMENTS (status):
- [ ] Certificate of Incorporation — [filed / needs filing]
- [ ] Bylaws — [adopted / pending]
- [ ] Founder IP Assignment — [signed / missing — FIX IMMEDIATELY]
- [ ] Terms of Service — [published / draft / needs review]
- [ ] Privacy Policy — [published / draft / needs review]
- [ ] NDA (standard) — [template created / needed]
- [ ] Consulting Agreement — [template created / needed]
- [ ] SAFE docs (if raising) — [YC template / custom]

LAW FIRM:
- Firm: [name]
- Contact: [name, email]
- Flat fees for: [incorporation, SAFE, Series Seed]
```

## Quality Checklist

- [ ] Incorporated in Delaware as C-Corp (if raising VC) — or intentional LLC choice
- [ ] 83(b) election filed within 30 days (keep proof forever)
- [ ] All founders signed IP assignment (PIIA) — no exceptions
- [ ] Prior Inventions Disclosure complete for all founders
- [ ] Terms of Service published and matches your actual business
- [ ] Privacy Policy published — accurate, specific, not copy-pasted
- [ ] DPA available for enterprise customers (required for GDPR compliance)
- [ ] Cookie consent mechanism if you have EU visitors (essential)
- [ ] Standard NDA and Consulting Agreement templates ready
- [ ] Fundraising docs using YC SAFE (not custom unless lawyer-reviewed)

## Common Pitfalls

1. **Missing 83(b) election.** Miss the 30-day window and you can be taxed on
   millions in phantom income as your company grows. Fix: File immediately
   after receiving shares. Certified mail. Keep proof.

2. **No IP assignment.** Founder builds the product. Keeps the IP personally.
   Leaves. Company has nothing. Fix: All founders sign PIIA before writing
   any code. If you haven't — do it this week.

3. **Copy-pasted Privacy Policy.** "We don't use cookies" (but you use Stripe,
   Intercom, Google Analytics — all of which use cookies). This is false.
   GDPR fines: up to 4% of global revenue. Fix: Write an accurate policy
   that matches what you actually do.

4. **Shaking hands on equity splits.** "50/50, we trust each other." No
   vesting. No agreement. No IP assignment. This is not a company — it's
   a lawsuit waiting to happen. Fix: Clerky incorporation with 4-year
   vesting. All founders sign.

5. **Using the wrong SAFE.** Pre-money SAFE (pre-2018) means dilution is
   unclear. Post-money SAFE (current YC standard) is clearer. Fix: Use
   the YC post-money SAFE. Don't modify unless your lawyer says so.

6. **No DPA for enterprise customers.** Enterprise customers will send you
   a DPA to sign. If you don't have one, they won't buy. Fix: Have a
   standard DPA ready. Termly and Iubenda can generate one. Lawyer-review
   if you're enterprise-scale.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available
frameworks and operator experience. It is NOT legal advice, accounting advice,
tax advice, financial advice, or professional services advice. Laws, regulations,
and best practices vary by jurisdiction and change over time.

- **Legal matters:** Consult a qualified attorney licensed in your jurisdiction.
- **Tax matters:** Consult a certified tax professional or CPA.
- **Accounting/financial matters:** Consult a qualified accountant or financial advisor.
- **Insurance matters:** Consult a licensed insurance broker.
- **Security/compliance matters:** Consult a qualified professional for your specific
  infrastructure and regulatory requirements.

This skill references publicly documented frameworks, standards, and operator
experiences. It does not constitute a professional opinion or create a
professional-client relationship. Use it as a starting point for your own
research and always verify against current regulations and professional guidance.

## Related Skills

- `soc2-compliance` — SOC2 Type II for SaaS
- `data-privacy-compliance` — GDPR, CCPA, data processing, cookie consent
- `equity-management` — Cap tables, 409A, option pools, equity types
- `vendor-contracts` — DPAs, MSAs, vendor security reviews
- `employment-compliance` — Contractor vs employee, offer letters, equity docs
- `business-insurance` — Insurance for SaaS companies
- `co-founder-dynamics` — Co-founder agreements, equity splits
- `fundraising-strategy` — SAFEs, priced rounds, term sheets