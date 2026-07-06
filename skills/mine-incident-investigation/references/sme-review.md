---
sme-review:
  personas:
    - role: "mining-incident lead investigator (ICAM-trained / DGMS-court-of-inquiry experienced)"
      expertise: "ICAM (default) + 5-Whys/SCAT/Fishbone/Swiss-Cheese, mine-accident evidence reconstruction, DGMS reportability (24h notice + Form J), organisational-factor causation"
      lens: "Does the RCA reach genuine organisational/systemic causes (not stop at 'the miner erred'), is every cause evidence-backed, and is the DGMS reportability verdict conservative and zone-correct?"
modes:
  investigation:
    detected_by: "Q1 — Outcome (Full investigation + RCA / RCA only / DGMS reportability check / CAPA from a finding); Q8 sets the RCA method (ICAM default). The floor applies to every investigation output."
    floor:
      - id: deid-scrub-before-analysis
        description: "Names become role labels and exact pit/shaft locations are scrubbed BEFORE any analysis; <5 cells suppressed. A re-identification is a de-id hard-fail, not a FLAG (intake Q5/Q6)"
        anchors: ['de.identif|role label']
        min_matches: 1
      - id: rca-reaches-organisational
        description: "The RCA reaches a systemic/organisational factor and never stops at 'the miner erred' — the ICAM organisational-factor tier is populated (intake Q8)"
        anchors: ['organi[sz]ational', 'systemic|latent', 'icam']
        min_matches: 2
      - id: cause-evidence-traceability
        description: "Every causal claim cites a numbered evidence item (E-n) and every corrective action traces to a named cause (RC-n) with owner + due date — no unsupported cause, no orphan CAPA (intake Q7)"
        anchors: ['evidence', 'rc-[0-9]|cause']
        min_matches: 2
      - id: absent-failed-critical-controls
        description: "The absent or failed critical controls (e.g. strata support) are identified — the control-failure analysis, not just a causal narrative"
        anchors: ['critical control', 'absent|failed']
        min_matches: 2
      - id: dgms-reportability-conservative
        description: "The DGMS reportability verdict is conservative and zone-correct — verdict + clause + deadline + the right anchor, zone resolved first; an over-confident verdict where the category is uncertain is a miss (intake Q3/Q4)"
        anchors: ['reportab', 'dgms', 'zone']
        min_matches: 2
      - id: mining-mechanism-coherent
        description: "The mining mechanism is physically coherent with the evidence (a strata/inrush/irrespirable-atmosphere sequence), not a generic slip/trip narrative"
        anchors: ['strata|inrush|roof|fall of ground']
        min_matches: 1
      - id: corrective-actions-hoc
        description: "Corrective and preventive actions are hierarchy-of-controls-ranked, each with a role owner and due date"
        anchors: ['corrective', 'hierarchy of controls|hoc']
        min_matches: 1
---

# SME Review & Sign-off — mine-incident-investigation

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — its "RCA reaches organisational factors
… not 'miner error' as the terminal cause" bullet, archetypes:311-312, plus the
DGMS-form bullet, archetypes:299-302) to the mining specialization of the B5
flagship investigator lead. The de-id-first 4-agent roster already discharges most
universal gates; this persona's added value is organisational-causation depth and
DGMS conservatism.

**Personnel de-identification is mandatory before this persona reviews.** Injured /
deceased miners, witnesses, the rescue team and bystanders are carried as **role
labels only** (never names); exact pit/shaft locations are scrubbed; small (<5)
fatality/injury cells are suppressed. A re-identification is a de-id hard-fail
(distinct from a FLAG) — confirm the draft reached this review already de-identified.

## Domain checklist (the nuanced things only this expert catches)
- [ ] RCA reaches a systemic/organisational factor, not 'miner error' — confirm `rca.validate reaches_systemic` is true for the chosen method; FLAG any RCA terminating at unsafe-act / individual blame.
- [ ] ICAM is the applied default and its categories are populated — absent/failed defences, individual/team actions, task/environment conditions, **organisational factors**; FLAG an "ICAM" analysis missing the organisational-factor tier.
- [ ] Every causal claim cites a numbered evidence item (E-n) and every CAPA traces to a named cause (RC-n) with owner + due date; FLAG an unsupported cause or an orphan CAPA.
- [ ] DGMS reportability is verdict + clause + deadline + the right anchor, conservatively — zone resolved first; FLAG an over-confident verdict where the category is uncertain ("ask a competent person").
- [ ] `incident_rates` stays context-only — no headline TRIR/LTIFR computed unless hours+counts supplied; FLAG a fabricated/asserted rate.
- [ ] The mining mechanism is correctly reasoned — an inrush/strata/irrespirable-atmosphere sequence is physically coherent with the evidence, not a generic "slip/trip" narrative; FLAG a timeline that does not match the named mining hazard mechanism.
- [ ] Personnel de-identification held end-to-end — names→role labels, exact pit/shaft locations scrubbed, <5 cells suppressed; a re-identification is a de-id hard-fail (forces a fix), not a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **RCA that stops at 'the miner erred'** — the analysis terminates at the unsafe act
  without reaching the organisational/latent factor (why the strata-support standard was
  unworkable, unenforced, or absent).
- **Incident-history silence** (canary S3) — no review of prior strata/inrush/gas events at
  this mine or seam, nor confirmation of their absence; a recurring geotechnical failure
  investigated as a first occurrence.
- **The mechanism that does not fit the evidence** — a timeline that reads like a generic
  slip/trip rather than a coherent fall-of-ground / inrush / irrespirable-atmosphere sequence
  consistent with the gas readings, strata log, or survey.
- **Reportability by silence** (canary S6) — the DGMS notification duty neither confirmed
  nor ruled out against the zone's actual triggers/deadlines; the most serious omission is a
  missed statutory clock, and an over-confident verdict on an uncertain category is its twin.
- **Cause without evidence, action without cause** — a root cause with no numbered evidence
  behind it, or a CAPA that traces to no named cause.

## Sign-off note
Reviewed-as: mining-incident lead investigator (ICAM) — model QA (decision-support);
recorded, FLAGs non-blocking. This review precedes — and never replaces, never emits
— the DGMS-qualified competent-person review / statutory inquiry; it never outputs
"approved by a competent person".
