# CRM Implementation Partners & Services

Use partners for **speed and specialized config** — not strategy. Document process in `pipeline-management` and `crm-integration` before engaging.

## When to Hire vs Self-Serve

| Situation | Self-serve | Partner |
|---|---|---|
| HubSpot Starter, < 5 users | ✓ | |
| HubSpot Pro + marketing automation | Maybe | ✓ if no RevOps hire |
| Salesforce first implementation | | ✓ always |
| Attio < $3M ARR | ✓ | Contractor for migrations |
| Migration from SF ↔ HubSpot | | ✓ |
| CPQ, territories, Einstein | | ✓ Salesforce SI |

## Partner Types

| Type | Delivers | Typical cost | Duration |
|---|---|---|---|
| **CRM implementation SI** | Object model, flows, migration, training | $15K–$150K+ | 6–16 weeks |
| **HubSpot Solutions Partner** | Portal setup, integrations, HubSpot best practices | $5K–$50K | 4–8 weeks |
| **RevOps agency** | Process + CRM + reporting + Clay | $5K–$20K/mo | Ongoing |
| **Freelance Salesforce admin** | Flows, fixes, reports | $75–$200/hr | Ad hoc |
| **Data hygiene vendor** | Dedupe, enrich, verify | $0.05–$0.20/record | Project |

## HubSpot Ecosystem

Find partners: HubSpot Solutions Directory (filter by tier: Elite, Diamond, Platinum).

**What to ask:**
- References in your ARR band ($1–10M vs enterprise)
- Migration experience from Salesforce
- Clay / enrichment integration projects
- Post-launch support model (hours vs retainer)

**Red flags:** No discovery phase; unlimited scope fixed fee; no data model doc delivered.

## Salesforce Ecosystem

Find partners: Salesforce AppExchange Consulting, partner tier (Summit, Crest, etc.).

**Specializations to match:**
- B2B SaaS opportunity model
- CPQ + subscription (if usage-based pricing)
- Marketing Cloud (only if needed — often separate from CRM project)
- Experience Cloud (customer portal)

**Red flags:** 100% custom Apex before standard objects configured; no admin handoff plan.

## Attio

No large SI tier like Salesforce. Options:

- **In-house** with Attio docs + `attio-setup` skill
- **RevOps contractors** familiar with API-first CRM
- **Migration specialists** (often HubSpot/SF freelancers pivoting)

## RevOps & GTM Ops Agencies

Use for ongoing ops when you won't hire RevOps yet. Evaluate with `hiring-agencies` pilot structure.

| Agency type | Good for | Verify |
|---|---|---|
| Clay-focused RevOps | Enrichment, outbound data, CRM sync | Sample table + CRM field map |
| Full-stack RevOps | CRM + reporting + process | WbD GTM Index score before start |
| Outbound agency | Sequences (not CRM architecture) | Domain + deliverability ownership |
| Demand gen agency | HubSpot marketing hub | Attribution model defined |

**Public names founders reference (evaluate — not endorsements):**
- HubSpot: SmartBug, New Breed, Lean Labs (inbound/marketing-heavy)
- Salesforce: Simplus, Coastal, Arkus (SI)
- RevOps community: RevOps Co-op vendor lists, Pavilion referrals
- Boutique: Carabiner Group (HubSpot), Gradient Works (ops strategy)

Always run **90-day pilot** with weekly scorecard (`hiring-agencies` template).

## RFP Checklist

- [ ] Current CRM and data volume (contacts, deals, history)
- [ ] GTM motion diagram (inbound, outbound, PLG)
- [ ] Required integrations (Clay, billing, product analytics)
- [ ] Contacts vs leads decision documented
- [ ] Stage definitions with exit criteria
- [ ] Admin owner named post-project
- [ ] Training plan for reps (2 weeks post go-live)
- [ ] Data migration acceptance criteria (dup rate < 1%)

## Handoff to Internal Team

Partners should deliver:

1. Data model diagram (objects, fields, required)
2. Automation catalog (workflows/flows with triggers)
3. Report/dashboard inventory
4. Runbook for enrichment and dedupe
5. 10-hour admin training recording

Then hire or designate RevOps owner — agencies amplify process; internal owns hygiene.

## Related Skills

- `hiring-agencies` — pilot, scorecard, kill switches
- `hiring-contractors` — freelance admin
- `crm-integration` — operating model before config
- `hubspot-setup` / `salesforce-setup` / `attio-setup` — platform playbooks
