# Activity 1 — Connect External Tools

**Goal:** Add MCP servers to Vibe so it can browse the web, fetch pages, and store data.

**Time:** ~20 minutes

---

## Step 1 — Find your config file

Vibe's config lives at:

```
# Mac / Linux
~/.vibe/config.toml

# Windows
%USERPROFILE%\.vibe\config.toml
```

If it doesn't exist yet:

```bash
mkdir -p ~/.vibe
touch ~/.vibe/config.toml
```

Open it:

```bash
# Mac
open -e ~/.vibe/config.toml

# Linux
nano ~/.vibe/config.toml

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
args = ["mcp-server-sqlite", "--db-path", "/tmp/workshop.db"]
```

Save and close the file. No API keys needed — all three are free.

---

## Step 3 — Restart Vibe

Config only loads at startup. Quit Vibe (`Ctrl+C`) and relaunch:

```bash
vibe
```

---

## Step 4 — Test Fetch

Type this in Vibe:

```
Use Fetch to get the content of https://mistral.ai and summarize it in 3 bullets.
```

You should see Vibe call the `mcp_fetch` tool. If it returns a summary, Fetch is working.

---

## Step 5 — Test SQLite

```
Create a SQLite table called "companies" with columns: name, industry, and website.
Insert 3 example companies, then query to show them all.
```

You should see Vibe create the table, insert rows, and return results.

---

## Step 6 — Test Playwright

```
Use Playwright to visit https://mistral.ai and describe what you see on the page.
```

Vibe will launch a browser, navigate to the page, and describe the content. This one can take a few seconds.

> **If Playwright fails:** Run `npx playwright install chromium` in your terminal, then restart Vibe.

---

## Step 7 — Chain all three

Now the fun part — use all three tools together:

```
Visit https://mistral.ai/pricing using Playwright.
Use Fetch to extract the pricing details.
Store the plans in a SQLite table with columns: plan_name, price, features.
Then query the table to show all plans.
```

When tools chain together, things get interesting. This is the workflow we'll turn into a skill in Activity 2.

---

## What you should have

- [ ] Config file with 3 MCP servers
- [ ] Fetch working (can retrieve web content)
- [ ] SQLite working (can create tables and query data)
- [ ] Playwright working (can browse websites)
- [ ] All three chained together successfully

**Done?** Move on to [Activity 2](../activity2/README.md) — build a skill that automates this workflow.
