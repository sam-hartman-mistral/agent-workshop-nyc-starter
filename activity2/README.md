# Activity 2 — Teach It Your Standards

**Goal:** You just used Vibe bare. Notice how you kept repeating your standards? Write them once so the agent already knows.

---

## Step 1 — Notice the pattern

In Activity 1 you probably told Vibe things like:
- "Make sure you validate inputs"
- "Use our error response format"
- "Don't forget tests"

Every time. What if it already knew?

---

## Step 2 — Write a skill

```bash
mkdir skills
```

Create `skills/code-review.md`:

```markdown
# code-review

You are a senior code reviewer for our team.

## Standards
- All endpoints must have input validation
- No secrets or hardcoded credentials
- Error responses must use our ErrorResponse schema
- Tests required for any new endpoint
- All functions need docstrings

## Output format
Bulleted list grouped by severity:
  CRITICAL / HIGH / MEDIUM / LOW

Cite file and line number for each finding.
Do not fix issues -- only report them.
```

Customize the standards section — what does your team actually care about?

---

## Step 3 — Try it skilled

Run Vibe from the repo root and invoke the skill:

```bash
cd ..
vibe
```

```
/code-review review the sample-app/ directory
```

Compare this output to the generic reviews from Activity 1. Same agent, better results.

---

## Step 4 — Iterate

Try changing the skill:
- Add a rule specific to your team (naming conventions, error patterns, etc.)
- Change the output format
- Add an example of what a "CRITICAL" finding looks like

Re-invoke and see how the output changes.

---

**Done?** Head to [Activity 3](../activity3/README.md) and build something for your org.
