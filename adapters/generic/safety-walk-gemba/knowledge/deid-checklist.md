# De-identification Checklist — Safety Walk / Gemba (REINFORCED — psychological safety)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This skill captures live worker voice.** Concerns raised on a leadership walk are
> sensitive: a worker who speaks up must not be identifiable from the record, or
> psychological safety collapses and the next walk surfaces nothing. The reinforced rule
> below — **no worker concern is ever attributed to a nameable individual** — is stricter
> than, and additional to, the standard de-id block, and it is enforced as a
> `de_identification` **hard-fail** in the eval suite (the de-id PAIR, eval case 2).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
psychological-safety reinforcement the De-identifier subagent applies **FIRST**.

## 1. Treat the walk record as worker-attributable voice

What a worker says on a walk, plus their **role / crew / shift** and the **specific area /
task**, can together identify the speaker in a small team — even with the name removed.
Handle the whole walk record under the strictest tier from the first read, before any
drafting.

## 2. DETECT & FLAG every identifier up front

List, before drafting: worker names, contact details, addresses, payroll / employee IDs,
exact dates, photos, and any **role / crew / shift label fine-grained enough to identify**
the person who raised a concern in a small group. If unsure whether something is identifying
in a small crew, treat it as identifying.

## 3. PSEUDONYMIZE worker concerns to role/group labels

Replace every individual with a stable **role/group label** ("a night-shift operator", "the
pick-face crew"). **No worker concern is ever attributed to a nameable individual** — a
concern is recorded against the **role/group**, never a person ("Operator A raised…", not
"Priya raised…"). Produce (a) the de-identified walk record and (b) a SEPARATE
re-identification key. **Never embed the key or any name↔label mapping in the document.**

## 4. SMALL-GROUP CARE — do not single out a sole speaker

Where only one worker covers an area/shift, a concern attributed even to "the night-shift
lead" can re-identify them. Aggregate up to a broader role/group, or paraphrase so the
concern is not traceable to the single speaker. Never reproduce a verbatim quote that
identifies the speaker in a small team.

## 5. WARN BEFORE WIDE DISTRIBUTION

Management summaries, board packs, and any widely shared walk record default to fully
role/group-level concerns. Warn the user before any finer-grained attribution enters a
widely shared copy — a worker who is identifiable as the source of a concern is exposed.

## 6. MINIMIZE & LIMIT PURPOSE

Capture only what the walk needs to convert concerns into tracked commitments. Keep raw walk
notes out of external services where you can. Where a genuine legal question arises (a
suspected breach, a consultation duty), stop and defer to a competent person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, payroll ID).
3. No re-identification key / name↔label mapping embedded in the output.
4. **No worker concern attributed to a nameable individual** (the psychological-safety rule).

Any single failing condition is a non-waivable `de_identification` hard-fail.
