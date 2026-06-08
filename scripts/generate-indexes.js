#!/usr/bin/env node
/**
 * generate-indexes.js — regenerate README, AGENTS.md, CLAUDE.md,
 * taxonomy.csv, and Claude plugin metadata from actual marketplace-discoverable
 * skills on disk.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const SKILLS_DIR = path.join(ROOT, 'skills');
const PLUGIN_DIR = path.join(ROOT, '.claude-plugin');

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
  return fm;
}

function discoverSkills() {
  const all = [];
  const missed = [];
  for (const file of fs.readdirSync(SKILLS_DIR, { withFileTypes: true })) {
    if (!file.isDirectory() || file.name.startsWith('_')) continue;
    const category = file.name;
    const categoryDir = path.join(SKILLS_DIR, category);
    for (const entry of fs.readdirSync(categoryDir, { withFileTypes: true })) {
      if (!entry.isDirectory() || entry.name.startsWith('_')) continue;
      const skillFile = path.join(categoryDir, entry.name, 'SKILL.md');
      if (fs.existsSync(skillFile)) {
        const fm = parseFrontmatter(skillFile);
        all.push({
          slug: entry.name,
          name: fm.name || entry.name,
          category,
          description: fm.description || '',
          compatibility: fm.compatibility || '',
          priority: fm.priority || 'medium',
          path: path.relative(ROOT, skillFile).replace(/\\/g, '/'),
        });
      } else {
        for (const deep of fs.readdirSync(path.join(categoryDir, entry.name), { withFileTypes: true })) {
          if (!deep.isDirectory()) continue;
          const deepFile = path.join(categoryDir, entry.name, deep.name, 'SKILL.md');
          if (fs.existsSync(deepFile)) missed.push(path.relative(ROOT, deepFile).replace(/\\/g, '/'));
        }
      }
    }
  }
  if (missed.length) {
    throw new Error(`Non-marketplace-discoverable skills:\n${missed.join('\n')}`);
  }
  return all.sort((a, b) => a.category.localeCompare(b.category) || a.slug.localeCompare(b.slug));
}

const skills = discoverSkills();
const total = skills.length;
const byCategory = {};
for (const s of skills) (byCategory[s.category] ||= []).push(s);
const categories = Object.keys(byCategory).sort();

const taxonomy = ['slug,name,category,path,description,priority,compatibility'];
for (const s of skills) taxonomy.push([s.slug, s.name, s.category, s.path, s.description, s.priority, s.compatibility].map(csvEscape).join(','));
fs.writeFileSync(path.join(ROOT, 'taxonomy.csv'), taxonomy.join('\n') + '\n');

let claude = `# GTM Skills\n\n${total} production go-to-market skills for Claude-compatible agents. Skills are self-contained folders with instructions, scripts, references, assets/templates, and metadata that agents load through progressive disclosure.\n\n`;
claude += `## Anthropic / agentskills Alignment\n\n- Every skill is a folder with required SKILL.md and optional scripts/, references/, templates/, or assets/.\n- Discovery loads name + description; activation loads SKILL.md; execution loads support files only when needed.\n- Marketplace-visible paths are exactly skills/<category>/<skill>/SKILL.md.\n- Use the narrowest skill that matches the task; combine skills only when the workflow requires it.\n\n## Skills Index\n\n`;
for (const cat of categories) {
  claude += `### ${cat} (${byCategory[cat].length})\n`;
  for (const s of byCategory[cat]) claude += `- **${s.slug}** — ${s.description.slice(0, 180).trimEnd()}\n`;
  claude += '\n';
}
fs.writeFileSync(path.join(ROOT, 'CLAUDE.md'), claude);

let agents = `# gtm-skills — Agent Skills Index\n\n${total} production GTM skills for AI agents. This repo follows the Anthropic/agentskills model: portable skill folders with SKILL.md plus optional scripts/, references/, templates/, and assets/.\n\n## Install\n\nClaude Code marketplace style:\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\nagentskills CLI style:\n\n\`\`\`bash\ngh skill install LeadMagic/gtm-skills\ngh skill install LeadMagic/gtm-skills pricing-strategy\ngh skill install LeadMagic/gtm-skills --category outbound\n\`\`\`\n\nLocal installer:\n\n\`\`\`bash\n./install.sh\n./install.sh --target hermes\n./install.sh --target cursor --project /path/to/project\n./install.sh --target all --dry-run\n\`\`\`\n\n## Skill Folder Standard\n\n\`\`\`text\nskill-name/\n├── SKILL.md\n├── references/\n├── scripts/\n├── templates/\n└── assets/\n\`\`\`\n\n## Categories\n\n`;
for (const cat of categories) agents += `- **${cat}** — ${byCategory[cat].length} skills\n`;
agents += `\n## Quality Standard\n\nEvery skill must be tactical, artifact-first, framework-cited, marketplace-discoverable, and clean for a public repository.\n`;
fs.writeFileSync(path.join(ROOT, 'AGENTS.md'), agents);

let readme = `# GTM Skills\n\n[![Skills](https://img.shields.io/badge/skills-${total}-blue)](skills/) [![Categories](https://img.shields.io/badge/categories-${categories.length}-green)](skills/)\n\n${total} production go-to-market skills for Claude Code and other AI agents. Built for sales, marketing, PLG, analytics, automation, customer success, RevOps, founder-led GTM, and tool operations.\n\nThis repo follows the Anthropic/agentskills pattern: skills are self-contained folders of instructions, scripts, references, templates/assets, and metadata that agents load dynamically through progressive disclosure.\n\n## Install\n\nClaude Code marketplace style:\n\n\`\`\`text\n/plugin marketplace add LeadMagic/gtm-skills\n/plugin install gtm-skills@gtm-skills\n\`\`\`\n\nagentskills CLI style:\n\n\`\`\`bash\ngh skill install LeadMagic/gtm-skills\n\`\`\`\n\nInteractive installer:\n\n\`\`\`bash\n./install.sh\n./install.sh --target all --dry-run\n\`\`\`\n\n## What makes this repo different\n\n- Artifact-first: skills produce copy, plans, scorecards, runbooks, dashboards, workflows, templates, or scripts.\n- Anthropic-style folders: SKILL.md for instructions; scripts/, references/, templates/, and assets/ for execution resources.\n- Authority-backed: skills cite named operators, vendors, books, and frameworks instead of vague best practices.\n- Progressive disclosure: SKILL.md stays focused; deep tables/templates live in support files.\n- Marketplace-ready: every skill is discoverable by agentskills.io patterns and validated in CI.\n- Supply-chain aware: skills.lock tracks SHA256 for every skill.\n\n## Categories\n\n`;
for (const cat of categories) {
  readme += `### ${cat} (${byCategory[cat].length})\n\n`;
  for (const s of byCategory[cat]) readme += `- [${s.slug}](${s.path}) — ${s.description.slice(0, 220).trimEnd()}\n`;
  readme += '\n';
}
readme += `## Validate\n\n\`\`\`bash\nnpm run build\nnpm run check\ngh skill publish --dry-run\n\`\`\`\n`;
fs.writeFileSync(path.join(ROOT, 'README.md'), readme);

fs.mkdirSync(PLUGIN_DIR, { recursive: true });
const plugin = {
  name: 'gtm-skills',
  version: '0.23.0',
  description: `${total} production go-to-market playbooks for AI agents across ${categories.length} categories.`,
  author: 'LeadMagic',
  license: 'MIT',
  homepage: 'https://leadmagic.io',
  repository: 'https://github.com/LeadMagic/gtm-skills',
  skills: ['skills/*/SKILL.md', 'skills/*/*/SKILL.md'],
};
fs.writeFileSync(path.join(PLUGIN_DIR, 'plugin.json'), JSON.stringify(plugin, null, 2) + '\n');
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
fs.writeFileSync(path.join(PLUGIN_DIR, 'marketplace.json'), JSON.stringify(marketplace, null, 2) + '\n');

console.log(`Generated taxonomy.csv, CLAUDE.md, AGENTS.md, README.md, plugin metadata for ${total} skills across ${categories.length} categories.`);
