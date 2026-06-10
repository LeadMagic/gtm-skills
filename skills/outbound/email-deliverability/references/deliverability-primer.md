# Deliverability Primer

Foundation for cold outbound infrastructure. Used by `email-deliverability`, `domain-infrastructure`, `cold-email-strategy`, `cold-email-copywriting`, and `sending-platforms`.

---

## Core concepts

| Term | Meaning |
|---|---|
| **SPF** | DNS record listing authorized senders |
| **DKIM** | Cryptographic signature proving message integrity |
| **DMARC** | Policy for failed SPF/DKIM; reporting |
| **Domain reputation** | ISP trust score for sending domain |
| **Inbox placement** | % landing in primary vs spam/promotions |
| **Warm-up** | Gradual volume ramp on new domains/mailboxes |

---

## Minimum technical stack

1. Dedicated sending domain (not primary corporate domain)
2. SPF + DKIM + DMARC `p=none` → `quarantine` → `reject` over time
3. Google Workspace or Microsoft 365 mailboxes (avoid cheap SMTP-only)
4. Custom tracking domain for sequencer (CNAME)
5. List hygiene before every send

---

## Volume guardrails (new domain)

| Week | Max cold emails/mailbox/day |
|---|---:|
| 1 | 10–15 |
| 2 | 20–30 |
| 3 | 30–40 |
| 4+ | 40–60 (monitor bounce/spam) |

See `sending-limits-reference.md` for platform-specific caps.

---

## Health signals

| Signal | Green | Red flag |
|---|---|---|
| Bounce rate | <2% | >5% |
| Spam complaint rate | <0.1% | >0.3% |
| Open rate (cold) | 30–60% (directional) | <15% sustained |
| Reply rate | Motion-dependent | Sudden zero across mailboxes |

**Fix order:** list quality → domain/auth → copy/spam triggers → volume.

---

## Spam trigger avoidance

- No URL shorteners in first touch
- Limit images and HTML complexity
- Plain-text or light HTML for cold
- Unsubscribe / opt-out honor <24h
- No purchased lists

---

## Multi-domain strategy

| Domain type | Use |
|---|---|
| `company.com` | Customer success, transactional |
| `trycompany.com` / `getcompany.com` | Outbound only |
| Per-region variants | Geo-specific campaigns |

Rotate domains when placement degrades — don't burn corporate root.

---

## Sequencer alignment

- One mailbox per user identity (no shared "sales@" cold blast)
- Match From name to real human
- Spread sends across business hours in recipient TZ
- Cap daily sends per `sending-platforms` config

---

## When to pause sends

- Blacklist appearance (check MXToolbox)
- Google Postmaster spam rate spike
- >3% hard bounce on a campaign
- Domain age <14 days without warm-up
