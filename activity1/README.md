# Activity 1 — Plan It, Challenge It, Delegate It

**Goal:** Use Vibe the way you'd work with a strong engineer — align on a plan, then let them execute.

---

## The feature

We're going to add **task priorities** to the sample app:
- A `priority` field (HIGH, MEDIUM, LOW) on every task
- Default to MEDIUM when not specified
- Filter tasks by priority on `GET /tasks?priority=HIGH`

---

## Step 1 — Plan with Vibe

Open Vibe in the sample-app directory:

```bash
cd sample-app
vibe
```

Start a conversation:

```
I want to add a priority field to tasks. HIGH, MEDIUM, LOW.
Users should be able to filter by priority on GET /tasks.
What's your plan?
```

Read the plan. Don't accept the first version.

---

## Step 2 — Challenge the plan

Push back. Ask hard questions:

- "What happens if someone sends an invalid priority?"
- "Should the filter support multiple priorities at once?"
- "What about existing tasks that don't have a priority?"
- "What tests are you going to write?"

Keep going until the plan is solid. This is the part that matters — a good plan means good output.

---

## Step 3 — Delegate

When you're happy with the plan:

```bash
vibe --dangerously-skip-permissions
```

This lets Vibe execute without asking for permission at each step. It will:
- Edit the model
- Update the endpoints
- Write tests
- Run them

Go get coffee. Or watch it work — your call.

---

## Step 4 — Review the result

When it's done:

```bash
git diff
```

Look at what it built:
- Did it follow the plan you agreed on?
- Do the tests pass? (`pytest`)
- Would you approve this PR?

---

## Step 5 — Try your own feature

Pick something else to add:
- Due dates on tasks
- A `/tasks/stats` endpoint that returns counts by status
- Bulk operations (mark multiple tasks complete at once)

Go through the same loop: plan, challenge, delegate, review.

---

**Done?** Move on to [Activity 2](../activity2/README.md).
