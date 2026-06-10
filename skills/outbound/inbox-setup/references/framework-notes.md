# Inbox Setup — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Google Bulk Sender Guidelines**
- **Microsoft Email Sender Guidelines**
- **Eric Nowoslawski Sending Volume Strategy**
- **Jed Mahrle Cold Email Infrastructure**

## Authoritative foundations

- **Google Bulk Sender Guidelines** — sender authentication, low spam complaint rates, and authenticated alignment are baseline requirements for sustainable outbound.
  Domain isolation is non-negotiable: never send cold from the primary business domain; use separate sending domains with independent reputation.
- **Microsoft Email Sender Guidelines** — maintain authenticated mail, clean lists, low complaints, and conservative volume ramps to protect sender reputation.
- **Eric Nowoslawski (Growth Engine X)** — inbox infrastructure at scale
  emails/month. Strategy: 2 inboxes per domain, 30 emails/day per inbox,
  3-week warmup minimum, keep 50% spare capacity warming at all times.
- **Jed Mahrle (Practical Prospecting)** — 30,000+ subscribers. "Cold email
  isn't a numbers game anymore. It's a relevance game. Send fewer emails to
  better fit accounts."

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4
- Phase 5

## Key reference tables

| Provider | Cost/Mailbox | Mailboxes/Domain | Sends/Day/Mailbox | Best For |
|---|---|---|---|---|
| **Google Workspace** | $6-15/mo | 2-3 | 25-30 | Highest deliverability, preferred by Google recipients |
| **Microsoft 365** | $4-6/mo | 25 | 10 | High deliverability to Outlook, best mailbox-to-domain ratio |
| **Azure/Entra (via Hypertide)** | $50/order (100 inboxes) | 50 | 2 (after warmup) | Maximum scale, lowest cost per inbox |
| **SMTP (via ScaledMail)** | $3.50-4/mo | 4 | 10 | Budget option, works with any sequencer |

| Provider | What They Do | Best For |
|---|---|---|
| **ScaledMail** | Done-for-you inbox provisioning. Google, M365, SMTP. 230K+ inboxes managed. | Teams that want hands-off setup |
| **Hypertide** | Automated Azure/Entra inboxes in 4-6 hours. Tenant isolation. $50/mo per 100 inboxes. | High-volume agencies, max scale |
| **Mailforge** | Full DNS monitoring, custom warmup, inbox health reports | Teams that want control + visibility |
| **Maildoso** | Pre-configured inboxes + domains + DNS. Master inboxes. | Budget-conscious teams |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
