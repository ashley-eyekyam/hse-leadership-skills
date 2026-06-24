# De-identification Checklist (A5) — LOWER TIER, reinforced for prior struck-by / rack-collapse injury

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting any
> output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and **cannot be
> waived**. `warehouse-racking-mhe-safety` is a **lower de-id tier** skill — asset / installation /
> site data dominates (bay configs, SWL ratings, damage findings carry no personal data) — but a
> racking + traffic assessment routinely cites a **prior struck-by / rack-collapse / forklift-impact
> incident**, and a named injured worker from that incident is **special-category health data**. The
> byte-identical `deid` block stays untouched; this checklist carries the stricter handling for the
> incident detail.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations, job title /
crew / shift, photos — **and every health detail** from any cited incident: the **named injured worker
(struck-by / crush / collapse), the injury, the body part, the medical outcome, restricted-duties
notes, and any diagnosis**. If unsure whether something is identifying, treat it as identifying. (Most
of this skill's inputs — SWL ratings, bay configurations, damage tolerances — carry **no** personal
data and need no scrub; the scrub focuses on any cited incident.)

## 2. Report by role, never by individual (special-category rule)
- Pseudonymize every individual to a **stable role label** ("Forklift Operator A", "Warehouse Lead",
  "PRRS"); keep the re-identification key **SEPARATE** — never in the document.
- **A prior struck-by / rack-collapse incident is de-identified.** The injured worker's name, the
  exact date, and the medical outcome are **never** circulated in the racking assessment — record the
  incident at role level ("a struck-by injury at this aisle/crossing", "a collapse on this Red-band
  run") as the evidence for the finding, without the individual's identity.

## 3. Aggregate small numbers — `<5` suppression on EVERY injury breakdown
- **Never publish an injury cell of fewer than 5 individuals** (e.g. "2 forklift-strike injuries in
  goods-in"). Aggregate up and apply **secondary suppression** so a suppressed `<5` cell can't be
  back-calculated from row/column totals.
- This applies to **any** breakdown by aisle, bay, shift, or MHE type — a `<5` cell surviving into the
  circulated output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
Board reports, toolbox talks, and posted racking/traffic registers default to de-identified /
role-aggregated; **warn the user before any name or any incident-injury detail enters a widely shared
artifact.**

## 5. Minimize & limit purpose
Use only the personal/health data the assessment needs — it needs the **damage finding, the SEMA band,
the traffic-conflict point, and the de-identified incident as evidence**, not a named worker's medical
history; keep raw incident data out of external services where you can. When in doubt, ask before
including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, the injured worker's role+shift+aisle combination (a quasi-identifier
on a small crew), and de-identified incident photos (no faces, no name) with the same care as a direct
identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA injury recordkeeping privacy
cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**, access-controlled
artifact and is **never embedded** in the circulated racking assessment.

---

**Hard-fail triggers (non-waivable):** a real name, a named injured worker from a prior struck-by /
rack-collapse incident, an embedded re-identification key, or an unsuppressed `<5` injury cell in the
circulated output. The De-identifier subagent runs FIRST and every downstream job consumes only its
scrubbed, role-labelled output.
