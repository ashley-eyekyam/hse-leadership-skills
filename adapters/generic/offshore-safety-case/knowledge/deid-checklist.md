# De-identification Checklist (A5) — offshore-safety-case

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> cannot be waived.

**Lower de-id tier:** an offshore safety case is dominated by **installation / asset-level
data** — field, water depth, MAH set, SCE register, performance standards, bowtie/HAZOP
references. That content carries no personal data. But a safety case routinely cites a
**prior major-accident / loss-of-containment incident** and a **station-bill / duty-holder
roster**, and a **named individual** from either is special-category data (GDPR Art. 9 /
India DPDP). So the scrub is precise: keep the installation/asset facts; pseudonymise every
prior-incident name, named role-holder, contact, and competence-certificate number to a
**role label**, and carry persons-on-board as a **count**, never a named manifest.

1. **DETECT & FLAG** every personal/health identifier in the inputs and list them up front — prior-incident names, OIM / station-bill role-holder names, contacts (phone/email), employee / certificate (OPITO / verifier) numbers, exact dates, and any medical detail. If unsure whether something is identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** to stable role labels ("OIM (role)", "Technical Authority", "Independent Verifier"); keep the re-identification key in a SEPARATE artifact — never embedded in the document or any name↔label mapping.
3. **AGGREGATE SMALL NUMBERS** — never publish a prior-incident injury/illness cell of fewer than 5 individuals on a named installation; aggregate up and apply secondary suppression so a suppressed cell cannot be back-calculated from the total.
4. **WARN BEFORE WIDE DISTRIBUTION** — a circulated safety-case argument defaults to role-level / aggregated; warn before any name or health detail enters it.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the safety-case argument needs (role accountabilities, not identities); persons-on-board is a count.
6. **GOLDEN OUTPUTS** — show accountability by ROLE LABEL ("OIM (role)", "Independent Verifier"), never a realistic personal name; a personal name in a de-identified deliverable reads as a leak even though it is a deliberate operational appointment.

## Jurisdiction quick-reference (mechanism, not statute text)
- **GDPR Art. 9** — special-category (health) data; prior-incident injury detail is special-category.
- **India DPDP** — sensitive personal data; shore-base statutory routing defers to `hse-india`.
- **OSHA privacy-case (29 CFR 1904.29)** — privacy-concern cases; small-cell suppression analogue.
- **Re-identification key handling** — the key is held in a SEPARATE artifact and is never embedded in the circulated document.
