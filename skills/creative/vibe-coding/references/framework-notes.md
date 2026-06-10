# Vibe Coding — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- ****

## Authoritative foundations

### Andrej Karpathy — Vibe Coding (Feb 2025)
"There's a new kind of coding I call 'vibe coding,' where you fully give in
to the vibes, embrace exponentials, and forget that the code even exists.
It's possible because the LLMs are getting so good. I just talk to Composer
with SuperWhisper so I barely touch the keyboard. I ask for the dumbest
things like 'decrease the padding on the sidebar by half' because I'm too
lazy to find it. I 'Accept All' always, I don't read the diffs anymore."

**The vibe coding philosophy in 4 principles:**
1. **Describe, don't write.** You provide intent. AI provides implementation.
2. **Iterate at conversation speed.** "Make it darker." "Add a CTA." "Change
   the font." Each takes 5 seconds, not 5 minutes.
3. **Accept and review later.** Ship fast. Fix what breaks. Don't obsess over
   code quality — obsess over user outcomes.
4. **The code is disposable.** If the AI can regenerate a page in 30 seconds,
   you don't need to understand every line. You need to understand if the
   OUTPUT works.

### Pieter Levels (@levelsio) — AI-Assisted Solo Building
Levels builds $100K+/mo products solo using AI tools. His principle: "The AI
writes 80% of the code. I g

*(See SKILL.md for full detail.)*

## Key reference tables

| Tool | Best For | Pricing | Skill Level | Output |
|---|---|---|---|---|
| **v0 by Vercel** | Landing pages, UI components, React apps | Free-$20/mo | Zero code | Production React/Next.js |
| **Lovable** | Full-stack apps, tools, SaaS MVPs | Free-$20/mo | Zero code | Full-stack apps with backend |
| **Bolt.new** | Rapid prototyping, full apps | Free-$20/mo | Zero code | Full-stack apps |
| **Cursor + Claude** | Codebase-level changes, complex features | $20/mo | Some code | Any codebase |
| **Claude Code** | Terminal-based, agentic development | API usage | Technical | Full codebases |
| **Replit Agent** | Quick tools, internal dashboards | $25/mo | Minimal code | Hosted apps |
| **Tempo Labs** | React UI components, design-to-code | Free-$15/mo | Zero code | React components |

| Expert | Platform | What They Teach |
|---|---|---|
| **Andrej Karpathy** | @karpathy (X) | Vibe coding philosophy, AI development |
| **Pieter Levels** | @levelsio (X) | Solo building with AI, $100K+/mo products |
| **Sahil Lavingia** | @shl (X) | Gumroad, AI-first product building |
| **Marc Lou** | @marc_lou (X) | AI shipping machine, 20+ products |
| **Guillermo Rauch** | @rauchg (X) | v0, Vercel, generative UI |
| **Riley Brown** | @rileybrown_ai (X) | AI coding tutorials, Cursor workflows |
| **Mckay Wrigley** | @mckaywrigley (X) | AI coding, Claude Code workflows |
| **Sully Omarr** | @SullyOmarr (X) | Lovable, Bolt, AI app building |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
