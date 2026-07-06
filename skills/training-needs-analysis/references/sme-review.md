---
sme-review:
  personas:
    - role: "Competence & Training Manager"
      expertise: "ISO 45001 cl. 7.2 competence & 7.3 awareness, competence-framework and training-matrix design, legal-required-competency mapping (statutory tickets / authorised persons), certification-expiry and refresher management, and training-needs prioritisation by risk and legal mandate."
      lens: "Is this TNA built on NAMED roles with an evidence source behind every competence level, are all legal-required competencies present and correctly cited, are single-points-of-failure flagged by role not identity, and is training framed as an administrative control — never the sole treatment of a higher-order-controllable hazard?"
modes:
  tna:
    detected_by: "Q = the requested deliverable (a training needs analysis for the named roles) — single-output skill; this mode is always active"
    floor:
      - id: named-roles-not-everyone
        description: "The matrix is built on named roles + headcounts, never a blanket 'everyone' — a role-less TNA is a FLAG"
        anchors: ['role', 'headcount|matrix|per role']
        min_matches: 2
      - id: gap-evidence-traced
        description: "Each competence level is banded from a named evidence source — a gap with no evidence basis is a FLAG"
        anchors: ['competenc', 'evidence|banded|source']
        min_matches: 2
      - id: legal-required-competencies-cited
        description: "Every statutory/legal-required competence for the roles is present and correctly cited"
        anchors: ['legal.required|statutory|mandatory', 'competenc|certificat']
        min_matches: 2
      - id: no-statutory-gap-downgraded
        description: "An unmet legal-required competence is never scored green — a statutory gap downgraded to conformant is a FLAG"
        anchors: ['statutory|legal.required', 'gap|blocker|red']
        min_matches: 2
      - id: spof-by-role-not-identity
        description: "A critical competence held by a single person is flagged as a single-point-of-failure by ROLE, not by identity"
        anchors: ['single.point|spof|single point of failure', 'role']
        min_matches: 2
      - id: training-as-admin-control
        description: "Training is framed as an administrative control, never the sole treatment of a higher-order-controllable hazard"
        anchors: ['administrative control|hierarchy', 'training']
        min_matches: 2
      - id: expiry-refresher-tracker
        description: "Time-limited statutory certificates carry an expiry/refresher tracker with dates — a cert with no expiry/refresher is a FLAG"
        anchors: ['expiry|refresher|certificat', 'tracker|expir|renew|date']
        min_matches: 2
---

# SME Review & Sign-off — training-needs-analysis

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Competence & Training Manager**. The universal hard gates
(de-id leak, citation accuracy, HoC/no-admin-only, owned-and-dated actions) are the enforced
class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Named roles, not "everyone"** — the matrix is built on named roles + headcounts; a TNA
      that treats the workforce as an undifferentiated "everyone" is a FLAG.
- [ ] **Every gap is evidence-traced** — each competence level is banded from a named evidence
      source; a level asserted with no evidence (and not flagged `[GAP]`) is a FLAG.
- [ ] **Legal-required competencies present + cited** — every statutory competence for the
      roles in scope is a matrix row, cited to its named legal source; a missing or
      "passed-over" statutory competence (e.g. scaffold-inspection competent person, LOTO
      authorised person) is a FLAG.
- [ ] **No statutory gap downgraded to green** — an unmet legal-required competence scored as
      "met" to avoid a gap is a FLAG.
- [ ] **Single-points-of-failure flagged by role, not identity** — a critical competence held by
      only one person must be flagged with a cross-training action, reported by role label; a
      SPOF that names the individual, or that is missed entirely, is a FLAG.
- [ ] **Training is an administrative control, not the sole treatment** — "more training" offered
      as the only control of a hazard that admits a higher-order control (without justification)
      is a FLAG.
- [ ] **Required levels reflect task risk** — a high-hazard task whose required competence is
      banded below level 3 (competent) to make the matrix look better is a FLAG.
- [ ] **Expiry tracker complete** — time-limited statutory certificates with no expiry/refresher
      date are a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The "everyone needs training" TNA** — a plan that offers blanket training with no named roles,
  no headcounts, and no current-vs-required gap per role is not an analysis; it is a course
  catalogue. Build the matrix on named roles.
- **The statutory gap painted green (S2)** — an unmet legal-required competence (e.g. an expired
  statutory ticket) scored as adequate hides a compliance-blocker behind a comfortable colour.
  Classify statutory gaps as blockers, not minor items.
- **Training as the sole treatment** — offering "more training" as the primary control for a
  hazard that is eliminable/engineerable inverts the hierarchy; training is an administrative
  control, a backstop, not the fix.
- **The invisible single-point-of-failure and expiry cliff** — a critical competence held by one
  person, or a statutory certificate with no expiry/refresher tracker, is a resilience gap that a
  role-labelled SPOF register and a dated expiry tracker surface.

## Sign-off note
SME review: ran (persona: Competence & Training Manager); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
