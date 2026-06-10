# GTM Prompt Library

Copy-paste into Clay AI columns, Claygent, n8n LLM nodes, or Cursor.

---

## P01 — Account Snapshot (SPICED)

```
Research {{company}} ({{domain}}) for a B2B sales call.

Return JSON only:
{
  "situation": "",
  "pain": "",
  "impact": "",
  "critical_event": "",
  "decision_notes": "",
  "sources": [{"claim":"","url":""}]
}

Rules:
- Every claim needs a source URL
- If unknown, use null — do not guess
- critical_event = why they might buy NOW (funding, hire, launch, pain spike)
```

---

## P02 — Work Email Find (No Guess)

```
Find a verified work email for {{first_name}} {{last_name}} at {{company}} ({{domain}}).

Search: company team page, LinkedIn, press releases, conference speaker lists.

Return JSON:
{"email":"","source_url":"","confidence":"high|medium|none"}

Rules:
- Do NOT construct emails from patterns (first.last@domain)
- If no verified source, return email="" and confidence="none"
```

---

## P03 — Signal Line (Cold Email Opener)

```
Write ONE personalization line (max 25 words) for outreach.

Signal: {{signal}}
Source: {{source_url}}
Prospect: {{title}} at {{company}}

Rules:
- Reference the signal specifically
- If source_url is empty, return {"line":"","usable":false}
- No invented news or metrics

Return JSON: {"line":"","usable":true|false}
```

---

## P04 — Cold Email Draft

```
Write a cold email for {{seller_company}} selling {{offer_one_liner}}.

Prospect: {{first_name}}, {{title}} at {{company}}
Personalization line: {{signal_line}} (source: {{source_url}})
ICP pain: {{icp_pain}}

Rules:
- Under 90 words total
- One pain, one proof point ({{proof_point}}), one low-friction CTA
- No "hope this finds you well", no fake "Re:", no invented ROI
- If proof_point empty, use category pain only

Return JSON: {"subject":"","body":"","word_count":0}
```

---

## P05 — Email Quality Score

```
Score this cold email 1–10 for B2B outbound quality.

Email:
{{email_body}}

Criteria:
- Relevance to signal/ICP (0–3)
- Brevity <90 words (0–2)
- One clear CTA (0–2)
- No banned claims or fluff (0–3)

Return JSON:
{"score":0,"pass":false,"feedback":"","revision_hints":[]}

pass = true if score >= 7
```

---

## P06 — Reply Classification

```
Classify this inbound sales reply.

Reply text:
{{reply_body}}

Categories:
- interested (wants meeting/info)
- objection (pushback, not a hard no)
- not_interested (clear no)
- ooo (out of office)
- unsubscribe (stop contact)
- referral (points to someone else)
- pricing (asks about cost)
- security (compliance/legal question)

Return JSON:
{"category":"","confidence":0.0,"suggested_owner":"sdr|ae|cs|stop","summary":""}
```

---

## P07 — ICP Fit Score

```
Score ICP fit 0–100 for {{seller_icp_description}}.

Company: {{company}}
Domain: {{domain}}
Employees: {{employees}}
Industry: {{industry}}
Title: {{title}}

Return JSON:
{"score":0,"tier":"tier1|tier2|tier3|disqualify","reasons":[],"missing_data":[]}
```

---

## P08 — Meeting Brief (Pre-Call)

```
Build a 60-second pre-call brief.

Account: {{company}} ({{domain}})
Attendees: {{attendees}}
Known context: {{crm_notes}}

Include: company snapshot, attendee priorities, 5 SPICED questions, competitive risks.

Return markdown under 400 words. Flag gaps needing live discovery.
```

---

## P09 — Champion Identification

```
From public info, assess if {{contact_name}} ({{title}}) could champion a {{category}} purchase at {{company}}.

Return JSON:
{
  "champion_likelihood":"low|medium|high",
  "power_signals":[],
  "personal_win_hypothesis":"",
  "gaps_for_meddicc":[],
  "sources":[]
}

Apply Andy Whyte champion test: power, personal win, articulation ability.
```

---

## P10 — Competitor Mention Extractor

```
Search for evidence {{company}} uses or evaluates competitors: {{competitor_list}}.

Return JSON:
{"competitors_found":[],"sources":[],"status_quo_risk":"low|medium|high"}
```
