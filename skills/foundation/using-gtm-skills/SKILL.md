---
name: using-gtm-skills
description: >-
  Complete guide to using the gtm-skills repository — installation, skill
  discovery, skill loading, combining skills, taxonomy navigation, CLI
  workflows, and advanced patterns for every supported AI system (Claude Code,
  Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI).
  The master key to the entire library. Use when first installing gtm-skills,
  discovering which skills to load, or building multi-skill workflows.
  Triggers on: "gtm-skills", "install gtm-skills", "how to use gtm-skills",
  "skill discovery", "which skills to load", "getting started with skills".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [gtm-skills, installation, discovery, taxonomy, getting-started, master-guide]
  related_skills: [skills-lock]
  frameworks:
    - "LeadMagic/gtm-skills — 176+ GTM agent skills"
---

# Using gtm-skills

## Overview

176 skills. 20+ categories. Every GTM discipline. This is the master key.
The mistake: cloning the repo and not knowing where to start — loading random
skills, missing dependencies, or treating skills as documentation instead of
executable playbooks. This skill covers the complete usage guide: installation,
discovery, loading patterns, multi-skill workflows, and advanced tactics for
getting maximum value from the gtm-skills library.

## When to Use

Trigger phrases: "gtm-skills", "install gtm-skills", "how to use gtm-skills",
"which skill for [task]", "skill discovery", "find skill for [topic]",
"taxonomy navigation", "combine skills", "skill dependencies"

## Installation

### Claude Code (Primary)
```bash
claude plugins add LeadMagic/gtm-skills
# Skills auto-discover. Ask: "list gtm skills"
```

### Hermes Agent
```bash
hermes skills install LeadMagic/gtm-skills
# Or manual: git clone to ~/.hermes/skills/
```

### Cursor
```bash
git clone https://github.com/LeadMagic/gtm-skills.git
# Cursor reads SKILL.md files from the repo. Add to .cursor/skills/
```

### Codex (OpenAI)
```bash
codex skills install LeadMagic/gtm-skills
```

### OpenCode
```bash
git clone https://github.com/LeadMagic/gtm-skills.git
# OpenCode auto-discovers SKILL.md files. Point config to repo.
```

### Windsurf
```bash
git clone https://github.com/LeadMagic/gtm-skills.git
# Add path to Windsurf skills directory
```

### GitHub Copilot
```bash
git clone https://github.com/LeadMagic/gtm-skills.git
# Add skills/ path to .github/copilot-instructions.md
```

### Gemini CLI
```bash
git clone https://github.com/LeadMagic/gtm-skills.git ~/.claude/skills/
# Gemini reads Claude-format skills
```

### Verify Installation
After install, ask your agent: "list gtm skills" or "what skills are available for [task]?"

### Integrity Check (skills.lock)
```bash
# Verify no tampered or corrupted skills
python3 -c "
import json, hashlib
with open('skills.lock') as f:
    lock = json.load(f)
for name, meta in lock['skills'].items():
    with open(meta['path'], 'rb') as fh:
        actual = hashlib.sha256(fh.read()).hexdigest()
    if actual != meta['sha256']:
        print(f'TAMPERED: {name}')
print('All skills verified.')
"
```

## Skill Discovery

### By Category (What You're Trying to Do)

| If You Need To... | Load These Categories |
|---|---|
| **Raise money, manage equity, run a board** | `founder-led/` (fundraising-strategy, financial-modeling, board-meeting-prep, equity-management) |
| **Sell as a founder or build a sales team** | `founder-led/` (founder-sales), `sales-revops/` (sales-enablement, demo-scripts, deal-desk) |
| **Build outbound / cold email** | `outbound/` (cold-email-strategy, cold-email-copywriting, email-deliverability, domain-infrastructure) |
| **Find and enrich leads** | `prospecting/` (lead-finding, lead-enrichment, email-finding, contact-verification) |
| **Automate GTM workflows** | `automation/` (clay-automation, n8n-automation, waterfall-enrichment, tool-selection-stack) |
| **Content, social, creative** | `creative/` (vibe-marketing, ai-content-creation, copywriting, social-media-strategy), `content-seo/` |
| **Customer success and support** | `customer-success/` (cs-playbooks, customer-onboarding, sla-management, headless-support) |
| **Analytics and metrics** | `analytics/` (gtm-metrics, event-analytics, campaign-analytics, attribution) |
| **AI-native GTM (vibe coding/marketing)** | `creative/` (vibe-coding, vibe-marketing, v0-lander, ai-content-creation, ai-video-creation) |
| **Legal, compliance, security** | `founder-led/` (legal-for-founders, soc2-compliance, data-privacy-compliance, security-assessments, business-insurance) |
| **Hiring and team building** | `founder-led/` (first-hires-playbook, job-posting-strategy, hiring-by-role, sales-team-building) |
| **Design and brand** | `design/` (pitch-deck-builder, roi-calculator, design-system-gtm, brand-kit) |

