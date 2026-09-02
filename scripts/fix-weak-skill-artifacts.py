#!/usr/bin/env python3
"""Add missing framework-notes.md, output-template.md, and update Execution Artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

# Skill-specific reference index: path -> (authority, use_when)
REF_INDEX: dict[str, dict[str, tuple[str, str]]] = {
    "founder-led/gtm-recruiting": {
        "references/inclusive-recruiting.md": (
            "It's Destiny Recruiting / Google re:Work",
            "Structured, inclusive interview loops without tokenization",
        ),
        "references/offer-negotiation.md": (
            "Betts Recruiting / Bridge Group",
            "OTE, equity, and close tactics for passive GTM candidates",
        ),
        "references/recruiter-partners.md": (
            "Betts Recruiting",
            "When to use contingency search vs in-house sourcing",
        ),
    },
    "founder-led/gtm-role-descriptions": {
        "references/comp-benchmarks.md": ("Bridge Group / RepVue", "OTE and quota benchmarks by role"),
        "references/gtm-engineer-hiring.md": ("Operator GTM patterns", "GTM engineer JD and comp bands"),
        "references/hr-gtm-playbook.md": ("SaaS HR operators", "Role sequencing and headcount planning"),
        "references/org-by-stage.md": ("David Skok / stage models", "Org chart by ARR stage"),
        "references/role-catalog.md": ("LeadMagic catalog", "Standard GTM role definitions"),
        "references/saas-comp-strategies.md": ("Patrick Campbell / OpenView", "Comp plan design patterns"),
    },
    "founder-led/hiring-by-role": {
        "references/interview-experts.md": (
            "Mark Roberge / Lou Adler",
            "Role-specific interview frameworks and scorecards",
        ),
    },
    "inbound/linkedin-algorithm": {
        "references/richard-van-der-blom-algorithm.md": (
            "Richard van der Blom (Just Connecting)",
            "Format rankings, dwell time, golden hour, interest graph mechanics",
        ),
    },
    "inbound/linkedin-live-strategy": {
        "references/jessie-lizak-linkedin-live.md": (
            "Jessie Lizak (Reveting)",
            "WinsDay Live engine, repurposing clips to feed posts",
        ),
    },
    "inbound/sales-navigator-prospecting": {
        "references/morgan-ingram-sales-navigator.md": (
            "Morgan J. Ingram (AMP Social)",
            "Filter-specific messaging, saved searches, insight+question engagement",
        ),
    },
    "management-leadership/gtm-leadership": {
        "references/benioff-v2mom-guide.md": ("Marc Benioff / Salesforce", "V2MOM planning for GTM orgs"),
        "references/cro-enterprise-strategy.md": ("Enterprise CRO operators", "Board-level GTM strategy"),
        "references/expert-frameworks.md": ("GTM leadership index", "Subsidiary expert map"),
        "references/resignation-playbook.md": ("HR best practice", "Executive departure communications"),
    },
    "outbound/cold-email-copywriting": {
        "references/email-frameworks.md": ("Joanna Wiebe / operators", "Message structure and CTA patterns"),
        "references/pat-spielmann-outbound-copy.md": (
            "Pat Spielmann",
            "Cold to Gold, Full-Circle multichannel copy",
        ),
        "references/sequence-touch-library.md": ("Operator library", "Multi-touch email variants"),
        "references/subject-line-patterns.md": ("Outbound research", "Subject line A/B patterns"),
    },
    "outbound/cold-email-strategy": {
        "references/becc-holland-playbook.md": ("Becc Holland", "Diagnostic selling, stellar email, SDR KPIs"),
        "references/deliverability-primer.md": ("Google Bulk Sender / operators", "Infra prerequisites"),
        "references/email-frameworks.md": ("Copy frameworks", "Sequence structure"),
        "references/eric-nowoslawski-outbound.md": (
            "Eric Nowoslawski (Growth Engine X)",
            "Scale infra, Creative Ideas, unit economics",
        ),
        "references/expert-frameworks.md": ("Expert index", "Outbound subsidiary map"),
        "references/jordan-crawford-blueprint-gtm.md": (
            "Jordan Crawford (Blueprint GTM)",
            "PQS, PVP, FIND, Cannonball GTM",
        ),
        "references/justin-michael-sales-borg.md": (
            "Justin Michael",
            "Sales Borg, TQ stack, human/bot division",
        ),
        "references/lemlist-guillaume-outbound.md": ("Guillaume Moubeche", "Problem-first, CTC multichannel"),
        "references/leslie-venetz-buyer-first-outbound.md": (
            "Leslie Venetz",
            "Earn-the-Right gate, buyer-first segmentation",
        ),
    },
    "outbound/domain-infrastructure": {
        "references/deliverability-primer.md": ("Google / Microsoft sender docs", "DNS and reputation basics"),
        "references/output-artifacts.md": ("Skill tables", "Extended domain/mailbox inventories"),
        "references/provider-decision-matrix.md": (
            "Eric Nowoslawski / operators",
            "Google vs M365 vs Zoho for cold email",
        ),
    },
    "outbound/email-deliverability": {
        "references/bounce-complaint-procedures.md": ("Google Bulk Sender Guidelines", "Bounce/complaint handling"),
        "references/deliverability-primer.md": ("Operator primer", "SPF/DKIM/DMARC fundamentals"),
        "references/output-artifacts.md": ("Skill tables", "Authentication audit fields"),
        "references/sending-limits-reference.md": ("Provider docs", "Per-mailbox and per-domain limits"),
    },
    "outbound/reply-handling": {
        "references/reply-funnel-reference.md": ("Operator playbook", "Reply routing and SLA tiers"),
        "references/reply-taxonomy.md": ("Outbound ops", "Positive/negative/OOO classification"),
    },
    "outbound/sending-platforms": {
        "references/deliverability-primer.md": ("Infra context", "Platform selection constraints"),
        "references/platform-comparison.md": (
            "Instantly / Smartlead / Lemlist / Outreach",
            "Feature and scale comparison matrix",
        ),
    },
    "product-led-growth/developer-gtm": {
        "references/vercel-developer-selling.md": (
            "Lee Robinson / Vercel",
            "Developer community GTM, docs-led distribution",
        ),
    },
    "sales-revops/buyer-indecision": {
        "references/jolt-playbook.md": (
            "Matthew Dixon & Ted McKenna",
            "JOLT moves: Judge, Offer, Limit, Take risk off table",
        ),
    },
    "abm/strategic-gifting": {
        "references/giftology-ruhlin.md": ("John Ruhlin — Giftology", "Go-deep-not-wide gifting principles"),
        "references/sendoso-playbook.md": ("Sendoso", "Platform logistics and campaign triggers"),
        "references/gifting-platforms.md": ("Sendoso / Alyce / Reachdesk", "Platform comparison"),
        "references/gifting-by-tier.md": ("ITSMA ABM", "1:1 vs 1:few vs 1:many gift budgets"),
        "references/gift-compliance.md": ("FCPA / corp policy", "Legal and employer gift caps"),
        "references/gifting-sequence.md": ("ABM operators", "Gift timing in deal journey"),
    },
    "growth/review-platforms": {
        "references/g2-playbook.md": ("G2 Grid Methodology", "Review velocity and Grid placement"),
        "references/trustradius-playbook.md": ("TrustRadius", "Enterprise depth reviews"),
        "references/review-platform-comparison.md": ("Vendor research", "G2 vs TrustRadius vs Capterra"),
    },
}

THIN_EXPAND: dict[str, str] = {
    "growth/review-platforms": """# Review Platforms — Framework Notes

