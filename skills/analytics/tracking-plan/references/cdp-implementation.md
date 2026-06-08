# CDP Implementation Details

Extracted from `SKILL.md` to keep SKILL.md marketplace-efficient while preserving implementation depth.

### Phase 5: CDP Implementation

**Segment implementation (reference pattern):**

```javascript
// 1. Identify on signup/login — THE MOST IMPORTANT CALL
analytics.identify(userId, {
  email: user.email,
  name: user.name,
  plan: user.plan,
  createdAt: user.createdAt,
  // DO NOT include: password, full credit card, SSN
});

// 2. Group for B2B — links user to company account
analytics.group(workspaceId, {
  name: workspace.name,
  plan: workspace.plan,
  employeeCount: workspace.employeeCount,
  mrr: workspace.mrr,
  created_at: workspace.createdAt
});

// 3. Page — auto-tracked or manual for SPAs
analytics.page('Dashboard', {
  path: '/dashboard',
  referrer: document.referrer
});

// 4. Track — every meaningful action
analytics.track('Feature Used', {
  feature_name: 'Email Finder',
  feature_category: 'prospecting',
  source: 'dashboard',
  credits_remaining: user.credits
});
```

**Server-side tracking (critical for revenue events):**
```python
# Python backend — Segment server-side
import analytics
analytics.write_key = 'YOUR_WRITE_KEY'

analytics.track(user_id='user_abc123', event='Subscription Started', properties={
    'plan': 'growth',
    'billing_period': 'annual',
    'amount': 19900,  # in cents
    'currency': 'USD'
})
```

**Destination configuration by category:**

| Destination | Events | Purpose |
|---|---|---|
| Amplitude | All usage + account + milestone events | Product analytics |
| GA4 | Page views, signups, conversions, session events | Web analytics + ad attribution |
| HubSpot | Account events (Signed Up, Upgraded, Canceled) + email events | CRM + marketing automation |
| Intercom | Account events + usage events + milestone events | In-app messaging + support |
| Salesforce | Account events + revenue events (Enterprise customers only) | CRM (enterprise) |
| Data Warehouse | ALL events | BI + cross-functional analytics |
| Google Ads | Signed Up, Subscription Started (conversion events) | Ad attribution + bidding |
| Meta CAPI | Signed Up, Subscription Started (via server-side) | Ad attribution |
| Mixpanel | Usage events (if used alongside/instead of Amplitude) | Product analytics |
