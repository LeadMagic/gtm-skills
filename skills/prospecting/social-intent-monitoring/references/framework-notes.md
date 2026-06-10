# Social Intent Monitoring — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- ****

## Authoritative foundations

### Max Mitchum — Signal, Context, Action Framework

Max Mitchum, Co-Founder & CEO of Trigify.io, published the Signal, Context,
Action model as the operating framework for signal-led outbound. The three
layers:

**Signal** — the public event that suggests an account is worth contacting
now. Examples from Mitchum's 2026 playbook: competitor engagement on LinkedIn
or X, hiring posts for GTM roles, founder or operator posts describing a
problem you solve, funding reactions, pain-point mentions in comments, product
launches in adjacent categories, public recommendation requests.

**Context** — the judgement layer. Who is this person? What company? Are they
in ICP? Why does this specific event matter? Is the timing strong? A signal
without context is noise; context without a signal is guessing.

**Action** — the downstream workflow. Enrich the person, find the email,
research the company, draft the message anchored to that specific signal,
push into the sequencer, alert the rep in Slack with the reasoning.

Source: https://maxmitcham.substack.com/p/48-meetings-from-120-leads-in-two

The core principle: the email is the commodity. AI can write decent emails.
The moat is knowing when the

*(See SKILL.md for full detail.)*

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4
- Phase 5
- Phase 6

## Key reference tables

| Signal Type | Description | Urgency | Outreach Angle |
|---|---|---|---|
| **Competitor engagement** | Prospect comments on, likes, or shares competitor content | High — 24-48hr window | Offer comparison, address common pain with that competitor |
| **Problem statement post** | Founder or operator publicly describes a problem you solve | High — act within 12 hrs | Reference their exact words; offer a specific solution |
| **Recommendation request** | "Does anyone have a recommendation for X?" | Very High — act within 2 hrs | Direct reply + personal DM |
| **Hiring for GTM role** | Post about hiring SDR, RevOps, VP Sales — roles your product supports | Medium — 3-5 day window | Tie outreach to the hiring intent; new hires evaluate tools |
| **Funding reaction post** | Company or founder posts about closing a round | Medium — 1 week window | Congratulate + connect to common post-funding challenges |
| **Pain-point comment** | Target prospect comments on someone else's post about a problem | High — act within 48 hrs | Reference the comment thread; show understanding |
| **Content engagement pattern** | Prospect consistently engages with content in your category | Low/Medium — warm long-play | Nurture track; add to account monitoring |

| Account Tier | Signal Strength | Action |
|---|---|---|
| Named target account | Any qualifying signal | Immediate Slack alert + email enroll |
| ICP-match not on named list | High signal (recommendation request, problem post) | Email enroll + add to CRM |
| ICP-match not on named list | Medium signal (competitor engagement, hiring post) | CRM add + nurture track |
| Non-ICP | Any signal | Discard |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
