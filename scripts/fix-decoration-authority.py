#!/usr/bin/env python3
"""Replace generic 'decoration' authority filler in SKILL.md with substantive foundations."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

DECORATION = "do not cite it as decoration"

# Substring hints → actionable one-liner (first match wins)
FRAMEWORK_HINTS: list[tuple[str, str]] = [
    ("ITSMA", "Tier-based ABM (1:1 / 1:few / 1:many); measure pipeline from target accounts, not lead volume."),
    ("Force Management", "Command of the Message — persona-specific value narrative and differentiation per stakeholder."),
    ("Giftology", "Go-deep-not-wide relationship gifting; remarkable personalization beats logo swag."),
    ("Sendoso", "Sending platform for physical touchpoints — address verify, warehouse, CRM triggers."),
    ("Winning by Design", "Bowtie lifecycle model — align sales, marketing, and CS on stage-based outcomes."),
    ("MEDDICC", "Qualification scorecard — Metrics, Economic buyer, Decision criteria, Champion, Competition."),
    ("SPICED", "Discovery framework — Situation, Pain, Impact, Critical event, Decision."),
    ("Challenger", "Teach-tailor-take control — reframe buyer thinking with insight-led conversations."),
    ("JOLT", "Late-stage indecision — Judge, Offer recommendation, Limit exploration, Take risk off table."),
    ("April Dunford", "Positioning — competitive alternatives, differentiated value, target segment."),
    ("Geoffrey Moore", "Crossing the Chasm — beachhead segment and whole-product thinking."),
    ("David Skok", "SaaS metrics — CAC payback, LTV/CAC, unit economics by stage."),
    ("Patrick Campbell", "ProfitWell pricing research — willingness-to-pay and packaging."),
    ("Brian Balfour", "Growth loops — acquisition/retention loops, not funnel-only thinking."),
    ("Chris Walker", "Dark social demand — self-reported attribution; LinkedIn influence is unmeasurable in last-touch."),
    ("van der Blom", "LinkedIn Algorithm Insights — interest graph, format rankings, dwell time, golden hour."),
    ("Morgan J. Ingram", "Sales Navigator filter-specific prospecting — one message per intent signal."),
    ("Eric Nowoslawski", "Cold email infra at scale — 2 inboxes/domain, backup inboxes, Creative Ideas testing."),
    ("Jordan Crawford", "Blueprint GTM — PQS/PVP/FIND research-led outbound."),
    ("Leslie Venetz", "Buyer-first outbound — earn-the-right gate before sequence enrollment."),
    ("Becc Holland", "Diagnostic selling and stellar cold email — problem-first, not pitch-first."),
    ("Joanna Wiebe", "Message mining and conversion copy — customer language in hero and CTA."),
    ("Google Bulk Sender", "Sender authentication, complaint rates, and warmup requirements for bulk mail."),
    ("HubSpot", "Lifecycle stages, object model, and workflow enrollment patterns."),
    ("Salesforce", "Opportunity stages, forecasting categories, and RevOps object hygiene."),
    ("Clay", "Waterfall enrichment, Claygent research, and table-based GTM automation."),
    ("Instantly", "Mailbox rotation, campaign caps, and deliverability-first sending setup."),
    ("Smartlead", "Unlimited mailboxes, master inbox, and agency-scale cold email ops."),
    ("Outreach", "Sequence governance, task-based selling, and CRM-locked cadences."),
    ("Salesloft", "Cadence + coaching rhythm; rhythm-based pipeline management."),
    ("Lemlist", "Multichannel sequences — email, LinkedIn, calls in one enrollment."),
    ("n8n", "Workflow automation — HTTP nodes, webhooks, and GTM glue between tools."),
    ("MCP", "Model Context Protocol — tool servers for agent-safe CRM and enrichment access."),
    ("SOC 2", "Trust service criteria — security, availability, confidentiality controls."),
    ("GDPR", "Lawful basis, data minimization, DPA requirements for EU buyers."),
    ("G2", "Review recency and volume drive Grid placement; ethical ask timing only."),
    ("TrustRadius", "Enterprise review depth — use cases, comparisons, ROI narrative."),
    ("ChartMogul", "SaaS revenue analytics benchmarks — churn, expansion, cohort curves."),
    ("OpenView", "Expansion SaaS benchmarks — PLG, sales-assist, and GTM efficiency."),
    ("YC", "Startup operating cadence — default alive, talk to users, launch fast."),
    ("Mark Roberge", "Sales Acceleration Formula — hire, train, coach with quantitative ramp."),
    ("John Ruhlin", "Giftology — strategic gifting as relationship signal, not bribery."),
    ("Huthwaite SPIN", "Situation, Problem, Implication, Need-payoff discovery questioning."),
    ("Cialdini", "Influence principles — reciprocity, social proof, authority in copy."),
    ("AIDA", "Attention, Interest, Desire, Action — email structure for cold outreach."),
    ("PAS", "Problem, Agitate, Solution — pain-led cold email framing."),
    ("BAB", "Before, After, Bridge — contrast-led narrative for transformation pitches."),
]


def framework_blurb(name: str, overview: str) -> str:
    for hint, blurb in FRAMEWORK_HINTS:
        if hint.lower() in name.lower():
            return blurb
    if " — " in name:
        return name.split(" — ", 1)[1].strip()
    if overview:
        first = overview.split(".")[0].strip()
        if len(first) > 20:
            return f"Shapes deliverables for this skill — {first[:120]}."
    return f"Named methodology governing recommendations in this skill's process."


def parse_frontmatter(content: str) -> list[str]:
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return []
    fm = m.group(1)
    frameworks: list[str] = []
    in_fw = False
    for line in fm.splitlines():
        if line.strip().startswith("frameworks:"):
            val = line.split(":", 1)[1].strip()
            if val.startswith("["):
                frameworks = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
            in_fw = True
            continue
        if in_fw:
            if line.strip().startswith("- "):
                frameworks.append(line.strip()[2:].strip().strip('"').strip("'"))
            elif re.match(r"^\S", line):
                in_fw = False
    return frameworks


def extract_overview(content: str) -> str:
    m = re.search(r"## Overview\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    return m.group(1).strip() if m else ""


def build_authority_section(frameworks: list[str], overview: str) -> str:
    lines = ["## Authoritative Foundations", ""]
    for fw in frameworks:
        blurb = framework_blurb(fw, overview)
        lines.append(f"- **{fw}** — {blurb}")
    lines.append("")
    return "\n".join(lines)


def fix_skill(skill_md: Path) -> bool:
    content = skill_md.read_text(encoding="utf-8")
    if DECORATION not in content:
        return False

    frameworks = parse_frontmatter(content)
    if not frameworks:
        return False

    overview = extract_overview(content)
    new_section = build_authority_section(frameworks, overview)

    pattern = r"## (?:Authoritative Foundations|Frameworks Referenced)\n\n.*?(?=\n## )"
    if not re.search(pattern, content, re.DOTALL):
        return False

    new_content = re.sub(pattern, new_section, content, count=1, flags=re.DOTALL)
    if new_content == content:
        return False

    skill_md.write_text(new_content, encoding="utf-8")
    return True


def main() -> int:
    fixed = 0
    for skill_md in sorted(SKILLS.rglob("SKILL.md")):
        if fix_skill(skill_md):
            fixed += 1
            print(f"  fixed: {skill_md.parent.relative_to(SKILLS)}")
    print(f"\nFixed {fixed} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
