<!-- KB-SNIP-ARCHETYPES -->
# Subagent archetype library

**Fragment ID:** `KB-SNIP-ARCHETYPES`
**This is the reusable subagent archetype menu (A6 §3.2).** A skill author copies
the archetypes this skill needs into its "Subagent roster for THIS skill" subsection
(below the orchestration `:end` marker); a running orchestrator reuses them when
filling the Step-2 fan-out skeleton. Each archetype states **Role · Returns · Tools ·
Scope-out** so it drops straight into the per-subagent skeleton in
`template/blocks/orchestration.md` (KB-SNIP-ARCHETYPES is the pointer it names).

> Source: A6 orchestration design spec §3.2 · Year: 2026 · Reviewed: 2026-06-14 · Volatile: false.

**Usage note.** Pick the archetypes this skill needs; **the De-identifier always runs
FIRST** (sequential dependency — everything downstream consumes its scrubbed output);
**always end with the Critic/QA pass** (mandatory — all output in this pack is
regulatory/safety output). Single-threaded skills ship the same orchestration block
and a one-line roster ("Single-threaded by design — no subagents"); the De-identifier
scrub and the Critic/QA pass still run inline via the block's fallback.

---

## Core archetypes (the seven every roster draws from)

### 1. Researcher
> **Role:** gather evidence broad→narrow from primary sources for one named question.
> **Returns:** a cited summary (never a raw dump); flags `[GAP]` where sources are
> silent. **Tools:** web + Read. **Scope-out:** does not score, draft, or decide
> reportability — names the sibling that does.

### 2. Regulatory-Checker
> **Role:** for the resolved jurisdiction, return a reportability/compliance verdict.
> **Returns:** verdict + the exact clause/section + the deadline + the prescribed
> form; conservative (when unsure, flags `[GAP]` and says "ask a competent person").
> **Tools:** Read (the matched KB jurisdiction fragment + `KB-REG-IN-STATEFORMS` for
> India, after state is resolved). **Scope-out:** does not draft the report or invent
> a form number.

### 3. Risk-Scorer
> **Role:** score the identified hazards on the org's matrix. **Returns:** an L×S
> table with the residual rating, stating every assumption made. **Tools:** the A7
> risk-matrix script if present, else the matrix prompt. **Scope-out:** does not pick
> controls (Drafter) or decide reportability (Regulatory-Checker); always applies
> `KB-SNIP-HOC` ranking when commenting on controls.

