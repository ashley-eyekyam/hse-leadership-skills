# De-identification Checklist (A5) — REINFORCED for the named-personnel ↔ medical-fitness distinction

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. A lift plan is a **named-personnel document by design** — the appointed
> person, crane operator, and slinger / signaller are **deliberately named for the competence
> record** — so the de-id challenge here is **precise**: keep the duty-holder names (a
> legitimate record) while scrubbing any **medical-fitness / health detail** and any
> **incident-derived** name. The byte-identical `deid` block stays untouched; this checklist
> carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail**: a **named operator's
medical-fitness note, a fitness-for-duty / medical-restriction record, an injury from any
cited prior dropped-load / near-miss, the body part, the medical outcome, restricted-duties
notes, and any diagnosis**. If unsure whether something is identifying, treat it as identifying.

## 2. The named-personnel ↔ medical-fitness distinction (the defining gate for this skill)
- The **appointed person, the crane operator, and the slinger / signaller the user supplies at
  Q5 for the competence record stay named** — they are **duty-holder assignments**, a
  legitimate contractual record, **not** leaked PII. Their **competence basis** (CPCS / NPORS /
  appointed-person training) is a legitimate record too.
- A **worker's medical-fitness / health detail is ALWAYS scrubbed and never circulated.** "The
  operator holds a current medical certificate" is a fitness fact at role level; "Operator
  J. Smith is on restricted duties for a back condition" is **special-category health data** —
  scrub the name, the condition, and the restriction; it has **no place in the circulated lift
  plan at all**.
- Any individual that arrives **as incident-style evidence** (a named operator from a prior
  dropped-load near-miss) is pseudonymized to a **stable role label** ("Operator A"); keep the
  re-identification key **SEPARATE** — never in the document. Record the incident at role level
  ("a prior dropped-load near-miss on this crane") as the evidence for the control, without the
  individual's identity, date, or medical outcome.

### Duty-holder exception (does NOT weaken the gate)
The distinction the de-id grader and Critic/QA enforce: **"the appointed person / operator /
slinger the user assigned as duty-holders for this lift"** (legitimate, stay named) vs **"a name
or a medical-fitness / health detail that leaked from incident or fitness evidence"** (scrub to
a role label / remove the health detail). Named personnel must **never** false-trip the gate; a
medical-fitness note must **always** be caught.

## 3. Aggregate small numbers — `<5` suppression on EVERY injury breakdown
- **Never publish an injury/illness cell of fewer than 5 individuals.** Aggregate up and apply
  **secondary suppression** so a suppressed `<5` cell can't be back-calculated from row/column
  totals.
- This applies to any dropped-load / lifting-incident breakdown by crew, crane, or shift — a
  `<5` cell surviving into the output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
A lift plan is briefed to the lift team and may be issued to the principal contractor; it
defaults to role labels for input-derived persons and **carries no medical-fitness detail**;
**warn the user before any health detail or any incident-injury detail enters the plan.**

## 5. Minimize & limit purpose
Use only the personal data the lift plan needs — it needs the **named duty-holders and their
competence basis**, not a named worker's medical history; keep raw incident / fitness data out
of external services where you can. When in doubt, ask before including it.

## 6. HSE addendum (beyond HIPAA Safe-Harbor)
Treat **Aadhaar / national-ID**, the operator's role+shift+crane combination (a quasi-identifier
in a small lift team), and a **medical-fitness / fitness-for-duty note** with the same care as a
direct identifier. The jurisdiction mechanisms: US **29 CFR 1904.29** (OSHA injury recordkeeping
privacy cases), GDPR **Art. 9** (special-category health data), India **DPDP**.

## 7. Re-identification key handling
The name↔role-label mapping (the re-identification key) is held in a **SEPARATE**,
access-controlled artifact and is **never embedded** in the circulated lift plan.

---

**Hard-fail triggers (non-waivable):** a real (input-derived) name from incident / fitness
evidence, **a worker's medical-fitness / health detail**, an embedded re-identification key, or
an unsuppressed `<5` injury cell in the circulated output. The De-identifier subagent runs
FIRST and every downstream job consumes only its scrubbed, role-labelled output. *(The
user-supplied appointed person / operator / slinger stay named per the §2 exception — that is a
legitimate competence record, not a leak.)*