### By Trigger Phrase

```
Tell your agent: "I need to [task]"
It will match to the right skill automatically.

Examples:
- "I need to build a pitch deck" → pitch-deck-builder
- "I need to set up cold email infrastructure" → domain-infrastructure, email-deliverability
- "I need to raise a seed round" → fundraising-strategy, yc-ecosystem, vc-outreach
- "I need to build a landing page with AI" → v0-lander, vibe-coding
- "I need to hire my first salesperson" → sales-team-building, hiring-by-role, job-posting-strategy
```

### Quick Reference: Top 10 Most-Used Skills

| # | Skill | Use For |
|---|---|---|
| 1 | `cold-email-strategy` | Building outreach sequences |
| 2 | `pitch-deck-builder` | Investor and sales presentations |
| 3 | `founder-sales` | Founder-led sales motion |
| 4 | `fundraising-strategy` | Raising capital |
| 5 | `vibe-marketing` | AI-powered marketing at scale |
| 6 | `financial-modeling` | P&L, runway, DCF valuation |
| 7 | `gtm-metrics` | SaaS metrics dashboard |
| 8 | `lead-finding` | Prospecting and list building |
| 9 | `sales-enablement` | Decks, one-pagers, battlecards |
| 10 | `solo-founder-gtm` | Bootstrapper GTM playbook |

## Loading and Combining Skills

### Single Skill
```
"Load the founder-sales skill and help me with [task]"
```

### Multiple Skills (Workflow)
```
"I need to: 1) find leads, 2) write cold emails, 3) set up domains.
Load lead-finding, cold-email-copywriting, and domain-infrastructure."
```

### Dependency Chain (Auto-Load)
Skills declare dependencies in their frontmatter. Your agent should load
dependencies automatically. Example: `founder-sales` depends on `pricing-strategy`
and `sales-enablement`. When you load `founder-sales`, your agent should
also load its dependencies.

### The "Full Stack" Pattern
For complex GTM projects, load the entire stack:
```
"Build a complete outbound engine for [company]. Load:
- lead-finding, lead-enrichment, email-finding, contact-verification (prospecting)
- cold-email-strategy, email-deliverability, domain-infrastructure (outbound)
- clay-automation (automation)
- gtm-metrics (analytics)"
```

## Advanced Patterns

### Pattern 1: Research → Build → Launch
```
1. competitive-intel + positioning-messaging (research the market)
2. pitch-deck-builder + pricing-strategy (build the assets)
3. launch-planning + content-marketing (launch)
```

### Pattern 2: Hire → Onboard → Manage
```
1. job-posting-strategy + hiring-by-role (hire)
2. customer-onboarding + first-hires-playbook (onboard)
3. team-management + sales-coaching (manage)
```

### Pattern 3: Data → Decision → Action
```
1. gtm-metrics + event-analytics (collect data)
2. cs-analytics-dashboards + financial-modeling (make decisions)
3. expansion-selling + churn-prevention (take action)
```

### Pattern 4: AI-First GTM (The Vibe Stack)
```
1. vibe-coding → Build landing pages, tools, dashboards
2. vibe-marketing → Generate campaigns, content, creative
3. ai-content-creation → Scale blog, social, email production
4. ai-video-creation → Produce video without a video team
```

## Skill Structure (What's Inside Every Skill)

Every skill in gtm-skills follows this structure:

1. **Overview** — What mistake does this skill prevent? (principle-first)
2. **When to Use** — Trigger phrases that activate this skill
3. **Authoritative Foundations** — Named experts and frameworks cited
4. **Step-by-Step Process** — Numbered phases with concrete outputs
5. **Output Format** — What the deliverable looks like
6. **Quality Checklist** — Verifiable checkboxes before considering it done
7. **Common Pitfalls** — Numbered mistakes with root cause + fix
8. **Related Skills** — What to load next

## Skill Quality Standards