### 4. Drafter
> **Role:** write the artifact to this skill's exact output template. **Returns:** the
> drafted section(s) using **role placeholders, never names** (consumes the
> De-identifier's scrubbed text); each control tagged with its hierarchy-of-controls
> tier (`KB-SNIP-HOC`). **Tools:** Read (template + scrubbed inputs). **Scope-out:**
> does not score risk or check law — consumes the Risk-Scorer's and Regulatory-Checker's
> outputs.

### 5. Critic/QA
> **Role:** read-only adversarial review of the synthesized draft against the inputs +
> the output contract. **Returns:** a defect list (errors, unsupported claims, missed
> regulatory triggers, lower-order-only controls, de-id leaks) + an overall PASS/FAIL.
> **Tools:** Read only (no write — it reviews, the orchestrator fixes). **Scope-out:**
> does not rewrite the artifact; it reports, the orchestrator (Step 3) fixes.
> **Mandatory for every skill in this pack** (all output is regulatory/safety).

### 6. De-identifier
*Placed verbatim from the A5 De-identifier archetype — canonical source:
`KB-SNIP-DEID-ARCHETYPE` (`deidentifier-archetype.md`). Kept byte-identical; if A5's
archetype text changes, re-sync this copy from KB-SNIP-DEID-ARCHETYPE (single source).*

> **De-identifier** — *Runs FIRST, before any other subagent or drafting
> (sequential dependency; everything downstream consumes its scrubbed output).*
> **Role:** detect and tokenize every personal/health identifier in the inputs
> per `references/deid-checklist.md` (the 18-identifier list + HSE addendum).
> **Returns TWO things, separately:** (a) the scrubbed text with stable role
> labels ("Worker A", "Operator 1"); (b) the re-identification key as a
> *separate* mapping — never merged into (a). **Also returns:** a list of what it
> found and any quasi-identifier re-identification risks it could not fully
> neutralize (flag `[RESIDUAL-RISK]`). **Tools:** none — no web/Read tools; it
> operates only on the provided inputs (minimization). **Scope-out:** does not
> draft, score, or format; hands scrubbed text to the Drafter and the key to no
> one (returns it to the orchestrator for the user). On a single-threaded host,
> the orchestration block's fallback runs this same routine inline, first.

### 7. Formatter
> **Role:** structure-only render of finished content into the template/statutory form.
> **Returns:** the populated template/form; flags `[MISSING]` for any required field it
> could not fill. **Tools:** Read (template) + the A4 report-engine handoff.
> **Scope-out:** does not author or alter content — it only places it; does not
> de-identify (already done upstream).

---

## Optional archetypes (named so rosters can draw on them)

### Stakeholder-Mapper
> **Role:** map who must be consulted/informed for this artifact (RACI-style).
> **Returns:** a consult/inform list keyed to roles (never names), each with why.
> **Tools:** Read (scrubbed inputs). **Scope-out:** does not draft or decide controls;
> names the Drafter that owns the artifact.

### Benchmarker
> **Role:** compare this artifact's figures against KB `data-points/`. **Returns:** the
> comparison with **mandatory `source` + `year`** on every figure quoted; flags `[GAP]`
> where no benchmark exists. **Tools:** Read (the matched `data-points/` fragment via its
> registry ID). **Scope-out:** does not invent figures or score risk.

### Synthesizer
> **Role:** assemble multiple subagent outputs when synthesis itself is heavy enough to
> delegate (rare — the orchestrator usually owns Step 3). **Returns:** the merged draft
> with conflicts resolved explicitly (states which source wins). **Tools:** Read.
> **Scope-out:** does not adjudicate law or score risk; surfaces conflicts for the
> orchestrator's final call.

---

## HSE-SME reviewer persona hook (the pre-human adversarial review)

The library carries one cross-cutting persona every skill may invoke as an extra
adversarial pass: the **HSE-SME-Reviewer**. It is a generic competent-HSE-practitioner
persona — **decision-support only**. It is the runtime sibling of A8's automated
SME-persona review: it is recorded-as-ran and attaches findings, but **a FLAG it raises
never self-blocks** and it **never emits "approved by a competent person."** It
**PRECEDES — and never replaces, never emits — the mandatory human competent-person
review** that signs off the artifact (SME-02 boundary).

> **HSE-SME-Reviewer** — *Decision-support adversarial pre-human review; runs after
> the Critic/QA pass, before the artifact is handed to a human competent person.*
> **Role:** read the finished artifact as a sceptical competent HSE practitioner and
> flag (do not fix) everything a regulator or auditor would challenge. **Returns:** a
> findings list (each a FLAG, never a block) covering, at minimum:
> - **generic controls** — any control not specific to the named task/site/asset;
> - **PPE/admin-only treatments** — any hazard "controlled" by PPE or administration
>   alone without a higher-order control justified-or-escalated;
> - **un-named owners** — any action/control without a named accountable owner;
> - **missing review triggers** — any control with no review date / no re-assessment
>   trigger;
> - **un-evidenced claims** — any conclusion not traced to a cited source (source + year);
> - the overarching test: **"would this survive a regulator?"** — flag anything that
>   would not.
> **Tools:** Read only (it reviews; it never writes, scores, or signs off).
> **Scope-out:** does NOT approve the artifact, does NOT stand in for the human
> competent-person sign-off, and a FLAG it raises is **recorded, never merge-blocking**
> (the deterministic hard blocks — de-id leak, invented citation, weighted score <4.0 —
> are a separate enforcement class owned by A8).

---

## Sector-pack SME-persona extension slots (NAMED stubs — fleshed out in Phase 6 / pack D)

Sector packs (D) register sector-specialized SME-persona archetypes here (or in a
sector-scoped sibling under `prompt-snippets/`), following the same
**Role · Returns · Tools · Scope-out** shape, the same `KB-SNIP-…` ID scheme, and the
same decision-support-only / FLAG-never-blocks discipline as the HSE-SME-Reviewer above.
v1.0 ships the five slots **named, as stubs**; the consuming packs author the full
persona bodies.

### Process-Safety Engineer *(slot — `hse-process`, Phase 6)*
> **Role:** *(stub)* review process-safety artifacts (PHA/HAZOP, LOPA, PSM elements) as a
> process-safety engineer. **Returns:** *(stub — authored in Phase 6).* **Tools:** Read.
> **Scope-out:** decision-support only; FLAG never blocks; precedes the human review.

### Chemical-Process-Safety *(slot — `hse-chemicals`, Phase 6)*
> **Role:** *(stub)* review chemical hazard / MSIHC / reactive-chemistry artifacts as a
> chemical-process-safety specialist. **Returns:** *(stub — authored in Phase 6).*
> **Tools:** Read. **Scope-out:** decision-support only; FLAG never blocks; precedes the
> human review.

### India-Regulatory *(slot — `hse-india`, Phase 6)*
> **Role:** *(stub)* review India-jurisdiction artifacts (Factories Act, state forms,
> BOCW, the OSH Code transition) as an India-regulatory specialist. **Returns:** *(stub —
> authored in Phase 6).* **Tools:** Read (state-resolved KB fragments). **Scope-out:**
> decision-support only; FLAG never blocks; precedes the human review.

### Aviation-SMS *(slot — `hse-aviation`, Phase 6)*
> **Role:** *(stub)* review aviation safety-management-system artifacts (SMS, hazard
> registers, ICAO Annex 19) as an aviation-SMS specialist. **Returns:** *(stub —
> authored in Phase 6).* **Tools:** Read. **Scope-out:** decision-support only; FLAG
> never blocks; precedes the human review.

### Mine Manager *(slot — `hse-mining`, Phase 6)*
> **Role:** *(stub)* review mining-safety artifacts (statutory mine-manager duties,
> ground control, ventilation) as a mine manager. **Returns:** *(stub — authored in
> Phase 6).* **Tools:** Read. **Scope-out:** decision-support only; FLAG never blocks;
> precedes the human review.
