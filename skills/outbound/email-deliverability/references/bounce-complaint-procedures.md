# Bounce and Complaint Handling Procedures

Extracted from `SKILL.md` to keep the main skill under the marketplace efficiency target.

#### Step 6: Establish Bounce and Complaint Handling Procedures

**Bounce handling:**

Hard bounces (permanent failure — invalid address, domain doesn't exist):
- Immediately remove from all active sequences.
- Suppress the address permanently (or at minimum 12 months).
- If hard bounce rate per domain exceeds 5% in any 24-hour period, pause
  all sending from that domain and investigate.

Soft bounces (temporary failure — mailbox full, server issue, rate limit):
- Pause contact for 7 days.
- After 3 consecutive soft bounces, treat as hard bounce and suppress.
- If soft bounce rate exceeds 10%, investigate sending infrastructure.

**Complaint handling:**

- Every spam complaint is an emergency. One complaint per 1,000 sends
  (0.1%) is already at the warning threshold.
- When a complaint is received: immediately remove the contact from all
  sequences, suppress permanently, and add to a "do not contact" list.
- If complaint rate exceeds 0.3% for any domain, pause all sending from
  that domain immediately. You are likely already being throttled or blocked
  by major inbox providers.
- Root cause analysis: was the email poorly targeted? No unsubscribe link?
  Sending volume too high? Recipient didn't remember opting in?

**Unsubscribe handling:**
- Every cold email must include a one-click unsubscribe mechanism. This is
  required by CAN-SPAM, GDPR, and CASL.
- The unsubscribe link should be a single line at the bottom: "Unsubscribe"
  linked to a working removal page.
- Unsubscribe requests must be processed within 24 hours (CAN-SPAM requirement)
  or immediately (GDPR requirement).
- The unsubscribe rate for cold email is typically 0.5-2%. Above 3% signals
  poor targeting or excessive sending frequency.
