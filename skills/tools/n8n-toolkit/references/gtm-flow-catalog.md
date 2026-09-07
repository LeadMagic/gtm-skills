# n8n GTM Flow Catalog

Production flow blueprints. Copy flow ID into workflow name: `[PROD] {ID} {name}`.

**Canonical schema** (all flows normalize to this):

```json
{
  "event_id": "uuid",
  "email": "",
  "domain": "",
  "first_name": "",
  "last_name": "",
  "company": "",
  "title": "",
  "source": "form|clay|crm|sequencer|api",
  "signal_type": "funding|job_change|hiring|stale_opp|trial|reply",
  "why_now": "",
  "source_url": "",
  "icp_score": 0,
  "icp_tier": "1|2|3"
}
```

---

## Inbound Flows

### INB-01 — Form → Enrich → Score → Route

**Trigger:** Webhook (HubSpot form, Typeform, Webflow, Cal.com booking)

**SLA:** <60 seconds end-to-end

```
Webhook
  → Set: normalize + event_id (hash email+timestamp)
  → Execute Workflow: sw-idempotency-check
  → HTTP: LeadMagic verify email
  → IF deliverable = false → Slack #bad-leads → Respond 200 → STOP
  → HTTP: LeadMagic company enrich (by domain)
  → Code: ICP score (employee_count, industry, geo, title)
  → Switch icp_score:
      branch A (≥70): sw-crm-upsert-contact → round-robin owner → Slack #hot-leads
      branch B (40-69): CRM upsert → list=nurture → tag inbound-nurture
      branch C (<40): log to Sheet disqualified + reason → STOP
  → Respond to Webhook 200 { status, crm_id }
```

**CRM required fields:** `lead_source`, `icp_score`, `inbound_date`, `situation` (SPICED-lite)

**Skills:** `inbound-triage`, `crm-toolkit`, `leadmagic-toolkit`

---

### INB-02 — Speed-to-Lead Slack Alert

**Trigger:** Webhook (parallel to INB-01 or standalone for speed)

**SLA:** <30 seconds

```
Webhook → Set normalize
  → IF icp_tier in (1,2) → Slack @channel with profile link + calendar link
  → CRM: set first_response_due
```

Use when SDR SLA is <5 min. Does not replace INB-01 enrichment.

---

### INB-03 — Chat / Product Qualified Lead

**Trigger:** Webhook (Intercom, Drift, in-app signup)

```
Webhook → Set normalize
  → IF product_qualified = true OR usage_threshold met
  → Enrich company → Score
  → CRM: create PQL contact + task for AE
  → Slack #pql
```

**Skills:** `plg-strategy`, `inbound-triage`

---

## Outbound Flows

### OUT-01 — Batch List Enrich → CRM

**Trigger:** Cron (weekly) or Manual webhook `{ list_id }`

```
Trigger → Airtable/Sheets: status=queued LIMIT 500
  → Split In Batches (25)
    → Wait 200ms
    → HTTP: LeadMagic find email
    → HTTP: LeadMagic verify
    → IF verified: sw-crm-upsert-contact, status=enriched
    → ELSE: status=manual_review, reason
  → Merge → Slack summary { enriched, failed, manual }
```

**Throughput:** ~5K rows in 2–4 hours at 200ms spacing.

**Skills:** `leadmagic-toolkit`, `data-enrichment-strategy`

---

### OUT-02 — Enriched → Sequencer Handoff

**Trigger:** Webhook from Clay or post OUT-01

```
Webhook { contacts[], campaign_id, human_approved: true }
  → IF human_approved != true → STOP (compliance gate)
  → Split In Batches (10)
    → HTTP: Smartlead/Instantly add to campaign
    → CRM: tag sequencer_enrolled, campaign_id
  → Slack: enrollment count
```

**Never enroll without `human_approved` flag.**

**Skills:** `sequencing-toolkit`, `clay-toolkit`

---

### OUT-03 — ABM Account → Contact Fan-Out

**Trigger:** Cron weekly (tier-1 accounts)

```
CRM: accounts tier=1, last_touch>30d
  → Per account: HTTP find contacts (3 titles)
  → Enrich each → Score → CRM create contacts
  → CRM task for AE: "ABM refresh"
```

**Skills:** `abm-strategy`, `multi-thread-orchestration`

---

## Signal Flows

### SIG-01 — Funding Signal

**Trigger:** Cron daily 6am UTC

```
Source (funding API / Clay webhook / Sheet)
  → Filter: announced_date < 7d AND icp_tier in (1,2)
  → Per account: enrich primary contacts
  → Set signal_type=funding, why_now, source_url
  → CRM: task + tag signal:funding
  → Slack #signals
```

**Do not auto-send email.** AE picks up task; copy from `funding-signal-play`.

---

### SIG-02 — Job Change / Champion Move

**Trigger:** Cron daily

```
CRM: contacts on watchlist OR open opps
  → Job change API / Clay webhook
  → IF new_company in ICP → champion play
  → ELSE → nurture alumni track
  → CRM: update contact + task
```

