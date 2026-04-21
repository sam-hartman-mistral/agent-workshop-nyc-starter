# Activity 2 — Build the Pricing Comparison Skill

**Goal:** Turn the chain from Activity 1 into a reusable skill using plan/challenge/delegate.

---

## What's a skill?

A markdown file that tells Vibe how to do something specific. It lives in `skills/` and you invoke it with `/skill-name`.

You just chained Playwright + Fetch + SQLite manually. Now let's make Vibe write a skill that does it every time.

---

## Step 1 — Set up

```bash
mkdir -p skills
vibe
```

---

## Step 2 — Plan with Vibe

Start a conversation:

```
I want to build a skill called "pricing-compare" that compares
pricing between two SaaS products.

It should:
1. Use Playwright to visit both pricing pages
2. Use Fetch to extract pricing details as markdown
3. Store the pricing tiers in SQLite (provider, tier, price, features)
4. Query SQLite to generate a side-by-side comparison

Output a comparison table + which is cheaper at different team sizes.
Create it as skills/pricing-compare.md.

What's your plan?
```

Read the plan carefully. Don't accept the first version.

---

## Step 3 — Challenge the plan

Push back. Ask hard questions:

- "What if the pricing page loads dynamically with JavaScript?"
- "What if one provider doesn't list prices publicly?"
- "How do you handle different billing periods (monthly vs annual)?"
- "What if the SQLite table already has old data from a previous run?"

Keep going until the plan is solid. This is the part that matters — a good plan means good output.

---

## Step 4 — Delegate

When you're happy with the plan:

```bash
vibe --dangerously-skip-permissions
```

Let Vibe write the skill file. It will create `skills/pricing-compare.md`.

---

## Step 5 — Test it

Invoke your skill:

```
/pricing-compare compare Mistral and OpenAI
```

Does it visit both sites? Extract pricing? Store in SQLite? Output a useful comparison?

---

## Step 6 — Iterate

Try it again with different products:

```
/pricing-compare compare Notion and Confluence
```

Tweak the skill file if needed:
- Change the output format
- Add handling for edge cases you discovered
- Add examples of good output

Each iteration makes it better.

---

**Done?** Move on to [Activity 3](../activity3/README.md) — build your own skill for your org.
