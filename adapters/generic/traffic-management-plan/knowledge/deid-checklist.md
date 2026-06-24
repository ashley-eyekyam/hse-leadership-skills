# De-identification Checklist (A5) — REINFORCED for the site/route-level (lowest-PII) TMP

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting any
> output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and **cannot
> be waived**. A traffic management plan is the **lowest-PII** artifact in the pack — it is a
> **site / route-level** document that **carries no named individual** in the circulated plan. The
> de-id challenge here is therefore precise but strict: a **named driver / operative / banksman**
> that arrives in the inputs (e.g. a named driver in a prior reversing near-miss, a
> fitness-for-duty note) must be **caught and scrubbed**; the clean site/route-level plan must
> **not false-trip**. The byte-identical `deid` block stays untouched; this checklist carries the
> stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail**: a **named driver's or operative's
fitness-for-duty / medical-restriction note, an injury from any cited prior reversing /
struck-by near-miss, the body part, the medical outcome, restricted-duties notes, and any
diagnosis**. If unsure whether something is identifying, treat it as identifying.

## 2. The site/route-level rule (the defining gate for this skill)
- The TMP names **routes, gates, bays, and zones — not people.** Vehicle routes, pedestrian
  routes, access points, loading bays, crossings, speed limits, and the banksman / traffic-marshal
  **requirement** are recorded at **role / location level** ("a trained banksman at the north
  loading bay"), **never** as a named individual.
- Any individual that arrives **as incident-style evidence** (a named driver from a prior reversing
  near-miss, an operative struck-by case) is pseudonymized to a **stable role label** ("Driver A",
  "Operative 1"); keep the re-identification key **SEPARATE** — never in the document. Record the
  incident at role + location level ("a prior reversing near-miss at the south gate") as the
  evidence for the segregation control, **without** the individual's identity, date, or medical
  outcome.
- A **worker's fitness-for-duty / health detail is ALWAYS scrubbed and never circulated.** "The
  banksman is trained and competent" is a role-level fact; "Driver J. Smith is on restricted duties
  for a back condition" is **special-category health data** — scrub the name, the condition, and
  the restriction; it has **no place in the circulated TMP at all**.

### Why there is no duty-holder exception here
Unlike the named-personnel construction documents (a RAMS / lift plan that deliberately names an
appointed person), **the TMP names no individual** — it is a site/route-level plan. So **every**
personal name in the inputs is input-derived PII to scrub. A named driver / operative / banksman
surviving into the circulated plan is a `de_identification` hard-fail.

## 3. Aggregate small numbers — `<5` suppression on EVERY injury breakdown
- **Never publish an injury/illness cell of fewer than 5 individuals.** Aggregate up and apply
  **secondary suppression** so a suppressed `<5` cell can't be back-calculated from row/column
  totals.
- This applies to any reversing / struck-by / vehicle-incident breakdown by gate, route, or shift —
  a `<5` cell surviving into the output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
A TMP is briefed to every operative, every delivery driver, and may be issued to the principal
contractor and the public-facing hoarding; it defaults to role / location labels and **carries no
fitness or incident-injury detail**; **warn the user before any health detail or any
incident-injury detail enters the plan.**

## 5. Minimize & limit purpose
Use only the data the TMP needs — it needs **routes, conflict points, and the banksman
requirement at role level**, not a named driver's history; keep raw incident / fitness data out of
external services where you can. When in doubt, ask before including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, a driver's role+shift+gate combination (a quasi-identifier on a
small site), and a **fitness-for-duty / medical-restriction note** with the same care as a direct
identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA injury recordkeeping privacy
cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the circulated TMP.

---

**Hard-fail triggers (non-waivable):** a real (input-derived) name from incident / fitness
evidence, **a worker's fitness-for-duty / health detail**, an embedded re-identification key, or
an unsuppressed `<5` injury cell in the circulated output. The De-identifier subagent runs
**FIRST** (even at this skill's low PII) and every downstream job consumes only its scrubbed,
role/location-labelled output. *(The TMP names no individual — there is no duty-holder exception;
every personal name in the inputs is scrubbed.)*
