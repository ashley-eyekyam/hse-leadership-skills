# Methodology — SOP / safe-work-procedure authoring (ISO 45001 8.1 operational control)

This is the domain method `sop-writer` applies. The SKILL.md Workflow is the
operational summary; this file is the full reference. The output is a **version-
controlled, task-specific procedure** with the **hierarchy of controls embedded into
the steps**, written to the **reader's literacy level**, that **composes with — never
duplicates** — an existing risk assessment or JSA.

## 1. The operational-control SOP loop (ISO 45001 clause 8.1)

The loop is jurisdiction-independent (Chennai / Houston / Aberdeen alike); the resolved
jurisdiction only changes the *documented-procedure-duty* citation, not the method. An
SOP is grounded in **ISO 45001 8.1 operational control** (and **8.1.2** hierarchy of
controls; **8.1.4** procurement/contractors when the SOP governs contractor work).

1. **De-identify first.** Scrub names, contacts, health detail, and any small injury
   cell to role labels (the `deid` block) before any authoring. No-op if the inputs are
   impersonal, but it always runs — and it guards the **approval/signatory block**, the
   SOP-specific place real names tend to leak.
2. **Fix the task, the scope, and the hazards.** Establish exactly what the SOP covers
   and what it does **not** (boundaries). Then source the hazards (see §2 — ingest or
   elicit). Record `[GAP]` where a step's hazards are uncertain; never invent.
3. **Derive the HoC-aware control set.** For each hazard tied to a step, apply
   `KB-SNIP-HOC` (rank Elimination → Substitution → Engineering → Administrative → PPE)
   then call `controls.rank_controls` + `controls.validate_treatment` on the **full**
   control set (see §3). This is the **only** A7 engine the skill calls.
4. **Author the steps with controls embedded** (see §4).
5. **Add responsibilities, competencies, equipment, emergency provisions** — roles
   (not names), the training each role needs, the equipment/permits, and the stop/abort/
   rescue provisions.
6. **Reference + revision-control the document** — cite ISO 45001 8.1, the jurisdiction
   fragment, **the ingested RA/JSA by id**, and build the revision/approval block.
7. **Validate** against `QUALITY_CHECKLIST.md`, then assemble the branded `report.json`.

## 2. Ingest-don't-overlap — composing with B1/B2 (the load-bearing rule)

`sop-writer` **authors the procedure**; B1 (risk-assessment) owns *risk assessment*
(hazard identification + L×S scoring + control selection + residual + SMART actions);
B2 (job-safety-analysis) owns *job-step hazard breakdown*. The compose boundary:

- **If a B1 RA or B2 JSA is supplied (intake Q4)** → **ingest it**: read its hazards and
  its **rated controls** and carry them forward, **cross-referencing the source by id**
  in the SOP (the "method ↔ RA cross-referenced" bar). **Do NOT re-score** — this skill
  never calls `risk_matrix` and never produces a risk register; that would duplicate B1
  and drift from its ratings. The ingested rating is the procedure's authority; if it is
  stale or wrong the Critic/QA pass + the competent-person reviewer catch it (the SOP
  must not silently launder a bad RA into a clean-looking procedure — provenance is the
  cross-referenced id).
- **If no prior analysis exists** → **elicit hazards + controls inline** (Q6/Q7) and
  **flag that a formal RA/JSA is the more rigorous source** (the skill composes with
  B1/B2, it does not substitute for them).

## 3. The hierarchy of controls, embedded (the core value, mechanically enforced)

The procedure is **itself an administrative control**, so a defensible SOP must surface
the **higher-order controls it operates within** — never present "wear PPE and follow
this procedure" as the sole defence. Mechanics:

- `controls.rank_controls(controls)` tags each control its HoC tier (Elimination /
  Substitution / Engineering / Administrative / PPE); `controls.validate_treatment`
  returns `ppe_admin_only` + a flag.
- If `ppe_admin_only` is `True`, the Workflow **must** either **add a higher-order
  control** (e.g. engineering: enclose/dampen the source, on-tool extraction;
  substitution: a quieter/less-hazardous process) **or record an explicit justification**
  ("higher-order controls not reasonably practicable because…"). An un-justified
  lower-order-only treatment is a **defect the Critic/QA pass catches** and scores ≤2 on
  `hierarchy_of_controls`.
