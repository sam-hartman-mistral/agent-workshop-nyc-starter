# Mistral AI Agent Workshop — NYC 2026

Your workspace for the workshop. Everything you need is in this README.

## Setup

### 1. Install Vibe

Pick one:

- **VSCode** (recommended): Extensions > search "Mistral Vibe" > Install
- **CLI**: `curl -LsSf https://mistral.ai/vibe/install.sh | bash`

### 2. Get your API key

1. Go to [console.mistral.ai](https://console.mistral.ai)
2. Switch to the **workshop org** (top-left dropdown)
3. API Keys > Create new key > copy it

### 3. Configure Vibe with your API key

- **VSCode**: open Vibe panel > paste key when prompted
- **CLI**: `vibe --setup`

### 4. Clone this repo

```bash
git clone https://github.com/sam-hartman-mistral/agent-workshop-nyc-starter
cd agent-workshop-nyc-starter
```

---

## Adding MCP Servers

MCP servers give Vibe access to external tools. No API keys needed for these.

### Where is the config file?

```
~/.vibe/config.toml
```

If it doesn't exist yet, create it:

```bash
mkdir -p ~/.vibe
touch ~/.vibe/config.toml
```

### Copy-paste this config

Open `~/.vibe/config.toml` and paste:

```toml
# Browser automation — visit pages, click, take screenshots
[[mcp_servers]]
name = "playwright"
transport = "stdio"
command = "npx"
args = ["-y", "@playwright/mcp"]

# Fetch any URL as clean markdown
[[mcp_servers]]
name = "fetch"
transport = "stdio"
command = "uvx"
args = ["mcp-server-fetch"]

# Read/write files outside your project directory
[[mcp_servers]]
name = "filesystem"
transport = "stdio"
command = "npx"
args = ["-y", "@anthropic-ai/mcp-filesystem", "/tmp"]
```

### After saving

Restart Vibe so it picks up the new servers:

- **VSCode**: close and reopen the Vibe panel
- **CLI**: quit and relaunch `vibe`

### Verify it works

In Vibe, try:

```
Use Playwright to take a screenshot of https://mistral.ai and save it to /tmp/screenshot.png
```

If you see Vibe calling the Playwright tool, you're good.

---

## Adding Skills

A skill is a markdown file that tells Vibe how to do something specific.

### Where do skills live?

```
skills/your-skill-name.md
```

Create the directory:

```bash
mkdir -p skills
```

### Example skill

Create `skills/company-brief.md`:

```markdown
# company-brief

Research a company and produce a 1-page brief.

## Workflow
1. Use Playwright to visit the company website
2. Use Fetch to pull recent news articles
3. Summarize into a structured brief

## Output format
- Company name and what they do (1 sentence)
- Key products/services
- Recent news (3 bullets)
- Team size and funding (if available)
```

### Invoke it

In Vibe:

```
/company-brief research Stripe
```

---

## Activities

| Activity | What you'll do |
|---|---|
| [Activity 1](./activity1/README.md) | Add MCP servers and test them |
| [Activity 2](./activity2/README.md) | Build a skill for your org using plan/challenge/delegate |

We'll walk through Activity 1 together. Activity 2 is yours.

---

## Templates

Starter skill templates to customize for your org:

```
templates/code-review/       Review PRs using your team's standards
templates/incident-runbook/  Generate on-call runbooks
templates/deploy-checklist/  Pre-deploy verification
templates/onboarding-guide/  Help new hires understand a codebase
```

Quick start:

```bash
cp -r templates/code-review/skills/ ./skills/
# Edit skills/code-review.md — look for CUSTOMIZE comments
```

---

## Questions?

Raise your hand or ask us — we're walking around.
