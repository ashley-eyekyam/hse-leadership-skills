# Methodology — CDM 2015 Health & Safety File (Reg 12(5)–(9))

The H&S File is the **as-built residual-risk record** the principal designer prepares and
maintains and hands to the client at completion — it is **a structured residual-risk record,
not calculation** (there is no risk matrix in this skill; the residual hazards are recorded as
located facts a future worker could not anticipate). The method is grounded in the **L153
Appendix-4 H&S-file content list** (`KB-SNIP-HS-FILE-CONTENT`) and the **Reg 12(5)–(9) duty**
(`KB-REG-CDM2015`). Its single lever is **residual-only discipline**: record **only what a
future worker could not reasonably anticipate** — a full general-spec dump is flagged, not a
file.

## Step 1 — De-identify the inputs (FIRST)
Run the `deid` block + `references/deid-checklist.md` before any drafting. **Commissioning,
survey, and as-built records routinely name an individual** — a commissioning engineer with an
incident/health note, a surveyor, an occupier — scrub these to role labels; a leak is an
auto-fail. **No worker health detail belongs in the file at all.** Set the
**restricted-distribution flag** where the file carries security-sensitive structural/services
detail. The user-supplied principal designer / client duty-holders and open-item owners stay
named (a legitimate contractual record).

## Step 2 — Capture the as-built & services information (Q4)
What was built and its intended use; the **key as-built drawings**; the **location of services
and isolation points**; material specifications. Each is **cited to its source**; every missing
record (no commissioning record, no services drawing) is a documented **`[GAP]`** — never
silently absent. Never invent an as-built detail.

## Step 3 — Identify the residual & unusual hazards — the "could-not-reasonably-anticipate" test (THE LEVER)
For each system, **include an item only if a competent future worker could not reasonably
anticipate it** from the structure itself: fragile roof glazing, no permanent edge protection
at high-level plant, presumed-asbestos lagging, restricted confined-plant egress, buried
services on an unusual route, an unusual structural loading limit. **Each residual hazard is
LOCATED** (where in the structure). **A routine/anticipatable hazard, or the full general
specification dumped in instead of the residuals, is REJECTED** — that is a
specificity/defensibility failure, not a file. This is the difference between a real H&S File
and a spec dump.

## Step 4 — Record the hazardous materials in situ
Asbestos register, coatings, insulation, and other materials **left in place — with their
locations**. Where a survey is outstanding, record **presumed-present-pending-survey** as a
`[GAP]` and flag it as a **hold-point** before any disturbance.

## Step 5 — Frame each residual hazard's future-work control by the hierarchy (`controls`)
For each located residual hazard, propose the future-work control and **apply `KB-SNIP-HOC`**
via `controls.rank_controls` + `controls.validate_treatment`: prefer a **higher-order**
future-work control (specify permanent edge protection / an anchor system at next
refurbishment; an asbestos management plan + survey before any riser disturbance) over a
PPE-/admin-only treatment ("wear a harness"). A lower-order-only arrangement with no
justification is a **defect the Critic/QA pass must catch** — doubly load-bearing for
demolition, where designed-in controls outrank "be careful".

## Step 6 — Build the maintenance/cleaning/refurb/demolition safety arrangements (Q5)
For the future-work scope captured at Q5, author the **safety information a future worker
needs** for each foreseeable activity — maintenance, cleaning, refurbishment, and (where in
scope) demolition. Demolition arrangements still rank controls via `KB-SNIP-HOC`.

## Step 7 — Information gaps & revision control
**Every unknown is a documented `[GAP]`** (never silently omitted); any **open completion
item** becomes a SMART action via `smart_actions.validate_register` (specific, **assignable
(named owner / role)**, **time-bound (ISO due date)**, linked). The file carries
**revision/version control**; **an update (Q2) APPENDS — it never overwrites prior
residual-risk content.**

## Step 8 — Cross-reference the CDM document chain (loose coupling)
Add the one-line **PCI → CPP → H&S File** (Reg 4 → 12 → 12(5)) cross-reference sourced from
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **without assuming the PCI or CPP skill ran**. State the
**principal designer's Reg 12(5) preparation duty AND the handover duty (Reg 12(6)–(9))** —
attributing preparation to the wrong duty-holder, or omitting the handover duty, is a
`regulatory_citation_accuracy` hard-fail.

## Step 9 — Validate & assemble
Validate against `references/QUALITY_CHECKLIST.md`, then build
`assets/health-safety-file.report.json` and render via the `report-output` block.

## Jurisdiction
- **UK** — CDM 2015 Reg 12(5)–(9) + L153 Appendix 4 (`KB-REG-CDM2015`).
- **USA** — 29 CFR 1926 as-built / record-retention equivalents (`KB-REG-OSHA1926` where
  seeded; otherwise note the equivalent and flag `[GAP]`).
- **India** — BOCW completion records; **defers to `hse-india` / `bocw-compliance`**, mandatory
  state detection, literal `[GAP]`, **never a minted national form number**.
