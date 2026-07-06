---
sme-review:
  personas:
    - role: "Statutory accident-notification / inspectorate-liaison specialist (factory + mine/DGMS routing)"
      expertise: "the state Factories-Rules accident-notice forms + registers; the 24-hour notification deadline; dangerous-occurrence vs serious vs fatal triggers; the receiving inspectorate/authority; the mine/DGMS cross-layer (Mines Act / DGMS — KB-REG-IN-MINES-ACT / KB-REG-IN-DGMS, 24h notice + Form J register, region/zone resolution) where the establishment is a mine"
      lens: "is the RIGHT notice form + deadline assembled for the resolved state and establishment type, with the 24h timing load-bearing — and, for a mine, is it routed through the resolved DGMS region and the mining layer, NOT a state-Factories form?"
modes:
  accident-notice:
    detected_by: "Q0 = India + Q2 = establishment type (Factory / Mine) → assemble the statutory accident notice for the resolved state (and, for a mine, the resolved DGMS region)"
    floor:
      - id: state-or-dgms-region-resolved
        description: "The state (and, for a mine, the DGMS region/zone) is resolved before any notice form is cited — a mine notice without a resolved DGMS region is a FLAG"
        anchors: ['dgms region|dgms regional|dgms zonal', 'mines act']
        min_matches: 1
      - id: twentyfour-hour-deadline-owned
        description: "The 24-hour notification deadline is surfaced as load-bearing and owned (named role + explicit date) — a notice with no explicit deadline/owner is a FLAG"
        anchors: ['24.hour|24h|twenty-four', 'deadline|by 6 july|mine manager']
        min_matches: 2
      - id: form-j-verified-anchor
        description: "The verified anchors — the 24h DGMS notice duty and the Form J accident/dangerous-occurrence register entry — are cited (grounded in the Mines Act / Mines Rules)"
        anchors: ['form j', 'verified anchor|register entry']
        min_matches: 1
      - id: dgms-form-id-gap-never-invented
        description: "The un-verified numbered DGMS accident-notice form id is a literal [GAP], never invented — a fabricated form number passes the row-blind grader but fails DGMS"
        anchors: ['\[gap', 'not.{0,12}(assum|verified|invent)|must not be assumed|never.{0,15}invent']
        min_matches: 2
      - id: mine-routing-dgms-not-factory
        description: "A mine incident is routed through the DGMS / Mines-Act layer, NOT the state-Factories form; mixing the two layers is a FLAG"
        anchors: ['dgms', 'mines act']
        min_matches: 2
      - id: no-rca-defers-incident-investigation
        description: "The artifact assembles the NOTICE only and defers the root-cause analysis to incident-investigation — asserting cause/blame beyond the notice particulars is a FLAG"
        anchors: ['incident-investigation', 'root.cause|rca|root-cause']
        min_matches: 2
      - id: deid-role-labels-suppressed
        description: "The injured party/witness are role labels; diagnosis is treated as highest-sensitivity and small (<5) injury cells are suppressed before entering the notice"
        anchors: ['role label|\(role\)', 'suppress|withheld|aggregat']
        min_matches: 2
      - id: osh-code-duty-retained
        description: "The OSH-Code transition note correctly states the accident-notification duty PERSISTS (is retained), not removed, under the consolidated regime"
        anchors: ['osh code', 'retained|persists']
        min_matches: 2
---

# SME Review & Sign-off — india-accident-notice

