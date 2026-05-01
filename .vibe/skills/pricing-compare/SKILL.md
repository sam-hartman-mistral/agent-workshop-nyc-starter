---
name: pricing-compare
description: Compare pricing between two SaaS products using Playwright, Fetch, and SQLite.
user-invocable: true
allowed-tools:
  - playwright_*
  - fetch_*
  - sqlite_*
  - bash
  - read_file
  - write_file
---

# Pricing Compare

Compare pricing tiers between two SaaS products side-by-side.

## Instructions

1. **Get the two products** from the user prompt (e.g. "compare Mistral and OpenAI").

2. **Visit pricing pages** using Playwright:
   - Navigate to each product's pricing page
   - Wait for dynamic content to load
   - If a page fails, fall back to Fetch for static HTML

3. **Extract pricing data** using Fetch:
   - Convert each pricing page to markdown
   - Parse tier names, prices, and key features

4. **Store in SQLite**:
   - Create table: `pricing(provider TEXT, tier TEXT, monthly_price REAL, annual_price REAL, features TEXT)`
   - Drop existing data for these providers before inserting
   - Insert all tiers for both providers

5. **Generate comparison**:
   - Query SQLite for a side-by-side comparison
   - Output a markdown table with per-token or per-seat pricing
   - Add a summary line: which is cheaper and by how much

## Output format

```
| Provider | Tier | Input $/1M tokens | Output $/1M tokens | Context |
|----------|------|--------------------|--------------------|---------|
| ...      | ...  | ...                | ...                | ...     |

Summary: ...
```
