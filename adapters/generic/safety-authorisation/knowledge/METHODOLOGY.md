# Methodology — safety-authorisation

The domain method this skill applies: assemble a **ROGS application pack for submission to
ORR** for a named dutyholder, with the route resolved first, the existing rail SMS
**referenced as an input** (never rebuilt), and the framing held **for-submission**
throughout. It grounds in `KB-REG-ROGS` (the route map + the SMS duties the application
packages), `KB-REG-CSM-RA` (the change-evidence limb), and `KB-REG-IN-RAIL` (India
framing); the bundle cross-walk `KB-SNIP-RAIL-CLAUSE-MAP` keeps the sibling boundaries clean
(this skill references RAIL-01's SMS; RAIL-03 owns level crossings). **This skill authors no
unique new KB.**

## Step 0 — De-identify first
Run the de-identification scrub before any analysis (`references/deid-checklist.md`).
Named accountable duty-holders, safety-critical role-holders, COSS, and any **Sentinel
number** become role labels in any circulated copy; the re-identification key is held
separately, never embedded.

## Step 1 — Resolve the dutyholder route (do this once, hold it)
The route is the first determination, because the whole application is framed against it
(`KB-REG-ROGS`):

| Dutyholder | Application this skill assembles |
|---|---|
| Mainline **infrastructure manager** | **Safety authorisation** application |
| Mainline **transport operator** (transport undertaking) | **Safety certificate** application |
| **Non-mainline** operation (tram / metro / heritage) | **ROGS Part 3 safety verification** |

An authorisation where a certificate is required (or vice-versa) is an integrity-of-advice
error. If the dutyholder type is ambiguous, ask — do not default.

## Step 2 — Reference the SMS as an input (NEVER rebuild it) — CONV-12
The full ROGS/ORR Safety Management System is the artifact of the sibling skill
`rail-safety-management-system` (RAIL-01). This skill **takes that SMS as an input** and
assembles the *application pack that submits it*:

- Confirm the SMS exists and capture its reference/version. Cite **where each application
  claim draws on the SMS** (e.g. "risk-control arrangements per SMS §3").
- **Do NOT re-author or regenerate the SMS element set.** Reconstructing the nine ROGS/ORR
  SMS elements inside this skill is the boundary violation this skill must not make
  (`KB-SNIP-RAIL-CLAUSE-MAP`).
- If the SMS does **not** exist, route the user to **RAIL-01** to build it first, and record
  the SMS as a `[GAP]` input — never silently build one here.

## Step 3 — Assemble the ROGS application elements
Populate each application element with dutyholder-specific content; record `[GAP]` for any
element the inputs do not supply (never invented), and close each `[GAP]` with a SMART action
(`smart_actions`) carrying a named role owner and a due date:

1. **Applicant identity & route declaration** — the named dutyholder, the dutyholder type, and the route declared (authorisation / certificate / Part-3 verification).
2. **SMS reference & scope** — the reference to the existing SMS (RAIL-01's artifact) and the operation scope the application covers. *Referenced, not reproduced.*
3. **Risk-control summary** — a summary of the operation's significant risks and controls drawn from the SMS; every mitigation ranked through the hierarchy of controls (`controls.py` / `KB-SNIP-HOC`) under the **SFAIRP** adequacy test; no PPE/admin-only treatment without an explicit "higher-order not reasonably practicable" justification.
4. **CSM-RA change evidence** (`KB-REG-CSM-RA`) — for a significant change, the **significance test**, the demonstrated **risk-acceptance principle** (codes of practice / reference systems / explicit risk estimation), and the **independent AsBo** assessment. Live change details are `[GAP]` until supplied.
5. **Competence/Sentinel & ECM assurance** — the competence-management, fitness-for-duty, and Entity-in-Charge-of-Maintenance assurance the application relies on (referenced from the SMS; individual medical detail held separately).
6. **Declaration & submission** — the dutyholder's declaration and the submission package for ORR.

## Step 4 — Hold the for-submission framing
The application is assembled **for submission**. ORR is the **Safety Authority**; granting
the authorisation / certificate is *its* act. Never write that the application is
"authorised / accepted / approved / granted by ORR" — even where the user reports a decision
status (that is reported back as a fact, not restated as a regulator decision in the
application body).

## Step 5 — India branch (CONV-8)
For India rail, cite the **Railways Act 1989 / Commissioner of Railway Safety** framing
(`KB-REG-IN-RAIL`). **State detection is mandatory** for any non-railway-depot statutory
obligation; defer state-specific content to the `hse-india` engine; **no national form
number is asserted** — unverified references stay `[GAP]`.

## Step 6 — Evidence & traceability
Every application element traces to a supplied input, the referenced SMS, or a cited KB
fragment (quote `source`+`year`); no element rests on an un-flagged assumption. Every action
carries a named **role** owner and a due date. The output renders via the shared report
engine (the Output format block).