**Skills:** `job-change-play`, `clay-loops-toolkit`

---

### SIG-03 — Hiring Signal

**Trigger:** Cron weekly

```
Account list tier 1-2
  → HTTP: job postings count / relevant roles
  → IF roles_match icp_buyer_titles → signal
  → CRM task + tag signal:hiring
```

**Skills:** `hiring-signal-play`

---

### SIG-04 — Stale Opportunity Refresh

**Trigger:** Cron weekly

```
CRM: opps stage=Solution+, last_activity>14d
  → Enrich account news
  → Slack owner with SPICED refresh prompt
  → CRM: task "stale opp review"
```

**Skills:** `pipeline-management`, `meeting-prep`

---

## Lifecycle Flows

### LIF-01 — Meeting Held → Follow-Up Branch

**Trigger:** CRM webhook (meeting outcome = held)

```
Webhook → Normalize
  → IF next_step empty → Slack AE "missing next step"
  → IF nurture → add to lifecycle sequence
  → IF proposal → CRM stage gate check (MEDDICC fields)
```

**Skills:** `meeting-prep`, `pipeline-management`

---

### LIF-02 — Trial Signup → Onboarding

**Trigger:** Webhook (product analytics / auth provider)

```
Webhook → Enrich company → CRM upsert
  → IF icp_tier 1 → assign AE task
  → IF tier 2-3 → CSM onboarding email via MAP
  → event-analytics: track trial_started
```

**Skills:** `customer-onboarding`, `event-analytics`

---

### LIF-03 — Reply Webhook → Classify → Route

**Trigger:** Sequencer reply webhook

```
Webhook (Instantly/Smartlead/Outreach)
  → Set: reply_body, thread_id, contact_email
  → AI node (P08 reply classify) OR HTTP OpenAI
  → Switch category:
      positive_intent → CRM task high priority + Slack AE
      objection → CRM task + tag objection:type
      ooo → reschedule sequence
      unsubscribe → CRM opt-out + global suppression
      wrong_person → extract referral → new contact
      not_interested → close task + nurture suppress outbound
  → Log row to Sheet
```

**Skills:** `reply-handling`, `ai-prompts-toolkit`

---

### LIF-04 — Closed-Won → CS Handoff (Bowtie)

**Trigger:** CRM deal stage = closed won

```
Webhook → Normalize
  → CRM: create CS onboarding project
  → Copy fields: SPICED summary, implementation notes, EB name
  → Slack #wins + @csm
  → IF missing handoff fields → block + notify sales manager
```

**Skills:** `customer-onboarding`, `pipeline-management` (Bowtie)

---

## RevOps Flows

### REV-01 — CRM Email Re-Verify

**Trigger:** Cron weekly

```
CRM: contacts last_verified>90d OR bounce_flag
  → Batch verify LeadMagic
  → Update email_status, last_verified
  → IF invalid → tag email_stale + remove from active sequences
```

---

### REV-02 — Forecast Rollup → Leadership Slack

**Trigger:** Cron Monday 8am

```
CRM: pull open pipeline by stage
  → Code: calculate coverage, commit, best case
  → Format message → Slack #forecast
  → Sheet archive for WoW compare
```

**Skills:** `gtm-metrics`, `pipeline-management`

---

### REV-03 — Lead Routing Audit

**Trigger:** Cron daily

```
CRM: unassigned leads >24h
  → Slack #revops with list
  → IF count>10 → Pager duty style @channel
```

---

## MCP / Agent Flows

### MCP-01 — Approved Job Runner

**Trigger:** Webhook POST from agent or internal tool

**Auth:** HMAC header + `approval_token` in body

```json
{
  "job_type": "enrich_batch|classify_replies|crm_sync",
  "params": { "list_id": "", "limit": 100 },
  "requested_by": "person@example.com",
  "approval_token": "one-time-token"
}
```

```
Webhook → Crypto: verify HMAC
  → IF approval_token invalid → 401
  → Switch job_type → Execute sub-workflow
  → Log: job_id, requested_by, rows_affected, status
  → Optional: HTTP callback
```

**Skills:** `mcp-setup`, `leadmagic-mcp`

---

### MCP-02 — Agent Research Log (Audit)

**Trigger:** Webhook from agent middleware

```
Webhook { tool_calls[], session_id, user }
  → Append to audit Sheet
  → IF write_action count > threshold → Slack security
```

Pairs with `mcp-setup` audit logging requirements.

---

## Flow Selection Matrix

| User Says | Start With |
|---|---|
| "Form leads going to CRM" | INB-01 |
| "SDR needs instant Slack" | INB-02 |
| "Upload CSV enrich weekly" | OUT-01 |
| "Clay to Smartlead" | OUT-02 |
| "Funding alerts" | SIG-01 |
| "Reply automation" | LIF-03 |
| "Closed won to CS" | LIF-04 |
| "Agent runs enrich batch" | MCP-01 |
