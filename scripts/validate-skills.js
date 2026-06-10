#!/usr/bin/env node
/**
 * validate-skills.js — strict validation for LeadMagic/gtm-skills.
 *
 * Enforces:
 * - AgentSkills/Claude SKILL.md structure
 * - frontmatter fields + metadata completeness
 * - exact supported-system compatibility string
 * - named framework attribution in frontmatter and body
 * - output format, quality check, pitfalls, related skills
 * - no duplicate core sections
 * - sensitive/professional-domain disclaimers
 * - public-safe content hygiene
 */

const fs = require('node:fs');
const path = require('node:path');
const { STANDARD_COMPATIBILITY } = require('./lib/compatibility');

const ROOT = path.join(__dirname, '..');
const SKILLS_DIR = path.join(ROOT, 'skills');
const MAX_NAME_LENGTH = 64;
const MAX_DESC_LENGTH = 1024;
const MIN_BODY_CHARS = 1200;
const MIN_BODY_LINES = 60;
const EXPECTED_COMPATIBILITY = STANDARD_COMPATIBILITY;

const REQUIRED_TOP_FIELDS = ['name', 'description', 'license', 'compatibility'];
const REQUIRED_METADATA_FIELDS = ['version', 'author', 'category', 'tags', 'frameworks'];
const REQUIRED_SECTIONS = [
  '## Overview',
  '## When to Use',
  '## Output Format',
  '## Quality Check',
  '## Common Pitfalls',
  '## Related Skills',
];
const ATTRIBUTION_SECTIONS = ['## Authoritative Foundations', '## Frameworks Referenced'];
const ARTIFACT_REQUIRED_CATEGORIES = new Set([
  'analytics',
  'automation',
  'design',
  'leadmagic',
  'tools',
]);
const REQUIRED_ARTIFACTS = [
  'references/framework-notes.md',
  'templates/output-template.md',
  'scripts/check-output.py',
];
const DUPLICATE_CHECK_SECTIONS = [
  ...REQUIRED_SECTIONS,
  '## Authoritative Foundations',
  '## Frameworks Referenced',
  '## Prerequisites',
  '## Step-by-Step Process',
];

const SENSITIVE_SKILLS_REQUIRING_DISCLAIMER = new Set([
  'legal-for-founders',
  'business-insurance',
  'soc2-compliance',
  'data-privacy-compliance',
  'employment-compliance',
  'equity-management',
  'vendor-contracts',
  'security-assessments',
  'financial-modeling',
  'exiting-company',
  'co-founder-dynamics',
  'fundraising-strategy',
  'advisor-recruitment',
  'hiring-by-role',
  'first-hires-playbook',
  'yc-ecosystem',
]);

const FORBIDDEN_TERMS = [
  // Keep this list public-safe. Do not commit private company, infra, or founder-specific strings here.
  // Use local one-off history scans for private denylist terms before release.
];

const PUBLIC_SAFETY_PATTERNS = [
  /[0-9]{1,3}(?:,[0-9]{3})\+?\s+inboxes/i,
  /[0-9]+(?:\.[0-9]+)?m\s+cold\s+emails/i,
  /crypto\s+payments?/i,
];

const AI_SLOP_PHRASES = [
  "in today's fast-paced",
  'unlock your potential',
  'supercharge your',
  'game-changing',
  'cutting-edge',
  'seamless and frictionless',
  'revolutionize your',
  'take your business to the next level',
];

const QUESTIONABLE_PATTERNS = [
  /purchased\s+lists?/i,
  /scraped\s+emails?/i,
  /buy\s+followers/i,
  /fake\s+reviews?/i,
  /sock\s*puppet/i,
  /astroturf/i,
  /bypass\s+(?:consent|opt[- ]?out|unsubscribe)/i,
  /evade\s+(?:filters?|detection|compliance)/i,
];

