# Activity 2 — Wire a Sub-Agent

**Goal:** Turn your skill into a named sub-agent that can be invoked on demand.

---

## What's a sub-agent?

A sub-agent is an agent with a fixed role, a set of tools, and a goal.
You define it in a markdown file — same format as a skill, with a bit more structure.

---

## Step 1 — Create the sub-agent file

Create `agents/pr-agent.md`:

```
mkdir agents
```

```markdown
# pr-agent

## Role
You are a senior code reviewer. You are thorough, direct, and specific.

## Behavior
When invoked, load the `/pr-reviewer` skill from skills/pr-reviewer.md
and apply it to the current working directory.

After reviewing, summarize:
1. The top 3 issues (with file + line if possible)
2. A one-sentence overall assessment
3. Whether you would approve or request changes

## Tools
- Read files
- Run git diff to see recent changes
```

---

## Step 2 — Invoke the sub-agent

```bash
vibe --agent agents/pr-agent.md
```

Or from inside a running Vibe session:

```
/agent agents/pr-agent.md review the last commit
```

---

## Step 3 — Extend it

Try adding:
- A rule to check for your team's specific patterns
- An output section that creates a review comment draft
- A second skill loaded alongside the first

---

**Done?** Head to [Activity 3](../activity3/README.md) and build something for your org.