Reference index for `SKILL.md`. G2/TrustRadius/Capterra are **distribution channels**, not growth hacks.

## Primary Frameworks

- **G2 Grid Methodology** — review recency + volume + market presence drive Grid placement; stale reviews decay rank.
- **TrustRadius** — enterprise buyers expect depth (use case, ROI, comparisons); longer-form reviews outperform star-only.
- **Capterra / Gartner Digital Markets** — paid placement vs organic; disclose spend in `gtm-spend-management`.
- **FTC Endorsement Guides** — no incentives for reviews; no quid pro quo; disclose material connections.
- **G2 Terms of Service** — no review gating (login wall for gift), no employee-only campaigns presented as customers.

## Operating Rules

| Rule | Why |
|---|---|
| Ask at milestone moments only | NPS peak, renewal, implementation win — not day-3 onboarding |
| Route negatives <48h offline | Public thread escalation kills conversion |
| Segment asks by persona | Admin vs end-user reviews serve different buyers |
| Track review velocity weekly | Recency matters more than total count after ~20 reviews |

## Agent Routing

| Question | Action |
|---|---|
| Review ask timing | Follow milestone table in `SKILL.md` |
| Platform choice | G2 for mid-market SaaS; TrustRadius for enterprise depth |
| Validate output | Run `scripts/check-output.py` |
""",
    "gtm-ops/gtm-tool-cost-model": """# GTM Tool Cost Model — Framework Notes

