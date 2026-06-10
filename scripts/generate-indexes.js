#!/usr/bin/env node
/**
 * generate-indexes.js — regenerate README, AGENTS.md, CLAUDE.md,
 * taxonomy.csv, and Claude plugin metadata from actual marketplace-discoverable
 * skills on disk.
 */

const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.join(__dirname, '..');
const SKILLS_DIR = path.join(ROOT, 'skills');
const PLUGIN_DIR = path.join(ROOT, '.claude-plugin');
const VERSION = '0.27.2';

// Human-facing category guide for references/skill-index-master.md (generated).
const CATEGORY_GUIDE = {
  abm: { title: 'Account-Based Marketing', blurb: 'Tiered ABM plays, gifting, multi-thread orchestration.', start: 'abm-strategy' },
  analytics: { title: 'Analytics & Measurement', blurb: 'Attribution, experiments, GTM metrics, tracking plans.', start: 'gtm-metrics' },
  automation: { title: 'Automation & Integrations', blurb: 'Clay, n8n, CRM setup, enrichment waterfalls.', start: 'clay-automation' },
  'content-seo': { title: 'Content & SEO', blurb: 'SEO strategy, pillars, pSEO, AEO, citation harvesting.', start: 'seo-strategy' },
  creative: { title: 'Creative & AI Content', blurb: 'Vibe marketing, AI content/video, copywriting, growth hacks.', start: 'vibe-marketing' },
  'customer-success': { title: 'Customer Success', blurb: 'Onboarding, CS playbooks, SLAs, headless support.', start: 'customer-onboarding' },
  'demand-gen': { title: 'Demand Generation', blurb: 'Webinars, podcasts, paid social, syndication.', start: 'webinar-strategy' },
  design: { title: 'Design & Collateral', blurb: 'Pitch decks, battlecards, ROI calculators, brand systems.', start: 'pitch-deck-builder' },
  events: { title: 'Events & Field', blurb: 'Conferences, field marketing, event-driven outreach.', start: 'conference-strategy' },
  foundation: { title: 'Foundation & ICP', blurb: 'ICP, positioning, pricing, master router.', start: 'using-gtm-skills' },
  'founder-led': { title: 'Founder-Led GTM', blurb: 'Fundraising, hiring, legal, founder sales, solo GTM.', start: 'solo-founder-gtm' },
  'gtm-ops': { title: 'GTM Operations', blurb: 'RevOps stack, spend, PM/RACI, campaign governance.', start: 'gtm-operations' },
  growth: { title: 'Growth & Expansion', blurb: 'Referrals, expansion, churn prevention, reviews.', start: 'expansion-selling' },
  inbound: { title: 'Inbound & PLG-adjacent', blurb: 'Content marketing, triage, landing pages, LinkedIn algorithm + Live, Sales Navigator, social selling, visitor ID.', start: 'linkedin-algorithm' },
  leadmagic: { title: 'LeadMagic Product', blurb: 'CLI, MCP, waterfall, bulk enrichment integrations.', start: 'leadmagic-waterfall' },
  'management-leadership': { title: 'Leadership & Coaching', blurb: 'GTM leadership, coaching, onboarding, exec comp.', start: 'gtm-leadership' },
  lifecycle: { title: 'Lifecycle Marketing', blurb: 'MQL nurture, onboarding drips, churn, re-engagement.', start: 'mql-nurture' },
  outbound: { title: 'Outbound', blurb: 'Cold email, calling, deliverability, domains, replies.', start: 'cold-email-strategy' },
  partnerships: { title: 'Partnerships', blurb: 'Co-marketing, integrations, partner strategy.', start: 'partnership-strategy' },
  'product-led-growth': { title: 'Product-Led Growth', blurb: 'PLG strategy, freemium optimization, developer GTM.', start: 'plg-strategy' },
  prospecting: { title: 'Prospecting & Data', blurb: 'Lead finding, enrichment, verification, signals.', start: 'lead-finding' },
  'sales-revops': { title: 'Sales & RevOps', blurb: 'Pipeline, demos, deal desk, enablement, objections.', start: 'pipeline-management' },
  'sales-plays': { title: 'Signal Sales Plays', blurb: 'Funding, hiring, job change, earnings plays.', start: 'funding-signal-play' },
  tools: {
    title: 'GTM Toolkits & Sequencers',
    blurb: 'Clay, CRM, n8n, analytics, support toolkits; sequencing-toolkit plus Instantly, Smartlead, lemlist, Outreach, Salesloft, HubSpot platform skills.',
    start: 'clay-toolkit',
  },
};

