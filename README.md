# GTM Skills

[![Skills](https://img.shields.io/badge/skills-206-blue)](skills/) [![Categories](https://img.shields.io/badge/categories-24-green)](skills/) [![Release](https://img.shields.io/github/v/release/LeadMagic/gtm-skills)](https://github.com/LeadMagic/gtm-skills/releases) [![CI](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE) [![Stars](https://img.shields.io/github/stars/LeadMagic/gtm-skills?style=social)](https://github.com/LeadMagic/gtm-skills)

**206 production GTM agent skills for Claude Code.** Sales, outbound, prospecting, RevOps, ABM, PLG, customer success, founder-led GTM, analytics, and automation — each with framework-cited playbooks, templates, and QA scripts.

Not a prompt pack. An agent-skills repository: portable folders with SKILL.md instructions, reference notes, output templates, and validation scripts. Install what you need. Leave the rest.

---

## Quick Install

### Claude Code (Plugin)

```text
/plugin marketplace add LeadMagic/gtm-skills
/plugin install gtm-skills@gtm-skills
```

### Smart CLI (Pick Your Skills)

Don't want all 206? Pick exactly what you need:

```bash
git clone https://github.com/LeadMagic/gtm-skills.git
cd gtm-skills

# Interactive menu
python3 scripts/cc-gtm.py

# Install a category
python3 scripts/cc-gtm.py --category outbound

# Install a curated bundle
python3 scripts/cc-gtm.py --bundle outbound-stack

# Install specific skills
python3 scripts/cc-gtm.py --skills rb2b-outbound-triggers,cold-email-strategy

# Claude Desktop mode
python3 scripts/cc-gtm.py --desktop --bundle startup-essentials

# List everything
python3 scripts/cc-gtm.py --list
```

Installs to `.claude/skills/gtm-skills/` — Claude Code auto-discovers them.

### Claude Desktop

1. Run `python3 scripts/cc-gtm.py --desktop --bundle <name> --project ./output`
2. Upload skill folders to [claude.ai/customize/skills](https://claude.ai/customize/skills)
3. Paste `claude-desktop-instructions.md` into Project Instructions
4. Ask Claude: "what GTM skills are available?"

---

## Curated Bundles

| Bundle | Skills | For |
|---|---:|---|
| `outbound-stack` | 7 | Cold email from zero |
| `prospecting-stack` | 6 | Find and verify leads |
| `sales-revops-stack` | 8 | Close deals |
| `founder-gtm` | 7 | Founder-led sales |
| `inbound-stack` | 6 | Inbound engine |
| `cs-stack` | 5 | Customer success |
| `analytics-stack` | 5 | Measure everything |
| `automation-stack` | 6 | Automate GTM |
| `abm-stack` | 4 | Account-based marketing |
| `tools-stack` | 5 | Platform toolkits |
| `startup-essentials` | 8 | First 8 skills every founder needs |

```bash
python3 scripts/cc-gtm.py --list-bundles
```

---

## 24 Categories - 206 Skills

<details>
<summary><b>Click to expand full catalog</b></summary>

| Category | # | Skills |
|---|---:|---|
| **foundation** | 8 | using-gtm-skills, gtm-context, icp-scoring, icp-targeting-tiers, positioning-messaging, pricing-strategy, buyer-psychology, competitive-intel |
| **outbound** | 10 | cold-email-strategy, cold-email-copywriting, cold-calling, domain-infrastructure, email-deliverability, inbox-setup, sending-platforms, reply-handling, multi-channel-outreach, rb2b-outbound-triggers |
| **prospecting** | 8 | lead-finding, lead-enrichment, email-finding, contact-verification, list-building, signal-scoring, data-enrichment-strategy, social-intent-monitoring |
| **sales-revops** | 8 | pipeline-management, meeting-prep, deal-desk, demo-scripts, objection-handling, sales-enablement, buyer-indecision, transparency-selling |
| **analytics** | 13 | gtm-metrics, attribution, campaign-analytics, tracking-plan, a-b-testing, growth-experimentation, gtm-system-architecture, marketing-strategy, paid-advertising, proactive-alerts, event-analytics, deliverability-monitoring, 1p-tagging-pixels |
| **automation** | 12 | clay-automation, n8n-automation, crm-integration, api-enrichment, waterfall-enrichment, mcp-setup, hubspot-setup, salesforce-setup, attio-setup, ai-sdr-setup, tool-selection-stack, skills-lock |
| **tools** | 15 | clay-toolkit, sequencing-toolkit, n8n-toolkit, ai-prompts-toolkit, crm-toolkit, analytics-toolkit, clay-loops-toolkit, leadmagic-toolkit, support-toolkit, smartlead-workflows, instantly-sequences, lemlist-setup, outreach-sequences, salesloft-cadences, hubspot-sequences |
| **founder-led** | 41 | solo-founder-gtm, founder-sales, fundraising-strategy, financial-modeling, pitch-deck-builder, pricing-psychology, saas-metrics-calculator, building-saas, brand-kit, content-led-growth, founder-brand, engineer-to-founder, and 30 more |
| **inbound** | 8 | content-marketing, inbound-triage, landing-pages, seo-strategy, linkedin-algorithm, linkedin-live-strategy, sales-navigator-prospecting, social-selling, website-visitor-identification |
| **content-seo** | 6 | seo-strategy, pillar-pages, pseo-strategy, aeo-strategy, faq-seo, citation-harvesting |
| **creative** | 12 | vibe-marketing, ai-content-creation, ai-video-creation, copywriting, landing-page-copy, ad-creative-strategy, social-media-strategy, content-distribution, growth-hacking-tactics, graphic-design-gtm, v0-lander, vibe-coding |
| **design** | 7 | pitch-deck-builder, battlecard-builder, case-study-builder, one-pager-builder, roi-calculator, design-system-gtm, ui-ux-gtm |
| **customer-success** | 7 | customer-onboarding, cs-playbooks, cs-analytics-dashboards, sla-management, headless-support, qbr-planning, support-tool-stack |
| **abm** | 7 | abm-strategy, account-selection, abm-1-to-1, abm-1-to-few, abm-1-to-many, multi-thread-orchestration, strategic-gifting |
| **growth** | 5 | expansion-selling, churn-prevention, customer-marketing, referral-programs, review-platforms |
| **gtm-ops** | 5 | gtm-operations, revops-tech-stack, campaign-governance, gtm-spend-management, gtm-tool-cost-model |
| **lifecycle** | 5 | mql-nurture, lifecycle-drips, onboarding-sequences, churn-prediction, re-engagement |
| **management-leadership** | 5 | gtm-leadership, sales-coaching, team-management, revenue-team-onboarding, executive-compensation |
| **sales-plays** | 5 | funding-signal-play, hiring-signal-play, job-change-play, earnings-signal-play, product-launch-play |
| **leadmagic** | 6 | leadmagic-cli, leadmagic-mcp, leadmagic-waterfall, leadmagic-bulk-enrichment, leadmagic-job-change, leadmagic-integrations |
| **demand-gen** | 4 | webinar-strategy, podcast-gtm, paid-social-strategy, content-syndication |
| **product-led-growth** | 3 | plg-strategy, freemium-optimization, developer-gtm |
| **events** | 3 | conference-strategy, event-driven-outreach, field-marketing |
| **partnerships** | 3 | partnership-strategy, co-marketing, integration-partnerships |

</details>

---

## What Makes This Different

- **Artifact-first.** Every skill produces copy, plans, scorecards, runbooks, dashboards, workflows, templates, scripts, and QA checklists.
- **Authority-backed.** 712 named frameworks from 110+ practitioners: Force Management, Winning by Design, April Dunford, Jeb Blount, Andy Whyte (MEDDICC), Todd Caponi, Chris Walker, Richard van der Blom, Jessie Lizak, Morgan Ingram, Eric Nowoslawski, Joey Gilkey, Jordan Crawford, Adam Robinson (RB2B), and more.
- **Progressive disclosure.** Skill name + description load at startup. Full SKILL.md loads on activation. References, templates, and scripts load on demand.
- **Validated in CI.** Every skill passes structure validation, reference integrity, and public hygiene checks on every push.
- **SHA256 integrity.** skills.lock verifies every skill file hash.
- **Zero telemetry.** Static skills and local scripts only.

---

## How Skills Work

```
skills/<category>/<skill-name>/
  SKILL.md                        # Instructions + frontmatter (name, description, triggers)
  references/framework-notes.md   # Named frameworks, citation anchors
  templates/output-template.md     # Copy-paste deliverable structure
  scripts/check-output.py          # Local quality validator
```

1. **Discovery** - Claude reads name + description from frontmatter
2. **Activation** - When your task matches, Claude loads SKILL.md
3. **Execution** - References, templates, and scripts load on demand

---

## Install Guide

| Platform | Command |
|---|---|
| **Claude Code** | `/plugin marketplace add LeadMagic/gtm-skills` then `/plugin install gtm-skills@gtm-skills` |
| **Smart CLI** | `python3 scripts/cc-gtm.py` (interactive) or `--category` / `--bundle` / `--skills` |
| **Claude Desktop** | `python3 scripts/cc-gtm.py --desktop --bundle <name>` then upload to [claude.ai/customize/skills](https://claude.ai/customize/skills) |
| **Claude Code CLI** | `claude plugin marketplace add LeadMagic/gtm-skills --scope user` |
| **Manual** | Copy skill folders to `.claude/skills/` in your project |

Full install docs: [docs/INSTALL.md](docs/INSTALL.md)

---

## Validate Locally

```bash
npm run verify
```

Expected: 206 skills checked, 0 errors, 0 warnings, lock verified, installer dry-run OK.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills must cite named authorities, produce concrete artifacts, pass validation, and avoid private/internal details.

---

## License

[MIT](LICENSE) - LeadMagic. Free for commercial and personal use.

---

Built by [LeadMagic](https://leadmagic.io/?utm_source=github&utm_medium=organic&utm_campaign=gtm-skills) - B2B enrichment, email verification, and job-change signals.

Star this repo if it helps you ship faster.
