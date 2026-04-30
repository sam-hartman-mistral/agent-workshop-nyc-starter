# Mistral AI Agent Workshop — NYC 2026

Your workspace for the workshop. Follow the setup below, then jump into the activities.

## Prerequisites

You need these installed before we start:

| Tool | Check | Install if missing |
|------|-------|--------------------|
| **Node.js** (v18+) | `node --version` | [nodejs.org](https://nodejs.org) |
| **Git** | `git --version` | [git-scm.com](https://git-scm.com) |

Vibe's installer also sets up `uv` and `uvx` (needed for some MCP servers). If you already have these, you're good.

---

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

### 5. Pre-install Playwright browser

This downloads Chromium so you don't have to wait during the workshop:

```bash
npx playwright install chromium
```

---

## Activities

| # | Activity | Time | What you'll do |
|---|----------|------|----------------|
| 1 | [Add MCP servers](./activity1/README.md) | ~25 min | Connect Vibe to Playwright, Fetch, and SQLite |
| 2 | [Build the pricing skill](./activity2/README.md) | ~50 min | Turn the MCP chain into a reusable skill |
| 3 | [Build your own](./activity3/README.md) | ~60 min | Create a skill that solves a real problem for you |

We'll walk through Activities 1 and 2 together. Activity 3 is yours.

---

## Troubleshooting

**`npx: command not found`**
You need Node.js. Install it from [nodejs.org](https://nodejs.org), then restart your terminal.

**`uvx: command not found`**
Vibe's installer should have set this up. Try restarting your terminal. If it still fails:
```bash
curl -LsSf https://astral.sh/uv/install.sh | bash
```

**Playwright won't launch / browser error**
Run `npx playwright install chromium` to download the browser binary.

**Vibe doesn't see MCP servers after editing config**
You must quit Vibe (`Ctrl+C`) and relaunch it. Config only loads at startup.

**Config file location on Windows**
Use `%USERPROFILE%\.vibe\config.toml` instead of `~/.vibe/config.toml`.

**Something else?**
Raise your hand — we're walking around.
