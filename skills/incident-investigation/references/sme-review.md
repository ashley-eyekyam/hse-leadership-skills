---
sme-review:
  personas:
    - role: "ICAM/TapRooT-trained lead incident investigator"
      expertise: "Serious-incident & SIF investigation, the 5 RCA methods (5-Whys/ICAM/SCAT/Fishbone/Swiss-Cheese), human-factors & latent-organisational-failure analysis, evidence discipline and chain-of-custody."
      lens: "Does the RCA reach a SYSTEMIC/organisational factor (not stop at 'worker error'), is every cause traced to a numbered evidence item, and were all personal identifiers scrubbed to role labels before any echo-back or draft?"
    - role: "HSE regulatory-reportability specialist"
      expertise: "RIDDOR 2013, OSHA 29 CFR 1904 recordkeeping + 1904.39 fatality/in-patient/amputation timelines, India state accident-notice forms and the OSH-Code 2020 transition; conservative notifiability judgement."
      lens: "Is the reportability verdict correct, conservative, and cited to the right rule/form/deadline — surfaced even when the conclusion is NOT reportable — with the India state resolved before any form is named?"
modes:
  investigation:
    detected_by: "Q8 — RCA method preference (5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese); Q4 severity drives reportability urgency. The floor applies to every investigation."
    floor:
      - id: deid-before-analysis
        description: "The de-identification pass ran BEFORE the echo-back and drafting — the echo and draft carry role labels only, never raw names/addresses/small-cell identifiers (a leak is a hard fail, not a FLAG) (intake Q5)"
        anchors: ['de.identif', 'role label|pseudonym']
        min_matches: 1
      - id: rca-reaches-system
        description: "The RCA reaches a systemic/organisational factor and does not stop at 'worker error' — method-specific (ICAM organisational factor, Swiss-Cheese latent layer, a 5-Whys terminal that is not 'careless/forgot') (intake Q8)"
        anchors: ['organi[sz]ational|systemic|latent']
        min_matches: 1
      - id: cause-evidence-ref
        description: "Every cause carries an evidence reference (evidence before cause, cause before control); an un-evidenced cause promoted to 'root' is a miss (intake Q7)"
        anchors: ['evidence', 'root cause']
        min_matches: 2
      - id: immediate-contributing-root-distinct
        description: "Immediate vs contributing vs root causes are not conflated — the causal chain is layered, not flattened"
        anchors: ['immediate cause', 'contributing', 'root cause']
        min_matches: 2
      - id: reportability-surfaced
        description: "The reportability verdict is surfaced even when NEGATIVE, cited to the right rule/form/deadline; a silent non-report or a missed notification trigger is the most serious miss (intake Q9)"
        anchors: ['reportab', 'riddor|osha 1904|notif|form']
        min_matches: 1
      - id: india-state-before-form
        description: "For India, the state is resolved before any accident form is cited — an un-seeded state resolves to [GAP], never a fabricated national form (intake Q9a)"
        anchors: ['\[GAP\]', 'state|national form']
        min_matches: 1
---

# SME Review & Sign-off — incident-investigation

Two distinct professions own two distinct failure modes here, so this skill carries
**two** SME lenses: causal-analysis *depth* (lead investigator) and regulatory
*reportability* (compliance/legal). Both specialize the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`); the first lens also narrows the mining-pack Mine
Manager archetype's "RCA reaches organisational factors" check. The universal hard
gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are deliberately not restated below.

**De-identification is a non-waivable HARD gate for this skill.** The Q5 people-involved
scrub runs *before* echo-back and before any drafting, so every echo and every draft
shows stable role labels ("Worker A", "W-1") and never a raw name. A de-id leak is a
hard fail, not a FLAG.

## Domain checklist (the nuanced things only this expert catches)
- [ ] De-id pass ran BEFORE the echo-back and before drafting — the echo and the draft carry role labels only ("Worker A", "W-1"), never raw names, addresses, or small-cell (<5) identifiers; a leak is a hard fail, not a FLAG.
- [ ] RCA reaches the system — method-specific test: a 5-Whys terminal why is not "careless/forgot"; ICAM has ≥1 Organisational Factor; SCAT has Basic Causes *and* Lack-of-Control; Fishbone has ≥1 non-"Man" branch; Swiss-Cheese names a latent organisational layer. A "valid but shallow" RCA is a FLAG.
- [ ] Every cause carries an evidence_ref, root causes especially — any un-evidenced cause promoted to "root" is a FLAG; evidence comes before cause, cause before control.
- [ ] Reportability is surfaced even when negative — a silent non-report is a FLAG; a missed notification trigger (e.g. an amputation under OSHA 1904.39's 24h clock) is the most serious FLAG.
- [ ] India: the state is resolved before any form is cited — a form named without a confirmed state, or inferred from an address, is wrong-form risk; an un-seeded state resolves to `[GAP]`, never a fabricated national form.
- [ ] Immediate vs contributing vs root causes are not conflated, and an optional single-event contextual rate (if Q3∈{injury,illness}) uses real hours+counts only and is framed as context — never a fabricated denominator and never used as a conclusion.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **RCA that stops at the sharp end** — the analysis terminates at "operator error /
  did not follow procedure" without reaching the organisational factor (why the procedure
  was unworkable, unenforced, or absent); a valid-but-shallow RCA.
- **Incident-history silence** (canary S3) — no check of whether this event (or a close
  precursor) has happened before, nor confirmation of its absence; a recurring failure
  investigated as if it were the first.
- **Cause without evidence** — a cause, especially a root cause, asserted with no numbered
  evidence item behind it; conclusions that outrun the evidence log.
- **Reportability by silence** (canary S6) — the notification duty neither confirmed nor
  ruled out against the regime's actual triggers/deadlines (RIDDOR, OSHA 1904.39, the India
  state form); the most serious omission is a missed clock.
- **Corrective actions that do not follow the causes** — recommendations that fix the
  immediate cause but leave the systemic/organisational factor the RCA found untreated.

## Sign-off note
SME review: ran (personas: ICAM-trained lead investigator + HSE regulatory-reportability
specialist); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