Reference index for `SKILL.md`. Model **fully-loaded** GTM stack cost, not list price.

## Primary Frameworks

- **David Skok — SaaS Metrics** — CAC payback must include tooling + services, not just payroll.
- **Bessemer Cloud Index** — benchmark G&A and S&M as % revenue by stage.
- **OpenView SaaS Benchmarks** — tooling spend bands for Series A–C.
- **Vendor list-price vs negotiated** — always model renewal uplift (10–20% default unless contracted).

## Cost Buckets

| Bucket | Examples | Allocation |
|---|---|---|
| Data & enrichment | Clay, ZoomInfo, LeadMagic | Per SDR/AE seat or per enriched lead |
| Sequencing | Instantly, Outreach, Salesloft | Per sender mailbox + platform fee |
| CRM & ops | HubSpot, Salesforce, Attio | Per seat + integration middleware |
| Intent & ABM | 6sense, Demandbase, RollWorks | Per target account or impression |
| Support & CS | Zendesk, Intercom, Plain | Per agent + automation tier |

## Agent Routing

| Question | Action |
|---|---|
| Build cost model | Use `templates/output-template.md` |
| Compare vendors | Cross-link `tool-selection-stack`, `revops-tech-stack` |
| Validate output | Run `scripts/check-output.py` |
""",
    "management-leadership/revenue-team-onboarding": """# Revenue Team Onboarding — Framework Notes

Reference index for `SKILL.md`. Onboarding is **time-to-first-meeting**, not time-to-Slack-emoji.

## Primary Frameworks

- **Winning by Design — Bowtie** — onboarding spans pre-sale handoff through activation; align CS + sales.
- **Mark Roberge — Sales Acceleration Formula** — hire → train → coach loop; 30-60-90 ramp scorecard.
- **SaaS onboarding research (WbD / Gainsight)** — time-to-value predicts expansion and churn.
- **Bridge Group SDR Metrics** — ramp expectations: meetings/month by week 4, 8, 12.

## Ramp Milestones

| Week | SDR | AE |
|---|---|---|
| 1 | ICP, tooling, shadow calls | Territory, CRM hygiene, ride-alongs |
| 2 | First sequences live (supervised) | First disco calls scheduled |
| 4 | Quota-path meetings/week | Pipeline $ target (stage 1+) |
| 8 | Full sequence ownership | First late-stage opp or closed-won path |
| 12 | Full quota | Full quota |

## Agent Routing

| Question | Action |
|---|---|
| Build 30-60-90 | Use `templates/output-template.md` |
| Role-specific ramp | Cross-link `gtm-role-descriptions`, `sales-coaching` |
| Validate output | Run `scripts/check-output.py` |
""",
    "founder-led/founder-comp-playbook": """# Founder Comp Playbook — Framework Notes

Reference index for `SKILL.md`. Founder compensation is **governance + signal**, not just cash.

## Primary Frameworks

- **Patrick Campbell (ProfitWell)** — founder salary bands by stage; underpaying signals risk to investors.
- **Carta / Pulley cap table data** — equity refresh and dilution modeling for founder grants.
- **SaaS Capital compensation surveys** — CEO/CRO cash comp by ARR band.
- **YC standard docs** — 4-year vest, 1-year cliff for founder-adjacent exec grants.

## Decision Rules

| Stage | Cash guidance | Equity note |
|---|---|---|
| Pre-revenue | Minimal livable salary | Preserve founder % for seed |
| $1–5M ARR | Market minus 20–30% | Refresh grants for co-founders if diluted |
| $5–20M ARR | Approaching market | Separate operating vs board roles |
| $20M+ ARR | Market comp | Performance equity tied to ARR/EBITDA |

## Agent Routing

