# Activity 2 — Build a Skill for Your Org

**Goal:** Use the plan/challenge/delegate loop to build a skill that chains your MCP tools into something useful for your organization.

---

## What's a skill?

A markdown file that tells Vibe how to do something specific. It lives in `skills/` and you invoke it with `/skill-name`.

Your MCP servers are connected. Now tell Vibe how to use them.

---

## Step 1 — Ideate

What workflow would save you or your team time? Some ideas:

- **Company research** — Playwright visits a website, Fetch pulls news, output a 1-page brief
- **Competitive analysis** — compare two products by visiting their sites
- **Documentation audit** — Fetch your docs site, check for broken links and outdated content
- **Meeting prep** — pull LinkedIn profiles and recent news about attendees

Pick one, or come up with your own.

---

## Step 2 — Plan with Vibe

Open Vibe in this directory:

```bash
vibe
```

Start a conversation:

```
I want to build a skill that [describe your workflow].
It should use Playwright to [what], Fetch to [what], and output [format].
What's your plan?
```

Read the plan carefully.

---

## Step 3 — Challenge the plan

Push back. Ask hard questions:

- "What if the page is behind a login wall?"
- "What if Fetch returns garbage HTML?"
- "How should it handle timeouts?"
- "Can you add a fallback for when Playwright can't reach the site?"

Keep going until the plan is solid. This is the part that matters.

---

## Step 4 — Delegate

When you're happy with the plan:

```bash
vibe --dangerously-skip-permissions
```

Let Vibe write the skill file. It will create `skills/your-skill.md` with the workflow, tool chain, and output format.

---

## Step 5 — Test it

Invoke your skill:

```
/your-skill [your input]
```

Does it work? Does it chain the tools correctly? Is the output useful?

---

## Step 6 — Iterate

Tweak the skill:
- Change the output format
- Add error handling instructions
- Add examples of good output

Re-invoke and compare. Each iteration makes it better.

---

## Want a head start?

Use one of the templates:

```bash
cp -r ../templates/code-review/skills/ ./skills/
# Edit skills/code-review.md — look for CUSTOMIZE comments
```

Available templates: `code-review`, `incident-runbook`, `deploy-checklist`, `onboarding-guide`.

---

## Share out

At the end of the session, you'll show what you built:
- What does your skill do?
- Which MCP tools does it use?
- What problem does it solve for your team?

2 minutes each. No pressure.
