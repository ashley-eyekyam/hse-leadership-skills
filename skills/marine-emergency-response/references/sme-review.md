---
sme-review:
  personas:
    - role: "Competent HSE practitioner (generic SME reviewer)"
      expertise: "General HSE law and standards, the hierarchy of controls, defensibility of conclusions, and de-identification of sensitive data."
      lens: "would a regulator accept this — every control specific to the named task/site/asset, higher-order controls before PPE/admin, every claim traced to a cited source, named owners and review dates, zero de-id leak"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (a marine/offshore emergency-response assessment for the named installation) — single-output skill; this mode is always active"
    floor:
      - id: escalation-prevention-tr-integrity
        description: "The lead posture is escalation prevention and temporary-refuge integrity, not abandonment-first"
        anchors: ['escalation|prevention', 'temporary refuge|tr integrity|refuge']
        min_matches: 1
      - id: eer-hierarchy-escalation-first
        description: "The EER hierarchy puts escalation control first and abandonment last"
        anchors: ['eer', 'escalation|abandon|hierarchy']
        min_matches: 2
      - id: tempsc-capacity-vs-pob
        description: "TEMPSC / survival-craft capacity is checked against the POB — a capacity shortfall is a FLAG"
        anchors: ['tempsc|survival craft|lifeboat', 'pob|capacity']
        min_matches: 2
      - id: muster-pob-station-bill
        description: "Muster, POB accounting and the station bill are specified for the installation"
        anchors: ['muster|pob', 'station bill|accounting']
        min_matches: 2
      - id: residual-scored
        description: "Residual risk is re-scored (5x5) after the escalation/EER controls"
        anchors: ['residual', '5×5|5x5|score']
        min_matches: 1
      - id: smart-gap-closure-owned
        description: "Recommendations are SMART, close every [GAP], and carry role-label owners and dates"
        anchors: ['smart|recommendation', 'owner|role|date|\[gap']
        min_matches: 2
      - id: cross-reference-sibling
        description: "The safety-case / offshore siblings are cross-referenced (EER not rebuilt in isolation)"
        anchors: ['cross.referenc', 'offshore|safety.case|eer']
        min_matches: 1
---

# SME Review & Sign-off — marine-emergency-response

<!-- TODO: author — this is a born-conformant SME-review stub. Replace the generic
     HSE-SME-Reviewer persona's lens and the checklist items below with the nuanced,
     domain-specific things only this skill's expert would catch. Add a 2nd persona
     (max 2) only where the domain genuinely needs two distinct expert views. -->

## Domain checklist (the nuanced things only this expert catches)
- [ ] TODO: every control is specific to the named task / site / asset — no generic controls
- [ ] TODO: hierarchy of controls applied — no PPE/admin-only treatment without a higher-order control justified or escalated
- [ ] TODO: every conclusion traced to evidence (cited source + year); actions have named owners and review dates

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The survival-craft shortfall with no bridge (S2)** — a TEMPSC/POB capacity gap acknowledged
  but with no interim manning/mitigation for the shortfall period is an accepted risk dressed as a
  plan. Surface the shortfall and its interim measure.
- **The record identity of muster (S8)** — the station bill, POB accounting method, and muster
  points must tie to the installation's real arrangement; a generic muster narrative cannot run on
  the day.
- **The escalation regime named, its barriers unswept (S6)** — naming "temporary-refuge integrity"
  while omitting the TR impairment criteria, the EER decision triggers, and the escalation barriers
  that must hold leaves the posture asserted, not demonstrated.
- **Sibling boundary** — the safety-case / offshore analysis is cross-referenced, not rebuilt here.

## Sign-off note
SME review: ran (persona: Competent HSE practitioner (generic SME reviewer)); this is
decision-support; competent-person review still required. A FLAG it raises is recorded,
never merge-blocking — it precedes and never replaces the human competent-person review.
