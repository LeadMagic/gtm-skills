---
name: hiring-by-role
description: >-
  Role-specific hiring guides for B2B SaaS — interview questions, evaluation
  criteria, scorecards, and assessment methods for engineering, sales, marketing,
  customer success, product, and design roles. Based on best practices from
  Betts Recruiting, Bridge Group, SaaStr, YC, and Google re:Work. Use when
  building an interview process for a specific role or evaluating candidates
  systematically. Triggers on: "interview questions for [role]", "how to
  hire [role]", "scorecard for [role]", "evaluate [role] candidates".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.3.0"
  author: LeadMagic
  category: founder-led
  tags: [hiring, interviews, scorecards, recruiting, evaluation, role-specific]
  related_skills: [gtm-recruiting, gtm-role-descriptions, job-posting-strategy, first-hires-playbook, sales-team-building, hiring-contractors, employment-compliance, revops-tech-stack, clay-toolkit, n8n-automation, revenue-team-onboarding]
  frameworks:
    - "Google re:Work — Structured interviewing and hiring"
    - "Betts Recruiting — GTM role evaluation"
    - "Bridge Group — SaaS sales compensation and hiring benchmarks"
    - "YC — Hiring and evaluating founders/early employees"
    - "Laszlo Bock — Work Rules! (Google hiring practices)"
    - "Patty McCord — Powerful (Netflix hiring for talent density)"
    - "RevOps Co-op — GTM systems hiring patterns"
    - "Stacey Nordwall (Culture Amp / Pyn) — Structured onboarding handoff from hire to ramp"
---

# Hiring by Role

## Overview

Every role requires a different evaluation approach. Hiring an engineer like
you'd hire a salesperson = mediocre hires in both roles. The mistake: using
the same interview process for every position — a generic "tell me about
yourself" plus some technical trivia. This skill covers role-specific interview
design, evaluation criteria, scorecards, and assessment methods for the 6 core
GTM roles. Based on structured hiring practices from Google re:Work, Betts
Recruiting, and YC.

## When to Use

Trigger phrases: "interview questions for engineer", "how to hire a salesperson",
"evaluate marketing candidates", "CS interview scorecard", "product manager
interview", "designer interview questions", "hire GTM engineer", "GTM engineer
interview", "evaluate RevOps candidates", "role-specific hiring guide"

## Authoritative Foundations

### Google re:Work — Structured Interviewing
Google's research proved: structured interviews with consistent questions and
scorecards predict performance 2x better than unstructured interviews. Key
principle: ask every candidate the same questions. Score on predefined
criteria. Compare apples to apples. Load `gtm-recruiting` for inclusive
scorecard template and diversity-of-thought hiring (It's Destiny Recruiting).
Full expert map: `references/interview-experts.md`.

### Laszlo Bock — Work Rules!
"Don't trust your gut. Gut instinct is just pattern recognition on incomplete
data. Use structured interviews, work samples, and scorecards."

### Betts Recruiting — GTM Evaluation
"Past performance is the best predictor of future performance. But past
QUOTA ATTAINMENT, not past experience. A 10-year VP Sales who never hit
quota is worse than a 2-year AE who hit 150% every quarter."

**Question banks:** Interviewer scripts → `templates/interviewer-questions-gtm.md`.
GTM Engineer scorecard → `templates/gtm-engineer-scorecard.md` (canonical interview loop).
Role definition + JD → `gtm-role-descriptions` → `skills/founder-led/gtm-role-descriptions/references/gtm-engineer-hiring.md`.
Candidate questions (both sides) → `templates/candidate-questions-to-ask.md`.

## Core Principles (All Roles)

1. **Structured process:** Same questions, same scorecard, same evaluators for
   every candidate for a given role.
2. **Work sample over interview:** A real task reveals more than 10 hours of
   conversation. Every role should include a work sample.
3. **Scorecard before discussion:** Each interviewer scores independently
   before discussing with the panel. Prevents groupthink.
4. **Multiple perspectives:** Minimum 3 interviewers. At least 1 from outside
   the hiring team.
5. **No "culture fit" assessment:** "Culture fit" is how unconscious bias
   hides. Assess: values alignment, working style compatibility, and
   contribution to team culture — not "would I get a beer with this person?"

## Role-by-Role Hiring Guides

### Engineering

**What you're evaluating:** Technical skill, shipping velocity, problem-solving
approach, code quality, collaboration, technical communication.

**Interview process (5 stages, 2-week clock):**
1. **Screen (30 min):** "Tell me about the most technically challenging project
   you've built. What made it hard? How did you solve it?" Look for:
   specificity (they built it, not their team), problem-solving depth,
   intellectual honesty about tradeoffs.

2. **Work sample — take-home or pair (2-4 hours):** Build a small feature or
   fix a bug in a codebase similar to yours. NOT LeetCode — real work. Evaluate:
   code quality, testing, documentation, design decisions, shipping speed.

3. **Technical deep dive (60 min):** Walk through their work sample. "Why did
   you choose this approach? What would you do differently with more time?
   How would this scale to 1000x the data?" Look for: depth of understanding,
   ability to reason about tradeoffs, comfort with ambiguity.

4. **System design (60 min — if senior):** "Design [system relevant to your
   product]." Look for: architecture thinking, scalability awareness,
   tradeoff discussion, asking clarifying questions.

