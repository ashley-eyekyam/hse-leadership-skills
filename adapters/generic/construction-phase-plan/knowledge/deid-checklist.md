# De-identification Checklist (A5) — REINFORCED for prior-incident injury detail + distributed copies

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. A Construction Phase Plan is a **distributed** document — it is briefed
> to and circulated among every contractor and operative on site — so its handling of personal
> data is stricter than an internal note: **distributed copies use role labels**, and any
> operative **named in a prior incident / near-miss** carried in the inputs is
> **special-category health data**. The byte-identical `deid` block stays untouched; this
> checklist carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail** from any cited incident: the
**named injured operative, the injury, the body part, the medical outcome, restricted-duties
notes, and any diagnosis**. If unsure whether something is identifying, treat it as identifying.

## 2. Report by role on distributed copies, never by individual (special-category rule)
- Pseudonymize every input-derived individual to a **stable role label** ("Operative A", "Site
  Supervisor"); keep the re-identification key **SEPARATE** — never in the document.
- **A prior incident / near-miss is de-identified.** The injured operative's name, the exact
  date, and the medical outcome are **never** circulated in the CPP — record the incident at
  role level ("a fall-from-height near-miss at this leading edge") as the evidence for the
  control, without the individual's identity.
- **Distributed copies use role labels.** The CPP is briefed and handed out site-wide; every
  circulated copy carries role labels for input-derived persons.

### Duty-holder exception (does NOT weaken the gate)
The **duty-holders the user deliberately supplies for the CPP record** — the principal
contractor, the CDM construction manager, the site manager — are a **legitimate contractual
record** and **stay named**; they are duty-holder assignments, **not** PII leaked from
incident-style inputs. The distinction the de-id grader and Critic/QA enforce: "the names the
user assigned as duty-holders for this plan" (legitimate) vs "a name that leaked from incident
evidence" (scrub to a role label).

## 3. Aggregate small numbers — `<5` suppression on EVERY injury breakdown
- **Never publish an injury/illness cell of fewer than 5 individuals.** Aggregate up and apply
  **secondary suppression** so a suppressed `<5` cell can't be back-calculated from row/column
  totals.
- This applies to **any** breakdown by activity, trade, or shift — a `<5` cell surviving into
  the circulated output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
The CPP is a widely distributed artifact by design; it defaults to de-identified /
role-aggregated for input-derived persons; **warn the user before any name or any
incident-injury detail enters the circulated plan.**

## 5. Minimize & limit purpose
Use only the personal/health data the CPP needs — it needs the **significant activity, the
hazard, and any de-identified incident as evidence**, not a named operative's medical history;
keep raw incident data out of external services where you can. When in doubt, ask before
including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, the injured operative's role+shift+activity combination (a
quasi-identifier in a small crew), and de-identified incident photos (no faces, no name) with
the same care as a direct identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA
injury recordkeeping privacy cases), GDPR **Art. 9** (special-category health data), India
**DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the circulated CPP.

---

**Hard-fail triggers (non-waivable):** a real (input-derived) name, a named injured operative
from a prior incident, an embedded re-identification key, or an unsuppressed `<5` injury cell
in the circulated output. The De-identifier subagent runs FIRST and every downstream job
consumes only its scrubbed, role-labelled output. *(The user-supplied duty-holders stay named
per the §2 exception — that is a legitimate record, not a leak.)*
