# Methodology — regulatory-returns

The domain method this skill applies: **determine → form → deadline → prepare**, per
jurisdiction, grounded in `KB-SNIP-RETURNS-METHOD` and `KB-DATA-RECORDABILITY-TESTS`
(every test cited to its `source`+`year`). One skill, a jurisdiction branch; the
India branch **defers entirely to `hse-india`** and never mints a national form number.

> **Disclaimer.** Decision-support only. A statutory return must be reviewed and signed
> off by a competent person before filing. Not legal advice.

## 0. De-identify FIRST (always)

A statutory return holds injured-person identity **by law**. Before any analysis, run
the `deid` block + `references/deid-checklist.md`: detect and list every identifier;
distinguish the **legally-required submission** (named, access-controlled) from every
**internal / shared / working copy** (role-labelled); apply `<5` suppression to any
aggregated summary; keep the re-identification key **separate, never embedded**.

## 1. Resolve the jurisdiction (intake Q1)

The jurisdiction selects the test, the form set, and the deadline rule. **Never assert
a deadline, a form, or a recordable/reportable verdict without it.**

| Jurisdiction | Test source | Form set |
|---|---|---|
| USA — OSHA 29 CFR 1904 | `KB-REG-US-OSHA` + `KB-DATA-RECORDABILITY-TESTS` | 300 (log) · 300A (annual summary) · 301 (incident report) · 1904.41 electronic |
| UK — RIDDOR 2013 | `KB-REG-UK-HSWA` + `KB-DATA-RECORDABILITY-TESTS` | specified injury · over-7-day · disease · dangerous occurrence |
| EU — member-state | `KB-REG-EU-OSH` | member-state equivalent (cite the national instrument) |
| India | **DEFERS to `hse-india`** — see §5 | resolved by `hse-india`; **never a national form number** |

## 2. Apply the recordability / reportability test

Run the cited decision logic in `KB-DATA-RECORDABILITY-TESTS` against the incident
facts (Q3). State the verdict **with the test cited**; flag `[GAP]` for a missing fact —
never assume to force a "yes" or a "no".

**OSHA 1904 recordability decision tree:**

1. Is the case **work-related** (1904.5)? If no → not recordable.
2. Is it a **new case** (1904.6)? A continuation of a prior recorded case is not a new entry.
3. Does it meet a **general recording criterion** (1904.7) — death, days away from work,
   restricted work / job transfer, medical treatment **beyond first aid**, loss of
   consciousness, or a significant diagnosed injury/illness? **First-aid-only is NOT
   recordable** — a first-aid case logged as recordable is the classic error this skill
   must flag.
4. If recordable → 300 log entry (+ a 301 incident report); contributes to the 300A summary.

**RIDDOR 2013 reportability decision tree:**

1. **Specified injury** (reg. 4 / Sch. 1) — e.g. fracture (not fingers/thumbs/toes),
   amputation, loss of sight, crush to head/torso, serious burns → reportable.
2. **Over-7-day incapacitation** (reg. 4) — incapacitated for >7 consecutive days
   (excluding the day of the accident) → reportable within **15 days**.
3. **Reportable disease** (reg. 8/9) — a diagnosed occupational disease on the list.
4. **Dangerous occurrence** (reg. 7 / Sch. 2) — a listed near-miss event.
A missed over-7-day report is the classic RIDDOR error this skill must flag.

## 3. Identify the correct form

From the verdict + the return type (Q2): the OSHA form (300 / 300A / 301; + 1904.41
electronic where the org profile (Q4) — size / SIC — triggers it), the RIDDOR category,
or the EU member-state equivalent. For **India**, do **not** name a form here — §5.

## 4. Calculate the deadline

From the jurisdiction's rule + the period (Q5):
- **OSHA 300A** — posted **Feb 1 – Apr 30**; electronic submission by the 1904.41 date
  where applicable.
- **RIDDOR** — within **15 days** of the accident (over-7-day; specified-injury
  notification is faster — by the quickest practicable means then the report).
- **EU** — per the national instrument.
**Never state a deadline without the jurisdiction.**

## 5. India — defer to `hse-india` (the D-04 three-tier degrade)

India returns are **not rebuilt here**. Run **mandatory state detection first**, then
produce the India leg by invoking `hse-india`:

1. **Subagent** — spawn one that runs the relevant `hse-india` skill:
   `factories-act-returns` (the state Factories Act return / register),
   `india-accident-notice` (the statutory accident notice), `india-state-form-finder`
   (to resolve the prescribed form for the detected state).
2. **Main-thread inline** — on hosts without subagents, read `KB-REG-IN-FACTORIES` /
   `KB-REG-IN-STATEFORMS` / `KB-REG-IN-PORTALS` inline and produce a single integrated
   output.
3. **Routing prose + `[GAP]`** — if `hse-india` is not installed, emit routing prose
   naming the skill to run + the KB pointer + a `[GAP]` for any unverified form value.

**At every tier:** state detection is mandatory; an unverified form value is a `[GAP]`;
**never mint a national form number**; **never hard-block**.

## 6. Prepare the return + evidence trail

Assemble the return from the role-labelled facts. Each determination links to the
**evidence item** that supports it. Any follow-up action carries a **named owner + an
ISO due date** (`smart_actions.validate_register`) — no anonymous actions, no "ASAP".

## 7. Validate + assemble

Run `references/QUALITY_CHECKLIST.md`, then build `report.json` from
`assets/regulatory-returns-report.template.json` and render via the shared engine.
