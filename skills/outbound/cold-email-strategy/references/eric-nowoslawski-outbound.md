# Eric Nowoslawski — Growth Engine X Outbound Playbook

**Sources:** Eric Nowoslawski — [growthenginex.com](https://www.growthenginex.com/) · 💼 [LinkedIn](https://www.linkedin.com/in/outboundphd/) · 𝕏 [@ENowoslawski](https://x.com/ENowoslawski) · ▶ [YouTube](https://www.youtube.com/channel/UC6ef5yDFz7gm8rARwX3HaDw) · [Smartlead case study — 1.5M emails/mo](https://www.smartlead.ai/case-study/case-study-eric-nowoslawski-growth-engine-x) · [GTM Engineer — Winning Cold Outbound Formula](https://thegtmengineer.substack.com/p/the-winning-cold-outbound-formula) · [Alex Berman — Creative Ideas Campaign](https://alexberman.com/creative-ideas-campaign-cold-email-infrastructure) · [LinkedIn — deliverability changes](https://www.linkedin.com/posts/outboundphd_here-are-some-changes-we-saw-with-email-deliverability-activity-7274777906105442306-YDd2) · [LinkedIn — 30 vs 50+ sends/day test](https://www.linkedin.com/posts/outboundphd_i-put-a-commonly-accepted-email-rule-and-activity-7284664261216206849-q43z)

**Canonical expert entry:** `references/experts.md` → Eric Nowoslawski

**Identity:** Founder **Growth Engine X (GEX)**; Clay Enterprise Partner; Clay's first marketing contractor (pre-agency). Agency sends millions of cold emails/month for 300+ clients — largest Clay user by enrichment volume.

---

## Core Thesis

Outbound at scale is an **infrastructure + offer** problem, not a signals arms race. Deliverability discipline and backup capacity let you survive spam complaints; **offers so strong prospects would pay for the discovery call** drive reply rates. Personalization without a differentiated offer is slop.

> "Sometimes people ask to pay me for coaching on our deliverability strategy and it's so simple I really can't take their money." — Eric Nowoslawski

**Complementary lane:** Jordan Crawford / Pat Spielmann / Becc Holland / Guillaume Moubeche own **segment research, copy structure, and sequence architecture**. Eric owns **unit-economics gate, infra at scale, Clay agency execution, and offer-led campaign types** — use both, don't duplicate.

---

## Primary Frameworks

### 1. Outbound Unit Economics Gate

Before building infra or Clay tables, validate cold outbound math:

| Criterion | GEX guidance |
|---|---|
| **TAM** | Prefer **>100,000** addressable accounts |
| **Customer LTV** | Prefer **>$10,000** |
| **CAC : LTV** | Ideal **1:10**; **1:3** minimum for healthy margins |

If unit economics fail, fix offer/pricing/ICP before scaling sends.

**Source:** [GTM Engineer podcast](https://thegtmengineer.substack.com/p/the-winning-cold-outbound-formula)

---

### 2. Cold Email Infrastructure at Scale

Operational defaults GEX uses across high-volume clients:

| Rule | Value | Notes |
|---|---|---|
| Inboxes per domain | **2** | Better than 10; 3 untested vs 2 |
| Sends per inbox per day (baseline) | **30** | Starting point; not hard ceiling |
| Warmup minimum | **3 weeks** | Plan for inboxes still not ready at 3 weeks |
| Backup capacity | **50% of active sending** | Spare inboxes always warming |
| 1:1 backup rule | Backup inboxes **=** active sending capacity | Zero-downtime swap when primaries burn |
| Provider mix | Google + Outlook | Outlook filters can be stricter — monitor placement |
| Burned inbox recycle | **No longer reliable** | If reply rates drop, don't relaunch same inboxes |

**Volume escalation (winning campaigns only):** If **~1 positive reply per 50 sends**, test pushing past 30/day — GEX has run winning campaigns above 50/day with stable placement. Requires inbox placement tests before/after ramp.

**Sources:** [LinkedIn deliverability post](https://www.linkedin.com/posts/outboundphd_here-are-some-changes-we-saw-with-email-deliverability-activity-7274777906105442306-YDd2) · [30 vs 50+ test](https://www.linkedin.com/posts/outboundphd_i-put-a-commonly-accepted-email-rule-and-activity-7284664261216206849-q43z)

---

### 3. Crawl → Walk → Run (Clay + Outbound Rollout)

| Phase | Action | Output |
|---|---|---|
| **Crawl** | Manual campaigns for 5–10 target companies — **no AI** for first examples | Training examples + tone/format anchors |
| **Walk** | Build system prompt with business context + manual examples; constrain AI to real capabilities | Repeatable prompt template; review first 50 outputs |
| **Run** | Automate in Clay → push to Smartlead/SEP; Supabase for block lists + metrics | Production workflow at scale |

Do not skip Crawl — AI without human examples hallucinates features and tone.

**Source:** [GTM Engineer podcast](https://thegtmengineer.substack.com/p/the-winning-cold-outbound-formula) · [Alex Berman Creative Ideas breakdown](https://alexberman.com/cold-email-automation-clay-creative-ideas-breakdown)

---

### 4. Creative Ideas Campaign

GEX's highest-performing campaign type across clients (including public companies):

**Structure:**
```
Hey {{first_name}} — I had some ideas about how we could target {{customer types}} together.
Here's what I'm thinking:
- {{Idea 1 — constrained to real capability A}}
- {{Idea 2 — constrained to real capability B}}
- {{Idea 3 — constrained to real capability C}}
{{Brief value prop + CTC}}
```

**Rules:**
- Each idea = different **flavor** of customer's offer — predetermined value props, not random AI suggestions
- Input: company website + LinkedIn + short company description
- Constrain AI: define what ideas are **off-limits** (e.g., pharma expense co. ≠ AR ideas)
- **One-idea + P.S.** variant when three bullets feel too long (AI Specificity Campaign)
- Manual-write 10 examples → embed in system prompt → use cached prompt prefix for cost at scale

**Source:** [LinkedIn Creative Ideas post](https://www.linkedin.com/posts/outboundphd_this-is-the-type-of-campaign-i-would-suggest-activity-7419050979062358016-mgZ2) · [Alex Berman](https://alexberman.com/creative-ideas-campaign-cold-email-infrastructure)

---

### 5. Pay-for-Discovery Offer Design

Craft offers competitors cannot copy:

1. Ask: **What could we say that competitors can't?**
2. Create value so compelling prospects would **pay for the discovery call**
3. Answer **why someone wouldn't respond** — address hidden objections in the offer
4. Remove risk where possible (e.g., free test campaign, pay-after-results)

**Example (reputation management):** Target businesses with 3.5–4.5★ ratings → cite specific negative reviews → offer removal with payment only after removal → **1 positive reply per 70 emails**.

**Signals caveat:** Signals help testing but are **not a silver bullet** — sustainable motion needs offer strength, not signal complexity alone.

**Source:** [GTM Engineer podcast](https://thegtmengineer.substack.com/p/the-winning-cold-outbound-formula)

---

### 6. GEX Agency Stack (Tooling)

| Layer | Tool | Role |
|---|---|---|
| Orchestration | **Clay** | Enrichment, AI copy, Sculptor workflows, Sequencer |
| Sending | **Smartlead** | Campaign management, block lists, CRM via Clay |
| Data hub | **Supabase** | Block lists, campaign metrics, single source of truth |
| Automation | **Pipedream** | Integrations between stack layers |
| AI routing | **OpenRouter** | Multi-model access at scale |

Pair with `clay-automation` (rollout process) and `tools/clay-toolkit` (column implementation).

---

## When to Use

- Scaling outbound past **~500 emails/day** — infra math and backup capacity
- Deliverability incidents, burned domains, Outlook placement collapse
- Evaluating **whether cold outbound fits** unit economics
- Clay agency-style rollout — Crawl Walk Run before automating
- Default campaign for new outbound programs — **Creative Ideas** test
- Offer redesign when reply rates stall despite good infra

## When NOT to Use

- Discovery call coaching — Keenan Gap Selling / Becc Diagnostic Selling
- Pain-qualified segment research from won deals — Jordan Crawford FIND/PQS
- Hook-Line-Sinker copy skeleton — Pat Spielmann
- lemlist-native multichannel cadence — Guillaume Moubeche
- SEP/TQ automation architecture — Justin Michael Sales Borg

---

## Infrastructure Checklist

- [ ] Unit economics pass (TAM, LTV, CAC:LTV)
- [ ] Secondary domains only — never primary business domain
- [ ] 2 inboxes per domain; 30 sends/day/inbox baseline
- [ ] 3-week warmup minimum; 50% spare capacity warming
- [ ] Backup inboxes = active sending capacity (1:1 rule)
- [ ] SPF + DKIM + DMARC configured; Google Postmaster + SNDS registered
- [ ] Block list + DNC sync (Clay → Smartlead or equivalent)
- [ ] Inbox placement test before volume escalation on winning campaigns

---

## Creative Ideas Campaign Checklist

- [ ] Crawl: 5–10 manual emails written (no AI)
- [ ] Three **specific** capabilities defined — not generic categories
- [ ] Off-limits ideas documented in prompt constraints
- [ ] System prompt includes manual examples + full business context
- [ ] First 50 AI outputs human-reviewed before Run phase
- [ ] Test one-idea + P.S. variant vs three-bullet version
- [ ] Offer answers "why wouldn't they respond?"

---

## Anti-Patterns

| Mistake | Fix |
|---|---|
| Scaling volume before infra + warmup | `domain-infrastructure` → `email-deliverability` first |
| No backup inboxes | 1:1 backup rule — spam marks happen on good copy |
| Complex signal workflows before offer test | Run Creative Ideas or plain offer-first email |
| AI copy without manual training examples | Crawl phase — 10 hand-written examples |
| Recycling burned inboxes | Provision fresh domains/inboxes |
| Signals as only strategy | Offer design + Creative Ideas split tests |
| Copying Jordan/Pat message frameworks for infra | Eric = scale lane; pair, don't replace |
| Outbound with LTV <$10k and tiny TAM | Fix economics or choose inbound/product-led |

---

## Stack Position vs Other Outbound Experts

| Layer | Expert | Skill |
|---|---|---|
| **Economics + infra gate** | Eric Nowoslawski | `cold-email-strategy`, `domain-infrastructure`, `email-deliverability` |
| Segment / pain research | Jordan Crawford | `list-building`, `cold-email-strategy` |
| Email structure / SDR KPIs | Becc Holland | `cold-email-strategy`, `sales-team-building` |
| Multichannel cadence | Guillaume Moubeche | `lemlist-setup`, `multi-channel-outreach` |
| Enrichment + copy skeleton | Pat Spielmann | `cold-email-copywriting`, `leadmagic-waterfall` |
| SEP automation / TQ | Justin Michael | `ai-sdr-setup`, `sending-platforms` |
| Offer-led AI campaigns at scale | **Eric Nowoslawski** | `cold-email-copywriting`, `clay-automation` |

**Recommended high-scale stack:**
```
Eric (unit economics) → Jordan/Becc/Pat (segment + message)
→ Eric (infra + backup capacity) → Eric Creative Ideas OR Guillaume cadence
→ clay-automation (Crawl Walk Run) → email-deliverability monitoring
```

---

## Skills That Cite This Playbook

`cold-email-strategy` · `cold-email-copywriting` · `email-deliverability` · `domain-infrastructure` · `inbox-setup` · `clay-automation` · `sending-platforms` · `smartlead-workflows` · `tool-selection-stack`
