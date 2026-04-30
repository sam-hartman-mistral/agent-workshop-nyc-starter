# Activity 3 — Build Your Own Skill

**Goal:** Create a skill that solves a real problem for your organization, using your own MCP servers.

---

## Step 1 — Ideate

Think about what would save you or your team time. Some ideas:

- **Company research** — visit a company's site, pull recent news, store findings, output a 1-page brief before a meeting
- **Competitive analysis** — compare two products by visiting their sites, extracting features, storing in SQLite
- **Documentation audit** — fetch your docs site, check for outdated content, output a list of pages to update
- **Meeting prep** — pull attendee profiles and recent news, store history across meetings
- **Dashboard builder** — scrape data sources, store in SQLite, generate a summary report

You can also add new MCP servers that are useful for your workflow. Browse [MCP servers](https://github.com/modelcontextprotocol/servers) for ideas.

---

## Step 2 — Plan with Vibe

```bash
vibe
```

```
I want to build a skill that [describe your workflow].
It should use [which MCP tools] to [do what].
Output [what format].
What's your plan?
```

---

## Step 3 — Challenge the plan

Push back hard:
- "What if [edge case]?"
- "How do you handle [failure mode]?"
- "What's the fallback if [tool] can't reach the site?"

---

## Step 4 — Delegate

```bash
vibe --dangerously-skip-permissions
```

---

## Step 5 — Test and iterate

```
/your-skill [your input]
```

Tweak, re-invoke, repeat until the output is useful.

---

## Share out

At the end of the session, you'll show what you built:
- What does your skill do?
- Which MCP tools does it use?
- What problem does it solve for your team?

2 minutes each. No pressure.
