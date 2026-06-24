# De-identification Checklist — Weather Dynamic Risk Assessment (lower tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **`de_identification` hard-fail**
> (A8) and **cannot be waived.**
>
> **Lower de-id tier.** A dynamic weather RA is dominated by **asset / installation / site-level
> data** (turbine IDs, anemometer placement, thresholds, forecast sources) — not personal data.
> The one personal-data surface is a **prior weather-related incident** referenced for context (a
> named worker caught out by weather on this site). That context, plus any personal contact, is
> de-identified to **role labels** in the distributed copy before any analysis.

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
lower-tier reinforcement that the De-identifier subagent applies FIRST. The reinforced rules
live ONLY here, in the SKILL.md Workflow de-id step, and in the De-identifier subagent prompt —
**never** in the `hse:block:deid` block text (anti-drift, Rule-1).

## 1. DETECT & FLAG every identifier up front

List, before drafting: any **name** of a worker / crew referenced in a prior weather-related
incident, their **personal contact / mobile number**, payroll / employee / badge IDs, NI /
Aadhaar / SSN numbers, exact dates tied to a named individual, vehicle registration tied to a
named worker, photos, and any disclosed health detail (e.g. a prior cold / hypothermia / fall-in-
high-wind episode). If unsure whether something is identifying for a single worker, treat it as
identifying. **Site, turbine, anemometer and threshold data are NOT personal data** — keep them.

## 2. Prior weather-incident context — role-labelled in the circulated copy

A prior weather-related incident referenced to justify a threshold is the lower-tier reinforcement:
the **worker / crew named in that incident is never carried verbatim** into the distributed
assessment. Replace each with a stable **role label** ("Site Lead (role)", "Rope-Access Supervisor
(role)", "Climb Lead (role)"). The incident is described at role / aggregate level — the threshold
it informs is kept; the individual is not.

## 3. PSEUDONYMIZE BY DEFAULT + keep the re-identification key SEPARATE

Produce (a) the de-identified assessment and (b) a SEPARATE re-identification key. **Never** put
the key or any name↔label mapping in the document. Tell the user to store the key access-controlled,
apart from the assessment.

## 4. AGGREGATE SMALL NUMBERS

Never publish a weather-related injury / incident category (e.g. cold-stress / fall-in-high-wind
events) with fewer than 5 individuals; aggregate up and apply **secondary suppression** so a
suppressed cell cannot be back-calculated from the totals. A `<5` cell tied to a named site / crew
de-anonymizes the individual and is a `de_identification` hard-fail.

## 5. WARN BEFORE WIDE DISTRIBUTION

A weather RA / working-limits matrix shared beyond the immediate crew / manager defaults to
de-identified / role-labelled. Warn the user before any worker name, personal contact, or precise
personnel detail enters a widely shared artifact.

## 6. MINIMIZE & LIMIT PURPOSE

Use only the personal data the assessment needs (the role and the threshold-relevant context, not
the individual's identity); keep names and contacts out of external services where you can.

## 7. Re-identification key handling

The re-identification key is a separate artifact, **never embedded** in the assessment. The
de-identified document carries role labels and the site / threshold data only; the key (label →
person, contact) is held access-controlled and apart.

## 8. Golden outputs — show accountability by ROLE LABEL

Show every owner / verifier / referenced worker by **role label** (e.g. "Site Lead (role)",
"Rope-Access Supervisor (role)"), never a realistic personal name; a personal name in a
de-identified deliverable reads as a leak even when it is a deliberate operational appointment.
The numeric thresholds, turbine IDs and anemometer placements are kept — they are asset data, not
PII.
