# n8n Node Patterns for GTM

Copy-paste patterns for production workflows. Adjust credentials per environment.

---

## Webhook Trigger (Inbound)

**Settings:**
- HTTP Method: POST
- Response: "When last node finishes"
- Authentication: Header Auth `X-Webhook-Secret` OR verify in next node

**First node after Webhook — Set (Normalize):**
```javascript
// n8n Set node — manual mapping
{
  "event_id": "={{ $json.body.email + '_' + $now.toISO() }}",
  "email": "={{ $json.body.email?.toLowerCase().trim() }}",
  "domain": "={{ $json.body.email?.split('@')[1] }}",
  "first_name": "={{ $json.body.firstname || $json.body.first_name }}",
  "last_name": "={{ $json.body.lastname || $json.body.last_name }}",
  "company": "={{ $json.body.company }}",
  "source": "form",
  "utm_source": "={{ $json.body.utm_source }}"
}
```

---

## HMAC Verification (Code Node)

```javascript
const crypto = require('crypto');
const secret = $env.N8N_WEBHOOK_HMAC_SECRET;
const payload = JSON.stringify($input.first().json.body);
const signature = $input.first().json.headers['x-n8n-hmac-sha256'];

const expected = crypto
  .createHmac('sha256', secret)
  .update(payload)
  .digest('hex');

if (signature !== expected) {
  throw new Error('Invalid HMAC');
}
return $input.all();
```

---

## HTTP Request — LeadMagic Verify Email

| Field | Value |
|---|---|
| Method | POST |
| URL | `https://api.leadmagic.io/v1/email/verify` |
| Auth | Header `X-API-Key` = credential |
| Body | `{ "email": "={{ $json.email }}" }` |

**Extract:** `deliverable`, `status`, `mx_found`

---

## HTTP Request — LeadMagic Find Email

| Field | Value |
|---|---|
| Method | POST |
| URL | `https://api.leadmagic.io/v1/email/find` |
| Body | `{ "first_name", "last_name", "domain" }` |

**Extract:** `email`, `confidence`

---

## ICP Score (Code Node)

```javascript
const item = $input.first().json;
let score = 0;

// Adjust weights to your ICP — load from gtm-context
const employees = item.employee_count || 0;
if (employees >= 50 && employees <= 500) score += 30;
else if (employees > 500 && employees <= 2000) score += 20;

const title = (item.title || '').toLowerCase();
if (/vp|director|head|chief/.test(title)) score += 25;
if (/sales|revenue|gtm|marketing/.test(title)) score += 15;

if (item.industry_match) score += 20;
if (item.geo_match) score += 10;

return [{ json: { ...item, icp_score: Math.min(score, 100) } }];
```

---

## Switch — Route by Score

| Rule | Output |
|---|---|
| `icp_score >= 70` | hot_lead |
| `icp_score >= 40` | nurture |
| else | disqualified |

---

## Split In Batches

| Setting | Value |
|---|---|
| Batch Size | 25 (API); 10 (sequencer) |
| Options | Reset |

**Always follow batch loop with Wait node 200ms** before HTTP calls.

---

## Wait (Rate Limit)

Insert between HTTP Request nodes in loops:
- **200ms** — LeadMagic, most enrichment APIs
- **500ms** — strict CRM rate limits
- **1000ms** — sequencer enroll if throttled

---

## HubSpot Upsert Contact

Use HubSpot node **Create or Update**:
- Email as duplicate key
- Properties map from canonical schema
- Required: `lead_source`, `icp_score`, `hs_lead_status`

Or HTTP: `PATCH /crm/v3/objects/contacts/batch/upsert`

---

## Slack Notification

```json
{
  "channel": "#hot-leads",
  "text": "🔥 Hot inbound: {{ $json.first_name }} @ {{ $json.company }} (score {{ $json.icp_score }})",
  "blocks": []
}
```

Load formatting rules from `proactive-alerts`.

---

## AI Agent Node (Reply Classify)

**Model:** gpt-4o-mini or claude-3-haiku (cost control)

**System prompt:** Load P08 from `ai-prompts-toolkit`

**Output parser:** Structured JSON:
```json
{
  "category": "positive_intent|objection|ooo|unsubscribe|wrong_person|not_interested",
  "confidence": 0.0,
  "suggested_action": "",
  "referral_email": ""
}
```

**Max iterations:** 2

---

## Error Trigger Workflow (Global)

Create separate workflow:
```
Error Trigger
  → Set: workflow_name, error_message, timestamp, execution_id
  → Slack #n8n-errors
  → Google Sheets append (dead letter log)
```

Link from every production workflow's settings → Error Workflow.

---

## Sub-Workflow: sw-idempotency-check

**Input:** `event_id`

```
Execute Workflow Trigger
  → Google Sheets / Redis: lookup event_id
  → IF exists → Stop and Error "duplicate"
  → ELSE → write event_id → return continue
```

---

## Respond to Webhook

Return fast for form UX:
```json
{ "status": "accepted", "crm_id": "={{ $json.crm_id }}" }
```

Heavy processing can use **Respond immediately** + continue in background
(n8n setting on Webhook node) for INB-02 Slack alerts.

---

## Execute Workflow Node

| Setting | Value |
|---|---|
| Source | Database |
| Workflow | `sw-enrich-contact` |
| Wait for completion | true |

Pass only required fields — keeps sub-workflow testable.

---

## Retry on Fail

Per HTTP Request node → Settings:
- Retry On Fail: true
- Max Tries: 3
- Wait Between Tries: 1000ms (exponential: use Code node for 1s/5s/25s)

---

## Production Naming Convention

```
[PROD] INB-01 Form Enrich Route
[PROD] OUT-01 Batch Enrich Weekly
[PROD] LIF-03 Reply Classify
[PROD] MCP-01 Job Runner
[SUB] sw-enrich-contact
[ERR] Global Error Handler
```

---

## Export Safety

Before sharing workflow JSON:
- Export **without** credentials
- Scrub webhook URLs
- Document required credentials in README
