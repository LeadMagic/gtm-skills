#!/usr/bin/env node
/**
 * validate-skills.js — Validates all SKILL.md files in the gtm-skills repo.
 * Checks: YAML frontmatter, required fields, description length, directory/name match.
 * Handles YAML block scalars (| and >-) and multi-line values.
 * Usage: node scripts/validate-skills.js
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const MAX_NAME_LENGTH = 64;
const MAX_DESC_LENGTH = 1024;

function parseFrontmatter(content) {
  if (!content.startsWith('---')) return { error: 'File must start with ---' };
  
  // Find closing --- (must be on its own line or \n---\n)
  const rest = content.slice(3);
  const closingMatch = rest.match(/\n---\s*\n/);
  if (!closingMatch) return { error: 'Missing closing --- for frontmatter' };
  
  const end = 3 + closingMatch.index;
  const fmText = content.slice(3, end);
  const lines = fmText.split('\n');
  const fm = {};
  
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const colonIdx = line.indexOf(':');
    
    // Skip empty lines and lines without colons
    if (colonIdx === -1) { i++; continue; }
    
    const key = line.slice(0, colonIdx).trim();
    const afterColon = line.slice(colonIdx + 1);
    
    // Check if this is a block scalar indicator (|, >, |-, >-)
    const blockMatch = afterColon.match(/^\s*[|>][-]?\s*$/);
    
    if (blockMatch) {
      // Block scalar — read subsequent indented lines
      const indent = '  '; // YAML block scalars expect at least one level of indentation
      const valueLines = [];
      i++;
      while (i < lines.length) {
        const nextLine = lines[i];
        // A line is part of the block scalar if it starts with whitespace
        // or is empty (blank line within the block)
        if (nextLine.trim() === '') {
          valueLines.push('');
          i++;
          continue;
        }
        if (nextLine.startsWith('  ') || nextLine.startsWith('\t')) {
          valueLines.push(nextLine.trimStart());
          i++;
        } else if (nextLine.trim() === '---') {
          // Hit closing ---, stop
          break;
        } else {
          // Unindented line — might be next key or end of frontmatter
          break;
        }
      }
      const value = valueLines.join(' ').replace(/\s+/g, ' ').trim();
      fm[key] = value;
      continue;
    }
    
    // Check if it's a quoted value (may span multiple lines for folded >-)
    let value = afterColon.trim();
    
    if (value.startsWith('"') || value.startsWith("'")) {
      const quote = value[0];
      // Find closing quote
      if (value.endsWith(quote) && value.length > 1) {
        value = value.slice(1, -1);
      } else {
        // Multi-line quoted — read until closing quote
        let fullValue = value.slice(1);
        i++;
        while (i < lines.length) {
          fullValue += ' ' + lines[i].trim();
          if (lines[i].trim().endsWith(quote)) {
            fullValue = fullValue.slice(0, -1);
            break;
          }
          i++;
        }
        value = fullValue;
      }
    }
    
    fm[key] = value;
    i++;
  }
  
  fm._bodyStart = end + closingMatch[0].length;
  return fm;
}

function walkSkills(dir) {
  const skills = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith('_')) continue;
    
    const skillDir = path.join(dir, entry.name);
    const skillFile = path.join(skillDir, 'SKILL.md');
    
    if (fs.existsSync(skillFile)) {
      skills.push({ dir: entry.name, path: skillFile, category: path.basename(dir) });
    } else {
      const subEntries = fs.readdirSync(skillDir, { withFileTypes: true });
      for (const sub of subEntries) {
        if (!sub.isDirectory()) continue;
        const subSkillFile = path.join(skillDir, sub.name, 'SKILL.md');
        if (fs.existsSync(subSkillFile)) {
          skills.push({ dir: sub.name, path: subSkillFile, category: entry.name });
        } else {
          // Third level: tools/crm/crm-toolkit/SKILL.md pattern
          const deepEntries = fs.readdirSync(path.join(skillDir, sub.name), { withFileTypes: true });
          for (const deep of deepEntries) {
            if (!deep.isDirectory()) continue;
            const deepSkillFile = path.join(skillDir, sub.name, deep.name, 'SKILL.md');
            if (fs.existsSync(deepSkillFile)) {
              skills.push({ dir: deep.name, path: deepSkillFile, category: entry.name });
            }
          }
        }
      }
    }
  }
  return skills;
}

let errors = 0;
let warnings = 0;

const skills = walkSkills(SKILLS_DIR);
console.log(`Validating ${skills.length} skills...\n`);

for (const skill of skills) {
  const content = fs.readFileSync(skill.path, 'utf-8');
  const fm = parseFrontmatter(content);
  
  if (fm.error) {
    console.error(`❌ ${skill.category}/${skill.dir}: ${fm.error}`);
    errors++;
    continue;
  }
  
  // Check name
  if (!fm.name) {
    console.error(`❌ ${skill.category}/${skill.dir}: Missing 'name' field`);
    errors++;
  } else if (fm.name.length > MAX_NAME_LENGTH) {
    console.error(`❌ ${skill.category}/${skill.dir}: Name too long (${fm.name.length} > ${MAX_NAME_LENGTH})`);
    errors++;
  } else if (fm.name !== skill.dir && fm.name !== 'template-skill') {
    console.warn(`⚠️  ${skill.category}/${skill.dir}: Name '${fm.name}' ≠ directory '${skill.dir}'`);
    warnings++;
  }
  
  // Check description
  if (!fm.description || fm.description.trim().length === 0) {
    console.error(`❌ ${skill.category}/${skill.dir}: Missing 'description' field`);
    errors++;
  } else if (fm.description.length > MAX_DESC_LENGTH) {
    console.error(`❌ ${skill.category}/${skill.dir}: Description too long (${fm.description.length} > ${MAX_DESC_LENGTH})`);
    errors++;
  }
  
  // Check body
  const body = content.slice(fm._bodyStart || 0);
  if (body.trim().length === 0) {
    console.error(`❌ ${skill.category}/${skill.dir}: Empty body after frontmatter`);
    errors++;
  }
  
  if (fm.name && fm.description && body.trim().length > 0) {
    console.log(`✅ ${skill.category}/${skill.dir} — ${fm.description.length}c desc, ${body.trim().length}c body`);
  }
}

console.log(`\n${skills.length} skills checked. ${errors} errors, ${warnings} warnings.`);
process.exit(errors > 0 ? 1 : 0);