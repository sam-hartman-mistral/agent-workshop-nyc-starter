# Activity 1 — Connect External Tools

**Goal:** Add MCP servers to Vibe so it can browse the web, fetch pages, and store data.

**Time:** ~25 minutes

## Step 1 — Launch Vibe

Three MCP servers (Playwright, Fetch, SQLite) are already configured in the repo's `.vibe/config.toml`. Just launch Vibe from the project root:

```bash
cd agent-workshop-nyc-starter
vibe
```

You should see `3 MCP servers` in the startup banner. If you see warnings about MCP servers failing to connect, raise your hand.

---

## Step 2 — Test Fetch

Type this in Vibe:

```
Use Fetch to get the content of https://mistral.ai and summarize it in 3 bullets.
```

You should see Vibe call the Fetch server and return a summary. If it works, Fetch is connected.

---

## Step 3 — Test SQLite

```
Create a SQLite table called "companies" with columns: name, industry, and website.
Insert 3 example companies, then query to show them all.
```

You should see Vibe create the table, insert rows, and return results. The data is saved to `workshop.db` in your project folder.

---

## Step 4 — Test Playwright

```
Use Playwright to visit https://mistral.ai and describe what you see on the page.
```

Vibe will launch a headless browser, navigate to the page, and describe the content. This one can take a few seconds — that's normal.

> **If Playwright fails:** Run `npx playwright install chromium` in your terminal, then restart Vibe.

---

## Step 5 — Chain all three

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
