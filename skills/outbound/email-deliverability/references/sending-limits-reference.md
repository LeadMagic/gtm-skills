# Sending Limits Reference

Extracted from `SKILL.md` to keep SKILL.md marketplace-efficient while preserving implementation depth.

## Sending Limits Reference

From `references/deliverability-primer.md` and industry best practices:

| Mailbox Provider | Daily Cold Limit | Notes |
|------------------|-----------------|-------|
| Google Workspace | 50 | Hard limit. 40 recommended for sustained sending. |
| Microsoft 365 | 50 | Similar to Google. Watch for outbound throttling. |
| Zoho Mail | 30-50 | Depends on plan. Free tier has lower limits. |
| Custom SMTP | Varies | Provider-specific. Check terms of service. |

These are cold email limits. Transactional email (password resets,
notifications) has separate, higher limits. Never mix cold and
transactional on the same domain — the cold reputation drags down
transactional deliverability.
