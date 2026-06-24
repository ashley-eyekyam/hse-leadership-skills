# De-identification Checklist (A5) — REINFORCED for commissioning-record individuals + restricted distribution

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. The Health & Safety File is handed to the **client** and consulted by
> **future maintenance, cleaning, refurbishment, and demolition** workers — so it circulates
> beyond the original project team. **Commissioning, survey, and as-built records routinely
> name an individual** — a commissioning engineer with an incident or health/fitness note, a
> surveyor, an occupier — and that is **special-category health data** when a health/incident
> detail is attached. **No worker health detail belongs in the file at all.** The
> byte-identical `deid` block stays untouched; this checklist carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations, job
title / crew / shift, photos — **and every health or incident detail** carried in any
commissioning record, survey, or as-built note: the **named commissioning engineer / surveyor
/ occupier, any individual incident or medical-fitness note, their personal contact**. If
unsure whether something is identifying, treat it as identifying.

## 2. Report by role on the file, never by individual (special-category rule)
- Pseudonymize every input-derived individual to a **stable role label** ("Commissioning
  Engineer", "Surveyor", "Occupier A"); keep the re-identification key **SEPARATE** — never in
  the file.
- **A commissioning record naming an individual with an incident/health detail is
  de-identified.** The individual's name, exact unit, and the incident/medical detail are
  **never** carried into the file — record only the residual *structural/services* fact a
  future worker needs (e.g. "the AHU isolation point is non-standard — located in the level-9
  riser"), without the individual's identity or any health detail.
- **No worker health detail in the file.** The H&S File records residual *structural* risk,
  not personnel health data.

### Restricted-distribution flag
Where the file carries **security-sensitive structural / services detail** (asset-security
locations, isolation points, an asbestos register), set a **restricted-distribution flag** and
state the limited circulation list — the Reg 12 handover duty is satisfied by issuing to the
client and the future-work duty-holders, not by unrestricted publication.

### Duty-holder exception (does NOT weaken the gate)
The **duty-holders the user deliberately supplies for the record** — the **principal designer**
(Reg 12(5)), the **client**, and the named owners of open completion items — are a
**legitimate contractual record** and **stay named**; they are duty-holder/owner assignments,
**not** PII leaked from commissioning or survey inputs. The distinction the de-id grader and
Critic/QA enforce: "the names the user assigned as duty-holders / open-item owners for this
file" (legitimate) vs "a name that leaked from a commissioning record, survey, or as-built
note" (scrub to a role label).

## 3. Aggregate small numbers — `<5` suppression on EVERY breakdown
- **Never publish an injury/illness or incident cell of fewer than 5 individuals.** Aggregate
  up and apply **secondary suppression** so a suppressed `<5` cell can't be back-calculated
  from row/column totals.
- A `<5` cell surviving into the file is a `de_identification` hard-fail.

## 4. Warn before wide distribution
The file is handed to the client and consulted by future-work duty-holders; it defaults to
de-identified / role-aggregated for input-derived persons; **warn the user before any
commissioning-record name or any health/incident detail enters the file.**

## 5. Minimize & limit purpose
Use only the data the file needs — it needs the **residual structural/services hazard and its
location**, not a named individual's incident or medical history; keep raw commissioning/survey
data out of external services where you can. When in doubt, ask before including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, an individual's role+condition combination (a quasi-identifier
in a small project team), and survey/commissioning photos (no faces, no name) with the same
care as a direct identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA injury
recordkeeping privacy cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the file.

---

**Hard-fail triggers (non-waivable):** a real (input-derived) name, a named commissioning
engineer / surveyor / occupier with an incident or health detail, an embedded re-identification
key, or an unsuppressed `<5` cell in the file. The De-identifier subagent runs FIRST and every
downstream job consumes only its scrubbed, role-labelled output. *(The user-supplied principal
designer / client duty-holders and open-item owners stay named per the §2 exception — that is a
legitimate record, not a leak.)*
