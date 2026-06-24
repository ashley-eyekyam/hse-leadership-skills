# De-identification Checklist — Lab Biosafety Assessment (canonical healthcare PHI extension, replicated CONV-7)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This is the catalog's HIGHEST-PHI tier.** Laboratory biosafety inputs are
> **special-category health data (PHI)** (GDPR Art. 9 / India DPDP / OSHA
> 1910.1030(f) confidentiality / US HIPAA-aligned). The reinforced `<5` small-cell
> suppression + secondary-suppression rules below, the **specimen-source-patient**
> confidentiality rule, the **worker serological-surveillance OH-record** rule, and
> the **re-identification-key separation** instruction are **stricter than, and
> additional to,** the standard de-id block — and they are enforced as a
> `de_identification` **hard-fail** in the eval suite. This replicates (CONV-7) the
> canonical healthcare PHI extension authored once for the `hse-healthcare` bundle.

This checklist reinforces — it does not replace — the canonical A5 de-id discipline.
The byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is
the special-category PHI reinforcement that the De-identifier subagent applies FIRST.
The PHI rules live ONLY here, in the SKILL.md De-identification field, and in the
Workflow de-id step — **never** in the `hse:block:deid` block (anti-drift, Rule-1).

## 1. Treat ALL biosafety / exposure inputs as special-category health data (PHI)

Every biosafety input that touches a person — the **specimen-source patient's identity**, the
**worker's identity and serological-surveillance / occupational-health record**, any
**post-exposure** medical record, and any lab-incident / exposure count — is **special-category
health data**. Handle every one of them under the strictest tier from the first read, before any
analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: worker names, the specimen-source / index patient name, contact details,
home/site addresses, payroll/employee IDs, MRN / hospital / NHS / Aadhaar / SSN numbers, exact dates
(incident date, DOB), job title / shift fine-grained enough to identify, photos, and **any disclosed
health detail** (serostatus, immunisation / serological-surveillance result, diagnosis, medication).
If unsure whether something is identifying in a small lab, treat it as identifying.

## 3. SPECIMEN-SOURCE PATIENT — never circulated

The **specimen-source / index patient's identity** (and any clinical / serostatus detail attached to
the sample) is among the most sensitive data in a biosafety assessment. It is **never** written into
a circulated assessment. The assessment references **"the specimen-source patient" by role only**;
any clinical result is held in a **separate confidential record** — not in the assessment.

## 4. WORKER serological-surveillance / OH record — confidential, separate, role-labelled

The worker is reduced to a stable **role label** ("Worker A"). Their identity, job, and
**serological-surveillance / occupational-health record** (immunisation status, antibody-titre /
surveillance result, any post-exposure follow-up) are held **confidentially and separately** from
the assessment, per OSHA **1910.1030(f)** / GDPR Art. 9. **No worker is ever named** as the subject
of a surveillance or exposure record in the circulated artifact.

## 5. SMALL-CELL SUPPRESSION — the `<5` rule (HARD), with secondary back-calc guard

- **Suppress any lab-incident / exposure category — by agent, procedure, unit, job, or period —
  with fewer than 5 individuals.** A category of 4 or fewer is **not** published — aggregate up to a
  category of ≥5 or report the parent category only.
- **Secondary suppression** — when one cell is suppressed, suppress (or aggregate) a second cell so
  the suppressed value **cannot be back-calculated** from row/column totals (publishing a total and
  all-but-one category re-derives the suppressed `<5` cell — this is the small-cell back-calculation,
  and it is a leak).
- The lab-incident / exposure summary in the **circulated** artifact is **structural / aggregated**,
  never line-level identified. A sub-5 cell published unsuppressed is a `de_identification`
  **hard-fail**.

## 6. RE-IDENTIFICATION KEY — held separately, never emitted as a file

Produce (a) the de-identified assessment and (b) a SEPARATE re-identification key.
**Never embed the key or any name↔label mapping in the document.** The skill emits **NO key file**
(no `*-key.md` / `*-key.json`): the re-identification key is an **instruction to the competent
person** (maintain the mapping separately, access-controlled, apart from the assessment), recorded in
METHODOLOGY / QUALITY_CHECKLIST — not a co-located artifact.

## 7. WARN BEFORE WIDE DISTRIBUTION

Management summaries, board packs, and any widely shared artifact default to fully aggregated,
role-level findings. Warn the user before any finer-grained breakdown, any worker /
specimen-source-patient detail, or any surveillance / serostatus result enters a widely shared copy.

## 8. MINIMIZE & LIMIT PURPOSE

Use only the data the assessment needs. Keep raw surveillance / exposure / source data out of
external services where you can. Where a genuine legal question arises (a consent question, a
suspected breach, a cross-border transfer), stop and defer to a competent person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, gov/payroll ID, MRN,
   DOB-with-value, serostatus / surveillance result tied to a person).
3. No re-identification key / name↔label mapping embedded in the output (no key file).
4. **No lab-incident / exposure cell of fewer than 5 published** (the `<5` small-cell rule, with the
   secondary back-calculation guard).

Any single failing condition is a non-waivable `de_identification` hard-fail.
