# De-identification Checklist — Wind Turbine Work at Height + Rescue (moderate tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **`de_identification` hard-fail**
> (A8) and **cannot be waived.**
>
> **Moderate de-id tier.** A turbine WAH + rescue plan circulates with the **climbers' / rescuers'
> names and their GWO certificate numbers** — together these directly re-identify named
> individuals and the certificate number is part of a **licensed** competence scheme. These, plus
> any prior fall / suspension / rescue incident detail, are de-identified to **role labels** in the
> distributed copy before any analysis; the GWO competence **requirement** is cited, the
> certificate number is **never reproduced** (`[GAP]`).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
moderate-tier reinforcement that the De-identifier subagent applies FIRST. The reinforced rules
live ONLY here, in the SKILL.md Workflow de-id step, and in the De-identifier subagent prompt —
**never** in the `hse:block:deid` block text (anti-drift, Rule-1).

## 1. DETECT & FLAG every identifier up front

List, before drafting: each climber's / rescuer's **name**, **GWO certificate number** (and any
training-record / licence number), **personal contact / mobile number**, payroll / employee /
badge IDs, NI / Aadhaar / SSN numbers, exact dates, vehicle registration tied to a named worker,
photos, and any disclosed health detail (a prior collapse / suspension episode at height). If
unsure whether something is identifying for a single climber, treat it as identifying.

## 2. Climber name + GWO certificate number — role-labelled / cited-only in the circulated copy

The climbers' **names and GWO certificate numbers** are the moderate-tier reinforcement: they are
**never** carried verbatim into the distributed plan. Replace each worker with a stable **role
label** ("Climber A (role)", "Rescue Lead (role)", "Ground Support (role)"). **Cite the GWO
competence *requirement* — current GWO WAH / First Aid / ART, 2-yr refresh — never the certificate
number** (the number is a licensed competence-scheme identifier → record `[GAP]` for the cert
detail). The actual certificate numbers and the personnel competence matrix live in a **separate,
access-controlled training record** — referenced, not reproduced.

## 3. PSEUDONYMIZE BY DEFAULT + keep the re-identification key SEPARATE

Produce (a) the de-identified plan and (b) a SEPARATE re-identification key. **Never** put the key
or any name↔label / label = person + certificate mapping in the document. Tell the user to store
the key access-controlled, apart from the plan.

## 4. AGGREGATE SMALL NUMBERS

Never publish an injury / incident category (e.g. fall / suspension / rescue events) with fewer
than 5 individuals; aggregate up and apply **secondary suppression** so a suppressed cell cannot be
back-calculated from the totals. A `<5` cell tied to a named turbine / team de-anonymizes the
individual and is a `de_identification` hard-fail.

## 5. WARN BEFORE WIDE DISTRIBUTION

A WAH + rescue plan shared beyond the immediate climb team / manager defaults to de-identified /
role-labelled. Warn the user before any climber name, GWO certificate number, personal contact, or
precise personnel detail enters a widely shared artifact.

## 6. MINIMIZE & LIMIT PURPOSE

Use only the personal data the plan needs (the role, the competence requirement and the activity,
not the individual's identity or certificate number); keep names, certificate numbers and contacts
out of external services where you can.

## 7. Re-identification key handling

The re-identification key is a separate artifact, **never embedded** in the plan. The de-identified
document carries role labels and the cited GWO competence requirement only; the key (label →
person, certificate number, contact) is held access-controlled and apart.

## 8. Golden outputs — show accountability by ROLE LABEL

Show every climber / rescuer / owner / verifier by **role label** (e.g. "Rescue Lead (role)",
"Site WAH Supervisor (role)"), never a realistic personal name or a GWO certificate number; a
personal name or certificate number in a de-identified deliverable reads as a leak even when it is
a deliberate operational appointment.
