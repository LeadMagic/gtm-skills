# Ramp Card Policy — GTM Stack

**Company:** ___ **Program admin:** RevOps + Finance

---

## Card types

| Type | Use | Who holds |
|---|---|---|
| **Vendor virtual (primary)** | Recurring SaaS — one card per vendor | RevOps pool; merchant locked |
| **Department budget** | Ads, events | Marketing lead |
| **Travel / field** | Physical card | Sales managers |
| **Trial** | 14-day eval | Requesting manager; auto-expire |
| **Gifting** | Sendoso / Alyce | ABM owner; monthly cap |

**Prohibited:** Shared company card credentials; personal card for recurring GTM SaaS.

---

## Standard GTM virtual cards

| Card ID | Vendor | GL code | Monthly limit $ | Merchant lock | Owner |
|---|---|---|---:|---|---|
| GTM-CRM-01 | [HubSpot/SF/Attio] | GTM-Sales-Tools |  | ☐ | RevOps |
| GTM-SEQ-01 | [Outreach/etc] | GTM-Sales-Tools |  | ☐ | RevOps |
| GTM-GONG-01 | Gong | GTM-Sales-Tools |  | ☐ | RevOps |
| GTM-DATA-01 | Clay | GTM-Data |  | ☐ | RevOps |
| GTM-ENR-01 | LeadMagic/API | GTM-Data |  | ☐ | RevOps |
| GTM-MA-01 | HubSpot MA | GTM-Marketing |  | ☐ | Marketing |
| GTM-ADS-01 | Google/Meta | GTM-Marketing |  | ☐ | Marketing |
| GTM-GIFT-01 | Sendoso | GTM-Gifting |  | ☐ | Marketing |

Limits = approved ACV ÷ 12 × 1.05 buffer (or lower for credit tools).

---

## Alerts

| Threshold | Action |
|---|---|
| 80% monthly limit | Slack #revops-alerts |
| 100% limit | Hard decline; RevOps reviews |
| New merchant on GTM card | Flag unless pre-approved vendor |

---

## Employee lifecycle

| Event | Ramp action |
|---|---|
| New GTM hire | No default SaaS cards — team tools via vendor cards |
| Role change | Review trial cards; revoke if any |
| Resignation / term | Freeze personal cards day 0; audit trials started |
| Vendor sunset | Terminate virtual card; rotate if compromised |

---

## Bill pay (not card)

| Vendor | Annual ACV | Invoice owner |
|---|---:|---|
| Salesforce enterprise |  | Finance + RevOps |
| ZoomInfo / data |  | RevOps |

Bill pay requires approval matrix sign-off before scheduling payment.

---

## Reconciliation (monthly)

- [ ] Ramp export ↔ vendor-spend-register
- [ ] Variance >10% explained
- [ ] Receipts attached per policy
- [ ] Accounting sync clean

Playbook: `references/ramp-playbook.md`
