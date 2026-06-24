# Methodology — the catalog router's handover method

This file houses the method detail the SKILL.md Workflow points to, so the body stays lean.
It covers: how the Context Capsule is composed, what a continuation prompt must and must not
contain, why an attached prior output is already de-identified, the Step-4a iteration-trail
convention, the Step-1-in-place vs Steps-2+-fresh-chat asymmetry, and the opt-in
expand-to-standalone fallback. The router produces no HSE artifact; its deliverable is an
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
