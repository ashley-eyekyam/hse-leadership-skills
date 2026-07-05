---
sme-review:
  personas:
    - role: "Chartered process-safety engineer & certified HAZOP chair/facilitator (TÜV FSEng / CMIChemE)"
      expertise: "IEC 61882 node-based HAZOP; guideword×parameter completeness; cause→consequence→safeguard logic on P&IDs; risk-ranked recommendation tracking; New / Revalidation / Write-up study modes."
      lens: "Would this worksheet survive a regulator's / licensor's review as a competently-facilitated, team-recorded HAZOP — and is every credible deviation either addressed or honestly [GAP]'d, never silently dropped?"
modes:
  worksheet:
    detected_by: "Q12 — What output do you need? (Worksheet only / Full report / Recommendation register — all emit the IEC 61882 node worksheet, the skill's single artifact class)"
    floor:
      - id: bounded-node-design-intent
        description: "One bounded node/P&ID section with its normal-operation design intent stated (flow, pressure, temperature…) — deviations are judged against that intent (intake Q2/Q3 specificity anchor); the design LIMITS the severities are judged against (MAWP / design pressure, design temperature) are recorded or explicitly [GAP]'d (19-02 canary fold-back)"
        anchors: ['node', 'design intent']
        min_matches: 2
      - id: guideword-parameter-coverage
        description: "Every relevant guideword × parameter cell is analysed or explicitly closed ('[GAP]' or 'not credible — justified') — no silently empty cells (KB-STD-IEC-61882 matrix discipline); the parameter SET itself is justified — parameters not examined (level, phase, time/sequence where relevant to the service) are recorded as considered-and-excluded, never silently absent (19-02 canary fold-back)"
        anchors: ['guideword', 'not credible|no credible deviation']
        min_matches: 1
      - id: deviation-chain-complete
        description: "Each row traces Deviation → Cause → Consequence → Existing safeguards → Recommendation whole; a consequence with no cause (or vice-versa) is incomplete"
        anchors: ['deviation', 'cause', 'safeguard']
        min_matches: 3
      - id: team-recorded-not-autonomous
        description: "The multidisciplinary team + chair/scribe are recorded as roles and the worksheet reads as team-recorded; an incomplete team carries the 'study not yet performed' banner (intake Q8/Q9, the assistive core)"
        anchors: ['multidisciplinary', 'chair|scribe']
        min_matches: 1
      - id: safeguard-hoc-adequacy
        description: "Safeguards are hierarchy-of-controls-ranked; a high-consequence deviation carried by administrative/PPE safeguards alone gets a higher-order closing recommendation (KB-SNIP-HOC applied to safeguards)"
        anchors: ['hierarchy of controls', 'higher.order (safeguard|control|recommendation)']
        min_matches: 1
      - id: recommendations-node-linked-owned
        description: "Each recommendation is a specific change linked to its node/deviation with a named role owner + due date, tracked to closure — never 'consider' / 'review further'"
        anchors: ['named owner|action owner', 'due date', 'tracked to closure|node.{0,40}(link|ref)']
        min_matches: 2
      - id: consequence-risk-ranked
        description: "Each deviation's consequence is risk-ranked (severity × likelihood band) on the named matrix (intake Q10, risk_matrix output)"
        anchors: ['risk rank|risk band|severity', '5.?[x×].?5|matrix']
        min_matches: 1
      - id: iec61882-grounding
        description: "The study method is grounded in IEC 61882 (cited from KB-STD-IEC-61882), plus the jurisdiction's PHA duty where one applies (OSHA PSM PHA element)"
        anchors: ['IEC 61882', 'KB-STD-IEC-61882']
        min_matches: 1
      - id: study-record-identity-and-basis
        description: "The record carries its filing identity and study basis — study type (new / revalidation), the workshop session date, and the source-document register (P&ID no./revision, line list, prior PHA) — each present or an explicit [GAP] with a closure action; a worksheet that cannot be tied to a session date and a P&ID revision cannot be filed as a PHA record (19-02 canary fold-back, D-14)"
        anchors: ['workshop session date|study date|session date', 'P&ID', 'study type|revalidation']
        min_matches: 2