5. **Team/values (30 min):** 2-3 team members. "Tell me about a time you
   disagreed with a teammate. How did you resolve it?" "What's the best
   feedback you've ever received?" Look for: collaboration, low ego,
   direct communication, growth mindset.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) | Notes |
|---|---|---|---|
| Technical Skill | 30% | | |
| Shipping Velocity | 25% | | |
| Problem Solving | 20% | | |
| Communication | 15% | | |
| Collaboration | 10% | | |

### GTM Engineer

**Before interviews:** Write the JD with `gtm-role-descriptions` →
`skills/founder-led/gtm-role-descriptions/templates/gtm-engineer-jd.md` and `skills/founder-led/gtm-role-descriptions/references/gtm-engineer-hiring.md` (role vs
RevOps / SE / Growth Engineer). Salary + OKR bonus — not quota.

**What you're evaluating:** Workflow design, data quality, CRM fluency, API
integration, GTM judgment, documentation. Portfolio required — not years of tenure.

**Interview process (5 stages, 2-week clock):**
1. **Screen (30 min):** "Walk me through a GTM workflow you shipped. What metric
   moved?" Role-boundary question (GTM Eng vs RevOps vs SE). Request portfolio link.
2. **Work sample (paid, 3–4 hrs):** Enrich 50 accounts → score ICP → CRM push with
   field mapping doc. Evaluate verify step, error handling, cost awareness.
3. **Technical review (60 min):** Walk work sample. Scale, provider order, sync
   tradeoffs, credit optimization.
4. **GTM judgment (45 min):** Stakeholder scenario (Marketing MQL vs Sales list
   quality). Design a signal play trigger → sequence.
5. **Team/values (30 min):** Runbooks, vacation handoff, security hygiene.

**Evaluation scorecard:** Full weighted rubric in `templates/gtm-engineer-scorecard.md`.

| Criteria | Weight |
|---|---|
| Workflow design | 25% |
| Data quality | 20% |
| CRM fluency | 15% |
| API / integration | 15% |
| GTM judgment | 15% |
| Documentation | 10% |

**Onboarding handoff:** `revenue-team-onboarding` — CRM/Clay/n8n access day 0.

### Sales (AE / SDR / VP Sales / RevOps)

**Before interviews:** Write the JD and comp plan with `gtm-role-descriptions`
(role catalog, org placement) + `executive-compensation` (Pattern 35: OTE × quota
math via `ote-calculator-template.md`, `comp-plan-design-worksheet.md`). Bands →
`comp-benchmarks.md`. Post via `job-posting-strategy`. Offer OTE must match
published JD range — candidates check RepVue.

**RevOps vs GTM Engineer:** RevOps interviews focus on forecast, CRM policy, and
cross-functional alignment. GTM Engineer interviews focus on Clay/n8n artifacts and
enrichment — use `gtm-engineer-scorecard.md`, not the sales numbers test.

**What you're evaluating:** Track record (quota attainment), discovery skill,
communication, resilience, coachability, competitive drive.

**The "tell me about your numbers" test (5 minutes):**
"Walk me through your last 4 quarters. Quota. Attainment %. Pipeline generated.
Deals closed. Average deal size. Why did you hit or miss each quarter?"
A great salesperson can answer this without hesitation. A mediocre one stumbles.

**Interview process (4 stages):**
1. **Screen (30 min):** Numbers. "Walk me through your last 4 quarters." Then:
   "Sell me this pen" is a terrible question. Instead: "We sell [product].
   Based on what you've learned in this conversation, how would you open a
   cold call to a VP Sales at a 50-person SaaS company?"

2. **Mock discovery call (45 min):** You role-play a prospect. They run a
   discovery call. Evaluate: do they ask great questions? Do they listen? Do
   they build a business case? Or do they pitch features?