function csvEscape(value) {
  const s = String(value ?? '');
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function parseFrontmatter(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  if (!content.startsWith('---\n')) throw new Error(`${filePath}: missing frontmatter`);
  const end = content.indexOf('\n---\n', 4);
  if (end === -1) throw new Error(`${filePath}: missing closing frontmatter`);
  const fmText = content.slice(4, end);
  const fm = {};
  const lines = fmText.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$/);
    if (!m) continue;
    const key = m[1];
    let value = m[2].trim();
    if (/^[>|]-?$/.test(value)) {
      const out = [];
      i += 1;
      while (i < lines.length && (/^\s+/.test(lines[i]) || lines[i].trim() === '')) {
        out.push(lines[i].trim());
        i += 1;
      }
      i -= 1;
      value = out.join(' ').replace(/\s+/g, ' ').trim();
    }
    fm[key] = value.replace(/^['"]|['"]$/g, '');
  }
  return { fm, fmText, content };
}

function parseFrameworks(fmText) {
  const frameworks = [];
  const inline = fmText.match(/^\s*frameworks:\s*\[([^\]]*)\]/m);
  if (inline) {
    for (const item of inline[1].split(',')) {
      const cleaned = item.trim().replace(/^['"]|['"]$/g, '');
      if (cleaned) frameworks.push(cleaned);
    }
    return frameworks;
  }
  // Block list: capture every "    - item" line (mirrors validate-skills.js).
  const block = fmText.match(/^\s{2}frameworks:\s*\n((?:\s{4}-\s+.*\n?)+)/m);
  if (block) {
    for (const line of block[1].split('\n')) {
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
    if (!catEntry.isDirectory() || catEntry.name.startsWith('_')) continue;
    const category = catEntry.name;
    const categoryDir = path.join(SKILLS_DIR, category);
    for (const skillEntry of fs.readdirSync(categoryDir, { withFileTypes: true })) {
      if (!skillEntry.isDirectory() || skillEntry.name.startsWith('_')) continue;
      const skillFile = path.join(categoryDir, skillEntry.name, 'SKILL.md');
      if (fs.existsSync(skillFile)) {
        const { fm, fmText } = parseFrontmatter(skillFile);
        skills.push({
          slug: skillEntry.name,
          name: fm.name || skillEntry.name,
          category,
          description: fm.description || '',
          compatibility: fm.compatibility || '',
          priority: fm.priority || 'medium',
          frameworks: parseFrameworks(fmText),
          path: path.relative(ROOT, skillFile).replace(/\\/g, '/'),
        });
      } else {
        // Flat layout only: any SKILL.md nested deeper than skills/<category>/<skill>/ is a layout error.
        const nestedBase = path.join(categoryDir, skillEntry.name);
        for (const deep of fs.readdirSync(nestedBase, { withFileTypes: true })) {
          if (!deep.isDirectory() || deep.name.startsWith('_')) continue;
          const deepFile = path.join(nestedBase, deep.name, 'SKILL.md');
          if (fs.existsSync(deepFile)) missed.push(path.relative(ROOT, deepFile).replace(/\\/g, '/'));
        }
      }
    }
  }
  if (missed.length) throw new Error(`Non-marketplace-discoverable skills:\n${missed.join('\n')}`);
  return skills.sort((a, b) => a.category.localeCompare(b.category) || a.slug.localeCompare(b.slug));
}

function truncate(s, n) {
  const text = String(s || '').replace(/\s+/g, ' ').trim();
  return text.length <= n ? text : `${text.slice(0, n - 1).trimEnd()}…`;
}

function buildSkillIndexMaster(total, categories, byCategory) {
  let out = `# GTM Skills — Master Skill Index\n\n`;
  out += `One-page map of **${total} skills** across **${categories.length} categories**. Load \`foundation/using-gtm-skills\` first for patterns and workflows.\n\n`;
  out += `**Master router:** \`skills/foundation/using-gtm-skills/SKILL.md\`\n\n`;
  out += `## Cross-repo indexes\n\n`;
  out += `| Index | Path | Use when |\n|---|---|---|\n`;
  out += `| Expert catalog | \`references/experts.md\` | Named practitioner lookup (~110 entries) |\n`;
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
    const guide = CATEGORY_GUIDE[cat] || { title: cat, blurb: '', start: byCategory[cat][0]?.slug || cat };
    const n = byCategory[cat].length;
    out += `### ${guide.title} (\`${cat}/\`) — ${n} skills\n\n`;
    out += `${guide.blurb} **Start skill:** \`${guide.start}\`\n\n`;
    out += `| Skill | One-line |\n|---|---|\n`;
    for (const s of byCategory[cat]) {
      out += `| \`${s.slug}\` | ${truncate(s.description, 90)} |\n`;
    }
    out += '\n';
  }
  return out;
}

function parseExpertsCatalog() {
  const expertsFile = path.join(ROOT, 'references', 'experts.md');
  if (!fs.existsSync(expertsFile)) return [];
  const content = fs.readFileSync(expertsFile, 'utf8');
  const experts = [];
  // Expert entries are H3 headers shaped "### Name — Affiliation (Org)".
  for (const m of content.matchAll(/^### ([^\n]+)$/gm)) {
    const name = m[1]
      .split(' — ')[0]
      .replace(/\s*\([^)]*\)\s*$/, '')
      .trim();
    if (name && !experts.includes(name)) experts.push(name);
  }
  return experts;
}

function expertMatcher(expert) {
  const escaped = expert.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // Word-boundary match so "Bench" does not match "Benchmarks".
  return new RegExp(`(^|[^A-Za-z])${escaped}($|[^A-Za-z])`);
}

function buildAuthorityCatalog(skills, authorityCounts, limit = 24) {
  const experts = parseExpertsCatalog().map(name => ({ name, re: expertMatcher(name) }));
  const catalog = new Map();
  // Aggregate per expert: distinct skills whose frameworks cite the expert by name.
  for (const { name, re } of experts) {
    const count = skills.filter(s => s.frameworks.some(f => re.test(f))).length;
    if (count > 0) catalog.set(name, count);
  }
  // Fill remaining capacity with top non-expert framework strings.
  const ranked = [...authorityCounts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
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

const authorityCounts = new Map();
for (const s of skills) {
  for (const framework of s.frameworks) {
    const normalized = framework.replace(/\s+/g, ' ').trim();
    if (!normalized || normalized === '[]') continue;
    authorityCounts.set(normalized, (authorityCounts.get(normalized) || 0) + 1);
  }
}
const topAuthorities = [...authorityCounts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, 30);
const authorityCatalog = buildAuthorityCatalog(skills, authorityCounts, 24);

const taxonomy = ['slug,name,category,path,description,priority,compatibility'];
for (const s of skills) taxonomy.push([s.slug, s.name, s.category, s.path, s.description, s.priority, s.compatibility].map(csvEscape).join(','));
fs.writeFileSync(path.join(ROOT, 'taxonomy.csv'), `${taxonomy.join('\n')}\n`);
fs.writeFileSync(path.join(ROOT, 'references', 'skill-index-master.md'), buildSkillIndexMaster(total, categories, byCategory));

let claude = `# GTM Skills\n\n${total} production go-to-market skills for Claude-compatible agents. Skills are self-contained folders with instructions, scripts, references, templates, assets, and metadata that agents load through progressive disclosure.\n\n`;
claude += `## Install\n\n\`/plugin marketplace add LeadMagic/gtm-skills\` then \`/plugin install gtm-skills@gtm-skills\`. agentskills CLI: \`gh skill install LeadMagic/gtm-skills\`.\n\n`;
claude += `## Operating Model\n\n- Discovery loads skill name + description.\n- Activation loads SKILL.md.\n- Execution loads references/, templates/, scripts/, and assets/ on demand.\n- Use the narrowest skill that matches the task; chain skills for full GTM workflows.\n- Verify integrity with \`skills.lock\` when installing from source.\n\n## Top Authority Signals\n\n`;
for (const [authority, count] of topAuthorities.slice(0, 12)) claude += `- ${authority} (${count} skills)\n`;
claude += `\n## Skills Index\n\n`;
for (const cat of categories) {
  claude += `### ${cat} (${byCategory[cat].length})\n`;
  for (const s of byCategory[cat]) claude += `- **${s.slug}** — ${truncate(s.description, 180)}\n`;
  claude += '\n';
}
claude = claude.replace(
  '- Verify integrity with `skills.lock` when installing from source.\n\n## Top Authority Signals',
  '- Verify integrity with `skills.lock` when installing from source.\n- Apply docs/SOURCE_STANDARDS.md: named public authorities, primary docs, and no placeholder framework labels.\n- Use docs/QUALITY_BAR.md to understand the quality bar every skill in this repo must meet.\n\n## Top Authority Signals'
);
fs.writeFileSync(path.join(ROOT, 'CLAUDE.md'), claude);

let agents = `# gtm-skills — Agent Skills Index\n\n${total} production GTM skills for AI agents. This repo follows the Anthropic/agentskills pattern: portable skill folders with SKILL.md plus optional scripts/, references/, templates/, and assets/.\n\n`;
agents += `## Install\n\nClaude Code marketplace style:\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\nagentskills CLI style:\n\n\`\`\`bash\ngh skill install LeadMagic/gtm-skills\ngh skill install LeadMagic/gtm-skills pricing-strategy\ngh skill install LeadMagic/gtm-skills --category outbound\n\`\`\`\n\nLocal installer:\n\n\`\`\`bash\n./install.sh\n./install.sh --target hermes\n./install.sh --target jesse --project /path/to/project\n./install.sh --target all --dry-run\n\`\`\`\n\n`;
agents += `## Repository Contract\n\n- Marketplace-visible skills live at \`skills/<category>/<skill>/SKILL.md\`.\n- Support artifacts live inside the skill folder.\n- Generated catalog files come from disk, not hand edits.\n- \`skills.lock\` verifies SHA256 integrity.\n- CI must pass before release.\n\n## Categories\n\n`;
for (const cat of categories) agents += `- **${cat}** — ${byCategory[cat].length} skills\n`;
agents += `\n## Quality Standard\n\nEvery skill must be tactical, artifact-first, source-backed, marketplace-discoverable, and clean for a public repository. See docs/SKILL_AUTHORING.md and docs/SOURCE_STANDARDS.md. The public quality bar is tracked in docs/QUALITY_BAR.md.\n`;
fs.writeFileSync(path.join(ROOT, 'AGENTS.md'), agents);

const categoryRows = categories.map(cat => `| ${cat} | ${byCategory[cat].length} | ${truncate(byCategory[cat].map(s => s.slug).slice(0, 5).join(', '), 90)} |`).join('\n');
const authorityRows = authorityCatalog.map(([authority, count]) => `| ${authority.replace(/\|/g, '/')} | ${count} |`).join('\n');

const startHere = `## Start Here

| Goal | Skill |
|---|---|
| Route any GTM task | [using-gtm-skills](skills/foundation/using-gtm-skills/SKILL.md) |
| LinkedIn feed reach (van der Blom) | [linkedin-algorithm](skills/inbound/linkedin-algorithm/SKILL.md) |
| LinkedIn Live / weekly show (Jessie Lizak / Reveting) | [linkedin-live-strategy](skills/inbound/linkedin-live-strategy/SKILL.md) |
| Sales Navigator prospecting (Morgan Ingram / AMP) | [sales-navigator-prospecting](skills/inbound/sales-navigator-prospecting/SKILL.md) |
| Cold outbound architecture | [cold-email-strategy](skills/outbound/cold-email-strategy/SKILL.md) |
| Named expert lookup | [references/experts.md](references/experts.md) |

## LinkedIn Inbound Stack

The **inbound** category (${byCategory.inbound?.length ?? 0} skills) covers LinkedIn GTM end-to-end: **van der Blom** feed mechanics (\`linkedin-algorithm\`), **Jessie Lizak** Live engine (\`linkedin-live-strategy\`), **Morgan Ingram** Sales Nav prospecting (\`sales-navigator-prospecting\`), plus \`social-selling\`, \`founder-brand\`, and \`website-visitor-identification\`. Release history: [CHANGELOG.md](CHANGELOG.md).

`;

let readme = `# GTM Skills\n\n[![Skills](https://img.shields.io/badge/skills-${total}-blue)](skills/) [![Categories](https://img.shields.io/badge/categories-${categories.length}-green)](skills/) [![Release](https://img.shields.io/github/v/release/LeadMagic/gtm-skills)](https://github.com/LeadMagic/gtm-skills/releases) [![CI](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/LeadMagic/gtm-skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)\n\n**Public repository:** [github.com/LeadMagic/gtm-skills](https://github.com/LeadMagic/gtm-skills)\n\n${total} production go-to-market skills for AI agents. Built for sales, marketing, outbound, prospecting, enrichment, PLG, analytics, automation, customer success, RevOps, founder-led GTM, and tool operations.\n\nThis is not a prompt pack. It is an agent-skills repository: portable skill folders with instructions, scripts, references, templates, assets, metadata, marketplace publishing, install tooling, and SHA256 integrity verification.\n\n## Public Links\n\n| Resource | URL |\n|---|---|\n| Source & issues | [github.com/LeadMagic/gtm-skills](https://github.com/LeadMagic/gtm-skills) |\n| Releases & changelog | [CHANGELOG.md](CHANGELOG.md) |\n| Install guide | [docs/INSTALL.md](docs/INSTALL.md) |\n| Master skill index | [references/skill-index-master.md](references/skill-index-master.md) |\n| Expert catalog | [references/experts.md](references/experts.md) |\n| Pitfalls index | [references/pitfalls-index.md](references/pitfalls-index.md) |\n| Citation metadata | [CITATION.cff](CITATION.cff) |\n| Marketplace install | \`gh skill install LeadMagic/gtm-skills\` |\n\n## Install\n\nClaude Code marketplace style:\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\nagentskills CLI style:\n\n\`\`\`bash\ngh skill install LeadMagic/gtm-skills\n\`\`\`\n\nInteractive installer:\n\n\`\`\`bash\ngit clone https://github.com/LeadMagic/gtm-skills.git\ncd gtm-skills\n./install.sh\n./install.sh --target all --dry-run\n\`\`\`\n\nFull install docs: [docs/INSTALL.md](docs/INSTALL.md).\n\n## Listed On\n\nAgent-skills directories and submission status:\n\n| Directory | Status |\n|---|---|\n| [agent-skills.md](https://agent-skills.md) | [Requested](https://github.com/futantan/agent-skills.md/issues/19) |\n| [agenticskills.io](https://agenticskills.io) | [Submit](https://agenticskills.io/submit) |\n| [skills.re](https://skills.re) | [Submit](https://skills.re/submit) |\n| [skillindex.dev](https://skillindex.dev) | [PR #1](https://github.com/gabeosx/agentskillsdir/pull/1) |\n| [theskills.directory](https://theskills.directory) | [Requested](https://github.com/theskillsdirectory/skills/issues/7) |\n\n## What Makes This Repo Different\n\n- **Artifact-first.** Skills produce copy, plans, scorecards, runbooks, dashboards, workflows, templates, scripts, and QA checklists.\n- **Authority-backed.** Every skill cites named operators, vendors, books, frameworks, platform docs, or primary sources instead of vague best practices.\n- **Quality-bar driven.** Public quality bar notes define the standard every skill must meet and track hardening work over time.\n- **Anthropic-style folders.** SKILL.md for instructions; references/, templates/, scripts/, and assets/ for execution resources.\n- **Progressive disclosure.** SKILL.md stays focused; deep tables and templates live in support files.\n- **Marketplace-ready.** Every skill is discoverable by agentskills.io-compatible patterns and validated in CI.\n- **Supply-chain aware.** skills.lock tracks SHA256 for every marketplace-discoverable skill.\n- **No telemetry.** Static skills and local scripts only; no analytics SDKs or hidden network behavior.\n\n${startHere}## Repository Quality Signals\n\n| Signal | Status |\n|---|---|\n| Marketplace-discoverable skills | ${total}/${total} |\n| Categories | ${categories.length} |\n| CI validation | \`npm run check\` |\n| Publish verification | \`gh skill publish --dry-run\` |\n| Integrity manifest | \`skills.lock\` |\n| Public governance | CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, GOVERNANCE |\n| Source standard | docs/SOURCE_STANDARDS.md |\n| Quality bar notes | docs/QUALITY_BAR.md |\n\n## Category Map\n\n| Category | Skills | Examples |\n|---|---:|---|\n${categoryRows}\n\n## Quality Bar\n\nThis repo is built on breadth, source hygiene, public governance, installability, and artifact-first execution rather than raw prompt count. See [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) for the quality bar and hardening notes.\n\n## Authority Catalog\n\nThe skills cite named methodologies, operators, vendor docs, and frameworks. Top recurring sources in the catalog:\n\n| Authority / Framework | Skills |\n|---|---:|\n${authorityRows}\n\nFull expert catalog — bios, public channels, and skill clusters: [references/experts.md](references/experts.md). Outbound/discovery routing: [references/gtm-experts-outbound-index.md](references/gtm-experts-outbound-index.md).\n\n## Documentation\n\n- [Install guide](docs/INSTALL.md)\n- [Architecture](docs/ARCHITECTURE.md)\n- [Skill authoring standard](docs/SKILL_AUTHORING.md)\n- [Source and authority standard](docs/SOURCE_STANDARDS.md)\n- [Quality bar notes](docs/QUALITY_BAR.md)\n- [Integrity verification](docs/INTEGRITY.md)\n- [Release process](docs/RELEASE_PROCESS.md)\n- [GitHub topics](docs/REPO_TOPICS.md)\n- [Contributing](CONTRIBUTING.md)\n- [Security](SECURITY.md)\n\n## Validate Locally\n\n\`\`\`bash\nnpm run regenerate\nnpm run verify\ngh skill publish --dry-run\n\`\`\`\n\nExpected result: ${total} skills checked, 0 errors, 0 warnings, generated artifacts current, lock verified, installer dry-run OK.\n\n## Skills Catalog\n\n`;
for (const cat of categories) {
  readme += `### ${cat} (${byCategory[cat].length})\n\n`;
  for (const s of byCategory[cat]) readme += `- [${s.slug}](${s.path}) — ${truncate(s.description, 220)}\n`;
  readme += '\n';
}
readme += `## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md). New skills must cite named authorities, produce concrete artifacts, pass validation, and avoid private/internal details.\n`;
fs.writeFileSync(path.join(ROOT, 'README.md'), readme);

fs.mkdirSync(PLUGIN_DIR, { recursive: true });
const plugin = {
  name: 'gtm-skills',
  version: VERSION,
  description: `${total} production go-to-market playbooks for AI agents across ${categories.length} categories.`,
  author: 'LeadMagic',
  license: 'MIT',
  homepage: 'https://leadmagic.io',
  repository: 'https://github.com/LeadMagic/gtm-skills',
  skills: ['skills/*/*/SKILL.md'],
};
fs.writeFileSync(path.join(PLUGIN_DIR, 'plugin.json'), `${JSON.stringify(plugin, null, 2)}\n`);
const marketplace = {
  name: 'gtm-skills',
  display_name: 'GTM Skills',
  description: `${total} production go-to-market skills for AI agents. Artifact-first GTM playbooks across ${categories.length} categories.`,
  author: 'LeadMagic',
  repository: 'https://github.com/LeadMagic/gtm-skills',
  license: 'MIT',
  categories,
  skills_count: total,
};
fs.writeFileSync(path.join(PLUGIN_DIR, 'marketplace.json'), `${JSON.stringify(marketplace, null, 2)}\n`);

console.log(`Generated taxonomy.csv, skill-index-master.md, CLAUDE.md, AGENTS.md, README.md, plugin metadata for ${total} skills across ${categories.length} categories.`);
