# De-identification Checklist (A5)

The deep reference the mandatory `hse:block:deid` block points to. Apply it
BEFORE drafting any output. A de-identification leak is an eval **hard-fail**
(A8) and cannot be waived — see §9 for what "leak" means observably.

> This is decision-support, not legal advice. Where a genuine legal question
> arises (cross-border transfer, a real consent question, a suspected breach),
> stop and defer to a competent person (§10).

## Contents

1. Why this matters
2. The 18-identifier scrub checklist (HIPAA Safe-Harbor) + HSE addendum
3. Direct vs quasi-identifier test
4. Tiered handling model
5. Small-cell (<5) suppression + secondary suppression
6. Distribution / sharing warnings
7. Re-identification key handling
8. Data minimization & purpose limitation
9. Jurisdiction quick-reference (mechanisms only)
10. Escalation / "ask a competent person" triggers

---

## 1. Why this matters

HSE outputs routinely carry **special-category health data** (injuries,
diagnoses, restrictions) and **personal data** (names, IDs, witness/contractor
detail). Mishandled, a single circulated risk assessment, incident report, or
toolbox talk can identify an injured worker. De-identification aligns the AI
with the duty regulators already impose — for example OSHA's requirement to keep
a worker's name *off* the publicly posted 300 Log. **Pseudonymized data is still
personal data**: the protection is the *access-controlled re-identification key
held apart from the document* (§7), not the act of relabelling alone.

## 2. The 18-identifier scrub checklist (HIPAA Safe-Harbor) + HSE addendum

The HIPAA Safe-Harbor list is used here as a **practical, concrete scrub
target** so the De-identifier has something to enumerate against — not as a
claim of HIPAA jurisdiction. Detect and treat each of these (18):

1. Names.
2. Geographic subdivisions smaller than a state (street, city, county, ZIP/PIN).
3. All date elements (except year) tied to an individual — admission, injury,
   birth, death, treatment dates.
4. Telephone numbers.
5. Fax numbers.
6. Email addresses.
7. Social Security / National Insurance numbers.
8. Medical record numbers.
9. Health-plan beneficiary numbers.
10. Account numbers.
11. Certificate / licence numbers.
12. Vehicle identifiers and licence plates.
13. Device identifiers and serial numbers.
14. URLs.
15. IP addresses.
16. Biometric identifiers (fingerprints, voiceprints, retina/iris scans).
17. Full-face photographs and any comparable images.
18. Any other unique identifying number, characteristic, or code.

**HSE addendum (this domain's extension — flagged for competent-person review):**

- **Aadhaar / national-ID numbers** and other government IDs.
- **Employee / payroll IDs** and badge numbers.
- **Job title + crew + shift combinations** (a powerful quasi-identifier on a
  small crew — see §3).
- **Exact incident location / asset tag** (e.g. "Tank-3, Bay 2") when tied to a
  small population.

## 3. Direct vs quasi-identifier test

- **Direct identifier** — identifies an individual *alone* (name, SSN/NI,
  Aadhaar, employee ID, email). **Rule: scrub directs always.**
- **Quasi-identifier** — identifies *in combination* (job title + shift + injury
  date + small site). **Rule: assess each quasi for re-identification risk in
  context — small crews are high-risk — and pseudonymize or generalize.** Flag
  any residual quasi-identifier risk you cannot fully neutralize as
  `[RESIDUAL-RISK]`.

## 4. Tiered handling model

| Tier | What it is | When appropriate | Block step |
|------|-----------|------------------|------------|
| **Identified** | Raw data with direct identifiers | Internal, access-controlled only; never circulated | Step 1 (detect) |
| **Pseudonymized** | Role labels + a separate key | Working documents that circulate internally | Step 2 |
| **Anonymized / aggregated** | No key, small cells aggregated | Anything widely distributed (boards, posters, public) | Steps 3 + 4 |

Move data to the *least-identifying* tier the purpose allows (§8).

## 5. Small-cell (<5) suppression + secondary suppression

- **Primary suppression:** never publish an injury/illness category with **fewer
  than 5 individuals**. Aggregate up (broader category, longer period, larger
  population) until each published cell ≥ 5, or suppress the cell.
- **Secondary suppression:** when you suppress one cell, suppress at least one
  more in the same row/column so the suppressed value cannot be **back-calculated
  from the row/column totals**.

**Worked mini-example.** A site reports total recordable injuries = 12, split:
Hands = 7, Eyes = 3, Back = 2. Eyes (3) and Back (2) are each < 5 → primary-
suppress both. Suppressing only Eyes would let a reader compute it from the
total (12 − 7 − 2 = 3), so **both** small cells are suppressed (secondary
suppression): publish "Hands = 7; other categories aggregated = 5 (suppressed,
small cells)".

## 6. Distribution / sharing warnings

Defaults by audience:

- **Internal working document** — pseudonymized; key held apart (§7).
- **Board / executive** — aggregated; no individual identifiable.
- **Frontline / toolbox** — de-identified, aggregated; no names.
- **Public / poster** — anonymized; no key exists.

Explicit trigger: **warn the user before any name or health detail enters a
widely shared artifact.** Remember that **screenshots and embedded photos leak
too** — a pasted 300 Log image or a face in a site photo defeats the text scrub.

## 7. Re-identification key handling

The de-identification process emits **two artifacts**: (a) the de-identified
document and (b) a **separate re-identification key**. The key — and any
name↔label mapping — is **never** embedded in, appended to, or footnoted within
the output document (consistent with deid block step 2).

- Store the key **access-controlled and physically/logically apart** from the
  document.
- **Do not transmit the document and the key together** (emailing both defeats
  the entire control).
- Limit who holds the key; destroy it when the lawful purpose ends.

## 8. Data minimization & purpose limitation

Collect and retain **only the personal data the task actually needs**. Prefer
keeping sensitive raw data out of external services where you can. Default-deny
on "nice to have" personal detail — if it does not change a control, an owner, or
a date, leave it out.

## 9. Jurisdiction quick-reference (mechanisms, not statute text)

*Mechanism pointers only — no statute bodies are reproduced here. For a live,
dated rule status, defer to the A3 knowledge base or a competent person.*

- **OSHA (US)** — the "privacy concern case" mechanism: a worker's name is kept
  *off* the OSHA 300 Log and held on a separate confidential list
  (**29 CFR 1904.29**). The default de-id behaviour *is* this posture.
- **GDPR (EU/UK)** — health data is **Art. 9** special-category data: it needs an
  explicit lawful basis / explicit consent; minimization and storage limitation
  apply; pseudonymization is a recognized *safeguard*, not anonymization.
- **India DPDP** — the **DPDP** Act 2023 + DPDP Rules (phased rollout): verifiable
  consent for personal-data processing and a breach-notification duty; treat
  health/injury detail as sensitive; obligations are tightening as rules notify.
- **Unknown jurisdiction** — apply the strictest default (pseudonymize +
  aggregate) and ask before relying on any specific legal basis.

## 10. Escalation / "ask a competent person" triggers

Stop and defer to a competent person when:

- a **cross-border transfer** of personal/health data is implied;
- there is a **genuine consent question** (whether consent exists or is valid);
- a **suspected data breach** has occurred or is alleged;
- the **legal basis** for processing is unclear and the output would rely on it.

This ties to the project's mandatory competent-person review disclaimer.
