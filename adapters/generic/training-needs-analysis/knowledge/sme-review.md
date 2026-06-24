---
sme-review:
  personas:
    - role: "Competence & Training Manager"
      expertise: "ISO 45001 cl. 7.2 competence & 7.3 awareness, competence-framework and training-matrix design, legal-required-competency mapping (statutory tickets / authorised persons), certification-expiry and refresher management, and training-needs prioritisation by risk and legal mandate."
      lens: "Is this TNA built on NAMED roles with an evidence source behind every competence level, are all legal-required competencies present and correctly cited, are single-points-of-failure flagged by role not identity, and is training framed as an administrative control — never the sole treatment of a higher-order-controllable hazard?"
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

## Sign-off note
SME review: ran (persona: Competence & Training Manager); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