---

# SME Review & Sign-off — hazop-facilitator

This skill carries **one** specialized SME lens: a certified HAZOP chair. It narrows the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) to the
IEC 61882 node-based worksheet; the generic **HSE-SME-Reviewer** hook is the inherited
fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**HAZOP is an assistive, team-recorded study.** The bounded node and the multidisciplinary
team are the assistive evidence: no full team present → the worksheet is structured and
marked **"study not yet performed"**, never presented as a completed HAZOP. The
**New / Revalidation / Write-up** study-mode branch is in scope for v1.0 (a revalidation
adds the change-delta / prior-recommendation-status view); it is the already-resolved
scope, not a new gap. A deviation, cause, consequence, or severity the team did not raise
is recorded `[GAP]`, never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every defined node has every relevant guideword×parameter cell analysed or explicitly `[GAP]`/"not credible — justified" — no silently empty cells.
- [ ] Each deviation traces a sound Deviation → Cause → Consequence → Existing-safeguard → Recommendation chain; a consequence with no credible cause (or a cause with no consequence) is flagged incomplete.
- [ ] No unmitigated high-consequence deviation: any high-severity deviation lacking a safeguard AND a closing recommendation is surfaced.
- [ ] Recommendations are actionable (specific change + node link + named owner + due date), not "review further" / "consider".
- [ ] Each node carries its normal-operation design intent, and deviations are judged against that stated intent — not against an unstated one.
- [ ] The worksheet names the multidisciplinary team + competencies (process, operations, instrumentation/SIS, mechanical, chair/scribe) and reads as team-recorded; an incomplete team carries the "study not yet performed" banner, and no deviation the team did not raise appears (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A worksheet of populated rows over an unswept matrix** — the recorded deviations look
  rigorous, but nothing shows the guideword × parameter cells that were EXAMINED and
  closed; the reader cannot distinguish "analysed, not credible" from "never asked", which
  is the difference between a HAZOP and a list of worries.
- **Confident engineering values with no provenance** — a likelihood, PFD or severity that
  the team never agreed, written in as fact instead of [GAP]; the worksheet reads
  authoritative precisely where it is invented.
- **Recommendations that dissolve on contact** — "review further", "consider upgrading" —
  no specific change, no node link, no owner, no date; the study produced activity, not
  closure.
- **The intent-less node** — deviations ranked against an unstated design intent; every
  judgement in the sheet is unanchored and unrepeatable at revalidation.
- **Safeguard credit with no independence case** *(19-02 canary fold-back)* — alarms and
  trips credited as separate layers with no BPCS/SIS split, no SIL, and no independence
  from the initiating failure; the safeguard column reads engineered precisely where it is
  unverifiable. Where a High deviation needs a layer count, reference `lopa-worksheet` —
  never rebuild it here.
- **The jurisdiction hook cited, its element set unswept** *(19-02 canary fold-back)* —
  "OSHA PSM PHA element" invoked while facility siting, human factors and incident history
  (29 CFR 1910.119(e)(3)) are silently absent; the frame is named but its demanded content
  is never addressed or [GAP]'d.
- **The high-severity open item with no bridge** *(19-02 canary fold-back)* — an
  acknowledged-inadequate safeguard rides a weeks-out recommendation due date with no
  interim measure and no justification; severity and urgency silently decoupled.
- **Single-cause deviations** *(19-02 canary fold-back)* — every chain reads complete but
  no cause SET was swept (fire case, control-valve failure modes, utility loss); prompt the
  team for the full credible set, record what they raise, never invent.

## Sign-off note
SME review: ran (persona: Chartered process-safety engineer & certified HAZOP chair); this
is **decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
