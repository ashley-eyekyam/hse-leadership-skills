# Methodology — the catalog router's handover method

This file houses the method detail the SKILL.md Workflow points to, so the body stays lean.
It covers: how the Context Capsule is composed, what a continuation prompt must and must not
contain, why an attached prior output is already de-identified, the Step-4a iteration-trail
convention, the Step-1-in-place vs Steps-2+-fresh-chat asymmetry, the opt-in
expand-to-standalone fallback, and the persist-then-clear rule (persist the run sheet, then gate
Step 1 on clearance). The router produces no HSE artifact; its deliverable is an
intuitive, educative, de-identified run sheet that chains the recommended skills.

## Context Capsule composition

The Context Capsule is emitted ONCE at the top of the run sheet and is the single block the
user pastes at the top of each fresh chat for Steps 2+. It is a compaction artifact — the
distilled shared context, not a transcript. It carries exactly:

- the six shared, carry-over facts the Step-0 intake captured (intent/scope, the named
  subject, the deliverable/success-criteria, jurisdiction — including the resolved India
  state where the branch ran — industry, and the exposed population);
- the agreed SEQUENCE MAP (the ordered chain `skill1 → skill2 → skill3 …`);
- a one-line de-id notice stating that role labels are used and the re-identification key is
  held separately.

It carries role labels ONLY (`[SITE-1]`, `[ROLE: site manager]`, `[CONTRACTOR]`). It must NOT
carry any verbatim identifier (name, address, phone, government or payroll ID, date of birth,
health detail) and must NOT carry the re-identification key or any name-to-label mapping. The
deep, per-artifact facets (scoring, baseline, evidence, obligations, competency, temporal,
location) are NOT in the capsule — each chosen skill's own intake asks for those.

## What a continuation prompt MUST contain (Steps 2+)

Each later step is a lean continuation prompt, not a self-contained context repeat. It carries:

- **WHY** — one line tying the step to the elicited intent / success-criteria (ROUTE-03).
- **RUN** — the explicit invocation (`/skill-name` or "use the X skill").
- **REFERENCE** — a pointer to the Context Capsule above ("paste the Context Capsule first"),
  so the shared context is carried by reference, not re-pasted.
- **ATTACH** — the specific prior skill OUTPUT to carry forward (e.g. the risk-assessment
  control set + residual risks), with the reassurance that it is already de-identified.
- **DELTA** — only the step-specific new detail (e.g. the permit type and validity window).
- **DEPENDENCY** — Independent (any order) or Dependent (run after Step N).
- **FEEDS →** — what this step hands to the next step.

## What a continuation prompt MUST NOT contain

- The full repeated shared context (that is what REFERENCE-to-capsule replaces — the whole
  point of the asymmetric run sheet is one capsule, not N repeats).
- Any verbatim direct identifier, or the re-identification key / name-to-label mapping. The
  capsule and every continuation prompt are in scope of the de-identification HARD-fail gate.

## The attached output is already de-identified

When a continuation prompt says ATTACH the prior skill's OUTPUT, that output is the prior
skill's own emitted, already-de-identified deliverable — every target skill runs its de-id
pass FIRST before emitting anything. So the chain stays clean as long as the user attaches the
skill's emitted output, not their raw notes. The educative Step-5 copy states this explicitly,
so the user carries the de-identified output forward and never re-introduces raw identifiers
into the next chat.

## Step-4a iteration-trail convention

The confirm-or-refine gate offers three choices on the echoed context + draft chain: accept /
edit / re-scope. An EDIT folds the change into the already-captured facts (it introduces no new
elicitation question), RE-DRIVES the Step-2 match so the chain refines, and shows a single
short iteration-trail line of what changed and why ("refined X because Y"). The gate loops until
the user accepts. This is the recommendation-accuracy lever: it corrects a mis-scoped chain
before any skill runs, and it is a Workflow addition only — it adds no ELI-* facet.

## Step-1-in-place vs Steps-2+-fresh-chat asymmetry

