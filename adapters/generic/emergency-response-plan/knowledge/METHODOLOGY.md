# Methodology — Scenario-keyed Emergency Response Plan (ISO 45001 clause 8.2)

The ERP method grounds every plan in the site's **credible emergency scenarios** and the
**hierarchy of controls — prevention before response**. The single lever: a defensible
ERP is **scenario-keyed and site-specific**, never a generic "evacuate" template. The
deterministic engines (`controls`, `smart_actions`) enforce the hierarchy and the
owned-and-dated drill schedule; everything else is structured prose grounded in the KB.

## 0. De-identify the inputs (first, always)

Before any drafting (the `deid` block + the De-identifier-runs-first orchestration rule),
scrub the inputs. The **call-out tree holds responder names + personal mobile numbers** —
a **legitimate internal operational record**, but any **widely distributed** copy uses
**role + duty-phone labels**. Produce (a) the de-identified plan and (b) a separate
re-identification key (the internal master contact list), never embedded in the document.
No responder health/medical detail in the plan.

## 1. Scope & ERP/BCP disambiguation (Q1)

Confirm the **named site + occupancy** (refuse a generic site). Confirm the user wants an
**emergency response plan** (scenarios / muster / evacuation / call-out tree) and **not**
**continuity of critical activities** (RTO / RPO / MTPD, recovery strategies) — that is
**`business-continuity-plan`** (route there; the two are complementary, never merged).
This generic ERP does **not** subsume `mine-rescue-erp` (mining) or the marine/offshore
skill.

## 2. Scenario selection (Q2 → `KB-SNIP-ERP-SCENARIOS`)

Select the site's **credible** scenarios from the catalogue (fire/explosion ·
chemical/gas release · medical · structural/collapse · severe weather/flood ·
security/violence · loss of utilities). For each, capture the site-specific trigger /
source / worst-credible case (Q2a). **Refuse a generic plan:** at least **one credible
scenario** must be captured, each keyed to this site — not a copy-paste menu.

## 3. Prevention-first hierarchy (the core-value lever — `controls` + `KB-SNIP-HOC`)

For each scenario, **before** designing the response, apply the hierarchy of controls to
**reduce the scenario at source**: Elimination → Substitution → Engineering →
Administrative → PPE. Call `controls.rank_controls` + `controls.validate_treatment`.
A plan that relies **only on response** (no prevention controls) for a preventable
scenario — e.g. a flammable-storage fire with no ignition-source/quantity control — is a
**defect the Critic/QA pass must catch**. If `ppe_admin_only` is `True`, add a
higher-order prevention control **or** record an explicit "higher-order prevention not
reasonably practicable because…" justification. This is the hard enforcement of the core
value, not a mention.

## 4. Scenario response procedures (`KB-SNIP-ERP-SCENARIOS` skeletons)

For each scenario build the **scenario-keyed** procedure from the skeleton: detection /
alarm → immediate actions → escalation / call-out → muster / evacuation → all-clear /
stand-down. Each step is specific to this site (named areas, isolation points, alarm
type) — a generic "evacuate" with no scenario-keyed steps **fails specificity**.

## 5. Roles & deputies + call-out tree (Q4b)

Build the **call-out tree and incident-command roles** (Incident Controller, wardens,
first-aiders, communications) — **every role has a named deputy/alternate** across the
shift pattern (a command-chain single point of failure is a FLAG). The call-out tree is
the internal operational record (real contacts in the master; role + duty-phone labels in
any circulated copy).

## 6. Muster & evacuation (Q4)

**Name** the muster/assembly points (not "assemble outside"), the evacuation routes, the
head-count / roll-call method, and the provisions for visitors, contractors and persons
needing assistance. Confirm reachability and that capacity matches the occupancy from Q1.

## 7. External-responder integration (Q4)

Specify the **fire/ambulance access** routes, **isolation points**, site-interface
(plans/keys/contacts handed over), and any **mutual-aid** arrangement. Where the plan
relies on an on-site ERT/fire team (Q3), the capability must be **proven** (training,
numbers, shift availability) — never assumed.

## 8. Drill schedule (Q6 → `KB-DATA-DRILL-FREQ` + `smart_actions`)

Set the **dated drill schedule** by scenario / site-class from `KB-DATA-DRILL-FREQ`
(quote `source`+`year`; `[GAP]` where unresolved — never a bare number). Each drill is a
`smart_actions` entry with a **named owner + date + measure** (e.g. evacuation time
target). `smart_actions.validate_register` rejects any anonymous or "ASAP" entry. Include
a **debrief / corrective-action** loop after each drill.

## 9. Validate against `references/QUALITY_CHECKLIST.md`

The self-check loop before output: prevention precedes response on every scenario; every
procedure scenario-keyed; every role deputised; muster points named; drill schedule
dated; capability proven; citations trace to the KB (8.2 / 1910.38 / RRFSO art.15 / s.41B
via `hse-india` for India); de-id applied; the ERP→BCP pointer present.

## 10. Assemble the branded report

Build `report.json` from `assets/emergency-response-plan-report.template.json` (the
section order: site & occupancy → credible scenarios → prevention controls → scenario
procedures → call-out tree & roles → muster & evacuation → responder integration → drill
schedule → review & sign-off → **the BCP cross-reference callout**) and run the canonical
`report-output` call. Render DOCX + PDF from the one `report.json`.
