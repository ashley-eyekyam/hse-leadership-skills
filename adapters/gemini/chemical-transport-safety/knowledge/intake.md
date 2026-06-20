---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-EXPOSURE: "route is the receptor proxy — covered as ELI-LOCATION (tunnels/populated areas)"
    ELI-TEMPORAL: "transport is per-consignment; no standing review cycle to elicit"
    ELI-BASELINE: "no standing controls to baseline — a fresh consignment assessment"
    ELI-INDUSTRY: "transport mode/regime supersedes sector for hazard selection"
  branches:
    - {when: Q5, option: road-India (CMVR), activates_questions: [Q6], mandatory: true}
    - {when: Q1, option: loading-guidance, activates_questions: [Q9]}
---

# Structured intake — chemical-transport-safety

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a UN number /
class). Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — classify for transport, full loading/unloading safety guidance, or a transport-document/placard check? | MCQ | classify-only / loading-guidance / document-placard-check | ELI-SCOPE | always |
| Q2 | Substance / proper shipping name + CAS + UN number if known. | free-text | resolve UN from user's DG list; "unknown" → `[GAP]` | ELI-SUBJECT | always |
| Q3 | Physical state + flashpoint (if flammable). | MCQ + free-text | solid / liquid / gas; flashpoint °C | ELI-EVIDENCE | always |
| Q4 | Quantity per package and total consignment. | free-text | mass/volume per package + total (drives LQ/placard/ADR category) | ELI-SUBJECT | always |
| Q5 | Transport mode + regime. | MCQ | road-EU (ADR) / road-US (DOT-HMR) / road-India (CMVR) / sea (IMDG) / multimodal · rail (RID) & air (IATA) OUT OF SCOPE — flagged | ELI-JURIS | always |
| Q6 | Which Indian state (origin/handling)? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; confirm before citing any rule/form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | if Q5==road-India |
| Q7 | Intended packaging / IBC / tank. | free-text | UN-spec packaging type | ELI-SUBJECT | always |
| Q8 | Known GHS classification, or do you hold the SDS §14? | MCQ | have GHS class / have SDS §14 / neither (`[GAP]`) | ELI-EVIDENCE | always |
| Q9 | Route detail — tunnels, populated areas, port handover? | free-text | drives ADR tunnel code / segregation at transfer | ELI-LOCATION | if Q1≠classify-only |
| Q10 | Is a DG safety adviser (DGSA) / responsible person named? | free-text | role-label owner for controls | ELI-COMPETENCY | always |
| Q11 | Transport-document / placard obligation set to satisfy. | MCQ | transport document / placard + marking / segregation check / all | ELI-OBLIGATIONS | always |
| Q12 | Org consequence/priority scheme for an `[GAP]` or incompatible load. | MCQ | org scheme / default — flag every unresolved entry | ELI-SCORING | always |

**Branch map**
- `Q5 == road-India` → Q6 state (**mandatory**); cite CMVR/state transport rule, not ADR; "Other"/"Unknown" → literal `[GAP]`.
- `Q5 ∈ {rail, air}` (if user asserts) → **refuse + flag out-of-scope**, route to specialist (METHODOLOGY step 3).
- `Q5 == multimodal` → activate per-leg cross-walk + handover-segregation questions.
- `Q8 == neither` → `[GAP]`; cannot assign a transport class without a GHS basis → route to `ghs-classification-sds-author`.
- `Q2 UN unknown / N.O.S.` → `[GAP]`-flag, never invent UN number / PSN (METHODOLOGY output discipline).

## Echo-back
> "**{substance/UN}**, {state}, flashpoint {x}; consignment **{qty}**; mode **{regime}**{; India state {s}}; packaging **{type}**; basis **{GHS class / SDS §14}**. I will cross-walk to the transport class + packing group for that mode, set marking/placarding/segregation, and HoC-rank loading/unloading controls. Rail/air are out of scope. Confirm."

Echo the captured facts back and **confirm before the cross-walk**. The named DGSA /
responsible person is held as a role label in the echo-back.

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "ship some chemicals" → demand substance + UN + quantity; **never proceed on a vague subject**.
- Rail/air requested → out-of-scope flag, no guessed class.
- No GHS basis and no SDS §14 → `[GAP]`, route to classification skill.

**Domain evidence types (`ELI-EVIDENCE`)**
SDS §14 (transport), GHS classification, UN/Dangerous Goods List entry, flashpoint/physical state, packing-group basis data, existing transport document / DG note.

**[GAP]** India road transport regime (CMVR/Rule 137) — `_skill-kb.md` / `transport-adr-dot.md` lists only ADR/DOT/IMDG/GHS; no India transport KB ID. The India branch may need a new KB fragment (`KB-REG-IN-CMVR`). Until confirmed, the India-road branch must `[GAP]`/route-to-competent-person rather than assume CMVR rules (intake audit `:127`). Verification path: confirm a `KB-REG-IN-CMVR` row before citing India road rules.
