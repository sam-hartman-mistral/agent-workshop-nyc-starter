# Activity 1 — Connect External Tools

**Goal:** Add MCP servers to Vibe so it can browse the web, fetch pages, and access files.

---

## Step 1 — Find your config file

```bash
# macOS / Linux
~/.vibe/config.toml

# If it doesn't exist:
mkdir -p ~/.vibe
touch ~/.vibe/config.toml
```

Open the file in your editor.

---

## Step 2 — Add MCP servers

Paste this into `~/.vibe/config.toml`:

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

No API keys. No sign up. All free.

---

## Step 3 — Restart Vibe

The config only loads at startup:

- **VSCode**: close and reopen the Vibe panel
- **CLI**: quit (`Ctrl+C`) and run `vibe` again

---

## Step 4 — Test Playwright

```
Use Playwright to visit https://mistral.ai and describe what you see.
```

You should see Vibe call the `playwright` tool. If it works, Vibe now has a browser.

---

## Step 5 — Test Fetch

```
Use Fetch to get the content of https://news.ycombinator.com and tell me the top 3 stories.
```

Fetch pulls web pages as clean markdown — useful for reading docs, articles, APIs.

---

## Step 6 — Try chaining them

```
Use Playwright to screenshot https://mistral.ai, save it to /tmp/mistral.png,
then use Fetch to get the page content and summarize it in 3 bullets.
```

When tools chain together, things get interesting.

---

**Done?** Move on to [Activity 2](../activity2/README.md) — build a skill that uses these tools.
