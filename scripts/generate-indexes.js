#!/usr/bin/env node
/**
 * generate-indexes.js — Regenerates CLAUDE.md, AGENTS.md, and taxonomy.csv
 * from the current skills directory. Handles up to 3-level nesting (tools/crm/toolkit).
 * Usage: node scripts/generate-indexes.js
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const TAXONOMY_PATH = path.join(__dirname, '..', 'taxonomy.csv');
const CLAUDE_PATH = path.join(__dirname, '..', 'CLAUDE.md');
const AGENTS_PATH = path.join(__dirname, '..', 'AGENTS.md');

function parseSkillFrontmatter(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    if (!content.startsWith('---')) return null;
    const end = content.indexOf('\n---', 3);
    if (end === -1) return null;
    const fmText = content.slice(3, end);
    const fm = {};
    for (const line of fmText.split('\n')) {
      const idx = line.indexOf(':');
      if (idx === -1) continue;
      const key = line.slice(0, idx).trim();
      let value = line.slice(idx + 1).trim();
      if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }
      fm[key] = value;
    }
    return fm;
  } catch { return null; }
}

function walkSkillsDeep(dir, category) {
  const skills = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  
  for (const entry of entries) {
    if (!entry.isDirectory() || entry.name.startsWith('_')) continue;
    const skillFile = path.join(dir, entry.name, 'SKILL.md');
    
    if (fs.existsSync(skillFile)) {
      const fm = parseSkillFrontmatter(skillFile);
      skills.push({ 
        slug: entry.name, 
        name: fm?.name || entry.name, 
        description: fm?.description || '', 
        category: category || path.basename(dir),
        priority: fm?.priority || 'medium'
      });
    } else {
      // Second level: category/skill-dir/ or tools/crm/
      const subEntries = fs.readdirSync(path.join(dir, entry.name), { withFileTypes: true });
      for (const sub of subEntries) {
        if (!sub.isDirectory()) continue;
        const subFile = path.join(dir, entry.name, sub.name, 'SKILL.md');
        if (fs.existsSync(subFile)) {
          const fm = parseSkillFrontmatter(subFile);
          skills.push({
            slug: sub.name,
            name: fm?.name || sub.name,
            description: fm?.description || '',
            category: category || path.basename(dir),
            priority: fm?.priority || 'medium'
          });
        } else {
          // Third level: tools/crm/crm-toolkit/
          const deepEntries = fs.readdirSync(path.join(dir, entry.name, sub.name), { withFileTypes: true });
          for (const deep of deepEntries) {
            if (!deep.isDirectory()) continue;
            const deepFile = path.join(dir, entry.name, sub.name, deep.name, 'SKILL.md');
            if (fs.existsSync(deepFile)) {
              const fm = parseSkillFrontmatter(deepFile);
              skills.push({
                slug: deep.name,
                name: fm?.name || deep.name,
                description: fm?.description || '',
                category: category || path.basename(dir),
                priority: fm?.priority || 'medium'
              });
            }
          }
        }
      }
    }
  }
  return skills;
}

// Walk all categories
const categories = fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
  .filter(e => e.isDirectory() && !e.name.startsWith('_'));

const allSkills = [];
for (const cat of categories) {
  const skills = walkSkillsDeep(path.join(SKILLS_DIR, cat.name), cat.name);
  allSkills.push(...skills);
}

// Generate taxonomy.csv
const csvHeader = 'slug,name,category,description,priority\n';
const csvRows = allSkills.map(s => 
  `${s.slug},${s.name},${s.category},"${(s.description || '').replace(/"/g, '""').slice(0, 120)}",${s.priority || 'medium'}`
).join('\n');
fs.writeFileSync(TAXONOMY_PATH, csvHeader + csvRows + '\n');

// Generate CLAUDE.md
const byCategory = {};
for (const s of allSkills) {
  if (!byCategory[s.category]) byCategory[s.category] = [];
  byCategory[s.category].push(s);
}

let claude = '# GTM Blueprints\n\n';
claude += `${allSkills.length} go-to-market skills for AI agents. Install into Claude Code, then ask for anything.\n\n`;
claude += '## Skills Index\n\n';

for (const [cat, skills] of Object.entries(byCategory).sort()) {
  claude += `### ${cat} (${skills.length})\n`;
  for (const s of skills.sort((a,b) => a.slug.localeCompare(b.slug))) {
    claude += `- **${s.slug}** — ${(s.description || '').slice(0, 120)}\n`;
  }
  claude += '\n';
}

fs.writeFileSync(CLAUDE_PATH, claude);

// Generate AGENTS.md
let agents = '# GTM Blueprints — Agent Skills\n\n';
agents += `${allSkills.length} go-to-market skills for AI coding agents. Works with Claude Code, Cursor, Codex, Windsurf, Hermes, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose.\n\n`;
agents += '## Install\n\n';
agents += '```bash\n';
agents += '# Interactive TUI installer\n';
agents += './install.sh\n\n';
agents += '# Non-interactive examples\n';
agents += './install.sh --target hermes\n';
agents += './install.sh --target cursor --project /path/to/project\n';
agents += './install.sh --target all --dry-run\n';
agents += '```\n\n';
agents += '## Categories\n\n';

for (const [cat, skills] of Object.entries(byCategory).sort()) {
  agents += `- **${cat}** (${skills.length} skills)\n`;
}
agents += '\n';

fs.writeFileSync(AGENTS_PATH, agents);

console.log(`Generated taxonomy.csv (${allSkills.length} skills)`);
console.log(`Generated CLAUDE.md (${allSkills.length} skills)`);
console.log(`Generated AGENTS.md (${allSkills.length} skills, ${Object.keys(byCategory).length} categories)`);