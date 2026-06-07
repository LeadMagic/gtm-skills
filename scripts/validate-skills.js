#!/usr/bin/env node
/**
 * validate-skills.js — Validates all SKILL.md files in the gtm-skills repo.
 * Checks: YAML frontmatter, required fields, description length, directory/name match.
 * Usage: node scripts/validate-skills.js
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const MAX_NAME_LENGTH = 64;
const MAX_DESC_LENGTH = 1024;
const MAX_BODY_LENGTH = 100000;

function parseFrontmatter(content) {
  if (!content.startsWith('---')) return { error: 'File must start with ---' };
  const end = content.indexOf('\n---', 3);
  if (end === -1) return { error: 'Missing closing --- for frontmatter' };
  
  const fmText = content.slice(3, end).trim();
  const lines = fmText.split('\n');
  const fm = {};
  
  for (const line of lines) {
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) continue;
    const key = line.slice(0, colonIdx).trim();
    let value = line.slice(colonIdx + 1).trim();
    
    if (value === '>-') {
      // Multi-line folded block scalar — read subsequent indented lines
      value = '';
      // Not implementing full YAML parsing; for simple key: >- this is enough
    } else if ((value.startsWith('"') && value.endsWith('"')) || 
               (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    fm[key] = value;
  }
  
  fm._bodyStart = end + 4; // skip \n---\n
  return fm;
}

function walkSkills(dir) {
  const skills = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith('_')) continue; // skip _TEMPLATE
    
    const skillDir = path.join(dir, entry.name);
    const skillFile = path.join(skillDir, 'SKILL.md');
    
    if (fs.existsSync(skillFile)) {
      skills.push({ dir: entry.name, path: skillFile, category: path.basename(dir) });
    } else {
      // Check subcategories
      const subEntries = fs.readdirSync(skillDir, { withFileTypes: true });
      for (const sub of subEntries) {
        if (!sub.isDirectory()) continue;
        const subSkillFile = path.join(skillDir, sub.name, 'SKILL.md');
        if (fs.existsSync(subSkillFile)) {
          skills.push({ dir: sub.name, path: subSkillFile, category: entry.name });
        }
      }
    }
  }
  return skills;
}

let errors = 0;
let warnings = 0;
let total = 0;

const skills = walkSkills(SKILLS_DIR);
total = skills.length;

console.log(`Validating ${total} skills...\n`);

for (const skill of skills) {
  const content = fs.readFileSync(skill.path, 'utf-8');
  const fm = parseFrontmatter(content);
  
  if (fm.error) {
    console.error(`❌ ${skill.path}: ${fm.error}`);
    errors++;
    continue;
  }
  
  // Check name
  if (!fm.name) {
    console.error(`❌ ${skill.path}: Missing 'name' field`);
    errors++;
  } else if (fm.name.length > MAX_NAME_LENGTH) {
    console.error(`❌ ${skill.path}: Name too long (${fm.name.length} > ${MAX_NAME_LENGTH})`);
    errors++;
  } else if (fm.name !== skill.dir) {
    console.warn(`⚠️  ${skill.path}: Name '${fm.name}' doesn't match directory '${skill.dir}'`);
    warnings++;
  }
  
  // Check description
  if (!fm.description) {
    console.error(`❌ ${skill.path}: Missing 'description' field`);
    errors++;
  } else if (fm.description.length > MAX_DESC_LENGTH) {
    console.error(`❌ ${skill.path}: Description too long (${fm.description.length} > ${MAX_DESC_LENGTH})`);
    errors++;
  }
  
  // Check body
  const body = content.slice(fm._bodyStart || 0);
  if (body.trim().length === 0) {
    console.error(`❌ ${skill.path}: Empty body after frontmatter`);
    errors++;
  }
  if (content.length > MAX_BODY_LENGTH) {
    console.warn(`⚠️  ${skill.path}: File too large (${content.length} > ${MAX_BODY_LENGTH})`);
    warnings++;
  }
  
  // Success
  if (!fm.error) {
    const bodyLen = body.trim().length;
    console.log(`✅ ${skill.category}/${skill.dir} — ${bodyLen} chars body`);
  }
}

console.log(`\n${total} skills checked. ${errors} errors, ${warnings} warnings.`);
process.exit(errors > 0 ? 1 : 0);
