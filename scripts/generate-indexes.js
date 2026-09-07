#!/usr/bin/env node
/**
 * generate-indexes.js — regenerate README, AGENTS.md, CLAUDE.md,
 * taxonomy.csv, and Claude plugin metadata from actual marketplace-discoverable
 * skills on disk.
 */

const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.join(__dirname, "..");
const SKILLS_DIR = path.join(ROOT, "skills");
const PLUGIN_DIR = path.join(ROOT, ".claude-plugin");
const VERSION = JSON.parse(
  fs.readFileSync(path.join(ROOT, "package.json"), "utf8"),
).version;

// Human-facing category guide for references/skill-index-master.md (generated).
const CATEGORY_GUIDE = {
  abm: {
    title: "Account-Based Marketing",
    blurb: "Tiered ABM plays, gifting, multi-thread orchestration.",
    start: "abm-strategy",
  },
  analytics: {
    title: "Analytics & Measurement",
    blurb: "Attribution, experiments, GTM metrics, tracking plans.",
    start: "gtm-metrics",
  },
  automation: {
    title: "Automation & Integrations",
    blurb: "Clay, n8n, CRM setup, enrichment waterfalls.",
    start: "clay-automation",
  },
  "content-seo": {
    title: "Content & SEO",
    blurb: "SEO strategy, technical audits, pillars, pSEO, AEO, citations.",
    start: "seo-strategy",
  },
  creative: {
    title: "Creative & AI Content",
    blurb: "Vibe marketing, AI content/video, copywriting, growth hacks.",
    start: "vibe-marketing",
  },
  "customer-success": {
    title: "Customer Success",
    blurb: "Onboarding, CS playbooks, SLAs, headless support.",
    start: "customer-onboarding",
  },
  "demand-gen": {
    title: "Demand Generation",
    blurb: "Webinars, podcasts, paid social, syndication.",
    start: "webinar-strategy",
  },
  design: {
    title: "Design & Collateral",
    blurb: "Pitch decks, battlecards, ROI calculators, brand systems.",
    start: "pitch-deck-builder",
  },
  events: {
    title: "Events & Field",
    blurb: "Conferences, field marketing, event-driven outreach.",
    start: "conference-strategy",
  },
  foundation: {
    title: "Foundation & ICP",
    blurb: "Context bootstrap, ICP, positioning, pricing, master router.",
    start: "using-gtm-skills",
  },
  "founder-led": {
    title: "Founder-Led GTM",
    blurb: "Fundraising, hiring, legal, founder sales, solo GTM.",
    start: "solo-founder-gtm",
  },
  "gtm-ops": {
    title: "GTM Operations",
    blurb: "RevOps stack, spend, PM/RACI, campaign governance.",
    start: "gtm-operations",
  },
  growth: {
    title: "Growth & Expansion",
    blurb: "Referrals, expansion, churn prevention, reviews.",
    start: "expansion-selling",
  },
  inbound: {
    title: "Inbound & PLG-adjacent",
    blurb:
      "Content marketing, triage, landing pages, LinkedIn algorithm + Live, Sales Navigator, social selling, visitor ID.",
    start: "linkedin-algorithm",
  },
  leadmagic: {
    title: "LeadMagic Product",
    blurb: "CLI, MCP, waterfall, bulk enrichment integrations.",
    start: "leadmagic-waterfall",
  },
  "management-leadership": {
    title: "Leadership & Coaching",
    blurb: "GTM leadership, coaching, onboarding, exec comp.",
    start: "gtm-leadership",
  },
  lifecycle: {
    title: "Lifecycle Marketing",
    blurb: "MQL nurture, onboarding drips, churn, re-engagement.",
    start: "mql-nurture",
  },
  outbound: {
    title: "Outbound",
    blurb: "Cold email, calling, deliverability, domains, replies.",
    start: "cold-email-strategy",
  },
  partnerships: {
    title: "Partnerships",
    blurb: "Co-marketing, integrations, partner strategy.",
    start: "partnership-strategy",
  },
  "product-led-growth": {
    title: "Product-Led Growth",
    blurb: "PLG strategy, freemium optimization, developer GTM.",
    start: "plg-strategy",
  },
  "product-marketing": {
    title: "Product Marketing & Buyer Insight",
    blurb: "Customer research, buying journeys, and win/loss learning.",
    start: "customer-research",
  },
  prospecting: {
    title: "Prospecting & Data",
    blurb: "Lead finding, enrichment, verification, signals.",
    start: "lead-finding",
  },
  "sales-revops": {
    title: "Sales & RevOps",
    blurb: "Pipeline, demos, deal desk, enablement, objections.",
    start: "pipeline-management",
  },
  "sales-plays": {
    title: "Signal Sales Plays",
    blurb: "Funding, hiring, job change, earnings plays.",
    start: "funding-signal-play",
  },
  tools: {
    title: "GTM Toolkits & Sequencers",
    blurb:
      "Clay, CRM, n8n, analytics, support toolkits; sequencing-toolkit plus Instantly, Smartlead, lemlist, Outreach, Salesloft, HubSpot platform skills.",
    start: "clay-toolkit",
  },
};