Step 1 runs in the triggering chat because the first skill does the heavy lifting and fills
that chat with context. Each later step is preferably run in a fresh chat because a long chat
degrades model focus (context rot); a fresh chat stays fast, and the Context Capsule re-seeds
the shared context cheaply. On a host with the Skill tool, Step 1 is invoked in place seeded
with the confirmed facts. Off-platform (no Skill tool), the run sheet prints a complete,
copy-pasteable Step-1 block to paste into the same chat — Step 1 is never part of the
copy-paste-to-fresh-chat set, preserving graceful degradation (ROUTE-04).

## Opt-in expand-to-standalone fallback

For a user who cannot carry the capsule between chats, the run sheet offers a short opt-in
"expand to standalone" note: it inlines the full shared context for one step so that single
step self-runs without the capsule. This preserves the old standalone-single-step behaviour as
an opt-in fallback rather than the default — the default is the lean capsule + continuation
prompts, which is the more intuitive, lower-token, smaller-de-id-surface path.

## Persist-then-clear (persist the run sheet, then gate Step 1)

The run sheet is the router's PRIMARY deliverable, but Step 1 floods the triggering chat — so
the durable Steps-2+ plan must be in the user's hands BEFORE Step 1 runs, and Step 1 must wait
for the user's go-ahead. This is the agent Plan-Mode shape: write the plan, present it, require
explicit approval, only then execute. The Workflow order is therefore 4a confirm-or-refine →
4b emit + persist + present → 4c clearance gate → 4d run Step 1 in place (gated).

**Portable persist (write-file vs present-save-block, by host capability).** "Persist" means
"produce a durable, user-held markdown artifact"; the mechanism degrades gracefully and never
assumes a filesystem (ROUTE-04):

- **File-capable host (has a file-write tool):** write the run sheet to a `.md` file and
  **surface its path** to the user (e.g. "Saved to: `hse-run-sheet-<subject-slug>.md`"). Surface
  the path means tell the user the exact filename/location so they can re-open it after Step 1
  has filled the chat.
- **Chat-only host (no file-write tool):** present the SAME run sheet as ONE clearly-delimited,
  copy-pasteable fenced markdown **save-block**, with an explicit instruction ("save this as your
  Steps-2+ run sheet"). The copy-paste block IS the portable degradation of persistence — the
  same plain-text-the-user-carries story as the Context Capsule itself.

The branded "HSE Skills Roadmap" docx/pdf (D-07) stays the OPT-IN render layer on top of this
plain-markdown default; chat-only hosts must not depend on the report engine.

**De-identified filename convention (role-label slug only).** The persisted filename is a
role-label / subject slug ONLY — e.g. `hse-run-sheet-re-roofing.md` — and NEVER a verbatim name,
home address, government ID, or precise site identifier. The filename is itself a circulated
surface, so it carries no identifier.

**What the persisted file MUST contain (the complete standalone plan).** The saved file is
self-sufficient — it is the WHOLE plan, not "only from step two": the ONE Context Capsule + the
ordered chain table + a Step-1 record (what Step 1 is / that it runs in place) + ALL Steps-2+
continuation prompts (with the opt-in expand-to-standalone note). A user who re-opens the saved
file after Step 1 has scrolled away has everything needed to resume each later step.

**What counts as clearance.** The clearance gate (Step 4c) asks ONE go/no-go on the presented
run sheet. Accepted clearances are **"go"**, **"proceed"**, or **"run step 1"**. An **"edit"**
routes back to Step 4a — re-drive the Step-2 match on the (possibly amended) facts and
**re-persist** the run sheet before re-presenting it. The gate is a Workflow control-flow step,
not a new elicitation facet (no ELI-* question is added — it asks for a go/no-go decision on a
presented artifact, not for a new fact).

**The persisted file is a de-id surface.** The written `.md` (or the chat-only save-block) is in
scope of the non-waivable de-id HARD-fail gate exactly as the inline capsule + continuation
prompts are: it carries role labels only, no verbatim identifier, no re-identification key, and
no name-to-label mapping. De-id runs FIRST (Workflow Step 3) — before the file is written — so
you can never present a file you have not scrubbed.

**Step 1 NEVER auto-fires.** On EVERY host, including a Skill-tool host, the clearance gate
precedes the Step-1 side effect; Step 1 is invoked only on the user's explicit clearance. This
overrides the earlier micro-behaviour where Step 1 auto-invoked in place on a Skill-tool host.
