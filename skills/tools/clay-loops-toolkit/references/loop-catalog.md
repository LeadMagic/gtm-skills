# GTM Clay Loop Catalog

**Path:** `tools/clay-loops-toolkit` · One signal per loop.

---

## L01 — Funding Signal

| Field | Value |
|---|---|
| Cadence | Daily |
| Monitor | `funding_round` not empty AND `funding_date` within 14 days |
| Play | `funding-signal-play` |
| Prompts | `ai-prompts-toolkit` P03 (research) + P04 (draft) |
| LeadMagic | Find → Verify → Enrich Person (on signal) |

**Monitor column (cheap):** Clay funding enrich OR Crunchbase — no email columns.

**Action:** CRM task + Slack #signals. Sequencer only if score ≥80 and approved.

---

## L02 — Job Change

| Field | Value |
|---|---|
| Cadence | Daily |
| Monitor | LeadMagic Job Change OR title/company changed ≤30d |
| Play | `job-change-play` |
| LeadMagic | Job Change → Find → Verify → Enrich |

**Champion variant:** Join CRM open opp → route to AE, not generic sequencer.

---

## L03 — Hiring Signal

| Field | Value |
|---|---|
| Cadence | Weekly |
| Monitor | GTM job postings (SDR, AE, RevOps, VP Sales) at account |
| Play | `hiring-signal-play` |
| LeadMagic | Find → Verify on 1–3 contacts at account |

**Monitor:** Job posting count / relevant titles — cheap enrich only.

---

## L04 — Stale Opportunity Refresh

| Field | Value |
|---|---|
| Cadence | Weekly |
| Source | CRM export — opps no activity >14d, stage ≥ Solution |
| Play | `pipeline-management` (deal review) |
| LeadMagic | Verify email on opp contacts only |

**Action:** CRM task for owner — no auto-email.

---

## L05 — Champion Move

| Field | Value |
|---|---|
| Cadence | Daily |
| Monitor | Job change on contact tied to open opp |
| Play | `job-change-play` (champion track) |
| LeadMagic | Job Change → Verify |

**Action:** Slack @AE + CRM task urgent.

---

## L06 — ICP Net-New Monitor

| Field | Value |
|---|---|
| Cadence | Weekly |
| Monitor | New companies matching firmographic + technographic filter |
| Play | `lead-finding` |
| LeadMagic | Full waterfall per new contact row |

**Source:** Net-new company list; enrich only new rows since last run.

---

## L07 — Post-Meeting Nurture

| Field | Value |
|---|---|
| Cadence | Daily |
| Monitor | CRM meeting held = true AND no follow-up task in 48h |
| Play | `meeting-prep` |
| LeadMagic | Verify email |

**Action:** CRM task + optional nurture sequence enroll.

---

## Loop vs n8n

| Prefer Clay Loop | Prefer n8n (`n8n-toolkit`) |
|---|---|
| Signal monitor on Clay sources | Inbound form SLA <60s |
| Credit-controlled enrich in Clay | Reply webhook classify |
| AE reviews in Clay table UI | HubSpot ↔ SF sync |
| Weekly batch signal scan | MCP-approved bulk jobs |

---

## Credit Budget Guide

| Loop | Credits/row (signal=true) | Monthly cap guidance |
|---|---:|---|
| L01 Funding | 4–6 (LeadMagic) + monitor | Row limit on source table |
| L02 Job change | 3–7 (+ job change) | Daily cap 500 monitors |
| L03 Hiring | 4–8 | Weekly batch only |
| L04 Stale opp | 1 (verify only) | CRM export size |
| L05 Champion | 2–5 | Open opp contacts only |
| L06 Net-new | 4+ per contact | New rows only |
| L07 Post-meeting | 1 | Meeting volume |
