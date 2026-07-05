---
sme-review:
  personas:
    - role: "Indian PESO licensing specialist (Petroleum Act / Explosives Act / Gas Cylinder & SMPV(U) Rules)"
      expertise: "Matching installation + capacity to the correct PESO instrument and form; MSIHC MAH on-site emergency plan; licence/authority routing."
      lens: "Is the licence type, form and authority correctly matched to this installation from the KB row — and is the MSIHC on-site emergency plan present whenever the installation is a MAH?"
    - role: "India HSE / labour-law compliance reviewer (state-form & legacy-first discipline)"
      expertise: "Mandatory state detection; legacy-first form citation; KB-REG-IN-STATEFORMS; OSH-Code transition framing."
      lens: "Is the site state resolved before any state-specific obligation is cited, and is every form taken from the KB row rather than a hard-coded national number — with any unverified form-id left as a literal [GAP]?"
modes:
  licence-package:
    detected_by: "Q1 — What's the task? (New licence application / Renewal or amendment / Compliance check → the licence package leg; Q9 output confirms package vs form+checklist vs gap report)"
    floor:
      - id: instrument-resolved-from-capacity
        description: "The installation + capacity is mapped to the correct PESO instrument — Petroleum Rules 2002 / Explosives Rules 2008 / Gas Cylinder Rules 2016 / SMPV(U) Rules 2016 — via KB-REG-IN-PESO (intake Q2/Q3; capacity gates the licence class)"
        anchors: ['Petroleum Rules|Explosives Rules|Gas Cylinder Rules|SMPV', 'KB-REG-IN-PESO']
        min_matches: 2
      - id: state-resolved-before-citing
        description: "The site state is resolved (asked, or inferred-from-address then confirmed) BEFORE any state-specific obligation is cited — never silently assumed (intake Q5, mandatory state detection)"
        anchors: ['Gujarat|Tamil Nadu|Karnataka|Maharashtra|Delhi', 'state.{0,50}(confirm|detect|resolv)']
        min_matches: 1
      - id: forms-from-kb-row-gap-honest
        description: "Every form is cited from the matched KB row; an unverified form-id (Form E / Form F / LS-1A) stays a literal [GAP] with a verification path — never a hard-coded national number (GATE-06)"
        anchors: ['KB-REG-IN-(PESO|STATEFORMS)', 'verif']
        min_matches: 2
      - id: authority-matched-to-instrument
        description: "The named licensing authority (PESO / Chief Controller of Explosives vs the state authority) matches the resolved instrument and state"
        anchors: ['Chief Controller|PESO', 'authority']
        min_matches: 2
      - id: osh-code-transition-note
        description: "The OSH-Code transition note is appended — legacy-first framing; no consolidated national form presented as live"
        anchors: ['OSH Code', 'transition']
        min_matches: 2
      - id: validity-renewal-timeline
        description: "The licence validity / renewal deadline is recorded (or a literal [GAP]) so the temporal obligation is visible (intake Q7)"
        anchors: ['validity|renewal', 'deadline|due date|expiry']
        min_matches: 1
      - id: competent-contact-role
        description: "The licensed competent person / authority point-of-contact is recorded as a role (intake Q8, de-identified)"
        anchors: ['competent person', 'point of contact']
        min_matches: 1
  msihc-emergency-plan:
    detected_by: "Q1 — What's the task? (MSIHC on-site emergency plan) / Q4 — MAH determination (Yes → the msihc-onsite-emergency-plan section is in scope)"
    floor:
      - id: mah-threshold-determination
        description: "The Major Accident Hazard determination is stated against the MSIHC threshold quantities for the named installation (intake Q4; KB-REG-IN-MSIHC)"
        anchors: ['Major Accident Hazard|MAH', 'threshold']
        min_matches: 2
      - id: msihc-plan-elements
        description: "The on-site emergency plan is structured to the KB-REG-IN-MSIHC element map — scenario basis, command structure, resources, alarm/communication, liaison with off-site authorities"
        anchors: ['on.site emergency plan', 'KB-REG-IN-MSIHC']
        min_matches: 2
      - id: scenarios-recorded-not-computed
        description: "MAH scenarios are referenced from the external studies the duty-holder supplies (recorded, never computed); an unsupplied scenario basis is a literal [GAP]"
        anchors: ['scenario', 'external|recorded|supplied']
        min_matches: 2
      - id: command-roles-accountable
        description: "The emergency command structure names the site controller / incident controller / coordinator as roles with accountabilities (de-identified)"
        anchors: ['site controller|incident controller', 'command']
        min_matches: 1
      - id: alarm-muster-communication
        description: "Alarm raising, internal/external communication and muster/assembly arrangements are present for the named installation"
        anchors: ['alarm', 'muster|assembly point']
        min_matches: 2
      - id: drill-review-cadence
        description: "Mock-drill / rehearsal cadence and the plan-review trigger are recorded (MSIHC periodic rehearsal duty)"
        anchors: ['mock drill|drill|rehears', 'review']
        min_matches: 2
      - id: state-resolved-before-citing
        description: "The site state is resolved and confirmed before any state-specific MSIHC/factories obligation is cited (intake Q5, mandatory state detection)"
        anchors: ['Gujarat|Tamil Nadu|Karnataka|Maharashtra|Delhi', 'state.{0,50}(confirm|detect|resolv)']
        min_matches: 1
