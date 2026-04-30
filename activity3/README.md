# Activity 3 — Build Your Own Skill

**Goal:** Create a skill that solves a real problem — something you'd actually use after this workshop.

**Time:** ~60 minutes

---

## Step 1 — Pick an idea

Make sure you're in the project directory and Vibe is running:

```bash
cd agent-workshop-nyc-starter
vibe
```

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
1. Use Playwright to visit Hacker News (news.ycombinator.com) and Lobste.rs
2. Use Fetch to extract the top 10 stories from each (title, url, score)
3. Store them in SQLite (source, title, url, score, fetched_at)
4. Output a formatted digest grouped by source with one-line summaries

Include fallback behavior if a source is unavailable or returns no results.

Create it as skills/tech-digest.md
Don't write the file yet — tell me your plan first.
```

### Option C: Documentation Checker

Audit a list of docs pages for outdated content.

> **Heads up:** This is the most advanced option. Pick it if you're comfortable with web scraping and want a real challenge.

```
I want to build a skill called "docs-audit" that checks a list of documentation pages for staleness.

Given a list of 3-5 URLs, it should:
1. Use Fetch to extract the text content of each page
2. Store in SQLite (url, title, word_count, has_code_blocks, fetched_at)
3. Flag pages that are very short (under 200 words) or have no code blocks
4. Output a prioritized list of pages to review, with a one-line reason for each

Include fallback behavior if a page is unavailable.

Create it as skills/docs-audit.md
Don't write the file yet — tell me your plan first.
```

### Option D: Your Own Idea

Think about what wastes your time weekly. Common patterns:
- **Research** something across multiple sources → summarize
- **Monitor** a set of pages for changes → alert
- **Compare** options by gathering data → rank
- **Extract** info from messy sources → structure into a table

> **Keep it simple.** If your idea has more than 3 steps, cut it down. Get the simplest version working first — one source, one output format, no edge cases. You can always add complexity later.

```
I want to build a skill called "[name]" that [what it does].

It should:
1. Use [which MCP tools] to [gather what data]
2. Store in SQLite with columns: [what fields]
3. Output [what format]

Include fallback behavior if a source is unavailable.

Create it as skills/[name].md
Don't write the file yet — tell me your plan first.
```

---

## Step 2 — Challenge the plan

Same **plan → challenge → delegate** workflow from Activity 2. Push back:
- "What if the site blocks automated access?"
- "What if there's no data for one of the inputs?"
- "How do you handle pages that take a long time to load?"
- "What if I run this twice — does it duplicate data or update it?"

---

## Step 3 — Delegate

When the plan is solid, use **Shift+Tab** to switch to Auto-Approve mode and tell Vibe to execute.

> If you prefer, you can also relaunch with `vibe --dangerously-skip-permissions` — but you'll lose your current conversation.

---

## Step 4 — Test and iterate

```
/your-skill-name [your input]
```

Run it. Check the output. Tweak the skill file. Run it again. Repeat until it's useful.

**What success looks like:** Your skill runs end-to-end without errors and produces structured output. It doesn't need to be perfect — it needs to be useful enough that you'd run it again tomorrow.

**If `/skill-name` doesn't trigger:** Check that the file is in the `skills/` directory and named correctly (e.g. `skills/meeting-prep.md` → `/meeting-prep`). You can also look at `skills/pricing-compare.md` from Activity 2 as a reference.

**If it errors out:** Try running each step manually in Vibe to isolate the problem. E.g. "use Playwright to visit news.ycombinator.com and show me the top 5 story titles."

---

## If you're stuck

**Checkpoints:**
- **Minute 10:** You should have a plan from Vibe. If not, simplify your prompt — remove one data source or one output requirement.
- **Minute 25:** You should have a skill file created. If not, skip Step 2 and delegate now.
- **Minute 40:** You should have run your skill at least once. If not, try running just one step manually.

**Bail-out option:** If your skill idea isn't working, fall back to this — it uses the same tools you tested in Activity 1 and is guaranteed to work:

```
Build a skill called "page-summary" that takes a URL, fetches the page content,
stores the title and word count in SQLite, and outputs a one-paragraph summary.
Create it as skills/page-summary.md
Don't write the file yet — tell me your plan first.
```

Or go back to `skills/pricing-compare.md` from Activity 2 and extend it — add a new feature, handle a new edge case, or support a new pair of products.

---

## Want to add more MCP servers?

Here are a few that are easy to install (no API key, no signup):

| Server | What it does | Install |
|--------|-------------|---------|
| **Filesystem** | Read/write local files | `npx -y @modelcontextprotocol/server-filesystem` |
| **Git** | Interact with git repos | `uvx mcp-server-git` |
| **Memory** | Persistent key-value store | `npx -y @modelcontextprotocol/server-memory` |

Add them to `~/.vibe/config.toml` following the same format as Activity 1.

Browse more at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

---

## Share Out

At the end of the session, we'll pick **5–6 volunteers** to demo what they built. **2 minutes each.**

Structure:
1. **What does your skill do?** (one sentence)
2. **Run it** — show the output
3. **What problem does it solve?** — why is this useful for you or your team?

No slides needed. Just your terminal.