| Question | Action |
|---|---|
| Model founder package | Use `templates/output-template.md` |
| Exec comp comparison | Cross-link `executive-compensation`, `equity-management` |
| Validate output | Run `scripts/check-output.py` |
""",
    "abm/strategic-gifting": """# Strategic Gifting — Framework Notes

Reference index for `SKILL.md`. Gifting is a **relationship signal**, not a pipeline hack.

## Primary Frameworks

- **John Ruhlin — Giftology** — go-deep-not-wide; remarkable > remarkable logo; never bribe.
- **Sendoso / Alyce / Reachdesk** — logistics layer: address verify, warehouse, CRM triggers.
- **ITSMA ABM** — tier budgets: 1:1 highest touch cost per account, 1:few scaled, 1:many digital only.
- **Winning by Design Bowtie** — physical touchpoints post-commit, not pre-problem-fit.
- **FCPA / corporate gift policy** — legal caps vary by industry; always check buyer employer policy.

## Gift Decision Matrix

| Deal stage | Gift? | Alternative |
|---|---|---|
| Cold outbound | Rarely | Research-led note, no swag |
| Active evaluation | Maybe | Send to team, not sole decision-maker |
| Verbal yes / procurement | Yes | Thank champion, ease signature |
| Post-close | Yes | Onboarding welcome, not upsell bribe |
| Lost deal | No | Relationship note only |

## Deep References

- Platform ops and compliance tables → `SKILL.md` Step-by-Step Process
- ABM tier budgets → `abm-strategy`, `account-selection`

## Agent Routing

