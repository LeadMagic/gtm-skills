# GTM Clay Table Blueprints

## Blueprint 1: Outbound Contact List

| # | Column | Type | Notes |
|---|---|---|---|
| 1 | first_name, last_name | input |  |
| 2 | company, domain | input/formula | domain from email or Clearbit |
| 3 | linkedin_url | input | optional |
| 4 | find_email_waterfall | enrichment | provider 1 → 2 → 3 |
| 5 | verify_email | enrichment | valid/invalid/catch_all |
| 6 | enrich_person | enrichment | title, seniority |
| 7 | icp_score | formula | see clay-toolkit formulas |
| 8 | suppression_check | formula | customer/competitor/DNC |
| 9 | ai_signal_line | LLM | `ai-prompts-toolkit` P03 |
| 10 | ai_email_draft | LLM | P04 — only if score≥50 |
| 11 | email_quality | LLM | P05 — gate ≥7 |
| 12 | clay_status | formula | pending/enriched/verified/exported |
| 13 | crm_push | action | if verified + score≥70 + not suppressed |

## Blueprint 2: Account ABM (Company Table)

| # | Column | Type |
|---|---|---|
| 1 | domain | input (key) |
| 2 | company_name | input |
| 3 | firmographics | enrichment |
| 4 | technographics | enrichment |
| 5 | funding_signal | enrichment/monitor |
| 6 | abm_tier | formula (1/2/3) |
| 7 | account_owner | formula/lookup |
| 8 | crm_company_push | action |

Person table references company via `domain` lookup — never duplicate firmographics per contact.

## Blueprint 3: Signal Outbound (Loop-Ready)

| # | Column | Type |
|---|---|---|
| 1 | domain, contact fields | input |
| 2 | signal_detected | formula/monitor |
| 3 | signal_type | formula |
| 4 | signal_date | enrichment |
| 5 | source_url | enrichment/LLM |
| 6 | why_now | formula/LLM |
| 7 | conditional_enrich | enrichment | only if signal_detected |
| 8 | signal_score | formula |
| 9 | route_action | formula | sequencer/task/skip |

See `clay-loops-toolkit` (`tools/clay-loops-toolkit`) for loop cadence and routing matrix.

## Blueprint 4: CRM Hygiene

| # | Column | Type |
|---|---|---|
| 1 | crm_contact_id | input from CRM |
| 2 | last_activity_days | formula |
| 3 | email_stale | formula (>90d) |
| 4 | re_verify_email | enrichment |
| 5 | title_changed | enrichment |
| 6 | update_crm | action |

## clay_status Values

| Status | Meaning |
|---|---|
| pending | Awaiting enrichment |
| enriched | Data complete, not verified |
| verified | Email valid, ready for review |
| exported | Pushed to CRM/sequencer |
| suppressed | Do not contact |
