# Notification discipline (Overwatch)

**Ratified:** 2026-07-03 — from LIS SECREP reminder feedback.

Overwatch wants **notifications that help**, not **cadences that train tune-out**. Hermes applies judgment before creating crons or Telegram deliveries.

---

## Default ladder (use in order)

| Step | Channel | When |
|------|---------|------|
| 1 | **Mission Control board** | Almost always — pending work SSOT |
| 2 | **Repo note** (`agents/hermes/content/…`) | Context, checklist, links — no ping |
| 3 | **One-shot cron** | Only when Overwatch asks to *remember* / *don’t forget* **and** a real deadline exists |
| 4 | **Recurring cron** | Repeated *operational* work (lint, cleanup) — not personal reminders |

**Do not** create a cron for every “remember this” unless Overwatch explicitly wants a ping or the deadline is high-stakes and easy to miss.

---

## Cron judgment rules

1. **Default count: one** reminder per user-requested deadline — at the **meaningful moment** (e.g. morning of due day), not a scatter of “helpful” nudges.
2. **Never** add Sat + Sun + Mon + event-day stacks without Overwatch choosing cadence. If unsure, **`clarify`** with 2 options: *board only* vs *one ping on [date/time]*.
3. **Day-of-event** pings are often **low value** when the task was “complete setup by Monday.” Remind at the **commitment deadline**, not the **calendar event**.
4. **Cancel** remaining crons when Overwatch says done (e.g. “scheduled”, “done”).
5. **Prefer `deliver: origin`** for personal reminders; reserve `all` for ops alerts.
6. **Scripts (`no_agent`)** for watchdogs; **agent cron** only when the reminder needs reasoning or links — keep prompts short.

---

## Anti-patterns (what annoyed Overwatch)

- Arbitrary multi-day reminder ladders for a single calendar task
- Notifying on **Thursday** when the ask was **finish by Monday morning**
- Treating “remember” as “schedule three crons”

---

## Good pattern (LIS SECREP example)

- Board task + content note immediately
- **One** cron: **Mon 7:00** — “due this morning: set up intro meeting (meeting Thu)”
- No Thursday meeting-day ping unless Overwatch asks

---

## Hermes checklist before `cronjob create`

- [ ] Board task (or existing quest) already captures the work?
- [ ] Is **one** ping enough? If not, did Overwatch pick the cadence?
- [ ] Is the fire time the **deadline Overwatch cares about**, not a generic “soon”?
- [ ] Will I tell Overwatch what was scheduled (date/time, single vs none)?

---

See also: `agents/_shared/TASK_WORKFLOW_LADDER.md` (board before automation).