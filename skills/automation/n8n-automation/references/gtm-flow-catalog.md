# GTM Flow Catalog — n8n

Reusable workflow patterns for RevOps. Adapt node names to your stack; test in sandbox before production.

---

## CRM & data hygiene

| Flow | Trigger | Actions | Output |
|---|---|---|---|
| **Lead → CRM contact** | Webhook (form) | Dedupe, enrich, assign owner, Slack notify | Contact + task |
| **Stale opp alert** | Cron daily | CRM query stage+age | `#deal-desk` Slack |
| **Hygiene score** | Weekly | Missing fields report | Email to managers |
| **Lead routing** | New record | Round-robin / territory rules | Owner assigned |

---

## Outbound & enrichment

| Flow | Trigger | Actions | Output |
|---|---|---|---|
| **Clay → CRM** | Webhook | Map columns, upsert contact | Enriched record |
| **Job change signal** | LinkedIn/Clay | Create task for AE | CRM task |
| **Sequence complete** | Sequencer webhook | Update lifecycle stage | CRM field |
| **Bounce handler** | Email webhook | Mark invalid, pause sequence | Suppression flag |

---

## Advocacy & reviews

| Flow | Trigger | Actions | Output |
|---|---|---|---|
| **NPS promoter** | Survey 9–10 | Create CSM task "review ask" | CRM task + template link |
| **CSAT 5 ticket close** | Zendesk | Delay 24h → email draft | Review ask queue |

---

## Intent & inbound

| Flow | Trigger | Actions | Output |
|---|---|---|---|
| **G2 intent** | G2 webhook | Create lead, route SDR | CRM + SLA task |
| **Inbound demo** | Calendly | Enrich, Slack, CRM opp | Meeting booked |
| **Product signup** | App event | PQL score → sales notify | Slack + CRM |

---

## Finance & ops

| Flow | Trigger | Actions | Output |
|---|---|---|---|
| **Renewal 90d** | CRM date | CSM task + forecast flag | Task |
| **Tool usage alert** | API quota | Slack finance | Budget review |

---

## Implementation notes

1. **Error handling:** Error workflow → `#revops-alerts`
2. **Idempotency:** Dedupe keys on email + company domain
3. **Secrets:** n8n credentials vault — never hardcode API keys
4. **SOC2:** Log access; no PII to unsecured webhooks (`soc2-compliance`)
5. **Rate limits:** Batch CRM updates; respect API quotas

---

## Node stack (common)

| System | n8n node |
|---|---|
| HubSpot / Salesforce / Attio | Native or HTTP |
| Slack | Slack node |
| Clay | Webhook + HTTP |
| Google Sheets | Sheets (audit logs) |
| OpenAI | LLM enrichment (optional) |

Cross-ref `crm-integration` for field mapping standards.
