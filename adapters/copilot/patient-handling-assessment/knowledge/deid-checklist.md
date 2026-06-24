# De-identification Checklist — Patient Handling Assessment (healthcare PHI extension)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This is the catalog's HIGHEST-PHI tier.** Patient mobility / dependency data and a
> worker's musculoskeletal / back-condition record are **special-category health data
> (PHI)** (GDPR Art. 9 / India DPDP / US HIPAA-aligned). The reinforced `<5` small-cell
> suppression + secondary-suppression rules below, the
> **patient-assessed-by-de-identified-mobility/dependency/weight-band** rule, the
> **worker back-condition / OH-record** rule, and the **re-identification-key
> separation** instruction are **stricter than, and additional to,** the standard
> de-id block — and they are enforced as a `de_identification` **hard-fail** in the
> eval suite. This is replicated (CONV-7) from the canonical healthcare PHI extension
> authored in the `hse-healthcare` bundle's first skill.

This checklist reinforces — it does not replace — the canonical A5 de-id discipline.
The byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is
the special-category PHI reinforcement that the De-identifier subagent applies FIRST.
The PHI rules live ONLY here, in the SKILL.md De-identification field, and in the
Workflow de-id step — **never** in the `hse:block:deid` block (anti-drift, Rule-1).

## 1. Treat ALL patient-handling / health inputs as special-category health data (PHI)

Every patient-handling input — the **patient's mobility, dependency, weight band,
diagnosis, and care-plan detail**, the **worker's individual capability and any
musculoskeletal / back-condition record**, and any **handling-injury count** — is
**special-category health data**. Handle every one of them under the strictest tier
from the first read, before any analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: patient names, the worker's name, contact details, home/site
addresses, payroll/employee IDs, MRN / hospital / NHS / Aadhaar / SSN numbers, exact
dates (injury date, DOB), **ward / bed / bay**, job title / shift fine-grained enough
to identify, photos, and **any disclosed health detail** (the patient's diagnosis or
care plan, the worker's fitness / back-condition / OH record). If unsure whether
something is identifying in a small unit, treat it as identifying. **"A bariatric,
fully-dependent patient on Ward 4 bay 2" is identifying — scrub the ward/bay and any
care-plan detail.**

## 3. PATIENT — assessed by de-identified mobility / dependency / weight band only

The **patient is assessed and recorded by de-identified mobility / dependency level
and weight band only** — never the patient's name, MRN / hospital / NHS number, DOB,
ward / bed / bay, diagnosis, or care-plan detail in the circulated assessment. The
TILE **Load** factor describes the patient by mobility, dependency, cooperation,
weight band, and attachments (lines, drains) — not by identity. A patient's diagnosis
is **never** written into the circulated assessment.

## 4. WORKER back-condition / OH record — confidential, separate, role-labelled

The worker is reduced to a stable **role label** ("Worker A"). The TILE **Individual**
factor assesses the worker's **capability** (training, handling competence, number of
handlers) **without** writing the worker's name or any **fitness / musculoskeletal /
back-condition / occupational-health record** into the circulated copy. Any
medical-fitness detail is held **confidentially and separately** from the assessment.
**No worker is ever named** as the subject of a back condition or handling injury in
the circulated artifact.

## 5. SMALL-CELL SUPPRESSION — the `<5` rule (HARD), with secondary back-calc guard

- **Suppress any handling-injury category — by unit, task, job, or period — with fewer
  than 5 individuals.** A category of 4 or fewer is **not** published — aggregate up to
  a category of ≥5 or report the parent category only. **Handling-injury data
  aggregated across the unit is the data this rule guards (D-03).**
- **Secondary suppression** — when one cell is suppressed, suppress (or aggregate) a
  second cell so the suppressed value **cannot be back-calculated** from row/column
  totals (e.g. publishing a total and all-but-one category re-derives the suppressed
  `<5` cell — this is the small-cell back-calculation, and it is a leak).
- Any handling-injury reporting in the **circulated** artifact is **structural /
  aggregated**, never line-level identified. A sub-5 cell published unsuppressed is a
  `de_identification` **hard-fail**.

## 6. RE-IDENTIFICATION KEY — held separately, never emitted as a file

Produce (a) the de-identified assessment and (b) a SEPARATE re-identification key.
**Never embed the key or any name↔label mapping in the document.** The skill emits **NO
key file** (no `*-key.md` / `*-key.json`): the re-identification key is an **instruction
to the competent person** (maintain the mapping separately, access-controlled, apart
from the assessment), recorded in METHODOLOGY / QUALITY_CHECKLIST — not a co-located
artifact.

## 7. WARN BEFORE WIDE DISTRIBUTION

Management summaries, board packs, and any widely shared artifact default to fully
aggregated, role-level findings. Warn the user before any finer-grained breakdown, any
worker / patient detail, or any diagnosis enters a widely shared copy.

## 8. MINIMIZE & LIMIT PURPOSE

Use only the data the assessment needs. Keep raw patient mobility / care-plan and
worker OH data out of external services where you can. Where a genuine legal question
arises (a consent question, a suspected breach, a cross-border transfer), stop and
defer to a competent person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, gov/payroll
   ID, MRN, DOB-with-value, diagnosis tied to a person, ward/bay).
3. No re-identification key / name↔label mapping embedded in the output (no key file).
4. **No handling-injury cell of fewer than 5 published** (the `<5` small-cell rule, with
   the secondary back-calculation guard).

Any single failing condition is a non-waivable `de_identification` hard-fail.
