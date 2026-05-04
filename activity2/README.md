# Activity 2 — Build the Pricing Comparison Skill

**Goal:** Turn the chain from Activity 1 into a reusable skill using the **plan → challenge → delegate** workflow.

**Time:** ~50 minutes

---

## What's a skill?

A markdown file called `SKILL.md` that teaches Vibe how to do something specific. It lives in `.vibe/skills/<skill-name>/SKILL.md` in your project. When Vibe sees a skill file, it learns that capability automatically.

Here's the basic structure:

```markdown
---
name: my-skill-name
description: One-line description of what it does.
user-invocable: true
---

# My Skill Name

## Steps
1. First, do X using [tool]
2. Then do Y
3. Finally, output Z

## Output format
Describe what the result should look like.
```

You invoke a skill by typing `/my-skill-name` in Vibe. That's a **slash command** — Vibe reads the matching SKILL.md file and follows its instructions.

You just chained Playwright + Fetch + SQLite manually. Now let's teach Vibe to do it every time.

---

## Step 1 — Launch Vibe from the project directory

A skeleton skill is already in the repo at `.vibe/skills/pricing-compare/SKILL.md`. Just launch Vibe from the project root:

```bash
cd agent-workshop-nyc-starter
vibe
```

---

## Step 2 — Plan with Vibe (plan → challenge → delegate)

This is the core workflow for working with coding agents. You'll use it in every activity:

1. **Plan** — Ask the agent to propose a plan. Don't let it code yet.
2. **Challenge** — Push back on the plan. Find edge cases, ask hard questions.
3. **Delegate** — When the plan is solid, let the agent execute.

Copy-paste this prompt into Vibe:

```
I want to build a skill called "pricing-compare" that compares
pricing between two SaaS products.

It should:
1. Use Playwright to visit both pricing pages
2. Use Fetch to extract pricing details as markdown
3. Store the pricing tiers in SQLite (provider, tier, price, features)
4. Query SQLite to generate a side-by-side comparison

Output a comparison table + which is cheaper at different team sizes.
Create it as .vibe/skills/pricing-compare/SKILL.md

Don't write the file yet — tell me your plan first.
```

Read the plan carefully. **Don't accept the first version.**

---

## Step 3 — Challenge the plan

Push back. Ask hard questions:

- "What if the pricing page loads dynamically with JavaScript — should you use Playwright or Fetch?"
- "What if one provider doesn't list prices publicly?"
- "How do you handle different billing periods — monthly vs annual?"
- "What if the SQLite table already has old data from a previous run? Should you drop it first?"
- "What happens if Playwright times out on a page?"

Keep going until the plan handles edge cases. This is the part that matters — **a good plan means good output**.

---

## Step 4 — Delegate

When you're happy with the plan, tell Vibe to execute it.

Use **Shift+Tab** to cycle to **Auto-Approve** mode (you'll see the indicator change in the bottom bar). Then say:

```
Go ahead and write the skill file.
```

Vibe will create `.vibe/skills/pricing-compare/SKILL.md`.

> **Tip:** You can also launch Vibe with `vibe --dangerously-skip-permissions` for full auto-approve from the start. But if you do this mid-conversation, you'll lose your current session — so Shift+Tab is usually better.

---

## Step 5 — Test it

> **Note:** If Vibe was already running when you created the skill, quit it (`Ctrl+C`) and relaunch it. Vibe only loads skills at startup.

Invoke your skill:

```
/pricing-compare compare Mistral and OpenAI
```

Watch what happens. Does it:
- [ ] Visit both pricing pages?
- [ ] Extract pricing details?
- [ ] Store data in SQLite?
- [ ] Output a useful comparison table?

### What success looks like

You should get something like:

```
| Provider | Model         | Input $/1M tokens | Output $/1M tokens | Context |
|----------|---------------|--------------------|--------------------|---------|
| Mistral  | Small         | $0.10              | $0.30              | 32k     |
| Mistral  | Large         | $2.00              | $6.00              | 128k    |
| OpenAI   | GPT-4o mini   | $0.15              | $0.60              | 128k    |
| OpenAI   | GPT-4o        | $2.50              | $10.00             | 128k    |
| ...      | ...           | ...                | ...                | ...     |

Summary: Mistral is cheaper at every tier. Small vs 4o-mini saves ~30%.
```

The exact numbers will vary (pricing pages change!) — the point is that Vibe chained all three tools automatically.

---

## Step 6 — Iterate

Try it with different products:

```
/pricing-compare compare Notion and Confluence
```

Tweak the skill file if needed:
- Open `.vibe/skills/pricing-compare/SKILL.md` in your editor
- Change the output format
- Add handling for edge cases you discovered
- Add examples of what good output looks like

Each iteration makes the skill better.

---

**Done?** Move on to [Activity 3](../activity3/README.md) — build your own skill.
