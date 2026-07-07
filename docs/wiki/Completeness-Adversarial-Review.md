# Completeness & Adversarial Review

A defensible HSE artifact is judged as much by what it **leaves out** as by what it says. A control that was never considered, a jurisdiction step that was never checked, a residual-risk figure that was quietly skipped — these silent omissions are what a regulator or an experienced auditor tends to find first. This page describes the completeness contract that every skill in the pack now runs, and how it is held in place by the quality harness.

> ⚠️ **Decision-support only.** The completeness contract makes missing work **visible** to your accountable competent-person review. It never claims the document is complete, approved, or fit to rely on — that judgement remains yours. See [`DISCLAIMER.md`](../DISCLAIMER.md).

---

## What the omission pass does

Every skill's built-in SME (subject-matter-expert) review runs an **omission pass** over its own draft before you see anything. Acting as the domain-expert persona for the artifact it is emitting, the skill asks an open-ended question first:

> For the deliverable I am actually producing, what would a competent consultant have included that is **absent** from this draft?

Only after answering that in its own words does it check the draft against that answer. The order matters: it is **open-ended first, then check** — deliberately not a fixed tick-box list.

## Why open-ended, not a checklist

A checklist can only find the gaps that someone remembered to write down. The omissions that actually sink a safety document are the ones no checklist anticipated — the unusual exposure, the missing interface control, the step that only applies in one jurisdiction. By reasoning open-ended first and only then reconciling against the draft, the omission pass can surface a gap that no pre-written list contained. The checklist becomes a floor, not a ceiling.

## What the completeness pair proves

The behaviour is held in place by a **completeness pair** built into the quality harness, one per skill:

#### The complete reference

A full, well-formed reference deliverable for the skill's artifact. It should score **high** on completeness — a competent draft has nothing conspicuously missing.

#### The gutted probe

The same artifact with sections, controls, and required elements deliberately **stripped out**. It should score **low** — a good omission pass notices the holes.

The **measurable separation** between the two scores is the signal. If a skill stops noticing what is missing, the complete reference and the gutted probe drift together, the separation collapses, and the check fails. The scores are produced by a **keyless, local grader**, so the result is reproducible rather than a subjective opinion.

## A hard, deterministic gate

The completeness separation is now a **hard gate**, not an advisory metric. A skill whose pair no longer separates cannot pass — the same way a de-identification leak or an invented citation is a non-waivable failure elsewhere in the quality gate. Because the grader is deterministic and local, the gate gives the same verdict on every run.

## The [GAP]-not-invented discipline

The single most important boundary of the omission pass: it **surfaces gaps — it never fabricates to fill them.**

When something required is missing or cannot be verified, the skill records it as a literal `[GAP]` marker or a named deficiency in the draft. It does **not** invent a form number, a measurement, a threshold, or a citation to paper over the hole. A missing India state form stays `[GAP]` until it is verified; an unstated gas-testing regime is flagged, not guessed. This is what keeps the completeness discipline inside the decision-support boundary — it makes the missing work visible to your review, it does not silently perform that work for you.

## What this means for you

- **You still own sign-off.** The omission pass strengthens the draft and points at what is missing; your competent-person review remains the accountable step.
- **Gaps are a feature, not a defect.** A draft that comes back with `[GAP]` markers is telling you exactly where to look — that is the contract working as intended.
- **Consistency across the pack.** The same completeness discipline runs inside every skill, so an audit, an SOP, and a risk assessment are all held to the same standard for what must not be silently omitted.

---

## Related pages

- [Home](Home) — the full skill manual and the five universal rules.
- [Start Here — Guided Mode](Start-Here-Guided-Mode) — the `/using-hse-skills` router for when you are unsure which skill to run.
- [`DISCLAIMER.md`](../DISCLAIMER.md) — the decision-support boundary in full.
