#!/usr/bin/env node
/**
 * generate-indexes.js — Regenerates CLAUDE.md skill index and taxonomy.csv
 * from the current skills directory.
 * Usage: node scripts/generate-indexes.js
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const TAXONOMY_PATH = path.join(__dirname, '..', 'taxonomy.csv');
const CLAUDE_PATH = path.join(__dirname, '..', 'CLAUDE.md');

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

function walkSkills(dir, category) {
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
        category: category || path.basename(dir) 
      });
    }
  }
  return skills;
}

// Walk all categories
const categories = fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
  .filter(e => e.isDirectory() && !e.name.startsWith('_'));

const allSkills = [];
for (const cat of categories) {
  const skills = walkSkills(path.join(SKILLS_DIR, cat.name), cat.name);
  allSkills.push(...skills);
}

// Generate taxonomy.csv
const csvHeader = 'slug,name,category,description,priority\n';
const csvRows = allSkills.map(s => 
  `${s.slug},"${s.name}","${s.category}","${(s.description || '').slice(0, 100)}",medium`
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

for (const [cat, skills] of Object.entries(byCategory)) {
  claude += `### ${cat}\n`;
  for (const s of skills) {
    claude += `- **${s.slug}** — ${s.description.slice(0, 120)}\n`;
  }
  claude += '\n';
}

fs.writeFileSync(CLAUDE_PATH, claude);

console.log(`Generated taxonomy.csv with ${allSkills.length} skills.`);
console.log('Generated CLAUDE.md.');
