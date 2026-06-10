# Referral Programs — Framework Notes

Reference tables for `SKILL.md`. Apply these to design decisions, benchmark
comparisons, and measurement targets — not as decorative citations.

---

## B2B SaaS Referral Benchmark Table

Sources: GrowSurf statistics roundup (citing OpenView, ProfitWell, SaaSquatch);
Cello B2B SaaS referral guides; Schmitt, Skiera & Van den Bulte (2011).

| Metric | Benchmark Range | Source |
|---|---|---|
| Referral share of new customers | 20-40% | GrowSurf / OpenView |
| Referred customer LTV vs non-referred | +16-25% | Schmitt et al. (2011); SaaSquatch |
| Referred customer churn vs non-referred | ~20% lower | ProfitWell / SaaSquatch |
| Referred leads conversion rate vs paid | 3-5x higher | GrowSurf / Cello |
| Program participation rate (active users) | 5-15% healthy | GrowSurf |
| Invitation acceptance rate | 25-40% | SaaSquatch |
| Referral CAC vs blended CAC | 40-60% lower | OpenView / Cello |
| In-app prompts vs email-only shares | ~4x more shares | GrowSurf |
| Credit/product rewards vs cash (SaaS) | Often higher participation | SaaSquatch |

**How to use this table:** Set program-specific targets before launch. If
participation drops below 3% of active users after 60 days, the incentive or
the in-app prompt placement needs redesign — not more marketing spend.

---

## Case Study Notes — Dropbox and PayPal

### Dropbox (2008-2009)
- **Program:** Double-sided storage reward — 500MB to referrer, 500MB to referred
- **Result:** 3,900% user growth in approximately 15 months (documented in Drew
  Houston's 2010 Startup Lessons Learned presentation)
- **Design lesson:** Reward currency matched the product value metric exactly.
  Dropbox's core value = storage. Giving storage as a reward reinforced the
  product's reason for being and drove additional usage, not just sign-ups.
  Cash would have been weaker because it does not create product engagement.
- **Transferable rule:** Before choosing cash rewards, ask: what is our product's
  value metric? If the metric is time saved, reward time (credits). If it is
  storage, reward storage. If it is data/leads/connections, reward those.

### PayPal (1999-2000)
- **Program:** Double-sided cash — initially $20 to referrer, $20 to referred;
  later reduced to $10/$10 as growth cost scaled
- **Result:** ~7-10% daily user growth at peak (documented in Elon Musk and
  Peter Thiel interviews; referenced in Thiel's *Zero to One*)
- **Design lesson:** Cash worked because the adoption barrier for PayPal was
  trust in payments. The reward matched the friction. A user who received $20
  in their PayPal account was immediately demonstrating the product's core
  promise: money moves digitally between people.
- **Caveat:** PayPal's margins and growth stage allowed this. Cash rewards
  scale in cost linearly and do not create product stickiness the way credit
  rewards do. Reducing from $20 to $10 maintained growth, confirming the
  network effect — not the cash value — was the real driver after critical mass.

---

## Incentive Design Decision Tree

Use this to select incentive model. Work top to bottom; first match wins.

```
1. Is the product's core value metric quantifiable and deliverable as a reward
   (e.g., storage, API calls, seats, credits)?
   → YES: Use double-sided product credit (Dropbox model)
   → NO: Continue

2. Is trust or price the primary adoption barrier for the referred prospect?
   → YES: Use double-sided cash (PayPal model); match amount to friction level
   → NO: Continue

3. Is the product freemium with a meaningful premium ceiling?
   → YES: Use feature unlock (unlock premium with N referrals)
   → NO: Continue

4. Is the product in pre-launch or invite-only mode?
   → YES: Use status/priority reward (waitlist jump, early access)
   → NO: Continue

5. Is the customer base mission-driven (nonprofit, social enterprise)?
   → YES: Consider charitable donation; pair with product credit for higher uptake
   → NO: Default to double-sided cash at 10-15% of year-1 ACV for B2B SaaS
```

---

## Schmitt, Skiera & Van den Bulte (2011) — Key Findings Summary

Full citation: Schmitt, Philipp, Bernd Skiera, and Christophe Van den Bulte.
"Referral Programs and Customer Value." *Journal of Marketing* 75.1 (2011): 46-59.
Institutions: Wharton School (UPenn) and Goethe University Frankfurt.

**Core finding:** Referred customers had approximately 16% higher CLV than
non-referred customers acquired through other channels, measured over 33 months
at a German bank.

**Supporting findings:**
- Referred customers had higher contribution margin (they bought more, at better margins)
- Referred customers had higher retention rates (they churned less)
- The CLV gap widened over time — referred customers compounded value

**Critical caveat (frequently ignored):** The CLV advantage was smaller for
older customers and customers in lower-margin product categories. This means:
- Do not apply referral program incentives uniformly to all customer segments
- Target the ask at high-margin, high-engagement customers who operate in
  networks of similar companies
- Measure referred cohort quality (LTV, churn) separately from non-referred
  cohort — do not assume program success from lead volume alone

**Implication for double-sided design:** The study's findings support double-sided
rewards because both sides benefit, reducing the social cost of referring (referrer
does not feel they are exploiting a relationship). One-sided cash to the referrer
alone creates a transactional dynamic that weakens trust transfer.

---

## Fraud Prevention Rules Reference

Hard rules that must be encoded in platform configuration, not just documented:

| Rule | Implementation |
|---|---|
| Pay on collection | Reward trigger = first payment received, not sign-up |
| Block self-referral | Compare referrer email domain to referred account domain |
| Minimum milestone requirement | Referred account must reach activation milestone before reward pays |
| Monthly reward cap per referrer (launch period) | Cap at 5-10 rewards/month to detect gaming; raise after 60 days |
| Unique link per referrer | One trackable link per customer; no shared or reused links |
| Delayed payout | 30-day hold on reward after conversion; allows for charge-back / fraud review |
