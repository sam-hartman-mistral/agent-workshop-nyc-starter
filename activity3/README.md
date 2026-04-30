# Activity 3 — Build Your Own Skill

**Goal:** Create a skill that solves a real problem — something you'd actually use after this workshop.

**Time:** ~60 minutes

---

## Step 1 — Pick an idea

Choose one that resonates, or come up with your own. Copy-paste the starter prompt into Vibe.

### Option A: Meeting Prep Brief

Before a meeting, research everyone you're meeting with.

```
I want to build a skill called "meeting-prep" that prepares me for meetings.

Given a list of names and companies, it should:
1. Use Playwright to visit each person's company website
2. Use Fetch to pull any recent news or blog posts about the company
3. Store findings in SQLite (person, company, role, recent_news, key_facts)
4. Output a 1-page briefing with key talking points per person

Create it as skills/meeting-prep.md
Don't write the file yet — tell me your plan first.
```

### Option B: Tech News Digest

Build a morning briefing from public tech news sources.

```
I want to build a skill called "tech-digest" that creates a daily tech news summary.

It should:
1. Use Playwright to visit Hacker News, TechCrunch, and The Verge
2. Use Fetch to extract the top 5 stories from each
3. Store them in SQLite (source, title, url, summary, date)
4. Output a formatted digest grouped by source with one-line summaries

Create it as skills/tech-digest.md
Don't write the file yet — tell me your plan first.
```

### Option C: Documentation Checker

Audit your company's docs for outdated content.

```
I want to build a skill called "docs-audit" that checks documentation for staleness.

Given a docs site URL, it should:
1. Use Playwright to crawl the sitemap or main pages
2. Use Fetch to extract content from each page
3. Store in SQLite (url, title, last_mentioned_date, word_count, has_code_blocks)
4. Flag pages that reference old versions, have broken links, or are very short
5. Output a prioritized list of pages to update

Create it as skills/docs-audit.md
Don't write the file yet — tell me your plan first.
```

### Option D: Your Own Idea

Think about what wastes your time weekly. Common patterns:
- **Research** something across multiple sources → summarize
- **Monitor** a set of pages for changes → alert
- **Compare** options by gathering data → rank
- **Extract** info from messy sources → structure into a table

```
I want to build a skill called "[name]" that [what it does].

It should:
1. Use [which MCP tools] to [gather what data]
2. Store in SQLite with columns: [what fields]
3. Output [what format]

Create it as skills/[name].md
Don't write the file yet — tell me your plan first.
```

---

## Step 2 — Challenge the plan

Same as Activity 2. Push back:
- "What if the site blocks automated access?"
- "What if there's no data for one of the inputs?"
- "How do you handle pages that take a long time to load?"
- "What if I run this twice — does it duplicate data or update it?"

---

## Step 3 — Delegate

When the plan is solid:

```bash
vibe --dangerously-skip-permissions
```

Or use Shift+Tab to cycle to Auto-Approve mode.

---

## Step 4 — Test and iterate

```
/your-skill-name [your input]
```

Run it. Check the output. Tweak the skill file. Run it again. Repeat until it's useful.

---

## Want to add more MCP servers?

Here are a few that are easy to install (no API key, no signup):

| Server | What it does | Install |
|--------|-------------|---------|
| **Filesystem** | Read/write local files | `npx -y @anthropic-ai/mcp-filesystem` |
| **Git** | Interact with git repos | `uvx mcp-server-git` |
| **Memory** | Persistent key-value store | `npx -y @anthropic-ai/mcp-memory` |

Add them to `~/.vibe/config.toml` following the same format as Activity 1.

Browse more at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

---

## Share Out

At the end of the session, you'll show what you built. **2 minutes each.**

Structure:
1. **What does your skill do?** (one sentence)
2. **Run it** — show the output
3. **What problem does it solve?** — why is this useful for you or your team?

No slides needed. Just your terminal.
