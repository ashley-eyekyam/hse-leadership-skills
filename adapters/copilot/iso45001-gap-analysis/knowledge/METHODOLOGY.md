# Methodology — ISO 45001 clause-by-clause gap analysis

The domain method `iso45001-gap-analysis` applies: a **clause-walk** over the full ISO
45001:2018 clause set (4–10), scoring each clause's conformance from evidence on the shared
5-level maturity scale, flagging certification-blockers, prioritising the gaps, and building
a costed remediation roadmap. The same method serves **ISO 14001:2015** and **ISO 45003:2021**
via the standard selector (intake Q1) — only the clause set changes.

**Grounded in:**
- `KB-STD-ISO45001` — the clause→artifact map (clause set 4–10); the binding clause
  requirements (the user holds the licensed standard; this skill paraphrases-and-cites, never
  reproduces verbatim standard text).
- `KB-DATA-ISO45001-MATURITY` — the **5-level conformance/maturity scale** (0 Absent → 1
  Ad-hoc → 2 Documented → 3 Implemented/conformant → 4 Measured & improving), each level with
  an **evidence test**, plus the **certification-readiness rule**.
- `KB-SNIP-GAP-PRIORITISATION` — the severity × certification-blocking gap-ordering method.
- `KB-SNIP-HOC` — the hierarchy of controls, applied to the planning-clause (6.1) controls
  and the remediation roadmap.
- `KB-SNIP-OPS-CLAUSE-MAP` — the bundle clause cross-walk (route a user to the owning sibling
  skill for an adjacent clause).
- ISO/IEC 17021-1 — certification-audit principles, to frame readiness (major vs minor
  nonconformity).

## The steps

### 1. De-identify the inputs (FIRST)
Before any analysis. Audit interview notes and evidence bundles may name individuals, disclose
health/psychosocial conditions, and carry exact dates/locations and small (<5) personnel cells.
Scrub all of it to stable role labels per the `deid` block + `references/deid-checklist.md`;
hold the re-identification key separately. Minimise supplier/commercial cost data carried into
the roadmap. Everything downstream consumes only the scrubbed text.

### 2. Resolve the standard + enumerate the clause set
From intake Q1, read the matching standards fragment (`KB-STD-ISO45001` default; `KB-STD-ISO14001`
/ `KB-STD-ISO45003` / combined via the selector). Enumerate **every** clause:

| Clause | Area | Mandatory-clause anchors |
|---|---|---|
| 4 | Context of the organisation | 4.1 context · 4.2 interested parties · 4.3 scope · 4.4 the OH&S MS |
| 5 | Leadership & worker participation | **5.2 OH&S policy** · 5.1 leadership · 5.3 roles · 5.4 consultation & participation |
| 6 | Planning | **6.1.2 hazard identification & risk assessment** · 6.1.3 legal & other requirements · 6.2 objectives |
| 7 | Support | 7.1 resources · 7.2 competence · 7.3 awareness · 7.4 communication · 7.5 documented information |
| 8 | Operation | 8.1 operational planning & control · 8.1.4 procurement/contractors · 8.2 emergency preparedness & response |
| 9 | Performance evaluation | 9.1 monitoring/measurement · 9.1.2 evaluation of compliance · **9.2 internal audit** · 9.3 management review |
| 10 | Improvement | **10.2 incident, nonconformity & corrective action** · 10.3 continual improvement |

**No clause is silently dropped** — each is scored or marked **N/A with a stated reason**.

### 3. Score each clause's conformance from evidence
For each clause, read the Q4 evidence and assign **level 0–4 on `KB-DATA-ISO45001-MATURITY`**,
applying that level's **evidence test** (e.g. level 3 requires *records showing the clause's
requirements met consistently*, not just a procedure on paper). A clause with **no evidence is
a scored gap (level 0/1)**, with the missing evidence named as a `[GAP]` — never an omission and
never a guess. The level is the scale's, traced to the cited evidence.

### 4. Flag certification-blockers
Apply the `KB-DATA-ISO45001-MATURITY` certification-readiness rule: any **mandatory clause** at
**level ≤ 2** (e.g. 5.2 policy, 6.1.2 hazard-id, 9.2 internal audit, 10.2 incident/nonconformity)
is a **certification-blocker** — flagged explicitly in the gap register, **never downgraded** to
a minor gap. Under ISO/IEC 17021-1 framing, a blocker is a **major nonconformity** that would stop
certification; a level-2 non-mandatory clause is a minor finding.

### 5. Classify & prioritise the gaps
Apply `KB-SNIP-GAP-PRIORITISATION`: classify each gap on **severity** (required − current maturity
× the risk the clause governs) and **certification-blocking**; **prioritise certification-blockers
first** (by severity), then high-severity non-blockers, then the remainder. Every gap traces to its
**clause + a named owner**.

### 6. Apply the hierarchy of controls to the planning clauses
Where clause 6.1 (planning / risk & opportunity) controls are assessed, rank them via `KB-SNIP-HOC`
(Elimination → Substitution → Engineering → Administrative → PPE). A PPE/admin-only remediation
with no higher-order option and no justification is a defect the Critic/QA pass must catch.

### 7. Build the costed remediation roadmap (named owners + dates)
Turn each prioritised gap into a **SMART action** via `smart_actions.validate_register` — specific,
measurable, **assignable (named owner)**, relevant, **time-bound (ISO due date)** — with a **cost
estimate** and ordered **blockers-first**. Any action missing an owner, a valid date, a measure, or
a clause link is invalid and must be fixed (no anonymous actions, no "ASAP").

### 8. Validate, then assemble the branded report
Run the `references/QUALITY_CHECKLIST.md` gate, then build `report.json` from
`assets/iso45001-gap-analysis-report.template.json` and render via the shared engine (the
`report-output` block in `SKILL.md`).

## Standard-selector note
For **ISO 14001** the clause set is the environmental MS (same 4–10 high-level structure; e.g.
6.1.2 environmental aspects); for **ISO 45003** the psychosocial extension of 6.1.2 hazard-id is
scored. The maturity scale, the blocker rule, and the prioritisation method are unchanged — only
the clause content and the cited standard differ.
