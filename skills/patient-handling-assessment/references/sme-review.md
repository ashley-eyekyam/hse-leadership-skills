---
sme-review:
  personas:
    - role: "Moving-and-Handling / Ergonomics Specialist (ANA SPHM / UK MHOR competent; back-care advisor)"
      expertise: "The UK Manual Handling Operations Regulations 1992 — reg 4(1)(a) avoid hazardous manual handling, reg 4(1)(b)(i) a suitable and sufficient assessment, reg 4(1)(b)(ii) reduce the risk, the Schedule 1 TILE factors (Task, Individual, Load, Environment), and reg 4(2) review; the ANA Safe Patient Handling and Mobility (SPHM): Interprofessional National Standards 2nd ed. (2021) eight standards and the move-toward-zero-manual-lift culture; NIOSH safe-lifting guidance (the recommended manual-lift limit; minimize manual patient lifting); ISO/TR 12296:2012 (ergonomics — manual handling of people in the healthcare sector); mechanical-aid selection (ceiling and mobile hoists, slings, slide sheets, transfer boards, stand-aids) and equipment safe-working-load (SWL); bariatric handling and environmental loading; post-fall handling; India factory/occupational-ergonomics provisions via hse-india; and the special-category-health-data (PHI) handling of patient mobility / dependency / diagnosis data and the worker's musculoskeletal / occupational-health record (GDPR Art. 9 / India DPDP / US HIPAA-aligned)."
      lens: "Does the assessment lead by avoiding the manual lift rather than lifting more carefully — is the avoid-the-manual-lift decision recorded BEFORE any equipment or technique, and is a 'two-person manual lift' recommended where a hoist or slide aid is reasonably available, or a 'use good technique / wear a back belt' headline, FLAGGED and pushed up the hierarchy? Are all four TILE elements (Task, Individual, Load, Environment) assessed? Is the mobility-and-equipment matrix (dependency level → equipment + handler count) present? Is the bariatric SWL + environmental loading addressed where it applies, and the post-fall handling plan present for a falls task? Is the patient assessed by de-identified mobility / dependency / weight band only — with no name, MRN, ward/bay, or diagnosis — and the worker's capability assessed under TILE Individual with no name or back-condition / OH record in the circulated copy? Is every <5 handling-injury category suppressed (including the secondary back-calculation), with ZERO leak and no re-identification key co-located or emitted as a file?"
modes:
  patient-handling-assessment:
    detected_by: Q9 — Output artifact wanted + its reader (full patient-handling risk assessment / handling-assessment summary + matrix / quick mechanical-aid + handler-count answer — all render the single handling assessment at the reader's depth)
    floor:
    - id: pha-avoid-manual-lift-first
      description: Avoiding the manual lift (ceiling / mobile hoist, slide sheet, transfer board) stated as the primary control before technique — the move-toward-zero-manual-lift principle (intake Q2; ANA SPHM / KB-STD-SPHM)
      anchors:
      - avoid.{0,20}manual|move.toward.zero
      - hoist
      - slide sheet|transfer board|mechanical aid
      min_matches: 1
    - id: pha-tile-four-elements
      description: A four-element TILE assessment of the residual handling — Task, Individual, Load, Environment (intake Q3; MHOR Schedule 1 / KB-REG-UK-MHOR; a TILE missing any element is not suitable and sufficient)
      anchors:
      - \bTILE\b
      - suitable and sufficient
      - Task, Individual, Load|Individual.{0,8}Load.{0,8}Environment
      min_matches: 1
    - id: pha-mobility-equipment-matrix
      description: A mobility-and-equipment matrix — the patient's dependency level mapped to matched equipment + number of handlers (intake Q4, the core artifact; a two-person manual lift where a hoist is available is FLAGGED)
      anchors:
      - mobility.{0,4}equipment|equipment matrix
      - dependency
      - number of handlers|handler count
      min_matches: 1
    - id: pha-bariatric-falls
      description: The bariatric / falls dimension where present — equipment safe-working-load (SWL), environmental loading, or a post-fall handling plan (intake Q5)
      anchors:
      - bariatric
      - safe.working.load|\bSWL\b
      - falls|post.fall
      min_matches: 1
    - id: pha-patient-deid
      description: The patient assessed by de-identified mobility / dependency / weight band only — never name, ward/bay, or diagnosis; the worker role-labelled with any back-condition record held separately (intake PHI gate)
      anchors:
      - de.identif
      - dependency|mobility|weight band
      - role.label|worker
      min_matches: 1
    - id: pha-owner-review
      description: Named action owner(s) + a competent moving-and-handling / ergonomics-specialist verifier + a review cycle (annual / on-change-of-task-or-patient / on-incident) (intake Q10/Q11)
      anchors:
      - owner
      - review
      - moving.and.handling|ergonomic
      min_matches: 1
---

# SME Review & Sign-off — patient-handling-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Moving-and-Handling / Ergonomics Specialist** (ANA SPHM / UK MHOR
competent; back-care advisor). The universal hard gates (de-id leak, citation accuracy,
HoC/no-behaviour-led, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The avoid-the-manual-lift decision is recorded FIRST, before any equipment or technique** —
      the assessment leads with avoiding the manual lift / a mechanical aid (`KB-SNIP-TILE-PEOPLE`,
      move-toward-zero); a "two-person manual lift" recommended where a hoist or slide aid is
      reasonably available, or a "use good technique / wear a back belt" treatment, is the headline
      failure, surfaced by `controls.validate_treatment` (`ppe_admin_only=True`) and pushed up the
      hierarchy.
- [ ] **All four TILE elements are assessed** — Task, Individual, Load, and Environment; a TILE
      assessment missing any element is not suitable and sufficient and is rejected.
- [ ] **The mobility-and-equipment matrix is present and correct** — the patient's mobility /
      dependency level maps to the matched equipment and the correct number of handlers; the matrix is
      the core artifact, never omitted.
- [ ] **The bariatric / falls plan is complete where it applies** — a bariatric move addresses
      equipment SWL and environmental loading; a falls task has a post-fall handling plan.
- [ ] **Technique and PPE are the documented last lines** — never the primary control; technique is an
      administrative measure and a back belt is PPE, residual after avoiding the lift, mechanical aids,
      and safe systems of work.
- [ ] **The patient + the worker are de-identified** — the patient is recorded by de-identified
      mobility / dependency / weight band only (no name, MRN, ward/bay, diagnosis); the worker is a
      role label with no back-condition / OH record in the circulated copy; no `<5` handling-injury
      cell, and no embedded / co-located re-identification key (and no key file) in the circulated
      artifact (a leak is a non-waivable `de_identification` hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The avoid-the-manual-lift duty skipped** — a professional-looking assessment can jump straight to "safe technique" and a handler count without recording whether a hoist / slide aid removes the manual lift first (MHOR reg-4 avoid duty / SPHM move-toward-zero).
- **A TILE assessment missing an element** — Individual (worker capability, number of handlers) and Environment (space, floor, bed/chair height, ceiling-track) are the ones quietly dropped; a TILE without all four is not suitable and sufficient.
- **The patient identified** — a "bariatric, fully-dependent patient on Ward 4 bay 2" re-identifies; the patient must be reduced to de-identified mobility / dependency / weight band, the worker role-labelled, and any back-condition / OH record held separately.

## Sign-off note
SME review: ran (persona: Moving-and-Handling / Ergonomics Specialist); this is **decision-support
only**. It **precedes — and never replaces — the human competent-person review**, and it never outputs
the affirmative claim that the work is approved. A FLAG it raises is recorded, never merge-blocking;
the deterministic hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
