---
sme-review:
  personas:
    - role: "Competent HSE practitioner (generic SME reviewer)"
      expertise: "General HSE law and standards, the hierarchy of controls, defensibility of conclusions, and de-identification of sensitive data."
      lens: "would a regulator accept this — every control specific to the named task/site/asset, higher-order controls before PPE/admin, every claim traced to a cited source, named owners and review dates, zero de-id leak"
modes:
  default:
    detected_by: always
    floor:
      - id: todo-1
        description: "TODO — author the must-include item"
        anchors: ["TODO"]
        min_matches: 1
      - id: todo-2
        description: "TODO — author the must-include item"
        anchors: ["TODO"]
        min_matches: 1
      - id: todo-3
        description: "TODO — author the must-include item"
        anchors: ["TODO"]
        min_matches: 1
---

# SME Review & Sign-off — <skill>

<!-- TODO: author — this is a born-conformant SME-review stub. Replace the generic
     HSE-SME-Reviewer persona's lens and the checklist items below with the nuanced,
     domain-specific things only this skill's expert would catch. Add a 2nd persona
     (max 2) only where the domain genuinely needs two distinct expert views. -->

## Domain checklist (the nuanced things only this expert catches)
- [ ] TODO: every control is specific to the named task / site / asset — no generic controls
- [ ] TODO: hierarchy of controls applied — no PPE/admin-only treatment without a higher-order control justified or escalated
- [ ] TODO: every conclusion traced to evidence (cited source + year); actions have named owners and review dates

## Omission lens
<!-- TODO: author the skill-specific blind-spot hints + mode floor — replace the
     todo-* placeholder floor items in the modes: frontmatter with 4-8 real
     must-include items derived from this skill's KB rows / jurisdiction triggers /
     intake facets (derive-don't-duplicate), and add per-mode blind-spot hints
     below. Multi-output skills add one mode per intake-detectable output; single-
     output skills keep the one `default` mode (detected_by: always). -->
After the checklist pass, run the unconstrained omission pass per the single-source
protocol `KB-SNIP-COMPLETENESS` (knowledge-base/prompt-snippets/completeness-lens.md):
for the detected
mode, list what a competent expert of this domain would have included that is ABSENT,
then refute or surface each as a `[GAP]`. Never restate the protocol here — reference it.

## Sign-off note
SME review: ran (persona: Competent HSE practitioner (generic SME reviewer)); this is
decision-support; competent-person review still required. A FLAG it raises is recorded,
never merge-blocking — it precedes and never replaces the human competent-person review.