---

# SME Review & Sign-off — peso-licensing-assistant

Two distinct disciplines own two failure modes on a PESO licensing artifact: matching
the **installation to the correct PESO instrument, form and authority** (the licensing
specialist) and the **state-form / legacy-first citation discipline** (the India
compliance reviewer). So this skill carries **two** SME lenses. Both specialize the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) — the
PESO/MSIHC remit — and the second lens deliberately overlaps the India-Regulatory slot
(licensing ≠ statutory-form discipline); it must stay consistent with that slot, never
contradict it. The generic **HSE-SME-Reviewer** hook is the inherited fallback. The
universal hard gates (de-id leak, citation/clause accuracy, HoC, owned-and-dated actions)
are the enforced class and are not restated below.

**Form-id honesty is load-bearing here (GATE-06).** Every form must be resolved from the
matched KB row (`KB-REG-IN-PESO` / `KB-REG-IN-STATEFORMS`), never a nationally-hard-coded
number. Any PESO form whose id is **not** verified in the KB — including Form E, Form F,
or LS-1A — is left as a literal `[GAP]` routed to the authority/competent person; it is
**never invented**. The citation grader is row-blind to a fabricated form value, so this
discipline is the load-bearing statutory check, not a formatting nicety.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every form is resolved from `KB-REG-IN-PESO` / `KB-REG-IN-STATEFORMS`; no nationally-hard-coded form number appears, and any unverified form-id (e.g. Form E / Form F / LS-1A) is left as a literal `[GAP]` — never invented.
- [ ] Installation + capacity maps to the right PESO instrument (Petroleum Rules 2002 · Explosives Rules 2008 · Gas Cylinder Rules 2016 · SMPV(U) Rules 2016) → the right form and the right authority.
- [ ] Site state is resolved (asked, or inferred-from-address then confirmed) before any state-specific siting/consent obligation is cited — never silently assumed; an unconfirmed state means no state-specific form is cited yet.
- [ ] If the installation crosses MSIHC MAH thresholds, the on-site emergency plan is structured (reading `KB-REG-IN-MSIHC`); a MAH installation with no on-site plan is flagged.
- [ ] The OSH-Code transition note is appended (legacy-first framing); the transition itself is left to the hse-india skill — this skill only appends the note, never presents a consolidated national form as live.
- [ ] The named authority (PESO / Chief Controller of Explosives vs the state authority) matches the resolved instrument and state, and the artifact reads as structured licensing support, not autonomous regulatory determination (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A confident package built on an unconfirmed state** — forms, authority and consents
  cited fluently while the site state was inferred and never confirmed; every
  state-specific line in the package inherits the unverified assumption.
- **The licence resolved, the timeline missing** — instrument/form/authority all correct
  but no validity period, renewal deadline or processing expectation anywhere; the client
  files once and lapses silently.
- **A MAH installation with a licence but no plan** — the MSIHC threshold crossing is
  noted (or ignored) and the on-site emergency plan never materialises; the licensing leg
  quietly swallowed the emergency-planning duty.
- **An emergency plan that commands nobody** — scenarios and resources listed but no
  command structure, no alarm/muster arrangements, no drill cadence; a filing artifact,
  not an operable plan.

## Sign-off note
SME review: ran (personas: Indian PESO licensing specialist + India state-form compliance
reviewer); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class owned by the automated harness.
