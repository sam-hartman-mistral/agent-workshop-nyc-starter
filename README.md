# Mistral AI Agent Workshop — NYC 2026

Your workspace for the workshop. Everything you need is in this README.

## Setup

### 1. Install Vibe

```bash
# Mac / Linux
curl -LsSf https://mistral.ai/vibe/install.sh | bash

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
uv tool install mistral-vibe

# Verify
vibe --version
```

### 2. Get your API key

1. Go to [console.mistral.ai](https://console.mistral.ai)
2. Switch to the **workshop org** (top-left dropdown)
3. API Keys > Create new key > copy it

### 3. Configure Vibe with your API key

```bash
vibe --setup
```

Paste your key when prompted.

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

# Local SQLite database — store, query, compare
[[mcp_servers]]
name = "sqlite"
transport = "stdio"
command = "uvx"
args = ["mcp-server-sqlite", "--db-path", "/tmp/workshop.db"]
```

### After saving

Quit Vibe (`Ctrl+C`) and relaunch it so it picks up the new servers.

### Verify it works

In Vibe, try:

```
Use Fetch to get the content of https://mistral.ai and summarize it in 3 bullets
```

If you see Vibe calling the Fetch tool, you're good.

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

Create `skills/pricing-compare.md`:

```markdown
# pricing-compare

Compare pricing between two SaaS products.

## Workflow
1. Use Playwright to visit both pricing pages
2. Use Fetch to extract pricing details as markdown
3. Store pricing tiers in SQLite (product, tier, price, features)
4. Query SQLite to generate a side-by-side comparison table

## Output format
- Comparison table (tier, price per seat, key features)
- Which is cheaper at 10, 100, 1000 seats
- Key differences summary (3 bullets)
```

### Invoke it

In Vibe:

```
/pricing-compare compare Notion and Confluence
```

---

## Activities

| Activity | What you'll do |
|---|---|
| [Activity 1](./activity1/README.md) | Add MCP servers and test them |
| [Activity 2](./activity2/README.md) | Build the pricing comparison skill (plan/challenge/delegate) |
| [Activity 3](./activity3/README.md) | Build your own skill for your org |

We'll walk through Activities 1 and 2 together. Activity 3 is yours.

---

## Questions?

Raise your hand or ask us — we're walking around.
