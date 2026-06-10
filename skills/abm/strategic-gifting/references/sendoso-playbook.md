# Sendoso Playbook

**Sendoso** — sending platform for revenue teams (eGifts, physical gifts, direct mail,
CRM integrations). Use for **execution** after Giftology strategy is defined.

**Public:** [sendoso.com](https://sendoso.com/)

## When Sendoso Fits

- SDR/AE team needs self-serve sends with guardrails
- Salesforce / HubSpot / Outreach / Salesloft in stack
- Mix of eGift (speed) and physical (Tier 2–3)
- Finance wants spend tracking per team/account

## Setup Checklist

- [ ] Integrate CRM (Contact/Lead → Sendoso)
- [ ] SSO + role permissions (who can send >$X)
- [ ] Manager approval queue for physical > threshold
- [ ] Budget caps per user / per team / month
- [ ] Address confirmation ON for physical
- [ ] Custom note template (Giftology — no logo items in Tier 1)
- [ ] CRM write-back: gift type, $, date, campaign, note

## Campaign Types

| Type | Use | Tier |
|---|---|---|
| eGift (coffee, lunch) | Fast thank-you post-meeting | 2–3 |
| Physical marketplace | Curated items with note | 2 |
| Custom bundle | AE-assembled with approval | 1 |
| Direct mail + note | Book, report, handwritten | 1–2 |

## Workflow (ABM-aligned)

```
1. AE completes gift-brief.md
2. Manager approves (Tier 1) or auto (Tier 3 eGift cap)
3. Sendoso sends + address confirm
4. CRM task: "Gift delivered — call within 24h"
5. SDR/AE references gift in follow-up (story, not "did you get my gift?")
```

## Messaging After Delivery

**Do:** "Hope the [specific item] was useful after our chat about [topic]."

**Don't:** "Just checking you got my gift" (transactional).

## Analytics

Track in Sendoso + CRM:
- Sends → meetings booked (gift-influenced touch)
- Cost per meeting
- Approval reject rate (compliance)

## Alternatives

See `gifting-platforms.md` — Alyce (recipient choice), Reachdesk (global), Postal (mail).