3. **Mock demo/presentation (45 min):** They present your product (or a
   product they know well) to a panel. Evaluate: do they tailor to the
   audience? Do they connect features to outcomes? Can they handle objections?

4. **Team/values (30 min):** "Tell me about the toughest deal you ever lost.
   What happened? What did you learn?" Look for: accountability, resilience,
   learning from failure.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) |
|---|---|---|
| Quota Attainment History | 35% | |
| Discovery Skill (asks, listens, diagnoses) | 25% | |
| Communication & Presence | 20% | |
| Coachability | 10% | |
| Competitive Drive / Resilience | 10% | |

### Marketing

**What you're evaluating:** Strategic thinking, content quality, analytical
rigor, creativity, channel expertise, writing ability, project ownership.

**Work sample (the most important stage):**
- Content marketer: "Write a blog post outline for [topic targeting our ICP]."
- Demand gen: "Design a campaign for [goal]. Include: channels, targeting,
  creative strategy, budget, and success metrics."
- Product marketer: "Write a launch plan for [upcoming feature]. Include:
  positioning, messaging, channels, timeline, and success metrics."
- Growth marketer: "Analyze this data [provide real data]. What's the biggest
  growth opportunity? Design an experiment to capture it."

**Interview process (4 stages):**
1. **Screen (30 min):** "Walk me through a campaign or project you're most
   proud of. What was your role? What was the result? What would you do
   differently?"
2. **Work sample (async, 2-4 hours):** Role-specific task.
3. **Deep dive (60 min):** Walk through work sample. Probe: "Why this approach?
   What alternatives did you consider? How would you measure success?"
4. **Team/values (30 min):** "Tell me about a time data proved you wrong."
   Look for: analytical honesty, comfort being wrong, learning from data.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) |
|---|---|---|
| Strategic Thinking | 30% | |
| Execution Quality (work sample) | 30% | |
| Analytical Rigor | 20% | |
| Creativity | 10% | |
| Collaboration | 10% | |

### Customer Success

**What you're evaluating:** Relationship building, business acumen, problem-solving,
communication, empathy, commercial instinct (expansion).

**Interview process (4 stages):**
1. **Screen (30 min):** "Tell me about a customer relationship you're most proud
   of. What made it successful? What was hard about it?" "How do you handle
   a customer who's about to churn?"
2. **Role-play: difficult conversation (30 min):** "I'm a customer. My NPS
   score just dropped from 9 to 5. My champion left the company. Call me."
3. **QBR presentation (30 min):** "Present a mock QBR for a customer who's
   been with us for 6 months." Evaluate: business acumen, value quantification,
   expansion identification.
4. **Team/values (30 min):** "Tell me about a time you disagreed with a
   customer. How did you handle it?" Look for: customer advocacy balanced
   with business reality, difficult conversation skill.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) |
|---|---|---|
| Relationship Building | 30% | |
| Business Acumen | 25% | |
| Communication | 20% | |
| Problem-Solving | 15% | |
| Commercial Instinct | 10% | |

### Product Management

**What you're evaluating:** Product sense, analytical thinking, user empathy,
technical fluency, prioritization, stakeholder management, written communication.

**Work samples:**
- "Identify the biggest product opportunity based on this data [provide user
  behavior data]."
- "Write a PRD for [specific feature]. Include: problem, evidence, solution,
  success metrics."
- "Prioritize these 6 features. Explain your framework and reasoning."

**Interview process (4 stages):**
1. **Screen (30 min):** "Tell me about a product you shipped that failed.
   Why did it fail? What did you learn?" Look for: ownership of failure,
   intellectual honesty.
2. **Product sense (45 min):** "Improve [product you both know]. What would
   you change and why?" Look for: user-first thinking, structured approach.
3. **Analytical (45 min):** "Here's data from our product. Diagnose what's
   happening and recommend next steps." Look for: data fluency, hypothesis
   generation, actionable recommendations.
4. **Team/values (30 min):** "Tell me about a time engineering pushed back
   on your product spec. How did you handle it?" Look for: collaboration,
   flexibility, ability to influence without authority.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) |
|---|---|---|
| Product Sense / User Empathy | 30% | |
| Analytical Thinking | 25% | |
| Execution & Prioritization | 20% | |
| Communication (written + verbal) | 15% | |
| Technical Fluency | 10% | |

### Design

**What you're evaluating:** Visual design skill, interaction design, user
research, systems thinking, tool proficiency, portfolio quality.

