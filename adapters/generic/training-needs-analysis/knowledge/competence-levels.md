<!-- KB-DATA-COMPETENCE-LEVELS -->
# Competence levels — a 4-level scale with evidence tests

**Fragment ID:** `KB-DATA-COMPETENCE-LEVELS`
**What this is:** the shared **4-level competence scale** (aware → trained → competent →
expert) the `training-needs-analysis` (#13) and `induction-pack` (#14) skills use to band
a role's current-vs-required competence and to define the induction verification level.
Each level carries an **evidence test** — what proof demonstrates the level is held.
**What this is NOT:** a certification standard or a legal definition of "competence" in any
jurisdiction. Statutory competence requirements (e.g. UK MHSWR 1999 reg. 7 competent person,
US OSHA standard-specific qualified/competent-person definitions, India Factories Act 1948)
are resolved from the relevant regulatory fragment at use time. This scale is a consistent
**banding convention**, not a substitute for a named legal competence requirement.

> Source: ISO 45001:2018 cl. 7.2 (competence = education + training + experience, demonstrated) · UK HSE HSG65 competence framework · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## The 4-level scale (each level subsumes the ones below)

| Level | Label | What it means | Evidence test (the proof required) |
|---|---|---|---|
| 1 | **Aware** | Knows the hazard/requirement exists and who to ask; cannot perform unsupervised. | Attendance/induction record; a short knowledge check. |
| 2 | **Trained** | Has received the training/instruction and can perform under supervision. | Dated training record + assessor sign-off; supervised-practice log. |
| 3 | **Competent** | Can perform unsupervised, to the required standard, and adapt to foreseeable variation; meets the role's statutory competence requirement where one applies. | Independent assessment against defined criteria; portfolio/experience evidence; valid certification where the law names one. |
| 4 | **Expert** | Can set the standard, assess others, and resolve non-routine/abnormal situations. | Track record of assessing/mentoring; recognised qualification or accreditation; peer/regulatory recognition. |

**Required level is set by the role's risk, not the person.** A high-hazard task
(hot work, confined-space entry, LOTO, work at height) requires **level 3 (competent)**
with a current valid certification where the jurisdiction mandates one; a low-risk task
may require only level 1–2.

## How the skills use this fragment

- **#13 training-needs-analysis** bands each role×competence cell as current level vs
  required level; the gap (required − current) drives the prioritised training plan, and a
  cell where only one named person holds level 3 is a **single-point-of-failure** flag
  (reported by role, not identity — see the de-id discipline).
- **#14 induction-pack** sets the induction's **verification level** from this scale
  (an induction typically targets level 1–2; competence-critical roles route to a separate
  competence assessment, not the induction alone).
- An unmet **statutory** competence requirement is never downgraded to a lower band to
  "pass" — it is flagged against its named legal source.