This is an **always-India** skill that assembles the filled statutory accident /
dangerous-occurrence notice. `ELI-JURIS` is the spine: the state (and, for a mine, the DGMS
region) must be resolved and confirmed BEFORE any notice form is cited — a wrong state is a
wrong statutory form, and a mine routes to a *different statutory layer* entirely. **One lens**
carries both the factory accident-notice surface and the mine/DGMS routing fork: the
establishment-type branch is a check *inside* this specialist's review, not a second profession
— the specialist who knows the state Factories-Rules notice also knows that a mine notice must
leave the factory layer and route through DGMS (24h notice + Form J), so the fork is one
coherent inspectorate-liaison competence. The persona **narrows** the `India-Regulatory`
SME-persona archetype (`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation
accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated
below.

**Row-blind-grader catch (load-bearing).** The citation grader checks only that the fragment ID
resolves, not that a form *value* is real — so a plausible-but-wrong notice form passes the
automated gate but fails a regulator. This SME pass is the catch: every claimed accident-notice
form id and deadline is carried forward `[GAP]` to verify against the live state Factories Rules
and Mines Rules, never asserted as ground truth.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **State (and, for a mine, DGMS region) resolved BEFORE any notice form is cited** — the notice form + deadline are state/region-specific; a form cited on an unconfirmed state, or a mine notice without a resolved DGMS region/zone, is FLAGged. An unseeded/unknown state → literal `[GAP]`, never a fabricated national form.
- [ ] **The 24-hour deadline is the load-bearing, owned-and-dated action** — every follow-up notification action carries a named owner + a deadline, and the **24h timing** is surfaced as load-bearing. A notice without an explicit deadline/owner is FLAGged.
- [ ] **Severity correctly drives the form + deadline** — fatal / serious / dangerous-occurrence maps to the correct form; a severity-form mismatch is FLAGged. **[GAP — verify the claimed state forms (MH Form 24/24A, TN Form 18 + Form 26 register, DL Form 23/27) and the mine Form J / DGMS 24h notice against the live state Factories Rules and Mines Rules; do not assert. NOTE: the KB seeds ONLY the MH accident-notice row — the claimed TN Form 18/26 and DL Form 23/27 must stay literal `[GAP]`, never emitted as real values, until the owner verifies and seeds the rows.]**
- [ ] **Mine routing uses the DGMS layer, not the state-Factories form** — a mine incident is notified under `KB-REG-IN-MINES-ACT`/`KB-REG-IN-DGMS` (24h notice + Form J), not the factory state form; mixing the two layers is FLAGged. The unverified DGMS form id stays a literal `[GAP]`.
- [ ] **No RCA performed — defers to `incident-investigation`** — the artifact assembles the *notice*, not a root-cause analysis; an output that asserts cause/blame beyond the notice's required particulars is FLAGged and routed onward.
- [ ] **Injured-party / witness de-id holds; diagnosis + small cells suppressed** — names→role labels, diagnosis treated as highest-sensitivity, <5 injury cells aggregated before they enter the notice. (A leak is a hard-fail, distinct from a FLAG.)
- [ ] **OSH-Code note: accident-notice duty retained** — the transition note correctly states the notification duty *persists* (not removed) under the consolidated regime.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The incomplete notification chain (S1)** — the statutory notice goes to the inspectorate,
  but the parallel duties (the internal control-room / management alert, next-of-kin, the
  workers'-compensation insurer, and scene-preservation for the inspector) are silently dropped.
  Name each downstream notification/preservation duty, or state it is not applicable.
- **The regime named, its paired duties unswept (S6)** — citing "Mines Act / DGMS" while omitting
  the duties that regime pairs with the notice: the Form J register entry, the statutory Mine
  Manager/Agent as notifier, and the dangerous-occurrence classification test. Cite the anchor AND
  sweep its element set.
- **The notice with no dated, located basis (S8)** — incident date and time, the exact
  seam/level/location (or an honest "held in the mine record"), and the establishment/region
  identity tie the notice to a filed basis; a notice missing when/where cannot be actioned.
- **Inventing particulars the team has not supplied (assistive boundary)** — the notice records
  only the statutory-minimum particulars actually captured; an un-supplied form id, cause, or
  count is surfaced as a literal [GAP] routed to the competent person, never fabricated to look
  complete.

## Sign-off note
SME review: ran (persona: statutory accident-notification / inspectorate-liaison specialist
(factory + mine/DGMS routing)); this is **decision-support only** and does not replace
competent-person sign-off before filing. It **precedes — and never replaces, never emits — the
human competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