function walkSkills(dir) {
  const skills = [];
  function walk(current, parts = []) {
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      if (!entry.isDirectory() || entry.name.startsWith('_')) continue;
      const p = path.join(current, entry.name);
      const skillFile = path.join(p, 'SKILL.md');
      if (fs.existsSync(skillFile)) {
        const relParts = [...parts, entry.name];
        const category = relParts[0];
        const dir = relParts.length === 2 ? relParts[1] : relParts.slice(1).join('/');
        skills.push({ category, dir, path: skillFile, rel: path.relative(ROOT, skillFile) });
      } else {
        walk(p, [...parts, entry.name]);
      }
    }
  }
  walk(dir);
  return skills.sort((a, b) => a.rel.localeCompare(b.rel));
}

function parseFrontmatter(content) {
  if (!content.startsWith('---\n')) return { error: 'File must start with YAML frontmatter delimiter ---' };
  const end = content.indexOf('\n---\n', 4);
  if (end === -1) return { error: 'Missing closing --- for frontmatter' };
  const fmText = content.slice(4, end);
  const bodyStart = end + 5;
  const fields = {};
  const lines = fmText.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const m = line.match(/^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$/);
    if (!m) continue;
    const key = m[1];
    let value = m[2].trim();
    if (/^[>|]-?$/.test(value)) {
      const valueLines = [];
      i += 1;
      while (i < lines.length && (/^\s+/.test(lines[i]) || lines[i].trim() === '')) {
        valueLines.push(lines[i].trim());
        i += 1;
      }
      i -= 1;
      value = valueLines.join(' ').replace(/\s+/g, ' ').trim();
    }
    fields[key] = value.replace(/^['"]|['"]$/g, '');
  }
  return { fields, fmText, bodyStart };
}

function metadataHas(fmText, key) {
  const re = new RegExp(`^\\s{2}${key}:`, 'm');
  return re.test(fmText);
}

function extractInlineOrList(fmText, key) {
  const inline = fmText.match(new RegExp(`^\\s{2}${key}:\\s*\\[([^\\]]*)\\]`, 'm'));
  if (inline) return inline[1].split(',').map(x => x.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean);
  const list = fmText.match(new RegExp(`^\\s{2}${key}:\\s*\\n((?:\\s{4}-\\s+.*\\n?)+)`, 'm'));
  if (list) return list[1].split('\n').map(x => x.replace(/^\s*-\s*/, '').trim().replace(/^['"]|['"]$/g, '')).filter(Boolean);
  return [];
}

function countSection(content, section) {
  const escaped = section.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const re = new RegExp(`^${escaped}\\s*$`, 'gmi');
  return (content.match(re) || []).length;
}

const CHECKABLE_EXT = /\.(?:md|py|js|csv|json)$/;
const BACKTICK_PATH = /^(?:\.\.\/|references|templates|scripts|assets|skills)\/[A-Za-z0-9._/-]+\.(?:md|py|js|csv|json)$/;

// Extract reference targets from a SKILL.md body: markdown links and
// backtick-quoted repo paths. Shared contract with scripts/audit-references.py.
function extractLinkTargets(content) {
  const targets = new Set();
  for (const m of content.matchAll(/\]\(([^)]+)\)/g)) {
    let target = m[1].trim();
    const space = target.search(/\s/);
    if (space !== -1) target = target.slice(0, space);
    if (!target || /^(?:https?:|mailto:|#)/i.test(target)) continue;
    target = target.split('#')[0];
    if (CHECKABLE_EXT.test(target)) targets.add(target);
  }
  for (const m of content.matchAll(/`([^`]+)`/g)) {
    const target = m[1].trim();
    if (BACKTICK_PATH.test(target)) targets.add(target);
  }
  return [...targets];
}

// A target resolves if it exists relative to the skill dir (skill-local
// artifact) OR relative to the repo root (shared catalog / full skills/ path).
function targetResolves(target, skillDir, filePath = null) {
  const candidates = [];
  if (target.startsWith('skills/')) {
    candidates.push(path.resolve(ROOT, target));
  } else if (target.startsWith('../') && filePath) {
    let cur = path.dirname(filePath);
    let rel = target;
    while (rel.startsWith('../')) {
      rel = rel.slice(3);
      cur = path.dirname(cur);
    }
    candidates.push(path.resolve(cur, rel));
  } else if (/^(?:references|templates|scripts|assets)\//.test(target)) {
    candidates.push(path.resolve(skillDir, target));
    candidates.push(path.resolve(ROOT, target));
  } else {
    if (filePath) candidates.push(path.resolve(path.dirname(filePath), target));
    candidates.push(path.resolve(skillDir, target));
    candidates.push(path.resolve(ROOT, target));
  }
  return candidates.some(p => fs.existsSync(p));
}

let errors = 0;
const warnings = 0;
const skills = walkSkills(SKILLS_DIR);
console.log(`Validating ${skills.length} skills...\n`);

for (const skill of skills) {
  const content = fs.readFileSync(skill.path, 'utf8');
  const parsed = parseFrontmatter(content);
  const skillId = `${skill.category}/${skill.dir}`;

  if (parsed.error) {
    console.error(`❌ ${skillId}: ${parsed.error}`);
    errors++;
    continue;
  }

  const { fields: fm, fmText, bodyStart } = parsed;
  const body = content.slice(bodyStart).trim();
  const lineCount = body.split('\n').length;
  let skillErrors = 0;

  const relParts = skill.rel.split(path.sep);
  const flatPath = relParts.length === 4 && relParts[0] === 'skills' && relParts[3] === 'SKILL.md';
  if (!flatPath) {
    console.error(`❌ ${skillId}: path must be marketplace-discoverable and flat: skills/<category>/<skill>/SKILL.md`);
    errors++; skillErrors++;
  }

  for (const field of REQUIRED_TOP_FIELDS) {
    if (!fm[field] || fm[field].trim().length === 0) {
      console.error(`❌ ${skillId}: Missing top-level '${field}' field`);
      errors++; skillErrors++;
    }
  }

  if (fm.name) {
    if (fm.name.length > MAX_NAME_LENGTH) {
      console.error(`❌ ${skillId}: name too long (${fm.name.length} > ${MAX_NAME_LENGTH})`);
      errors++; skillErrors++;
    }
    if (fm.name !== skill.dir) {
      console.error(`❌ ${skillId}: frontmatter name '${fm.name}' must equal skill directory name '${skill.dir}'`);
      errors++; skillErrors++;
    }
  }

  if (fm.description) {
    if (fm.description.length > MAX_DESC_LENGTH) {
      console.error(`❌ ${skillId}: description too long (${fm.description.length} > ${MAX_DESC_LENGTH})`);
      errors++; skillErrors++;
    }
    if (!/\b(use when|triggers on|when to use)\b/i.test(fm.description)) {
      console.error(`❌ ${skillId}: description should include trigger/use-case language`);
      errors++; skillErrors++;
    }
  }

  if (fm.license !== 'MIT') {
    console.error(`❌ ${skillId}: license must be MIT`);
    errors++; skillErrors++;
  }

  if (fm.compatibility !== EXPECTED_COMPATIBILITY) {
    console.error(`❌ ${skillId}: compatibility must exactly match the supported-system compatibility string`);
    errors++; skillErrors++;
  }

  for (const field of REQUIRED_METADATA_FIELDS) {
    if (!metadataHas(fmText, field)) {
      console.error(`❌ ${skillId}: metadata.${field} missing`);
      errors++; skillErrors++;
    }
  }

  const tags = extractInlineOrList(fmText, 'tags');
  const frameworks = extractInlineOrList(fmText, 'frameworks');
  if (tags.length < 3) {
    console.error(`❌ ${skillId}: metadata.tags must contain at least 3 tags`);
    errors++; skillErrors++;
  }
  if (frameworks.length < 3) {
    console.error(`❌ ${skillId}: metadata.frameworks must contain at least 3 named frameworks/sources`);
    errors++; skillErrors++;
  }

  if (body.length < MIN_BODY_CHARS) {
    console.error(`❌ ${skillId}: body too shallow (${body.length} chars < ${MIN_BODY_CHARS})`);
    errors++; skillErrors++;
  }
  if (lineCount < MIN_BODY_LINES) {
    console.error(`❌ ${skillId}: body too short (${lineCount} lines < ${MIN_BODY_LINES})`);
    errors++; skillErrors++;
  }

  for (const section of REQUIRED_SECTIONS) {
    if (!content.includes(section)) {
      console.error(`❌ ${skillId}: missing required section '${section}'`);
      errors++; skillErrors++;
    }
  }

  if (!ATTRIBUTION_SECTIONS.some(section => content.includes(section))) {
    console.error(`❌ ${skillId}: missing body-level attribution section (${ATTRIBUTION_SECTIONS.join(' or ')})`);
    errors++; skillErrors++;
  }

  if (ARTIFACT_REQUIRED_CATEGORIES.has(skill.category)) {
    if (!content.includes('## Execution Artifacts')) {
      console.error(`❌ ${skillId}: artifact-heavy category missing '## Execution Artifacts' section`);
      errors++; skillErrors++;
    }
    for (const relArtifact of REQUIRED_ARTIFACTS) {
      const artifactPath = path.join(path.dirname(skill.path), relArtifact);
      if (!fs.existsSync(artifactPath)) {
        console.error(`❌ ${skillId}: missing required artifact '${relArtifact}'`);
        errors++; skillErrors++;
      }
    }
  }

  for (const section of DUPLICATE_CHECK_SECTIONS) {
    const n = countSection(content, section);
    if (n > 1) {
      console.error(`❌ ${skillId}: duplicate section '${section}' (${n} occurrences)`);
      errors++; skillErrors++;
    }
  }

  if (SENSITIVE_SKILLS_REQUIRING_DISCLAIMER.has(fm.name)) {
    const hasDisclaimer = /## ⚠️ Disclaimer|## Disclaimer/.test(content)
      && /NOT legal advice/i.test(content)
      && /accounting advice/i.test(content)
      && /tax advice/i.test(content)
      && /qualified professionals/i.test(content);
    if (!hasDisclaimer) {
      console.error(`❌ ${skillId}: sensitive/professional-domain skill missing required disclaimer`);
      errors++; skillErrors++;
    }
  }

  for (const term of FORBIDDEN_TERMS) {
    if (content.includes(term)) {
      console.error(`❌ ${skillId}: forbidden public-safety term found: ${term}`);
      errors++; skillErrors++;
    }
  }

  for (const pattern of PUBLIC_SAFETY_PATTERNS) {
    if (pattern.test(content)) {
      console.error(`❌ ${skillId}: public-safety pattern found: ${pattern}`);
      errors++; skillErrors++;
    }
  }

  const lower = content.toLowerCase();
  for (const phrase of AI_SLOP_PHRASES) {
    if (lower.includes(phrase)) {
      console.error(`❌ ${skillId}: AI-slop phrase found: '${phrase}'`);
      errors++; skillErrors++;
    }
  }

  for (const pattern of QUESTIONABLE_PATTERNS) {
    if (pattern.test(content)) {
      console.error(`❌ ${skillId}: questionable/gray-hat pattern found: ${pattern}`);
      errors++; skillErrors++;
    }
  }

  const skillDir = path.dirname(skill.path);
  for (const target of extractLinkTargets(content)) {
    if (!targetResolves(target, skillDir, skill.path)) {
      console.error(`❌ ${skillId}: unresolvable reference target '${target}' (not found relative to skill dir or repo root)`);
      errors++; skillErrors++;
    }
  }

  if (skillErrors === 0) {
    console.log(`✅ ${skillId} — ${fm.description?.length || 0}c desc, ${body.length}c body, ${lineCount} lines`);
  }
}

console.log(`\n${skills.length} skills checked. ${errors} errors, ${warnings} warnings.`);
process.exit(errors > 0 ? 1 : 0);