Every gtm-skills skill is:
- **Principle-first** — Opens with the mistake it prevents, not a description
- **Authority-anchored** — Names specific practitioners and frameworks
- **Executable** — Step-by-step. You can follow it without asking questions
- **Pitfall-aware** — Teaches what goes wrong, not just what goes right
- **Artifact-producing** — Every skill produces something (document, deck, calculator, dashboard)
- **Non-fluff** — No guru nonsense. No AI-generated filler. No "one weird trick."

## Navigating the Repo

```
gtm-skills/
├── README.md              # Hero, install, category overview, authority catalog
├── skills.lock             # SHA256-verified integrity for all 176+ skills
├── taxonomy.csv            # slug → name → category → description → priority
├── AGENTS.md              # Cross-tool skill index
├── CLAUDE.md              # Claude Code-specific index
├── skills/
│   ├── foundation/         # ICP, positioning, pricing, competitive intel
│   ├── founder-led/        # 35+ skills — everything a founder needs
│   ├── prospecting/        # Lead finding, enrichment, verification
│   ├── outbound/           # Cold email, deliverability, domains, inboxes
│   ├── automation/         # Clay, n8n, enrichment waterfalls, tool stacks
│   ├── creative/           # AI content, vibe coding/marketing, growth hacks
│   ├── design/             # Pitch decks, ROI calculators, brand systems
│   ├── sales-revops/       # Sales enablement, demo scripts, deal desk
│   ├── analytics/          # Metrics, event analytics, attribution
│   ├── inbound/            # Content marketing, landing pages, social selling
│   ├── customer-success/   # CS playbooks, support, onboarding, SLAs
│   ├── growth/             # Churn prevention, expansion, referrals
│   └── ...                 # 20+ categories total
├── scripts/
│   ├── validate-skills.js  # YAML validator — runs in CI
│   └── generate-skills-lock.sh
└── .github/workflows/
    └── validate.yml        # CI: validates all skills on push and PR
```

## Contributing

See `CONTRIBUTING.md` in the repo. Quick rules:
- Use the template: `skills/_TEMPLATE.md`
- Every skill cites named authorities
- No internal tool internals exposed (blackbox rule)
- Every new skill → update `taxonomy.csv`
- Run `node scripts/validate-skills.js` before PR
- Run `bash scripts/generate-skills-lock.sh` after adding skills
- Every skill must work without paid tools

## Output Format (This Guide)

```
GTM-SKILLS USAGE PLAN

TASK: [what you're trying to do]

RECOMMENDED SKILLS:
1. [skill] — [why]. Dependencies: [list]
2. [skill] — [why]
3. [skill] — [why]

LOAD SEQUENCE:
"Load [skill-1], [skill-2], and [skill-3]. Then help me [task]."

ESTIMATED TIME: [X hours/minutes]
EXPECTED OUTPUT: [what you'll have when done]
```

## Quality Checklist (For Agents Using gtm-skills)

- [ ] Identified the right skills for the task (use taxonomy or discovery)
- [ ] Loaded skill dependencies (check `related_skills` in frontmatter)
- [ ] Followed the skill's step-by-step process (not just read the overview)
- [ ] Produced the expected output format
- [ ] Checked against the skill's quality checklist before considering it done
- [ ] Reviewed the common pitfalls section (prevents known mistakes)
- [ ] Verified skills.lock integrity before executing
- [ ] Combined skills when the task spans multiple domains

## Expert Voices: Who Built This

gtm-skills is maintained by LeadMagic, built by operators who run real GTM
infrastructure. Every skill draws from:

- **Winning by Design** — SPICED methodology, Bowtie funnel, POD structures
- **Reforge** — Growth loops, experimentation, retention frameworks
- **YC Partners** — Paul Graham, Sam Altman, Michael Seibel, Dalton Caldwell
- **SaaStr / Jason Lemkin** — SaaS benchmarks, founder sales, hiring
- **David Skok (Matrix)** — SaaS unit economics, CAC payback, sales learning curve
- **Betts Recruiting** — GTM hiring and talent strategy
- **Bridge Group** — SaaS sales compensation and hiring data
- **Andrej Karpathy** — Vibe coding philosophy
- **Pieter Levels, Sahil Lavingia, Marc Lou** — AI-assisted solo building
- **Brian Balfour, Andrew Chen, Sean Ellis** — Growth hacking
- **Nielsen Norman Group, Baymard Institute, Steve Krug** — UX research
- **Ben Murray (SaaS CFO), Aswath Damodaran (NYU)** — Financial modeling
- **Brad Feld, Fred Wilson** — Venture capital and board governance

No fluff. All science. Built by operators.

## Related Skills

- `skills-lock` — Verify skill integrity before use