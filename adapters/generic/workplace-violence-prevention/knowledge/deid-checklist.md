# De-identification Checklist — Workplace-Violence Prevention (healthcare PHI extension)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This is the catalog's HIGHEST-PHI tier.** Workplace-violence incident data is
> **special-category health data (PHI)** (GDPR Art. 9 / India DPDP / OSHA
> 1910.1030(f)-aligned confidentiality / US HIPAA-aligned). The reinforced `<5`
> small-cell suppression + secondary-suppression rules below, the **named-victim /
> assailant / known-risk-patient** rule, the **behavioural-health-flag** rule, and
> the **re-identification-key separation** instruction are **stricter than, and
> additional to,** the standard de-id block — and they are enforced as a
> `de_identification` **hard-fail** in the eval suite. **This replicates the
> canonical healthcare PHI extension** (CONV-7) into this `hse-healthcare` skill's
> checklist.

This checklist reinforces — it does not replace — the canonical A5 de-id discipline.
The byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is
the special-category PHI reinforcement that the De-identifier subagent applies FIRST.
The PHI rules live ONLY here, in the SKILL.md De-identification field, and in the
Workflow de-id step — **never** in the `hse:block:deid` block (anti-drift, Rule-1).

## 1. Treat ALL violence / incident inputs as special-category health data (PHI)

Every workplace-violence input — a named victim, a named assailant, a known-risk
patient, the worksite-analysis incident detail, any behavioural-health flag, and any
incident count — is **special-category health data**. Handle every one of them under
the strictest tier from the first read, before any analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: worker / victim names, the assailant / known-risk patient name,
contact details, home / site addresses, payroll / employee IDs, MRN / hospital / NHS /
Aadhaar / SSN numbers, exact dates (incident date, DOB), ward / bed / unit, job title /
shift fine-grained enough to identify, photos, and **any disclosed health detail**
(behavioural-health flag, diagnosis, medication, clinical risk note). If unsure whether
something is identifying in a small unit, treat it as identifying.

## 3. NAMED victim / assailant / known-risk patient — never circulated

A **named victim, assailant, or known-risk patient** is the most sensitive datum in a
WPV program. None is **ever** written into a circulated program. The worksite analysis
and the incident log reference people **by role only** ("Worker A", "the patient", "a
visitor"); a known-risk patient is flagged **by a de-identified clinical mechanism held
in a separate confidential record**, never by name in the plan.

## 4. BEHAVIOURAL-HEALTH flag — confidential, separate, role-labelled

A **behavioural-health flag** on a patient or person (a clinical risk note, a diagnosis,
a behavioural-management plan) is special-category health data. It is reduced to a
de-identified, role-level control mechanism and held **confidentially and separately**
from the plan. **No person is ever named** as the subject of a behavioural-health flag
in the circulated artifact.

## 5. SMALL-CELL SUPPRESSION — the `<5` rule (HARD), with secondary back-calc guard

- **Suppress any incident category — by unit, ward, job, type, or period — with fewer
  than 5 individuals.** A category of 4 or fewer is **not** published — aggregate up to
  a category of ≥5 or report the parent category only.
- **Secondary suppression** — when one cell is suppressed, suppress (or aggregate) a
  second cell so the suppressed value **cannot be back-calculated** from row/column
  totals (e.g. publishing a total and all-but-one category re-derives the suppressed
  `<5` cell — this is the small-cell back-calculation, and it is a leak). A 2-incident
  category on a named ward de-anonymizes the people involved and is a leak.
- The WPV incident log in the **circulated** artifact is **structural / aggregated**,
  never line-level identified. A sub-5 cell published unsuppressed is a
  `de_identification` **hard-fail**.

## 6. RE-IDENTIFICATION KEY — held separately, never emitted as a file

Produce (a) the de-identified program and (b) a SEPARATE re-identification key.
**Never embed the key or any name↔label mapping in the document.** The skill emits **NO
key file** (no `*-key.md` / `*-key.json`): the re-identification key is an **instruction
to the competent person** (maintain the mapping separately, access-controlled, apart
from the program), recorded in METHODOLOGY / QUALITY_CHECKLIST — not a co-located
artifact.

## 7. WARN BEFORE WIDE DISTRIBUTION

Management summaries, board packs, and any widely shared artifact default to fully
aggregated, role-level findings. Warn the user before any finer-grained breakdown, any
victim / assailant / known-risk-patient detail, or any behavioural-health flag enters a
widely shared copy.

## 8. MINIMIZE & LIMIT PURPOSE

Use only the data the program needs. Keep raw incident / behavioural-health / clinical
data out of external services where you can. Where a genuine legal question arises (a
consent question, a suspected breach, a cross-border transfer), stop and defer to a
competent person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, gov/payroll
   ID, MRN, DOB-with-value, behavioural-health flag tied to a person).
3. No re-identification key / name↔label mapping embedded in the output (no key file).
4. **No incident cell of fewer than 5 published** (the `<5` small-cell rule, with the
   secondary back-calculation guard).

Any single failing condition is a non-waivable `de_identification` hard-fail.
