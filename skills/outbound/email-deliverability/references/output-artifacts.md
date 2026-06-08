# Email Deliverability Output Artifacts

Extracted from `SKILL.md` to keep SKILL.md under the marketplace efficiency target.

## Current State Audit
[DNS records, blacklist status, reputation scores, bounce/complaint rates]

## DNS Configuration
### SPF Record
[Exact TXT record to add]

### DKIM Configuration
[Provider-specific setup instructions with selectors]

### DMARC Record
[Exact TXT record with phased rollout schedule]

## Warmup Schedule
### Week 1 (Days 1-7)
[Daily volume, recipient composition, checkpoint]

[Repeat Weeks 2-4]

## Reputation Monitoring Dashboard
| Metric | Source | Frequency | Target | Warning Threshold | Critical Threshold |
|--------|--------|-----------|--------|-------------------|---------------------|
| [Metric rows] |

## Incident Response Plan
### Bounce Spike (>5%)
[Hour 1, Day 1, Week 1 actions]

### Spam Complaint Spike (>0.3%)
[Hour 1, Day 1, Week 1 actions]

### Blacklisting
[Immediate actions, delisting procedures]

### Domain Reputation Drop
[Diagnosis steps, recovery plan]

## Quarterly Audit Checklist
- [ ] Verify all DNS records unchanged
- [ ] Check Postmaster Tools reputation
- [ ] Review blacklist status
- [ ] Audit bounce rate trends
- [ ] Audit complaint rate trends
- [ ] Review DMARC reports for unauthorized senders
- [ ] Test inbox placement across Google, Microsoft, Yahoo
- [ ] Re-verify sending limits match current volume
- [ ] Rotate DKIM keys if older than 12 months
- [ ] Check sending platform deliverability metrics
```
