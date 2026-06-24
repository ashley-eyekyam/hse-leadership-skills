# Methodology — rail-safety-management-system

The domain method this skill applies: build a **ROGS goal-based Safety Management
System** to the ROGS/ORR element set for a named dutyholder, with the route resolved
first and the framing held **for-acceptance** throughout. It grounds in `KB-REG-ROGS`
(ROGS 2006), `KB-REG-CSM-RA` (the change interface), and `KB-REG-IN-RAIL` (India
framing); the bundle cross-walk `KB-SNIP-RAIL-CLAUSE-MAP` keeps the sibling boundaries
clean (RAIL-02 references this SMS; RAIL-03 owns level crossings).

## Step 0 — De-identify first
Run the de-identification scrub before any analysis (`references/deid-checklist.md`).
Named accountable duty-holders, safety-critical role-holders, COSS, and any **Sentinel
number** become role labels in any circulated copy; the re-identification key is held
separately, never embedded.

## Step 1 — Resolve the dutyholder route (do this once, hold it)
The route is the first determination, because the whole SMS is framed against it
(`KB-REG-ROGS`):

| Dutyholder | Route artifact the SMS supports |
|---|---|
| Mainline **transport operator** (transport undertaking) | **Safety certificate** |
| Mainline **infrastructure manager** | **Safety authorisation** |
| **Non-mainline** operation (tram / metro / heritage) | **ROGS Part 3 safety verification** |

A certificate where an authorisation is required (or vice-versa) is an integrity-of-advice
error. If the dutyholder type is ambiguous, ask — do not default.

## Step 2 — Walk the ROGS/ORR SMS element set
Populate each element with operator-specific content; record `[GAP]` for any element the
inputs do not supply (never invented), and close each `[GAP]` with a SMART action
(`smart_actions`) carrying a named role owner and a due date:

1. **Safety policy & objectives** — the dutyholder's policy + measurable objectives.
2. **Accountabilities** — name the accountable duty-holder + safety-critical roles (role labels; the role is *filled*).
3. **Risk-control arrangements** — the operation's significant risks; controls ranked through the hierarchy of controls (`controls.py` / `KB-SNIP-HOC`) under the **SFAIRP** ("so far as is reasonably practicable") adequacy test; residual risk re-scored on the `risk_matrix` 5×5. No PPE/admin-only treatment without an explicit "higher-order not reasonably practicable" justification.
4. **CSM-RA change interface** (`KB-REG-CSM-RA`) — for a significant change, apply the **significance test** (safety relevance / novelty / complexity / monitoring / reversibility / additionality), demonstrate acceptability via one of the **three risk-acceptance principles** (codes of practice / reference systems / explicit risk estimation), and engage the **independent AsBo** (Assessment Body). Live change details are `[GAP]` until supplied.
5. **Competence & Sentinel** — competence management + fitness-for-duty for safety-critical work.
6. **Asset & ECM maintenance** — asset/infrastructure condition + Entity in Charge of Maintenance.
7. **Emergency arrangements** — preparedness + response coordination.
8. **Monitoring, audit & review** — the assurance and audit regime + the stated review cadence.
9. **Continuous improvement** — how the SMS learns (incident learning, audit findings) and improves.

## Step 3 — Hold the for-acceptance framing
The SMS is built **for submission / for acceptance**. ORR is the **Safety Authority**;
acceptance is *its* act. Never write that the SMS, certificate, or authorisation is
"accepted / approved / granted by ORR" — even where the user reports an acceptance status
(that is reported back as a fact, not restated as a regulator decision in the SMS body).

## Step 4 — India branch (CONV-8)
For India rail, cite the **Railways Act 1989 / Commissioner of Railway Safety** framing
(`KB-REG-IN-RAIL`). **State detection is mandatory** for any non-railway-depot statutory
obligation; defer state-specific content to the `hse-india` engine; **no national form
number is asserted** — unverified references stay `[GAP]`.

## Step 5 — Evidence & traceability
Every element traces to a supplied input or a cited KB fragment (quote `source`+`year`);
no element rests on an un-flagged assumption. Every action carries a named **role** owner
and a due date. The output renders via the shared report engine (the Output format block).
