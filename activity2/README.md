# Activity 2 — Build the Pricing Comparison Skill

**Goal:** Turn the chain from Activity 1 into a reusable skill using the plan/challenge/delegate workflow.

**Time:** ~40 minutes

---

## What's a skill?

A markdown file that tells Vibe how to do something specific. It lives in the `skills/` directory of your project and you invoke it with `/skill-name`.

You just chained Playwright + Fetch + SQLite manually. Now let's teach Vibe to do it every time.

---

## Step 1 — Set up the skills directory

```bash
cd agent-workshop-nyc-starter
mkdir -p skills
vibe
```

---

## Step 2 — Plan with Vibe

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
Create it as skills/pricing-compare.md

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

When you're happy with the plan, tell Vibe to execute it. You can either:

**Option A:** Use Shift+Tab to cycle to Auto-Approve mode, then say "go ahead and write the skill file."

**Option B:** Relaunch in autonomous mode:
```bash
vibe --dangerously-skip-permissions
```

Vibe will create `skills/pricing-compare.md`.

---

## Step 5 — Test it

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
| Provider | Tier      | Price        | Key Features              |
|----------|-----------|--------------|---------------------------|
| Mistral  | Free      | $0           | Rate-limited, community   |
| Mistral  | Team      | $25/user/mo  | Higher limits, support    |
| OpenAI   | Free      | $0           | GPT-4o mini, limited      |
| OpenAI   | Plus      | $20/user/mo  | GPT-4o, higher limits     |
| ...      | ...       | ...          | ...                       |

At 10 users: Mistral Team = $250/mo vs OpenAI Plus = $200/mo
At 100 users: ...
```

The exact numbers don't matter — the point is that Vibe chained all three tools automatically.

---

## Step 6 — Iterate

Try it with different products:

```
/pricing-compare compare Notion and Confluence
```

Tweak the skill file if needed:
- Open `skills/pricing-compare.md` in your editor
- Change the output format
- Add handling for edge cases you discovered
- Add examples of what good output looks like

Each iteration makes the skill better.

---

**Done?** Move on to [Activity 3](../activity3/README.md) — build your own skill.
