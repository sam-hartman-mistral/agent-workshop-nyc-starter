# Activity 3 — Build Something for Your Org

**Pick a template, customize it, run it.**

---

## Quick start

```bash
# Pick a template
cp -r ../templates/code-review ./my-skill

# Edit the skill file -- add your org's standards
# Look for the "CUSTOMIZE" comments

# Run it
vibe
/code-review review the sample-app/ directory
```

---

## Available templates

| Template | What it does |
|---|---|
| `templates/code-review/` | Review PRs using your team's standards |
| `templates/incident-runbook/` | Generate on-call runbooks from alerts |
| `templates/deploy-checklist/` | Pre-deploy verification for your stack |
| `templates/onboarding-guide/` | Help new hires understand a codebase |

Each template has `<!-- CUSTOMIZE -->` comments showing where to add your org's specifics.

Or start from scratch — a skill is just a markdown file.

---

## Try it on real code

If you have time, clone one of your own repos and run your skill against it:

```bash
git clone <your-repo-url> my-repo
vibe
/your-skill review the my-repo/ directory
```

---

## Share out

At the end of the session, you'll show what you built:
- What does your skill/agent do?
- What problem does it solve for your team?
- What would you build next?

2 minutes each. No pressure.