- The higher-order controls the procedure sits within (isolation, lock-out, fixed guard,
  ventilation) are surfaced **up front and in the `hoc_table`**, visually distinct from
  PPE — never buried in a flat PPE list at the end.

## 4. Steps with controls embedded INTO them (not appended) + the literacy lever

- Steps are **real, ordered, task-derived** (from intake Q8) — one action per step. The
  Workflow **refuses generic "work safely" / "follow all rules" steps**; it asks for the
  real ordered steps or records `[GAP]`.
- Each **risk-bearing** step names, **inline**, the controls / PPE / checks / hold-points
  that make *that* step safe — e.g. *"Step 4 — Open valve V-12 slowly. Control: stand
  clear of the discharge line (engineering guard in place); wear face shield + chemical
  gloves [PPE]; confirm pressure gauge reads <2 bar [check/hold-point]."* Controls are
  **embedded into the step**, never collected into a separate appendix divorced from the
  step they protect.
- **Literacy calibration (`KB-SNIP-AUDIENCE`, intake Q10):** author to the stated reader.
  Frontline operator → short imperative sentences, one action per step, plain-language
  hazard cues, optional bilingual note for the India-first scope; technician/supervisor →
  more technical register. A procedure a frontline worker cannot read is not a control.

## 5. Responsibilities, competencies, emergency provisions, revision control

- **Responsibilities** — role labels only (who authorises, who executes, who verifies);
  never real names, even in the approval block (role + signature-placeholder).
- **Competencies** — the training/qualification each role needs (the "tied to training
  records" bar).
- **Emergency / abnormal-condition provisions** — stop conditions, what to do if a
  hold-point fails, rescue/spill/first-aid arrangements (a `warning` callout for the
  critical stop conditions).
- **Revision/approval block** — SOP id/number, version, effective date, author role,
  reviewer role, approver role, and the **review cycle / next-review trigger**. **When
  the user gives no review cycle (intake Q11), record "review on change (MoC-triggered)
  or at minimum annually" and flag it `[ASSUMPTION]`** for the competent-person reviewer
  to set — the conservative default surfaces directly in the approval block.

## 6. Regulatory grounding & the no-form-number rule

An SOP is an **internal management-system document, not a statutory filing**. The
jurisdiction fragment grounds any **documented-procedure duty** the procedure must
satisfy (e.g. a documented-procedure obligation), never a fabricated SOP form number.
For an India site, resolve the state (Q1a, **mandatory state detection**) before citing
any state-specific duty via `KB-REG-IN-STATEFORMS`; cite **no national or state SOP form
number** — none exists for an internal procedure.

## 7. This is the narrative-document spine

This method is the reusable spine for the pack's document-shaped skills (B4
rams-builder, B9 board-safety-report, sector-pack procedure/manual skills):
**structured intake (with an ingest gate for upstream analysis) → derive a HoC-aware
control set via `controls` → author a specific, ordered document with controls embedded
per section → add responsibilities/competencies/emergency/references/revision-control →
validate → branded `report.json`.** It leans on `heading`/`paragraph`/`bullets`/ordered
steps + an `hoc_table` + an appendix revision/approval block (distinct from B1's
risk-card-heavy mapping).

## Intake guidance (relocated from SKILL.md Step 0 for char-fit — substance unchanged)

The two specificity anchors are Q3 (task/operation) and Q8 (procedure steps). Refuse
to proceed on a vague task or generic/missing steps such as "work safely" or "follow
all rules" — ask again, or record `[GAP]` / `[ASSUMPTION]`; never invent.

- **Q3 worked example:** "manual changeover of the print-head on Press 4 during a
  planned stop — does NOT cover electrical fault repair, which needs a competent
  electrician."
- **Q8 worked example:** "isolate & lock out Press 4 → confirm zero energy → remove
  guard → unclip print-head → fit replacement → refit guard → remove locks →
  function-test."
- **Echo-back example:** "Authoring: SOP for manual print-head changeover on Press 4,
  Plant 2, Maharashtra; hazards/controls ingested from JSA-2026-A14; 9 ordered steps;
  roles = operator + authorised PTW person; frontline literacy level; annual +
  on-change review — correct?"
