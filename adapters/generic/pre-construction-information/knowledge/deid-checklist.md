# De-identification Checklist (A5) — REINFORCED for survey-occupier health detail + restricted distribution

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. Pre-Construction Information is **provided to every designer and
> contractor being considered or appointed** (Reg 4(4)) — so it circulates beyond the client.
> Existing-structure surveys routinely **name an occupier / resident / tenant with a health
> detail** (an asbestos survey naming a resident's respiratory condition; an occupier's
> medical-vulnerability note in an access constraint) — that is **special-category health
> data**. The byte-identical `deid` block stays untouched; this checklist carries the stricter
> handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail** carried in any survey,
occupier note, or existing H&S file: the **named occupier / resident / tenant, their medical
or vulnerability detail, the surveyor's personal contact, and any individual injury/illness
note**. If unsure whether something is identifying, treat it as identifying.

## 2. Report by role on circulated copies, never by individual (special-category rule)
- Pseudonymize every input-derived individual to a **stable role label** ("Occupier A",
  "Adjacent Resident", "Surveyor"); keep the re-identification key **SEPARATE** — never in the
  document.
- **A survey occupier / resident with a health detail is de-identified.** The occupier's name,
  exact unit, and the medical/vulnerability detail are **never** circulated in the PCI — record
  the constraint at role level ("an adjacent occupier with a documented mobility constraint
  affects the access sequence") as the information for the designers, without the individual's
  identity.
- **Circulated copies use role labels.** The PCI is issued to every designer/contractor being
  considered; every circulated copy carries role labels for input-derived persons.

### Restricted-distribution flag
Where the PCI carries sensitive site detail (security-sensitive asset locations, an occupier's
vulnerability, an existing H&S file extract), set a **restricted-distribution flag** on the
pack and state the limited circulation list — the Reg 4 duty to share is satisfied by issuing
to the appointed/considered parties, not by unrestricted publication.

### Duty-holder exception (does NOT weaken the gate)
The **duty-holders the user deliberately supplies for the PCI record** — the client, the
principal designer, the named gap-action owners — are a **legitimate contractual record** and
**stay named**; they are duty-holder/owner assignments, **not** PII leaked from survey inputs.
The distinction the de-id grader and Critic/QA enforce: "the names the user assigned as
duty-holders / gap-action owners for this pack" (legitimate) vs "a name that leaked from a
survey or occupier note" (scrub to a role label).

## 3. Aggregate small numbers — `<5` suppression on EVERY breakdown
- **Never publish an injury/illness or occupier-health cell of fewer than 5 individuals.**
  Aggregate up and apply **secondary suppression** so a suppressed `<5` cell can't be
  back-calculated from row/column totals.
- A `<5` cell surviving into the circulated output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
The PCI is issued to multiple designers/contractors by design; it defaults to de-identified /
role-aggregated for input-derived persons; **warn the user before any occupier name or any
health detail enters the circulated pack.**

## 5. Minimize & limit purpose
Use only the personal/health data the PCI needs — it needs the **existing-structure hazard,
its location, and any de-identified access/occupier constraint as information**, not a named
occupier's medical history; keep raw survey data out of external services where you can. When
in doubt, ask before including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, the occupier's unit+condition combination (a quasi-identifier
in a small building), and survey photos (no faces, no name) with the same care as a direct
identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA injury recordkeeping
privacy cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the circulated PCI.

---

**Hard-fail triggers (non-waivable):** a real (input-derived) name, a named occupier /
resident with a health detail from a survey, an embedded re-identification key, or an
unsuppressed `<5` cell in the circulated output. The De-identifier subagent runs FIRST and
every downstream job consumes only its scrubbed, role-labelled output. *(The user-supplied
duty-holders / gap-action owners stay named per the §2 exception — that is a legitimate
record, not a leak.)*
