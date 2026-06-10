# Crisis FAQ for Support & Sales

*Single source of truth during active incident. Update timestamp on every edit.*

**Incident ID:** INC-_____  
**Last updated:** [timestamp]  
**Status page:** [URL]

---

## Quick talk track (30 seconds)

> "We're aware of [issue] affecting [scope]. Our team is [investigating / implementing a fix]. Latest updates are on our status page at [URL]. I'm logging your account so we can follow up when resolved. Is there a specific workflow blocked for you right now?"

---

## FAQ

### What happened?

[Copy from war room facts doc — plain language, no jargon]

### Who is affected?

[All customers / customers using X / region Y / accounts that did Z between times]

### Is my data safe?

[Counsel-approved answer only. Default: "We're investigating and will notify affected customers directly if we determine data was impacted."]

### How long until it's fixed?

"We don't have a confirmed ETA yet. The status page is updated every [30/60] minutes. I'll note your account for proactive outreach when resolved."

**Never:** Promise a time unless eng liaison approved it in writing.

### Will we get credits / SLA relief?

[Yes/no/pending — link to policy or "CS leadership will contact enterprise accounts"]

### Can I still use [feature]?

[Per-component status]

### What should I tell my team / boss?

Point them to status page + this incident ID. Offer to schedule a call for enterprise accounts.

### Is this a security breach?

[Counsel-approved. Default: "We're treating this as a serious incident and following our security response process. We'll communicate directly if customer action is required."]

### Why didn't we know sooner?

[Optional — only if true] "We detected at [time] and notified affected customers within [X] minutes."

---

## Objection handling (sales in-flight deals)

| Prospect says… | Response |
|---|---|
| "I saw on LinkedIn you're down" | "Yes — here's our status page and what we're doing. Happy to walk your team through impact on your use case." |
| "Should we delay signing?" | "That's your call. Here's factual impact on [their use case]. We can connect you with [CS/engineering] for technical Q&A." |
| "Competitor says you're unreliable" | Don't trash competitor. Stick to facts + post-mortem commitment. |

---

## Escalation

| Trigger | Escalate to |
|---|---|
| Customer mentions churn / legal | CS captain + comms lead |
| Press/journalist contact | Comms lead only — do not respond |
| Request for root cause detail | Eng liaison |
| Executive at $100K+ ACV angry | CSM + VP CS |

---

## Macros (support desk)

**Macro: Incident acknowledgment**

```
Thanks for reaching out. We're actively working on [issue] (incident INC-XXX). 
Live updates: [status URL]. I've flagged your account for follow-up when resolved.
```

**Macro: No ETA yet**

```
We don't have a confirmed resolution time yet. Our team posts updates every [interval] at [status URL]. I'll keep your ticket open and update you here.
```

---

## After resolution

- [ ] Send "resolved" email template to open tickets
- [ ] Update G2/TR if public complaints referenced incident
- [ ] Remove macros when incident closed + post-mortem published

**Templates:** `crisis-customer-email.md` · **Playbook:** `crisis-management-playbook.md`
