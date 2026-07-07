# Email Deliverability — Deliverable

## Context
- Company / product:
- Owner:
- Date:

## Summary
[One paragraph: what this deliverable decides or enables]

## Core output

<!-- Structure derived from SKILL.md Output Format -->
```markdown

## Frameworks Applied

- **ColdIQ Multi-Channel Cadence**
- **Eric Nowoslawski Cold Email Infrastructure**
- **Eric Nowoslawski 1:1 Backup Inbox Strategy**
- **Jed Mahrle Practical Prospecting**
- **Google Bulk Sender Guidelines**

## Quality check

Before delivering, verify:
- [ ] Are SPF, DKIM, DMARC records provided in copy-paste format?
- [ ] Does SPF use `-all` (hard fail), not `~all`?
- [ ] Is DKIM using 2048-bit keys minimum?
- [ ] Does DMARC start with `p=none` and plan to progress to `p=reject`?
- [ ] Is the warmup schedule 2-4 weeks with per-week volume targets?
- [ ] Does the plan NEVER recommend sending cold from the primary domain?
- [ ] Are bounce thresholds clear (target <2%, warning 2-5%, critical >5%)?
- [ ] Are complaint thresholds clear (target <0.1%, critical >0.3%)?
- [ ] Is Google Postmaster Tools registration included?
- [ ] Is blacklist monitoring included with specific blacklists named?
- [ ] Does the incident response plan have time-based escalation steps?
- [ ] Is there a quarterly audit checklist?
- [ ] Are unsubscribe requirements specified (CAN-SPAM, GDPR)?
- [ ] Is email validation mentioned but NEVER described internally?

## Next steps
1. 
2. 
3. 
