# Crisis Preparedness Checklist

*Build before the crisis — not during the war room.*

**Owner:** CEO + CMO/Head of Marketing (or founder wearing both hats). **RevOps/GTM ops** maintains contact tree and artifact locations.

**Not legal advice.** Insurance and counsel contacts are operational references only.

---

## 1. Crisis contact tree / on-call rotation

| Role | Primary | Backup | Phone / Slack |
|---|---|---|---|
| Incident Commander | | | |
| Comms lead | | | |
| CEO (external voice) | | | |
| Legal liaison | | | |
| CS captain | | | |
| Sales liaison | | | |
| Eng on-call | | | |

- [ ] Contact tree stored in password manager + printed copy in ops runbook
- [ ] Rotation calendar with holiday coverage
- [ ] Escalation: IC → CEO within 30 min for Sev 2+
- [ ] After-hours bridge number or permanent Slack channel (`#incident-war-room`)

---

## 2. Pre-approved statement shells

Store in shared drive / Notion — link from this checklist.

- [ ] `templates/crisis-holding-statement.md` — outage, security, general
- [ ] `templates/crisis-customer-email.md` — affected customer segment
- [ ] `templates/crisis-internal-memo.md` — all-hands
- [ ] `templates/crisis-faq-for-support.md` — sales + CS macros
- [ ] Legal pre-review of shells (annual refresh)
- [ ] **[ ]** shells findable in **< 60 seconds** by on-call comms lead

---

## 3. Status page setup

| Vendor | Use when |
|---|---|
| [Atlassian Statuspage](https://www.atlassian.com/software/statuspage) | Default enterprise choice |
| [Instatus](https://instatus.com/) | Lightweight / startup |
| Native cloud health | Supplement only — not a substitute |

- [ ] Status page URL published on trust/security site
- [ ] Email/SMS/webhook subscribers enabled for enterprise customers
- [ ] Components match product surfaces customers actually use
- [ ] Runbook: who can post updates (named individuals, not "anyone in eng")
- [ ] Test post quarterly (internal drill)

---

## 4. Media / trust center readiness

- [ ] Public trust center or security page (SOC 2, privacy policy, subprocessors)
- [ ] Media contact: `press@` or comms lead alias — monitored
- [ ] Executive bios + approved headshots (CEO statement ready)
- [ ] G2/Capterra owner accounts for review response <24h
- [ ] Social listening: LinkedIn + X keyword alerts on company + product name
- [ ] Generative search spot-check quarterly ("Is [Company] reliable?")

→ `references/security-questionnaire-deal-guide.md` · Vanta/Drata trust center patterns in `references/experts.md`

---

## 5. Tabletop exercise cadence

| Quarter | Scenario | Participants |
|---|---|---|
| Q1 | Multi-hour outage during peak usage | Eng, CS, comms, CEO |
| Q2 | Suspected credential leak | Eng, legal, comms |
| Q3 | Viral negative G2 + sales deal at risk | Marketing, sales, CS |
| Q4 | Layoff communication drill | CEO, HR, comms |

- [ ] 60-minute tabletop scheduled on calendar
- [ ] Post-drill: update contact tree + statement shells
- [ ] Document gaps in GTM ops backlog

---

## 6. Insurance / comms counsel contacts

| Type | Firm / contact | Policy # | Notes |
|---|---|---|---|
| Cyber insurance | | | Breach coach hotline |
| D&O insurance | | | Board notification |
| Employment counsel | | | Layoffs, WARN |
| Commercial counsel | | | Customer contracts, regulatory |
| PR agency (retainer or standby) | | | See `saas-pr-crisis-experts.md` |

- [ ] Cyber policy **breach coach** number in contact tree
- [ ] Know whether policy covers PR/crisis management fees
- [ ] Retainer or LOE signed with B2B SaaS PR firm before Series B (recommended)

---

## 7. Internal enablement

- [ ] All employees: "no social posts about incidents" policy in handbook
- [ ] Sales + CS trained on FAQ doc location
- [ ] `revenue-team-onboarding` includes crisis contact tree pointer
- [ ] Pause rules for marketing automation during Sev 3+ documented

---

## 8. Integration with GTM stack

| System | Crisis use |
|---|---|
| CRM | Flag at-risk accounts during outage; log exec outreach |
| Support desk | Incident macro + priority queue |
| Sequencer | Pause outbound to affected domains |
| Slack | War room channel template |
| Investor update template | `investor-updates` — crisis addendum section |

---

## Sign-off

| Role | Name | Date reviewed |
|---|---|---|
| CEO | | |
| Comms lead | | |
| Legal | | |

**Next tabletop date:** ___________

**Canonical playbook:** `references/crisis-management-playbook.md` · **Pattern 33**
