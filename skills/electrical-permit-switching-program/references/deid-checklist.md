# De-identification Checklist (A5) — REINFORCED for a prior switching / electrocution incident

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. `electrical-permit-switching-program` is a **low-PII / apparatus-level**
> skill — the authorised/senior authorised person is a legitimate retained operational record on
> the switching schedule — but a switching program may cite a **prior switching, electrocution, or
> arc-flash incident** as context, and a named injured operator from that incident is
> **special-category health data**. The byte-identical `deid` block stays untouched; this checklist
> carries the stricter handling for the incident detail.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail** from any cited incident: the
**named injured operator, the injury (electrocution / arc-flash burn / contact), the body part,
the medical outcome, restricted-duties notes, and any diagnosis**. If unsure whether something is
identifying, treat it as identifying.

## 2. Report by role, never by individual (special-category rule)
- Pseudonymize every individual to a **stable role label** ("Authorised Person", "Senior Authorised
  Person", "Operator A"); keep the re-identification key **SEPARATE** — never in the document.
- **A prior switching / electrocution incident is de-identified.** The injured operator's name, the
  exact date, and the medical outcome are **never** circulated in the switching program — record the
  incident at role level ("a contact/electrocution injury during a prior switching operation") as
  the evidence for the control, without the individual's identity.

## 3. Aggregate small numbers — `<5` suppression on EVERY injury breakdown
- **Never publish an injury cell of fewer than 5 individuals** (e.g. "2 electrocutions on this
  feeder"). Aggregate up and apply **secondary suppression** so a suppressed `<5` cell can't be
  back-calculated from row/column totals.
- This applies to **any** breakdown by apparatus, substation, or shift — a `<5` cell surviving into
  the circulated output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
Board reports, toolbox talks, and posted switching schedules default to de-identified /
role-aggregated; **warn the user before any name or any incident-injury detail enters a widely
shared artifact.**

## 5. Minimize & limit purpose
Use only the personal/health data the switching program needs — the program needs the **apparatus,
the points of isolation/earthing, and the de-identified incident as context**, not a named
operator's medical history; keep raw incident data out of external services where you can. When in
doubt, ask before including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, the injured operator's role+shift+apparatus combination (a
quasi-identifier in a small switching team), and de-identified incident photos (no faces, no name)
with the same care as a direct identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA
injury recordkeeping privacy cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the circulated switching program.

---

**Hard-fail triggers (non-waivable):** a real name, a named injured operator from a prior switching
/ electrocution incident, an embedded re-identification key, or an unsuppressed `<5` injury cell in
the circulated output. The De-identifier subagent runs FIRST and every downstream job consumes only
its scrubbed, role-labelled output.
