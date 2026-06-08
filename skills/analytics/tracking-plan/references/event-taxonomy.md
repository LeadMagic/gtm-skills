# Event Taxonomy for PLG and SaaS

Extracted from `SKILL.md` to keep SKILL.md marketplace-efficient while preserving implementation depth.

### Phase 2: Event Taxonomy for PLG and SaaS

**The complete event taxonomy — every event a PLG SaaS company needs:**

```
ACCOUNT EVENTS (tracked server-side for reliability):
□ Signed Up
  Properties: plan (string), source (string), referrer (string)
  + all UTM params + gclid/fbclid if present
□ Email Verified
□ Account Created (B2B: workspace/team created)
□ Profile Completed (properties: completion_percentage)
□ Subscription Started
  Properties: plan, billing_period, amount, currency
□ Subscription Upgraded
  Properties: from_plan, to_plan, upgrade_reason
□ Subscription Downgraded
  Properties: from_plan, to_plan, downgrade_reason
□ Subscription Canceled
  Properties: plan, cancellation_reason, tenure_days, mrr_lost
□ Trial Started
  Properties: plan, source, trial_length_days
□ Trial Converted (trial → paid)
  Properties: trial_days_used, plan_converted_to
□ Trial Expired (no conversion)
  Properties: trial_days, last_activity_date

ACTIVATION EVENTS (the PLG funnel):
□ Onboarding Started
□ Onboarding Step Completed (properties: step_name, step_number)
□ Activation Complete
  Properties: time_to_activate_hours, activation_milestone
  THIS IS YOUR MOST IMPORTANT EVENT. Define it ruthlessly.
□ Aha Moment Reached
  Properties: aha_moment_type, time_to_aha_hours

USAGE EVENTS (core product actions):
□ Feature Used
  Properties: feature_name, feature_category, source (where in app)
□ Search Performed
  Properties: query, results_count, search_type
□ [Product-Specific Action 1]: e.g., Campaign Created, Report Generated
□ [Product-Specific Action 2]: e.g., Email Sent, Integration Connected
□ File Exported / Downloaded
  Properties: file_type, file_size_kb
□ Item Created / Edited / Deleted
  Properties: item_type, source

COLLABORATION EVENTS (key for B2B PLG):
□ Invite Sent
  Properties: invite_method (email/link), role_invited
□ Invite Accepted
  Properties: invite_method, days_to_accept
□ Team Created
  Properties: team_size
□ Team Member Added / Removed
□ Comment / Note Added
□ Asset Shared (internal or external)
  Properties: share_method, share_audience

ENGAGEMENT EVENTS:
□ Notification Viewed / Clicked
  Properties: notification_type, notification_channel
□ Email Opened / Clicked
  Properties: email_type, campaign_id, campaign_name
□ In-App Message Viewed / Clicked
  Properties: message_type, message_id
□ Help Article Viewed
  Properties: article_title, article_category
□ Support Ticket Created / Resolved
  Properties: ticket_category, ticket_priority

REVENUE EVENTS:
□ Invoice Created / Paid / Overdue
□ Credit Card Added / Updated / Failed
□ Payment Method Changed
□ Coupon Applied
  Properties: coupon_code, discount_amount
□ Refund Requested / Processed
□ Expansion Purchase
  Properties: product_added, additional_mrr
□ Renewal Started / Completed

MILESTONE EVENTS (for customer health):
□ 7-Day Active (used product 3+ days in week 1)
□ 30-Day Active (used product 10+ days in month 1)
□ Power User Threshold Reached
  Properties: power_user_criteria (e.g., "used 5+ features in one session")
□ Monthly Active User (MAU) — fire once per calendar month
□ Quarterly Active User — fire once per quarter

NPS / FEEDBACK EVENTS:
□ NPS Survey Sent / Viewed / Submitted
  Properties: score, comments
□ CSAT Survey Sent / Viewed / Submitted
  Properties: score, interaction_type
□ Feature Request Submitted
□ Bug Reported
□ Feedback Submitted
  Properties: feedback_type, sentiment (positive/neutral/negative)

SESSION EVENTS (for GA4 / web analytics):
□ Page Viewed
  Properties: page_title, page_path, page_category
□ Session Started
  Properties: source, medium, campaign, referrer
□ Scroll Depth Reached
  Properties: scroll_percentage (25/50/75/100)
□ Video Played / Completed
□ File Downloaded
□ Outbound Link Clicked
□ Site Search Performed
  Properties: search_term, results_count

IDENTITY EVENTS (internal — not sent to analytics):
□ Identified (user logged in or was recognized)
  Properties: user_id, email (if available via identify)
□ Group Identified (B2B — workspace/account context)
  Properties: group_id, group_name, plan, employee_count
□ Alias (merge anonymous user with authenticated user)
  Used when: anonymous visitor signs up → merge their pre-signup
  events with their authenticated user_id
```