**Portfolio review (most important):** "Walk me through 3 projects. For each:
what problem were you solving? What was YOUR specific contribution? What
would you change if you could do it again?" Look for: they did the work
(not their team), design rationale, iteration based on feedback, outcomes.

**Work sample:** "Redesign this page [provide page/screen]. 2 hours. Explain
your decisions."

**Interview process (3 stages):**
1. **Portfolio review (45 min):** Walkthrough. "Why this solution? What
   alternatives did you explore?"
2. **Design exercise (45 min):** "Design a [feature] for [product]. Think
   aloud. Show your process." OR: "Critique this design. What works? What
   doesn't? What would you change?"
3. **Team/values (30 min):** "Tell me about a time engineering couldn't
   build what you designed. What happened?" Look for: collaboration, pragmatism.

**Evaluation scorecard:**
| Criteria | Weight | Score (1-5) |
|---|---|---|
| Visual Design Quality | 30% | |
| Interaction / UX Thinking | 25% | |
| Problem-Solving Process | 20% | |
| Communication of Design Decisions | 15% | |
| Collaboration | 10% | |

## Output Format

```
INTERVIEW PLAN — [Role] at [Company]

PROCESS: [N stages, timeline]
INTERVIEW PANEL: [names and roles]

SCORECARD: [criteria table with weights]

STAGE 1 — SCREEN (30 min):
Questions:
1. [question] — what to look for
2. [question] — what to look for
3. [question] — what to look for

STAGE 2 — WORK SAMPLE (async, X hours):
Task: [specific task]
Evaluation: [criteria]

STAGE 3 — DEEP DIVE (X min):
[Role-specific deep dive]

STAGE 4 — TEAM/VALUES (30 min):
Questions:
1. [question]
2. [question]

DECISION: Scorecard average > 4.0 = strong hire. 3.5-4.0 = hire with reservations.
< 3.5 = no hire. No exceptions for "gut feeling."
```

## Implementation Checklist

- [ ] Structured process documented (same questions, same scorecard per role)
- [ ] Work sample designed (real task, not brainteaser)
- [ ] Scorecard with weighted criteria (not "overall impression")
- [ ] Multiple interviewers (3+. At least 1 outside hiring team)
- [ ] Independent scoring (each interviewer scores before discussing)
- [ ] No "culture fit" language (use values alignment, working style)
- [ ] No questions about age, family, religion, health, or other protected
  characteristics (illegal and irrelevant)
- [ ] Decision thresholds defined (scorecard > X = hire)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Trusting gut over scorecard.** "They didn't score well, but I liked them."
   Likability bias is one of the strongest hiring biases. Fix: If scorecard <
   threshold, no hire. Gut is a tiebreaker, not a decider.

2. **Same process for every role.** Engineering interview for sales candidate =
   "what's your favorite data structure?" Salesperson walks out. Fix:
   Role-specific processes.

3. **No work sample.** "They interviewed well" but can't do the actual work.
   Fix: Every role includes a work sample that mirrors the actual job.

4. **"Would I get a beer with them?" test.** Filters for people like you.
   Reduces diversity. Amplifies unconscious bias. Fix: Assess values alignment,
   working style, and contribution to team — not social compatibility.

5. **Asking about past salary.** Banned in many states. Anchors offer to
   previous pay (which may reflect discrimination). Fix: Pay based on the
   role, not the candidate's previous salary.

6. **Years of experience as a requirement.** "15+ years experience" filters
   out the 10-year person who's done 3x as much. Fix: Describe what they've
   achieved, not how long they've been working.

## Execution Artifacts

- `references/interview-experts.md` — re:Work, Betts, Roberge, Destiny, Bock, Nordwall handoff
- `../gtm-role-descriptions/references/hr-gtm-playbook.md` — post-hire onboarding system (Pattern 28)
- `templates/gtm-engineer-scorecard.md` — full loop + work sample for GTM Engineer
- `templates/interviewer-questions-gtm.md` — SDR, AE, manager, VP, RevOps, GTM Engineer, CS
- `templates/candidate-questions-to-ask.md` — both sides; offer-stage + panel
- `templates/output-template.md` — interview plan deliverable
- `scripts/check-output.py` — validates interview plan sections

## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Related Skills

- `job-posting-strategy` — Where to post jobs by role, sourcing channels
- `first-hires-playbook` — First 10 hires, compensation, interview design
- `sales-team-building` — Sales team structure, POD design, compensation
- `employment-compliance` — Legal requirements for hiring
- `co-founder-dynamics` — Evaluating co-founders
