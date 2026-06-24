<!-- KB-DATA-BBS-METRICS -->
# Behaviour-based safety metrics — percent-safe / participation / trend (defined + guarded)

**Fragment ID:** `KB-DATA-BBS-METRICS`
**What this is:** the **defined-metric reference** the `bbs-program-designer` skill computes its
observation-programme indicators from. Each metric carries its **formula** and the **non-punitive,
small-cell** guardrail. The method (ABC + observation-card design) lives in `KB-SNIP-BBS-METHOD`.
**What this is NOT:** a worker-ranking score. None of these metrics is ever used to rank, blame, or
discipline a nameable individual. Observation data is de-identified by design.

> Source: applied behaviour analysis (ABC) / behaviour-based safety method; DuPont STOP and Krause/BST peer-observation as exemplars · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Defined metrics (each with formula + guardrail)

| Metric | Formula | Guardrail |
|---|---|---|
| **Percent-safe** | (safe behaviours observed ÷ total behaviours observed) × 100 | trend it; **never** use to rank/blame a named individual. |
| **Participation rate** | (observers active in period ÷ trained observer pool) × 100 | a programme metric, not a worker metric. |
| **Trend** | period-over-period movement of percent-safe **by behaviour category** | never by person; trend categories, not people. |

## Small-cell suppression guardrail (mandatory)

- **`<5` small-cell suppression on any team/crew breakdown** — a percent-safe computed over a 4-person
  crew is **suppressed**; it could identify whose behaviour was observed.
- All reporting is **non-punitive** and **role-labelled / anonymous** by default.
- A team breakdown that survives suppression still carries **no named individual** — categories and
  roles only.

## How the skill uses this fragment

`bbs-program-designer` computes percent-safe, participation, and category trend from this fragment,
applies the `<5` small-cell suppression to every breakdown, and routes at-risk categories to
hierarchy-ranked system fixes (via `controls`) — never to the individual, never to discipline.
