# Start Here - Guided Mode

`using-hse-skills` is the catalog front door. Use it when you know the HSE job you need to do, but you are not sure which skill name, pack, or sequence fits.

> Everything these skills produce is a **draft to assist a qualified professional - not a finished or approved document.** Every output **must be reviewed and signed off by a competent person** before you rely on it. See [`DISCLAIMER.md`](../DISCLAIMER.md).

---

## What to run first

```text
/using-hse-skills
```

It ships in `hse-core` and `hse-all`, so the core install and the all-skills install both give new users the router.

## What it is

- The catalog front door for the v1.2 skill manual.
- A router for ambiguous, meta, or multi-deliverable HSE tasks.
- A way to describe the job once and carry the captured context forward.
- A recommender that names one skill or an ordered chain and explains why.

## What it is not

- Not a risk assessment.
- Not a toolbox talk.
- Not a regulatory or HSE deliverable generator by itself.
- Not required when you already know the exact artifact skill you want.

## Typical use patterns

- "I am not sure which assessment is needed."
- "Where do I start with HSE for this site?"
- "What is needed for a new contractor job?"
- "Give me an overview of the toolbox."
- "This job needs several deliverables: risk assessment, permit, toolbox talk."
- "I know the task, but not what this plugin calls the right skill."

## When to skip it

- Direct "write a toolbox talk for this roof work" requests can go straight to [`toolbox-talk`](Core#toolbox-talk).
- Direct "do a risk assessment for this tank clean" requests can go straight to [`risk-assessment`](Core#risk-assessment).
- Direct "investigate this incident" requests can go straight to [`incident-investigation`](Core#incident-investigation).

## How routing works

1. Captures intent, requirement, success criteria, jurisdiction, industry, and exposure.
2. Asks only the minimum disambiguating questions needed to choose the right path.
3. Echoes back captured facts so you can correct the setup before handoff.
4. Reads the generated skill index instead of relying on a hand-written list.
5. Recommends one skill or an ordered chain with a WHY for each recommendation.
6. Pauses at a confirm-or-refine gate before running the first selected skill.
7. De-identifies captured facts and prepares a context capsule or run sheet for multi-step chains.
8. Hands off into the first skill with the captured context already carried forward.

## Examples

### 30-second single-skill route

> **You:** I need to brief the team before they clean out tank T-402 tomorrow.
>
> **Router:** That is a pre-task crew briefing. The best fit is `toolbox-talk` because you need a short supervisor-led briefing before the job. I need two quick facts before handoff: which crew is attending, and is this a confined-space entry?
>
> **You:** Maintenance crew, and yes, confined-space entry.
>
> **Router:** Got it. I will hand off to `toolbox-talk` with the tank, crew, date, and confined-space context already captured.

### Multi-skill chain route

> **You:** We have a contractor starting hot work and confined-space cleaning on a construction site next week. I need the paperwork and briefing.
>
> **Router:** This is a chain, not one artifact. Start with `risk-assessment` for the task hazards, then `permit-to-work` for the hot-work and confined-space controls, then `toolbox-talk` for the crew briefing. I will carry the site, contractor, work scope, date, and known high-risk activities through the chain.

## Links

- Back to the full manual: [Home](Home)
- Core router card: [using-hse-skills](Core#using-hse-skills)
- Install instructions: [README](../README.md#install-in-30-seconds)
- Getting Started: [`USER_MANUAL.md`](../docs/USER_MANUAL.md)
- End-to-end journeys: [`USER_JOURNEYS.md`](../docs/USER_JOURNEYS.md)
