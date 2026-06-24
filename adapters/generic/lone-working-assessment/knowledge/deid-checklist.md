# De-identification Checklist — Lone Working Assessment (moderate tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **`de_identification` hard-fail**
> (A8) and **cannot be waived.**
>
> **Moderate de-id tier.** A lone-working assessment circulates with the lone worker's
> **personal contact number, shift pattern, and precise work / home location** — together these
> directly re-identify a single person and are themselves a **personal-safety** risk (they reveal
> where and when an individual is working alone). These, plus any prior lone-working
> incident / assault / collapse detail, are de-identified to **role labels** in the distributed
> copy before any analysis.

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
moderate-tier reinforcement that the De-identifier subagent applies FIRST. The reinforced rules
live ONLY here, in the SKILL.md Workflow de-id step, and in the De-identifier subagent prompt —
**never** in the `hse:block:deid` block text (anti-drift, Rule-1).

## 1. DETECT & FLAG every identifier up front

List, before drafting: the lone worker's **name**, **personal contact / mobile number**, **shift
pattern / roster**, **precise work location and home location**, payroll / employee / badge IDs,
Aadhaar / SSN / NI numbers, exact dates, vehicle registration tied to a named worker, photos, and
any disclosed health detail (a prior collapse / medical episode while working alone). If unsure
whether something is identifying for a single lone worker, treat it as identifying.

## 2. Personal contact / shift / location — role-labelled in the circulated copy

The lone worker's **personal contact number, shift pattern, and precise location** are the
moderate-tier reinforcement: they are **never** carried verbatim into the distributed assessment.
Replace the worker with a stable **role label** ("Lone Worker A (role)", "O&M Technician (role)");
carry the check-in / escalation **responder by role** ("Site Lead (role)"), never by name + phone.
The specific contact numbers and the on-call roster live in a **separate, access-controlled
operational record** — referenced, not reproduced — so circulating the assessment does not reveal
who is working alone, when, or where.

## 3. PSEUDONYMIZE BY DEFAULT + keep the re-identification key SEPARATE

Produce (a) the de-identified assessment and (b) a SEPARATE re-identification key. **Never** put
the key or any name↔label / label = person mapping in the document. Tell the user to store the key
access-controlled, apart from the assessment.

## 4. AGGREGATE SMALL NUMBERS

Never publish an injury / incident category (e.g. lone-working assault or collapse events) with
fewer than 5 individuals; aggregate up and apply **secondary suppression** so a suppressed cell
cannot be back-calculated from the totals. A `<5` cell tied to a named role / site
de-anonymizes the individual and is a `de_identification` hard-fail.

## 5. WARN BEFORE WIDE DISTRIBUTION

A lone-working assessment shared beyond the immediate manager defaults to de-identified /
role-labelled. Warn the user before any name, personal contact number, shift pattern, or precise
location enters a widely shared artifact.

## 6. MINIMIZE & LIMIT PURPOSE

Use only the personal data the assessment needs (the role and the activity, not the individual's
identity); keep contact numbers, rosters and locations out of external services where you can.

## 7. Re-identification key handling

The re-identification key is a separate artifact, **never embedded** in the assessment. The
de-identified document carries role labels only; the key (label → person, contact, shift,
location) is held access-controlled and apart.

## 8. Golden outputs — show accountability by ROLE LABEL

Show every owner / responder / check-in contact by **role label** (e.g. "Site Lead (role)", "O&M
Supervisor (role)"), never a realistic personal name + number; a personal name or contact in a
de-identified deliverable reads as a leak even when it is a deliberate operational appointment.
