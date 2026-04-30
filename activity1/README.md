# Activity 1 — Connect External Tools

**Goal:** Add MCP servers to Vibe so it can browse the web, fetch pages, and store data.

**Time:** ~25 minutes

---

## Step 1 — Find your config file

Vibe's config lives at:

```
# Mac / Linux
~/.vibe/config.toml

# Windows
%USERPROFILE%\.vibe\config.toml
```

If it doesn't exist yet, run this in your terminal (creates the directory and an empty config file):

```bash
mkdir -p ~/.vibe
touch ~/.vibe/config.toml
```

Open it in any text editor:

```bash
# Mac (VS Code if you have it, otherwise nano)
code ~/.vibe/config.toml || nano ~/.vibe/config.toml

# Windows
notepad %USERPROFILE%\.vibe\config.toml
```

---

## Step 2 — Add MCP servers

Paste this into the config file:

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
args = ["mcp-server-sqlite", "--db-path", "workshop.db"]
```

Save and close the file. No API keys needed — all three are free.

> **Note:** `npx` comes with Node.js. `uvx` comes with `uv`, which Vibe's installer sets up. If either is missing, check the troubleshooting section in the main README.

---

## Step 3 — Restart Vibe

Config only loads at startup. Quit Vibe (`Ctrl+C` — that's **Control**, not Command) and relaunch:

```bash
cd agent-workshop-nyc-starter
vibe
```

You should see Vibe start without errors. If you see warnings about MCP servers failing to connect, check that your config file is saved correctly.

---

## Step 4 — Test Fetch

Type this in Vibe:

```
Use Fetch to get the content of https://mistral.ai and summarize it in 3 bullets.
```

You should see Vibe call the Fetch server and return a summary. If it works, Fetch is connected.

---

## Step 5 — Test SQLite

```
Create a SQLite table called "companies" with columns: name, industry, and website.
Insert 3 example companies, then query to show them all.
```

You should see Vibe create the table, insert rows, and return results. The data is saved to `workshop.db` in your project folder.

---

## Step 6 — Test Playwright

```
Use Playwright to visit https://mistral.ai and describe what you see on the page.
```

Vibe will launch a headless browser, navigate to the page, and describe the content. This one can take a few seconds — that's normal.

> **If Playwright fails:** Run `npx playwright install chromium` in your terminal, then restart Vibe.

---

## Step 7 — Chain all three

Now the fun part — use all three tools together:

```
Use Playwright to visit https://mistral.ai/pricing and extract the pricing plans.
Store each plan in a SQLite table with columns: plan_name, price, features.
Then query the table and show me a summary of all plans.
```

When tools chain together, things get interesting. This is the workflow we'll turn into a reusable skill in Activity 2.

---

## Checklist

- [ ] Config file with 3 MCP servers
- [ ] Fetch working (can retrieve web content)
- [ ] SQLite working (can create tables and query data)
- [ ] Playwright working (can browse websites)
- [ ] All three chained in one prompt

**All boxes checked? Raise your hand so we know you're ready.** Then move on to [Activity 2](../activity2/README.md).