function csvEscape(value) {
  const s = String(value ?? "");
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function parseFrontmatter(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  if (!content.startsWith("---\n"))
    throw new Error(`${filePath}: missing frontmatter`);
  const end = content.indexOf("\n---\n", 4);
  if (end === -1) throw new Error(`${filePath}: missing closing frontmatter`);
  const fmText = content.slice(4, end);
  const fm = {};
  const lines = fmText.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$/);
    if (!m) continue;
    const key = m[1];
    let value = m[2].trim();
    if (/^[>|]-?$/.test(value)) {
      const out = [];
      i += 1;
      while (
        i < lines.length &&
        (/^\s+/.test(lines[i]) || lines[i].trim() === "")
      ) {
        out.push(lines[i].trim());
        i += 1;
      }
      i -= 1;
      value = out.join(" ").replace(/\s+/g, " ").trim();
    }
    fm[key] = value.replace(/^['"]|['"]$/g, "");
  }
  return { fm, fmText, content };
}

function parseFrameworks(fmText) {
  const frameworks = [];
  const inline = fmText.match(/^\s*frameworks:\s*\[([^\]]*)\]/m);
  if (inline) {
    for (const item of inline[1].split(",")) {
      const cleaned = item.trim().replace(/^['"]|['"]$/g, "");
      if (cleaned) frameworks.push(cleaned);
    }
    return frameworks;
  }
  // Block list: capture every "    - item" line (mirrors validate-skills.js).
  const block = fmText.match(/^\s{2}frameworks:\s*\n((?:\s{4}-\s+.*\n?)+)/m);
  if (block) {
    for (const line of block[1].split("\n")) {
      const m = line.match(/^\s*-\s*["']?(.+?)["']?\s*$/);
      if (m) frameworks.push(m[1].trim());
    }
  }
  return frameworks.filter(Boolean);
}

function discoverSkills() {
  const skills = [];
  const missed = [];
  for (const catEntry of fs.readdirSync(SKILLS_DIR, { withFileTypes: true })) {
    if (!catEntry.isDirectory() || catEntry.name.startsWith("_")) continue;
    const category = catEntry.name;
    const categoryDir = path.join(SKILLS_DIR, category);
    for (const skillEntry of fs.readdirSync(categoryDir, {
      withFileTypes: true,
    })) {
      if (!skillEntry.isDirectory() || skillEntry.name.startsWith("_"))
        continue;
      const skillFile = path.join(categoryDir, skillEntry.name, "SKILL.md");
      if (fs.existsSync(skillFile)) {
        const { fm, fmText } = parseFrontmatter(skillFile);
        skills.push({
          slug: skillEntry.name,
          name: fm.name || skillEntry.name,
          category,
          description: fm.description || "",
          compatibility: fm.compatibility || "",
          priority: fm.priority || "medium",
          frameworks: parseFrameworks(fmText),
          path: path.relative(ROOT, skillFile).replace(/\\/g, "/"),
        });
      } else {
        // Flat layout only: any SKILL.md nested deeper than skills/<category>/<skill>/ is a layout error.
        const nestedBase = path.join(categoryDir, skillEntry.name);
        for (const deep of fs.readdirSync(nestedBase, {
          withFileTypes: true,
        })) {
          if (!deep.isDirectory() || deep.name.startsWith("_")) continue;
          const deepFile = path.join(nestedBase, deep.name, "SKILL.md");
          if (fs.existsSync(deepFile))
            missed.push(path.relative(ROOT, deepFile).replace(/\\/g, "/"));
        }
      }
    }
  }
  if (missed.length)
    throw new Error(
      `Non-marketplace-discoverable skills:\n${missed.join("\n")}`,
    );
  return skills.sort(
    (a, b) =>
      a.category.localeCompare(b.category) || a.slug.localeCompare(b.slug),
  );
}

function discoverPackageFiles() {
  const files = [];
  const visit = (directory) => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      if (entry.name === ".DS_Store" || entry.name === "__pycache__") continue;
      const absolute = path.join(directory, entry.name);
      if (entry.isDirectory()) visit(absolute);
      else if (entry.isFile() && !entry.name.endsWith(".pyc")) files.push(absolute);
    }
  };
  visit(SKILLS_DIR);
  return files.sort();
}

function packageFileKind(filePath) {
  const relativeParts = path.relative(SKILLS_DIR, filePath).split(path.sep);
  if (path.basename(filePath) === "SKILL.md") return "entrypoints";
  for (const kind of ["references", "templates", "scripts", "assets"])
    if (relativeParts.slice(2).includes(kind)) return kind;
  return "other";
}

function truncate(s, n) {
  const text = String(s || "")
    .replace(/\s+/g, " ")
    .trim();
  return text.length <= n ? text : `${text.slice(0, n - 1).trimEnd()}…`;
}

function buildSkillIndexMaster(total, categories, byCategory, expertCount) {
  let out = `# GTM Skills — Master Skill Index\n\n`;
  out += `One-page map of **${total} skills** across **${categories.length} categories**. Load \`foundation/using-gtm-skills\` first for patterns and workflows.\n\n`;
  out += `**Master router:** \`skills/foundation/using-gtm-skills/SKILL.md\`\n\n`;
  out += `## Cross-repo indexes\n\n`;
  out += `| Index | Path | Use when |\n|---|---|---|\n`;
  out += `| Expert catalog | \`references/experts.md\` | Named practitioner lookup (${expertCount} entries) |\n`;
  out += `| Outbound experts | \`references/gtm-experts-outbound-index.md\` | Cold email + discovery routing |\n`;
  out += `| Cold calling experts | \`references/cold-calling-experts-index.md\` | Phone-first outbound |\n`;
  out += `| Automation playbooks | \`references/automation-playbook-index.md\` | Clay, n8n, sequencing, LeadMagic (38 playbooks) |\n`;
  out += `| Lifecycle router | \`references/lifecycle-skill-index.md\` | Stage-based skill selection |\n`;
  out += `| Lifecycle stages | \`references/gtm-lifecycle-stages.md\` | Canonical 7-stage definitions |\n`;
  out += `| GTM ops router | \`skills/gtm-ops/gtm-operations/references/gtm-ops-skill-index.md\` | RevOps + spend cluster |\n`;
  out += `| Pitfalls catalog | \`references/pitfalls-index.md\` | Cross-skill mistake patterns |\n`;
  out += `| GTM glossary | \`references/gtm-glossary.md\` | Shared terminology |\n`;
  out += `| SaaS metrics ref | \`references/saas-metrics-reference.md\` | Benchmark formulas |\n`;
  out += `| SEO playbook | \`references/seo-strategy-playbook.md\` | Product-led SEO stack |\n\n`;
  out += `## Categories (${categories.length})\n\n`;
  for (const cat of categories) {
    const guide = CATEGORY_GUIDE[cat] || {
      title: cat,
      blurb: "",
      start: byCategory[cat][0]?.slug || cat,
    };
    const n = byCategory[cat].length;
    out += `### ${guide.title} (\`${cat}/\`) — ${n} skills\n\n`;
    out += `${guide.blurb} **Start skill:** \`${guide.start}\`\n\n`;
    out += `| Skill | One-line |\n|---|---|\n`;
    for (const s of byCategory[cat]) {
      out += `| \`${s.slug}\` | ${truncate(s.description, 90)} |\n`;
    }
    out += "\n";
  }
  return out;
}

function parseExpertsCatalog() {
  const expertsFile = path.join(ROOT, "references", "experts.md");
  if (!fs.existsSync(expertsFile)) return [];
  const content = fs.readFileSync(expertsFile, "utf8");
  const experts = [];
  // Expert entries are H3 headers shaped "### Name — Affiliation (Org)".
  for (const m of content.matchAll(/^### ([^\n]+)$/gm)) {
    const name = m[1]
      .split(" — ")[0]
      .replace(/\s*\([^)]*\)\s*$/, "")
      .trim();
    if (name && !experts.includes(name)) experts.push(name);
  }
  return experts;
}

function expertMatcher(expert) {
  const escaped = expert.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  // Word-boundary match so "Bench" does not match "Benchmarks".
  return new RegExp(`(^|[^A-Za-z])${escaped}($|[^A-Za-z])`);
}

function buildAuthorityCatalog(skills, authorityCounts, limit = 24) {
  const experts = parseExpertsCatalog().map((name) => ({
    name,
    re: expertMatcher(name),
  }));
  const catalog = new Map();
  // Aggregate per expert: distinct skills whose frameworks cite the expert by name.
  for (const { name, re } of experts) {
    const count = skills.filter((s) =>
      s.frameworks.some((f) => re.test(f)),
    ).length;
    if (count > 0) catalog.set(name, count);
  }
  // Fill remaining capacity with top non-expert framework strings.
  const ranked = [...authorityCounts.entries()].sort(
    (a, b) => b[1] - a[1] || a[0].localeCompare(b[0]),
  );
  for (const [authority, count] of ranked) {
    if (catalog.size >= limit) break;
    if (catalog.has(authority)) continue;
    if (experts.some(({ re }) => re.test(authority))) continue;
    catalog.set(authority, count);
  }
  return [...catalog.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, limit);
}

const skills = discoverSkills();
const total = skills.length;
const byCategory = {};
for (const s of skills) {
  if (!byCategory[s.category]) byCategory[s.category] = [];
  byCategory[s.category].push(s);
}
const categories = Object.keys(byCategory).sort();
const packageFiles = discoverPackageFiles();
const packageFileCounts = Object.fromEntries(
  ["entrypoints", "references", "templates", "scripts", "assets", "other"].map(
    (kind) => [kind, packageFiles.filter((file) => packageFileKind(file) === kind).length],
  ),
);
const generatedSharedReferences = packageFiles.filter(
  (file) =>
    packageFileKind(file) === "references" &&
    fs.readFileSync(file, "utf8").startsWith("<!-- AUTO-GENERATED shared reference: "),
).length;

const authorityCounts = new Map();
for (const s of skills) {
  for (const framework of s.frameworks) {
    const normalized = framework.replace(/\s+/g, " ").trim();
    if (!normalized || normalized === "[]") continue;
    authorityCounts.set(normalized, (authorityCounts.get(normalized) || 0) + 1);
  }
}
const topAuthorities = [...authorityCounts.entries()]
  .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
  .slice(0, 30);
const authorityCatalog = buildAuthorityCatalog(skills, authorityCounts, 24);
const frameworkAssignments = skills.reduce(
  (sum, skill) => sum + skill.frameworks.length,
  0,
);
const expertCount = parseExpertsCatalog().length;

const taxonomy = ["slug,name,category,path,description,priority,compatibility"];
for (const s of skills)
  taxonomy.push(
    [
      s.slug,
      s.name,
      s.category,
      s.path,
      s.description,
      s.priority,
      s.compatibility,
    ]
      .map(csvEscape)
      .join(","),
  );
fs.writeFileSync(path.join(ROOT, "taxonomy.csv"), `${taxonomy.join("\n")}\n`);
fs.writeFileSync(
  path.join(ROOT, "references", "skill-index-master.md"),
  buildSkillIndexMaster(total, categories, byCategory, expertCount),
);

let claude = `# GTM Skills\n\n${total} production go-to-market skills for Claude-compatible agents. Skills are self-contained folders with instructions, scripts, references, templates, assets, and metadata that agents load through progressive disclosure.\n\n`;
claude += `## Install\n\n\`/plugin marketplace add LeadMagic/gtm-skills\` then \`/plugin install gtm-skills@gtm-skills\`. Portable Agent Skills install: \`gh skill install LeadMagic/gtm-skills --all --agent claude-code --scope user\`.\n\n`;
claude += `## Operating Model\n\n- Discovery loads skill name + description.\n- Activation loads SKILL.md.\n- Execution loads references/, templates/, scripts/, and assets/ on demand.\n- Use the narrowest skill that matches the task; chain skills for full GTM workflows.\n- Verify integrity with \`skills.lock\` when installing from source.\n\n## Top Authority Signals\n\n`;
for (const [authority, count] of topAuthorities.slice(0, 12))
  claude += `- ${authority} (${count} skills)\n`;
claude += `\n## Skills Index\n\n`;
for (const cat of categories) {
  claude += `### ${cat} (${byCategory[cat].length})\n`;
  for (const s of byCategory[cat])
    claude += `- **${s.slug}** — ${truncate(s.description, 180)}\n`;
  claude += "\n";
}
claude = claude.replace(
  "- Verify integrity with `skills.lock` when installing from source.\n\n## Top Authority Signals",
  "- Verify integrity with `skills.lock` when installing from source.\n- Apply docs/SOURCE_STANDARDS.md: named public authorities, primary docs, and no placeholder framework labels.\n- Use docs/QUALITY_BAR.md to understand the quality bar every skill in this repo must meet.\n\n## Top Authority Signals",
);
fs.writeFileSync(path.join(ROOT, "CLAUDE.md"), claude);

let agents = `# gtm-skills — Agent Skills Index\n\n${total} production GTM skills for AI agents. This repository follows the Agent Skills open specification: portable skill folders with SKILL.md plus optional scripts/, references/, templates/, and assets/.\n\n`;
agents += `## Install\n\nClaude Code marketplace style:\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\nPortable Agent Skills CLI:\n\n\`\`\`bash\ngh skill install LeadMagic/gtm-skills --all --agent codex --scope user\ngh skill install LeadMagic/gtm-skills foundation/pricing-strategy --agent github-copilot --scope project\n\`\`\`\n\nLocal installer:\n\n\`\`\`bash\n./install.sh --target codex --scope project\n./install.sh --target claude --scope user\n./install.sh --target all --dry-run\n\`\`\`\n\n`;
agents += `## Repository Contract\n\n- Marketplace-visible skills live at \`skills/<category>/<skill>/SKILL.md\`.\n- Support artifacts live inside the skill folder.\n- Generated catalog files come from disk, not hand edits.\n- \`skills.lock\` verifies SHA256 integrity.\n- CI must pass before release.\n\n## Categories\n\n`;
for (const cat of categories)
  agents += `- **${cat}** — ${byCategory[cat].length} skills\n`;
agents += `\n## Quality Standard\n\nEvery skill must be tactical, artifact-first, source-backed, marketplace-discoverable, and clean for a public repository. See docs/SKILL_AUTHORING.md and docs/SOURCE_STANDARDS.md. The public quality bar is tracked in docs/QUALITY_BAR.md.\n`;
fs.writeFileSync(path.join(ROOT, "AGENTS.md"), agents);

const categoryRows = categories
  .map(
    (cat) =>
      `| ${cat} | ${byCategory[cat].length} | ${truncate(
        byCategory[cat]
          .map((s) => s.slug)
          .slice(0, 5)
          .join(", "),
        90,
      )} |`,
  )
  .join("\n");
const authorityRows = authorityCatalog
  .map(
    ([authority, count]) => `| ${authority.replace(/\|/g, "/")} | ${count} |`,
  )
  .join("\n");

const startHere = `## Start Here

| Goal | Skill |
|---|---|
| Route any GTM task | [using-gtm-skills](skills/foundation/using-gtm-skills/SKILL.md) |
| Bootstrap reusable GTM context | [gtm-context-bootstrap](skills/foundation/gtm-context-bootstrap/SKILL.md) |
| Audit technical SEO and crawlability | [technical-seo-audit](skills/content-seo/technical-seo-audit/SKILL.md) |
| LinkedIn feed reach (van der Blom) | [linkedin-algorithm](skills/inbound/linkedin-algorithm/SKILL.md) |
| LinkedIn Live / weekly show (Jessie Lizak / Reveting) | [linkedin-live-strategy](skills/inbound/linkedin-live-strategy/SKILL.md) |
| Sales Navigator prospecting (Morgan Ingram / AMP) | [sales-navigator-prospecting](skills/inbound/sales-navigator-prospecting/SKILL.md) |
| Cold outbound architecture | [cold-email-strategy](skills/outbound/cold-email-strategy/SKILL.md) |
| Named expert lookup | [references/experts.md](references/experts.md) |

## LinkedIn Inbound Stack

The **inbound** category (${byCategory.inbound?.length ?? 0} skills) covers LinkedIn GTM end-to-end: **van der Blom** feed mechanics (\`linkedin-algorithm\`), **Jessie Lizak** Live engine (\`linkedin-live-strategy\`), **Morgan Ingram** Sales Nav prospecting (\`sales-navigator-prospecting\`), plus \`social-selling\`, \`founder-brand\`, and \`website-visitor-identification\`. Release history: [CHANGELOG.md](CHANGELOG.md).

`;

let readme = `# GTM Agent Skills for Claude Code, Codex & GitHub Copilot\n\n[![Skills](https://img.shields.io/badge/skills-${total}-blue)](skills/) [![Categories](https://img.shields.io/badge/categories-${categories.length}-green)](skills/) [![Release](https://img.shields.io/github/v/release/LeadMagic/gtm-skills)](https://github.com/LeadMagic/gtm-skills/releases) [![CI](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE) [![Stars](https://img.shields.io/github/stars/LeadMagic/gtm-skills?style=social)](https://github.com/LeadMagic/gtm-skills)\n\n**${total} production go-to-market (GTM) Agent Skills across ${categories.length} categories.** Install source-backed sales, marketing, outbound, RevOps, SEO, ABM, product-led growth, customer-success, analytics, and automation workflows in Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, and other Agent Skills-compatible runtimes.\n\nThis is an artifact-first skill library, not a prompt pack. Every skill ships a \`SKILL.md\`, framework notes, an output template, and an executable deliverable checker. The current catalog contains exactly **${packageFiles.length} packaged skill files**, **${frameworkAssignments} framework/source assignments**, and **${expertCount} named expert entries**. Counts and catalogs are generated from the skill folders on disk.\n\n## Install Agent Skills\n\n### Preview first, then install one skill\n\n\`\`\`bash\ngh skill preview LeadMagic/gtm-skills foundation/gtm-context-bootstrap\ngh skill install LeadMagic/gtm-skills foundation/gtm-context-bootstrap --agent codex --scope project\n\`\`\`\n\n### Install the complete catalog\n\n\`\`\`bash\n# Replace codex with github-copilot, claude-code, cursor, gemini-cli, opencode, or goose.\ngh skill install LeadMagic/gtm-skills --all --agent codex --scope user\n\n# Pin reproducible installations to a published release or commit.\ngh skill install LeadMagic/gtm-skills --all --agent codex --scope user --pin <release-tag-or-commit>\n\`\`\`\n\n### Claude Code plugin\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\n### Audited local checkout\n\n\`\`\`bash\ngh repo clone LeadMagic/gtm-skills\ncd gtm-skills\n./install.sh --target codex --scope project\n./install.sh --target all --dry-run\n\`\`\`\n\nUse project scope for repository-specific work, user scope for skills you intentionally trust everywhere, and \`gh skill update --all\` to refresh tracked installs. Skills can contain executable scripts, so review before installing. See the [complete install and verification guide](docs/INSTALL.md).\n\n## Exact Catalog Value\n\n| Inventory | Exact value |\n|---|---:|\n| Marketplace-discoverable skills | ${total} |\n| Categories | ${categories.length} |\n| Skill entrypoint files | ${packageFileCounts.entrypoints} |\n| Reference files | ${packageFileCounts.references} |\n| Template files | ${packageFileCounts.templates} |\n| Script files | ${packageFileCounts.scripts} |\n| Asset files | ${packageFileCounts.assets} |\n| Other packaged files | ${packageFileCounts.other} |\n| Total packaged skill files | ${packageFiles.length} |\n| Generated shared-reference copies | ${generatedSharedReferences} |\n| Minimum required skill files | ${total * 4} |\n| Framework/source assignments | ${frameworkAssignments} |\n| Named expert index entries | ${expertCount} |\n\n## Why GTM Skills\n\n- **Concrete outputs.** Plans, scorecards, briefs, runbooks, dashboards, workflows, templates, and QA checks.\n- **Named sources.** Public operators, platform documentation, research, and standards shape the work.\n- **Progressive disclosure.** Metadata supports discovery; \`SKILL.md\` loads on activation; resources load when needed.\n- **Portable installation.** The repository follows the [Agent Skills specification](https://agentskills.io/specification) and validates with \`gh skill publish --dry-run\`.\n- **Reproducible integrity.** \`skills.lock\` inventories and hashes every packaged skill file.\n- **No telemetry.** Static content and local validation scripts only.\n\n${startHere}## Category Map\n\n| Category | Skills | Examples |\n|---|---:|---|\n${categoryRows}\n\n## Authority Catalog\n\n| Authority / Framework | Skills |\n|---|---:|\n${authorityRows}\n\nBrowse the [expert catalog](references/experts.md), [master skill index](references/skill-index-master.md), and [pitfalls index](references/pitfalls-index.md).\n\n## Validate the Repository\n\n\`\`\`bash\nnpm run regenerate\nnpm run verify\ngh skill publish --dry-run\n\`\`\`\n\nExpected result: ${total} skills checked, 0 errors, 0 warnings; ${total} checkers reject unfilled templates; generated catalogs and \`skills.lock\` are current; installer dry-runs succeed.\n\n## Skills Catalog\n\n`;
readme = readme
  .replace(
    "Install source-backed sales, marketing, outbound, RevOps, SEO, ABM, product-led growth, customer-success, analytics, and automation workflows",
    "Install source-backed buyer research, product marketing, sales, outbound, RevOps, SEO, ABM, product-led growth, customer-success, analytics, and automation workflows",
  )
  .replace(
    "## Install Agent Skills\n\n",
    "## Install Agent Skills\n\n### Interactive, preview-first installer\n\n```bash\ngh repo clone LeadMagic/gtm-skills && cd gtm-skills\n./install.sh\n```\n\nThe zero-dependency wizard lets you check off agent targets, choose project or user scope, and select curated bundles, full categories, individual skills, or the complete catalog. It shows exact destinations and collision counts, asks before writing, and skips existing skill folders unless `--force` is explicit.\n\n",
  )
  .replace(
    "```bash\ngh repo clone LeadMagic/gtm-skills\ncd gtm-skills\n./install.sh --target codex --scope project\n./install.sh --target all --dry-run\n```",
    "```bash\n./install.sh --target claude --scope project --bundle buyer-insight --dry-run\n./install.sh --target claude --scope project --bundle buyer-insight --yes\n```",
  );
for (const cat of categories) {
  readme += `### ${cat} (${byCategory[cat].length})\n\n`;
  for (const s of byCategory[cat])
    readme += `- [${s.slug}](${s.path}) — ${truncate(s.description, 220)}\n`;
  readme += "\n";
}
readme += `## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md). New skills must cite named authorities, produce concrete artifacts, pass validation, and avoid private/internal details.\n`;
readme = readme.replace("production go-to-market (GTM) Agent Skills", "go-to-market (GTM) agent skills")
  .replace("This is an artifact-first skill library, not a prompt pack.", "Use these playbooks to produce research briefs, sales plans, marketing assets, and workflow checks.")
  .replace("## Install Agent Skills", "[LeadMagic B2B enrichment](https://leadmagic.io?utm_source=github&utm_medium=readme&utm_campaign=gtm-skills&utm_content=readme-intro) \u00b7 [API documentation](https://leadmagic.io/docs?utm_source=github&utm_medium=readme&utm_campaign=gtm-skills&utm_content=readme-intro) \u00b7 [Pricing and credits](https://leadmagic.io/pricing?utm_source=github&utm_medium=readme&utm_campaign=gtm-skills&utm_content=readme-intro)" + "\n\n## Install Agent Skills");
readme += "\n## LeadMagic enrichment integrations\n\nUse [LeadMagic product skills](https://github.com/LeadMagic/leadmagic-skills) for API and enrichment guidance, [n8n workflows](https://github.com/LeadMagic/leadmagic-n8n) for automation, and the [public OpenAPI specification](https://github.com/LeadMagic/leadmagic-openapi) for REST clients.\n";
readme += "\n## License and contributions\n\n[MIT license](LICENSE) · [Third-party materials and contribution policy](LICENSE-NOTES.md). Reuse is allowed under the license; changes to this repository require maintainer review.\n";
fs.writeFileSync(path.join(ROOT, "README.md"), readme);

fs.mkdirSync(PLUGIN_DIR, { recursive: true });
const plugin = {
  name: "gtm-skills",
  displayName: "GTM Skills",
  version: VERSION,
  description: `${total} production go-to-market skills for AI agents across ${categories.length} categories.`,
  author: { name: "LeadMagic", url: "https://leadmagic.io" },
  license: "MIT",
  homepage: "https://github.com/LeadMagic/gtm-skills",
  repository: "https://github.com/LeadMagic/gtm-skills",
  skills: ["./skills"],
  defaultEnabled: true,
};
fs.writeFileSync(
  path.join(PLUGIN_DIR, "plugin.json"),
  `${JSON.stringify(plugin, null, 2)}\n`,
);
const marketplace = {
  name: "gtm-skills",
  owner: {
    name: "LeadMagic",
    email: "team@leadmagic.io",
    url: "https://leadmagic.io",
  },
  description: `${total} production go-to-market skills for AI agents. Artifact-first GTM playbooks across ${categories.length} categories.`,
  plugins: [
    {
      name: "gtm-skills",
      source: "./",
      description: `${total} production go-to-market skills for AI agents across ${categories.length} categories.`,
      version: VERSION,
      author: { name: "LeadMagic", url: "https://leadmagic.io" },
      homepage: "https://github.com/LeadMagic/gtm-skills",
      license: "MIT",
      keywords: [
        "gtm",
        "sales",
        "marketing",
        "product-marketing",
        "customer-research",
        "win-loss-analysis",
        "revenue-forecasting",
        "outbound",
        "prospecting",
        "revops",
        "claude-code",
        "agent-skills",
      ],
    },
  ],
};
fs.writeFileSync(
  path.join(PLUGIN_DIR, "marketplace.json"),
  `${JSON.stringify(marketplace, null, 2)}\n`,
);

console.log(
  `Generated taxonomy.csv, skill-index-master.md, CLAUDE.md, AGENTS.md, plugin metadata for ${total} skills across ${categories.length} categories.`,
);
