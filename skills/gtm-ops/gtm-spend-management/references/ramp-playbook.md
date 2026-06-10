# Ramp Playbook — GTM Spend

*Ramp: corporate cards, virtual cards, spend controls, bill pay, accounting sync.
Verify current Ramp features at [ramp.com](https://ramp.com) before rollout.*

---

## Why Ramp for GTM

| Problem | Ramp fix |
|---|---|
| SaaS on personal Amex | Central visibility + policy |
| 40 vendors, one statement | Virtual card per vendor in GL |
| Annual invoice chaos | Bill pay + approval workflow |
| Renewal surprises | Merchant-level spend history |
| Receipt hunting | Auto-capture + accounting sync |

Pair with `gtm-tool-cost-model` for **planned** spend; Ramp shows **actual** spend.

---

## Setup checklist (Week 1)

### Foundation

- [ ] Connect accounting (QuickBooks / NetSuite / Xero)
- [ ] Map GL accounts: `GTM-Sales-Tools`, `GTM-Data`, `GTM-Marketing`, `GTM-Gifting`, `GTM-Cloud`
- [ ] Invite Finance + RevOps as admins
- [ ] Receipt policy: required ≥$25 (adjust per policy)
- [ ] Enable spend alerts at 80% of card limits

### Departments & users

| Ramp entity | Maps to |
|---|---|
| Sales | AE, SDR, sales managers |
| Marketing | Demand gen, events, ABM |
| RevOps | Stack owner — approves new tools |
| Customer Success | Support tools (separate from GTM if needed) |

### Virtual cards — GTM vendor pattern

Create **one virtual card per core vendor**:

| Vendor | Suggested limit/mo | Merchant lock | Owner |
|---|---:|---|---|
| HubSpot / Salesforce | Per contract ÷ 12 | Vendor MCC | RevOps |
| Clay | Credit runway × $/credit | clay.com | RevOps |
| Gong / Chorus | Seats × price | Vendor | RevOps |
| Outreach / Salesloft | Mailboxes × price | Vendor | RevOps |
| LeadMagic / enrichment API | Usage cap | API vendor | RevOps |
| Sendoso | ABM gifting budget | sendoso.com | Marketing |
| LinkedIn Sales Nav | Seats | LinkedIn | Sales |
| Google Ads / Meta | Campaign cap | Platform | Marketing |

Template: `templates/ramp-card-policy-gtm.md`

### Bill pay (annual contracts)

Use bill pay for:

- Salesforce annual invoice
- HubSpot annual prepay
- ZoomInfo / enterprise data contracts
- Conference sponsorship invoices

Workflow: vendor invoice → approval matrix → bill pay → attach MSA/order form → sync to GL.

---

## Spend controls

| Control | Setting |
|---|---|
| **Per-transaction max** | Trial tools: $500; production: per vendor contract |
| **Monthly cap** | Per virtual card = budget ÷ 12 |
| **Category lock** | Software/SaaS MCC where supported |
| **Receipt required** | Yes for audit / SOC2 vendor spend trail |

### Per-rep discretionary (optional)

If allowed at all:

- $50–100/mo virtual card for **trials only**
- 14-day expiry; must convert to roster + proper card or cancel
- Manager approval in Ramp before issue

---

## Accounting sync

| Ramp field | Accounting |
|---|---|
| Merchant name | Vendor in register |
| GL code | GTM category |
| Department | Sales / Marketing / RevOps |
| Memo | Owner email + tool purpose |

**Monthly close:** Finance reconciles Ramp ↔ `vendor-spend-register.md` ↔ `tool-cost-sheet.md`.

---

## Offboarding

When GTM hire leaves:

- [ ] Freeze personal Ramp cards same day
- [ ] Rotate shared virtual cards they knew (if any — avoid shared)
- [ ] Audit trials they started

Cross-ref: `gtm-leadership` resignation handoff; `soc2-compliance` access removal.

---

## Ramp alternatives

| Platform | When |
|---|---|
| **Brex** | Similar; evaluate existing banking relationship |
| **Airbase / Zip** | Heavy procurement + approval workflows |
| **Mesh** | EU-heavy teams |

**Rule:** One primary spend platform — duplicate programs hide spend.

---

## Integration with skills

| Task | Skill |
|---|---|
| TCO budget | `gtm-tool-cost-model` |
| New tool approval | `revops-tech-stack` + `spend-approval-matrix` |
| Contract terms | `vendor-contracts` |
| Gifting caps | `strategic-gifting` |
