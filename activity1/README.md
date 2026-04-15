# Activity 1 — Your First Skill

**Goal:** Write a `/pr-reviewer` skill and invoke it in Vibe.

A skill is a markdown file that tells an agent how to behave. That's it.

---

## Step 1 — Create the skill file

Create a file called `pr-reviewer.md` in a `skills/` folder:

```
mkdir skills
```

Paste this into `skills/pr-reviewer.md`:

```markdown
# pr-reviewer

You are a specialized code review agent.

When reviewing a pull request:
- Check for missing or insufficient tests
- Flag any hardcoded secrets or environment variables
- Suggest naming improvements
- Note security concerns (SQL injection, XSS, etc.)

Output format: bulleted list grouped by severity.
  CRITICAL · HIGH · MEDIUM · LOW

Do not attempt to fix issues — only report them.
```

---

## Step 2 — Invoke it in Vibe

Open Vibe in this directory:

```bash
vibe
```

Then type:

```
/pr-reviewer review the changes in this repo
```

Vibe will load the skill and apply it.

---

## Step 3 — Iterate

Try changing the skill:
- Add a rule specific to your team's standards
- Change the output format
- Add an example of what a "CRITICAL" issue looks like

Re-invoke it and see the difference.

---

**Done?** Move on to [Activity 2](../activity2/README.md).
