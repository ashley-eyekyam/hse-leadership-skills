---
sme-review:
  personas:
    - role: "Regulatory Compliance Counsel / HSE Legal Specialist"
      expertise: "ISO 45001 6.1.3 (determination of legal & other requirements) + 9.1.2 (evaluation of compliance), multi-jurisdiction HSE law (UK HSWA/MHSWR, US OSH Act + 29 CFR, EU Framework Directive transposition), legal-register applicability determination, and India legacy-first statutory practice (state-form resolution deferred to the hse-india engine; OSH-Code transition)."
      lens: "Is every listed obligation actually APPLICABLE to the named activities (not a copy-paste reg an office never triggers), evidenced + owned + review-dated, and — for India — DEFERRED to hse-india after state detection rather than asserted with an invented national form number?"
modes:
  register:
    detected_by: "Q = the requested deliverable (a legal & compliance register for the named activities/jurisdictions) — single-output skill; this mode is always active"
    floor:
      - id: applicability-confirmed
        description: "Every listed obligation traces to a named in-scope activity — an inapplicable regulation the site never triggers is a FLAG (copy-paste register)"
        anchors: ['applicab', 'activit|scope|in-scope']
        min_matches: 2
      - id: india-deferred-not-minted
        description: "The India leg routes to hse-india after state detection — no invented national form number is minted here"
        anchors: ['hse-india|india-state-form-finder|factories-act-returns', 'defer|state detection|\[gap']
        min_matches: 2
      - id: citations-jurisdiction-correct
        description: "Each obligation cites the resolved jurisdiction's instrument (UK HSWA/MHSWR · US OSHA · etc.), not a generic or wrong-jurisdiction reference"
        anchors: ['hswa|mhswr|osha|jurisdiction', 'regulation|act|instrument']
        min_matches: 2
      - id: rows-complete-owner-review-dated
        description: "Every obligation row is complete — applicability rationale + compliance-evidence + named (role-label) owner + review date"
        anchors: ['owner', 'review date|review']
        min_matches: 2
      - id: compliance-evaluation-present
        description: "Compliance evaluation (ISO 45001 9.1.2) is present — gaps flagged with an owner and target date, never an unevidenced 'all compliant'"
        anchors: ['9.1.2|compliance evaluation', 'gap|target']
        min_matches: 2
---

# SME Review & Sign-off — legal-compliance-register

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a Regulatory Compliance Counsel / HSE Legal Specialist.
The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Applicability is CONFIRMED, not asserted — every obligation traces to a named in-scope activity; an inapplicable regulation listed for an activity the org does not perform (e.g. a construction reg for an office) is a FLAG.
- [ ] India is DEFERRED, not minted — the India leg routes to `hse-india` (`india-state-form-finder` / `factories-act-returns`) after mandatory state detection; a hard-coded national form number is a FLAG (and a citation hard-fail); an unverified state form must read `[GAP]`.
- [ ] Citations are real and jurisdiction-correct — each obligation cites the resolved jurisdiction's instrument (UK HSWA/MHSWR · US OSH Act/29 CFR · EU 89/391 transposition); an invented or mis-jurisdiction citation is a FLAG.
- [ ] Every obligation row is COMPLETE — applicability rationale + compliance-evidence cell + named (role-label) owner + review date; a bare obligation list with no evidence/owner/date is a FLAG.
- [ ] Compliance evaluation (9.1.2) is present — gaps are flagged with an owner and a target date, not silently omitted; an "all compliant" register with no evidence behind it is a FLAG.
- [ ] De-identification holds — named compliance owners + any enforcement/disciplinary detail are role-labelled in the shared register; a leaked name or disciplinary note is a FLAG (and a de-id hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The copy-paste obligation that never triggers (S6)** — a register padded with regulations the
  named activities never engage reads comprehensive but buries the applicable duties. Every row
  earns its place by tracing to a real in-scope activity, or it is removed.
- **The "all compliant" with no evidence (S5)** — a compliance-evaluation column of green ticks
  with no sighted evidence, no gap, and no owner is an assertion, not an evaluation. Each status
  cites its evidence or is flagged a gap with an owner and target date.
- **The India national-form mint** — asserting a single national Indian form/number instead of
  deferring to hse-india after state detection is the family's load-bearing error; the India leg
  routes onward and surfaces an unresolved form as [GAP], never a fabricated number.
- **The register that never gets re-evaluated** — obligations change; a register with no review
  date/cadence and no owner for the re-evaluation is a snapshot that silently goes stale.

## Sign-off note
SME review: ran (persona: Regulatory Compliance Counsel / HSE Legal Specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
