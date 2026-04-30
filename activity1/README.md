# Activity 1 — Connect External Tools

**Goal:** Add MCP servers to Vibe so it can browse the web, fetch pages, and store data.

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

# Local SQLite database — store, query, compare
[[mcp_servers]]
name = "sqlite"
transport = "stdio"
command = "uvx"
args = ["mcp-server-sqlite", "--db-path", "/tmp/workshop.db"]
```

No API keys. No sign up. All free.

---

## Step 3 — Restart Vibe

The config only loads at startup. Quit Vibe (`Ctrl+C`) and run `vibe` again.

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

## Step 6 — Test SQLite

```
Create a SQLite table called "companies" with columns: name, industry, and website.
Insert 3 example companies, then query to show them all.
```

You should see Vibe create the table, insert rows, and return results. Data persists in `/tmp/workshop.db`.

---

## Step 7 — Chain all three

```
Use Playwright to visit https://mistral.ai/pricing and https://openai.com/pricing.
Use Fetch to extract the pricing details from both pages.
Store the pricing tiers in a SQLite table (provider, tier, price, features).
Then query the table to show a side-by-side comparison.
```

When tools chain together, things get interesting.

---

**Done?** Move on to [Activity 2](../activity2/README.md) — build a skill that uses these tools.
