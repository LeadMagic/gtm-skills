#!/usr/bin/env node
/**
 * generate-pitfalls-index.js — aggregate ## Common Pitfalls from every skill
 * into references/pitfalls-index.md for cross-skill discovery.
 *
 * Run via npm run build or: node scripts/generate-pitfalls-index.js
 */

const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.join(__dirname, '..');
const SKILLS_DIR = path.join(ROOT, 'skills');
const OUT = path.join(ROOT, 'references', 'pitfalls-index.md');

function walkSkills(dir, parts = []) {
  const skills = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.startsWith('_')) continue;
    const p = path.join(dir, entry.name);
    const skillFile = path.join(p, 'SKILL.md');
    if (fs.existsSync(skillFile)) {
      const relParts = [...parts, entry.name];
      skills.push({
        category: relParts[0],
        slug: relParts.length === 2 ? relParts[1] : relParts.slice(1).join('/'),
        path: path.relative(ROOT, skillFile).replace(/\\/g, '/'),
      });
    } else {
      walkSkills(p, [...parts, entry.name]).forEach((s) => {
        skills.push(s);
      });
    }
  }
  return skills.sort((a, b) => a.path.localeCompare(b.path));
}

function extractPitfalls(content) {
  const start = content.indexOf('## Common Pitfalls');
  if (start === -1) return [];
  const after = content.slice(start + '## Common Pitfalls'.length);
  const next = after.search(/^## /m);
  const section = next === -1 ? after : after.slice(0, next);
  const items = [];
  const lines = section.split('\n');
  let current = null;
  for (const line of lines) {
    const m = line.match(/^(\d+)\.\s+\*\*(.+?)\*\*(.*)$/);
    if (m) {
      if (current) items.push(current);
      current = { title: m[2].trim(), detail: m[3].trim().replace(/^[.:]\s*/, '') };
      continue;
    }
    if (current && line.trim()) {
      current.detail = `${current.detail} ${line.trim()}`.trim();
    }
  }
  if (current) items.push(current);
  return items;
}

function parseName(content) {
  const m = content.match(/^name:\s*(.+)$/m);
  return m ? m[1].trim() : null;
}

const skills = walkSkills(SKILLS_DIR);
const byCategory = {};
let totalPitfalls = 0;
let skillsWithPitfalls = 0;

for (const skill of skills) {
  const content = fs.readFileSync(path.join(ROOT, skill.path), 'utf8');
  const pitfalls = extractPitfalls(content);
  if (!pitfalls.length) continue;
  skillsWithPitfalls += 1;
  totalPitfalls += pitfalls.length;
  if (!byCategory[skill.category]) byCategory[skill.category] = [];
  byCategory[skill.category].push({
    ...skill,
    name: parseName(content) || skill.slug,
    pitfalls,
  });
}

const categories = Object.keys(byCategory).sort();
const lines = [
  '# GTM Skills — Common Pitfalls Index',
  '',
  `Auto-generated from skill \`## Common Pitfalls\` sections. **${totalPitfalls} pitfalls** across **${skillsWithPitfalls}** skills (${skills.length} total). Regenerate: \`npm run build\`.`,
  '',
  'Agents: load the source skill for full context, fixes, and quality checks — this index is for discovery and cross-skill pattern matching.',
  '',
  'Master router: `skills/foundation/using-gtm-skills/SKILL.md` · Expert catalog: `references/experts.md`',
  '',
];

for (const cat of categories) {
  lines.push(`## ${cat}`, '');
  for (const skill of byCategory[cat]) {
    lines.push(`### [${skill.name}](${skill.path})`, '');
    for (const p of skill.pitfalls) {
      const detail = p.detail ? ` — ${p.detail}` : '';
      lines.push(`- **${p.title}**${detail}`);
    }
    lines.push('');
  }
}

fs.writeFileSync(OUT, `${lines.join('\n').trimEnd()}\n`);
console.log(
  `Generated references/pitfalls-index.md: ${totalPitfalls} pitfalls from ${skillsWithPitfalls} skills.`,
);