| Question | Action |
|---|---|
| Design gift play | Use `templates/output-template.md` |
| Sendoso setup | Cross-link `event-driven-outreach` for direct mail |
| Validate output | Run `scripts/check-output.py` |
""",
}


def parse_frontmatter(content: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    fm = m.group(1)
    meta: dict = {}
    frameworks: list[str] = []
    in_meta = False
    in_fw = False
    for line in fm.splitlines():
        if line.startswith("metadata:"):
            in_meta = True
            continue
        if in_meta:
            if re.match(r"^\S", line):
                in_meta = False
            elif line.strip().startswith("frameworks:"):
                in_fw = True
                continue
            elif in_fw:
                if line.strip().startswith("- "):
                    frameworks.append(line.strip()[2:].strip().strip('"').strip("'"))
                elif re.match(r"^\s{4}-\s+", line):
                    frameworks.append(line.strip()[2:].strip().strip('"').strip("'"))
                else:
                    in_fw = False
            continue
        if line.strip().startswith("frameworks:"):
            val = line.split(":", 1)[1].strip()
            if val.startswith("["):
                frameworks = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
            in_fw = True
            continue
        if in_fw and line.strip().startswith("- "):
            frameworks.append(line.strip()[2:].strip().strip('"').strip("'"))
    return {"frameworks": frameworks}


def humanize(name: str) -> str:
    return name.replace("-", " ").title()


def make_framework_notes(skill_key: str, skill_dir: Path) -> str:
    skill_name = skill_dir.name
    title = humanize(skill_name)
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    frameworks = fm.get("frameworks", [])

    lines = [
        f"# {title} — Framework Notes",
        "",
        "Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.",
        "",
    ]

    if frameworks:
        lines.extend(["## Primary Frameworks", ""])
        for fw in frameworks[:10]:
            lines.append(f"- **{fw}**")
        lines.append("")

    index = REF_INDEX.get(skill_key, {})
    refs = sorted(p for p in skill_dir.glob("references/*.md") if p.name != "framework-notes.md")
    if refs:
        lines.extend(["## Deep-dive references", "", "| File | Authority | Use when |", "|---|---|---|"])
        for ref in refs:
            rel = f"references/{ref.name}"
            auth, use = index.get(rel, ("See SKILL.md", "Extended tables and examples"))
            lines.append(f"| `{rel}` | {auth} | {use} |")
        lines.append("")

    tmpl_count = len(list(skill_dir.glob("templates/*.md"))) if (skill_dir / "templates").exists() else 0
    if tmpl_count > 1 or (skill_dir / "templates").exists():
        lines.extend(["## Templates", ""])
        if (skill_dir / "templates" / "output-template.md").exists():
            lines.append("- `templates/output-template.md` — Primary deliverable shell")
        for t in sorted(skill_dir.glob("templates/*.md")):
            if t.name == "output-template.md":
                continue
            lines.append(f"- `templates/{t.name}` — Role-specific deliverable")
        lines.append("")

    lines.extend([
        "## Agent routing",
        "",
        "| Question | Action |",
        "|---|---|",
        "| Full process | Follow `SKILL.md` step-by-step |",
        "| Build deliverable | Start from `templates/output-template.md` |",
        "| Validate output | Run `scripts/check-output.py` |",
        "",
        "Before final output, cite which framework shaped the recommendation.",
        "",
    ])
    return "\n".join(lines)


def ensure_output_template(skill_dir: Path) -> bool:
    path = skill_dir / "templates" / "output-template.md"
    if path.exists():
        return False
    skill_name = skill_dir.name
    title = humanize(skill_name)
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    # Extract output format section
    m = re.search(r"## Output Format\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    out_fmt = m.group(1).strip() if m else ""

    lines = [f"# {title} — Deliverable", "", "## Context", "- Company / product:", "- Owner:", "- Date:", ""]

    if out_fmt and len(out_fmt) > 80:
        lines.extend(["## Deliverable spec", "", out_fmt[:2000], ""])
        if len(out_fmt) > 2000:
            lines.append("*(See SKILL.md Output Format for full spec.)*")
            lines.append("")
    else:
        lines.extend(["## Core output", "[Fill per SKILL.md Output Format]", ""])

    # List other templates if skill has many
    others = [t for t in skill_dir.glob("templates/*.md") if t.name != "output-template.md"]
    if others:
        lines.extend(["## Specialized templates", ""])
        for t in sorted(others):
            lines.append(f"- `{t.relative_to(skill_dir)}`")
        lines.append("")

    lines.extend(["## Quality check", "- [ ] Named framework cited in recommendations", "- [ ] All required fields populated", ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return True


def update_execution_artifacts(skill_dir: Path) -> bool:
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    fn_line = "- `references/framework-notes.md` — Framework index and authority routing"

    if "## Execution Artifacts" not in content:
        return False
    if fn_line in content:
        return False

    content = content.replace(
        "## Execution Artifacts\n\n",
        f"## Execution Artifacts\n\n{fn_line}\n",
        1,
    )
    skill_md.write_text(content, encoding="utf-8")
    return True


def guess_ref_description(filename: str, skill_name: str) -> tuple[str, str]:
    name = filename.replace(".md", "").replace("-", " ")
    if "expert" in filename or "framework" in filename:
        return ("Expert index", "Subsidiary authority map")
    if "primer" in filename:
        return ("Operator primer", "Prerequisites and fundamentals")
    if "template" in filename or "output" in filename:
        return ("Skill tables", "Extended output fields and inventories")
    if "comparison" in filename or "matrix" in filename:
        return ("Vendor research", "Selection and tradeoff matrix")
    return (f"{humanize(skill_name)} reference", f"Extended {name} detail")


def fix_decoration_filler(skill_dir: Path) -> bool:
    """Replace batch-script decoration filler with SKILL.md authority content."""
    fn_path = skill_dir / "references" / "framework-notes.md"
    if not fn_path.exists():
        return False
    text = fn_path.read_text(encoding="utf-8")
    if "do not cite it as decoration" not in text:
        return False

    skill_key = str(skill_dir.relative_to(SKILLS))
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    frameworks = fm.get("frameworks", [])

    auth = ""
    for heading in ("## Authoritative Foundations", "## Frameworks Referenced"):
        m = re.search(rf"^{re.escape(heading)}\n\n(.*?)(?=\n## |\Z)", content, re.MULTILINE | re.DOTALL)
        if m:
            auth = m.group(1).strip()
            break

    title = humanize(skill_dir.name)
    lines = [
        f"# {title} — Framework Notes",
        "",
        "Reference index for `SKILL.md`. Apply named frameworks to justify recommendations.",
        "",
    ]
    if frameworks:
        lines.extend(["## Primary Frameworks", ""])
        for fw in frameworks[:10]:
            lines.append(f"- **{fw}**")
        lines.append("")

    if auth:
        # Strip markdown links to keep notes portable; keep named authorities
        auth_clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", auth)
        auth_clean = re.sub(r"`([^`]+)`", r"\1", auth_clean)
        lines.extend(["## Authoritative foundations", "", auth_clean[:2500], ""])
        if len(auth_clean) > 2500:
            lines.append("*(See SKILL.md for full detail.)*")
            lines.append("")

    phases = extract_process_phases(content)
    if phases:
        lines.extend(["## Process phases", ""])
        for p in phases:
            lines.append(f"- {p}")
        lines.append("")

    lines.extend([
        "## Agent routing",
        "",
        "| Question | Action |",
        "|---|---|",
        "| Full process | Follow `SKILL.md` step-by-step |",
        "| Build deliverable | Use `templates/output-template.md` |",
        "| Validate output | Run `scripts/check-output.py` |",
        "",
    ])
    fn_path.write_text("\n".join(lines), encoding="utf-8")
    return True


def extract_process_phases(content: str) -> list[str]:
    proc = re.search(r"## Step-by-Step Process\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not proc:
        return []
    phases = re.findall(r"^### (Phase \d+[^:\n]*|Step \d+[^:\n]*)", proc.group(1), re.MULTILINE)
    if not phases:
        phases = re.findall(r"^### ([^\n]+)", proc.group(1), re.MULTILINE)
    return phases[:8]


def expand_generic_framework_notes(skill_dir: Path) -> bool:
    skill_key = str(skill_dir.relative_to(SKILLS))
    fn_path = skill_dir / "references" / "framework-notes.md"
    if not fn_path.exists():
        return False
    text = fn_path.read_text(encoding="utf-8")
    if "## Deep-dive references" in text and len(text) >= 800:
        return False

    index = REF_INDEX.get(skill_key, {})
    refs = [p for p in sorted(skill_dir.glob("references/*.md")) if p.name != "framework-notes.md"]
    if not refs:
        return False

    # Merge auto-discovered refs into index
    for ref in refs:
        rel = f"references/{ref.name}"
        if rel not in index:
            index[rel] = guess_ref_description(ref.name, skill_dir.name)
    REF_INDEX[skill_key] = index

    fn_path.write_text(make_framework_notes(skill_key, skill_dir), encoding="utf-8")
    return True


def main() -> int:
    created_fn = 0
    created_ot = 0
    updated_ea = 0
    expanded = 0
    generic_expanded = 0

    for skill_key in REF_INDEX:
        skill_dir = SKILLS / skill_key
        fn_path = skill_dir / "references" / "framework-notes.md"
        if not fn_path.exists():
            fn_path.parent.mkdir(parents=True, exist_ok=True)
            fn_path.write_text(make_framework_notes(skill_key, skill_dir), encoding="utf-8")
            created_fn += 1
            print(f"  + framework-notes: {skill_key}")

        if ensure_output_template(skill_dir):
            created_ot += 1
            print(f"  + output-template: {skill_key}")

        if update_execution_artifacts(skill_dir):
            updated_ea += 1

    # saas-outcomes missing output-template only
    saas = SKILLS / "founder-led" / "saas-outcomes"
    if ensure_output_template(saas):
        created_ot += 1
        print("  + output-template: founder-led/saas-outcomes")
        update_execution_artifacts(saas)

    for skill_key, text in THIN_EXPAND.items():
        path = SKILLS / skill_key / "references" / "framework-notes.md"
        if path.exists():
            path.write_text(text, encoding="utf-8")
            expanded += 1
            print(f"  ~ expanded: {skill_key}")

    decoration_fixed = 0
    for skill_md in sorted(SKILLS.rglob("SKILL.md")):
        if expand_generic_framework_notes(skill_md.parent):
            generic_expanded += 1
            print(f"  ~ generic→rich: {skill_md.parent.relative_to(SKILLS)}")

    for skill_md in sorted(SKILLS.rglob("SKILL.md")):
        if fix_decoration_filler(skill_md.parent):
            decoration_fixed += 1
            print(f"  ~ decoration→authority: {skill_md.parent.relative_to(SKILLS)}")

    print(f"\nCreated framework-notes: {created_fn}")
    print(f"Created output-template: {created_ot}")
    print(f"Updated Execution Artifacts: {updated_ea}")
    print(f"Expanded thin framework-notes: {expanded}")
    print(f"Expanded generic framework-notes: {generic_expanded}")
    print(f"Fixed decoration filler: {decoration_fixed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
