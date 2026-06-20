---
sme-review:
  personas:
    - role: "Skill-authoring SME / HSE standards reviewer"
      expertise: "The six-block skill contract, the Agent Skills open standard, the elicitation-coverage + SME-sign-off authoring rules, the hierarchy of controls, defensibility of HSE conclusions, and de-identification of sensitive data."
      lens: "would a competent HSE author accept this scaffolded skill — five blocks byte-identical to template/blocks/*, a real branched intake covering the must-ask dimensions, a domain-true SME persona, every reference resolving, zero de-id leak — or is it a generic, born-non-conformant stub?"
---

# SME Review & Sign-off — hse-skill-forge

The forge is the build-time authoring tool (plugin `hse-systems`); its "intake" is the
author-interview, not a runtime HSE intake — so it is exempt from the runtime
intake-coverage / sme-review structure checks (Rules 11/12). The orchestration block still
applies and is re-stamped by `--sync`, so this reference exists to satisfy the promoted
block's citation and to define the review lens for a forge-authored deliverable: the
scaffolded skill itself. The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] All five inline `hse:block:*` regions are BYTE-IDENTICAL to `template/blocks/*` (Rule 1 anti-drift) — a hand-edited block region is a FLAG.
- [ ] The scaffolded `references/intake.md` covers the must-ask dimensions (ELI-SCOPE / ELI-SUBJECT / ELI-OUTPUT) and justifies every omitted conditional — a blanket-stubbed or unjustified-omission intake is a FLAG.
- [ ] The SME persona is domain-true, not a generic placeholder left as TODO — a born-non-conformant emit that still carries scaffold TODOs into a shipped skill is a FLAG.
- [ ] Every `references/` path the SKILL.md cites resolves on disk (Rule 8) — a dead reference is a FLAG.
- [ ] The skill metadata resolves to a registered marketplace bundle and Apache-2.0 license — an unregistered plugin or wrong license is a FLAG.

## Sign-off note
SME review: ran (persona: Skill-authoring SME / HSE standards reviewer); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
