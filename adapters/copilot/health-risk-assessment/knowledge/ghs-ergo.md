<!-- KB-STD-GHS-ERGO -->
# Ergonomics assessment methods — NIOSH / RULA / REBA (method→artifact map)

**Fragment ID:** `KB-STD-GHS-ERGO`
**What this is:** a copyright-safe **method → output-artifact map** for the three
published manual-handling / posture ergonomics methods — the NIOSH revised lifting
equation, RULA, and REBA — describing what each method scores and how it grounds an
ergonomics risk assessment. Pairs with the SUB-01 ergonomics engine.
**What this is NOT:** a reproduction of the copyrighted scoring tables (RULA/REBA
Tables A/B/C; the NIOSH frequency/coupling tables). The engine embeds the published
constants under their own citation; this fragment maps the *method structure* only.

> Source: NIOSH revised lifting equation (Waters et al. 1993; NIOSH 94-110, public-domain US-gov) · RULA (McAtamney & Corlett 1993) · REBA (Hignett & McAtamney 2000) — method structure · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false (stable published methods).

These three methods cover manual-handling and working-posture ergonomic risk. The
SUB-01 engine (`scripts/hse_components/ergonomics.py`) computes the scores from the
published formulas/tables; this fragment is the structural reference that grounds an
ergonomics assessment and tells the skill which method fits the task.

## Method → what it produces → what it grounds

| Method | Scores | Output | Grounds (artifact) |
|---|---|---|---|
| **NIOSH** revised lifting equation | `RWL = LC × HM × VM × DM × AM × FM × CM` (LC = 23 kg); Lifting Index `LI = load / RWL` | RWL (kg) + LI | manual-lifting risk evaluation |
| **RULA** (McAtamney & Corlett 1993) | Group A (arm/wrist) + Group B (neck/trunk/leg) → Table C grand score 1–7 | grand score 1–7 + action level (1–4) | upper-limb / whole-posture screening |
| **REBA** (Hignett & McAtamney 2000) | Group A (trunk/neck/leg) + Group B (arm/wrist) + activity → final score 1–15 | final score 1–15 + action level (1–5) | whole-body postural-load assessment |

## Method-selection note
- **NIOSH** — lifting/lowering tasks where a recommended weight limit matters.
- **RULA** — rapid screening of upper-limb-dominant static postures (e.g. seated/VDU).
- **REBA** — whole-body, dynamic or unpredictable postures (e.g. patient handling).
- The LI / action levels are computed by the engine — never invented; the score
  feeds control selection ranked via `KB-SNIP-HOC` (engineer the task, not the worker).

## How the skill uses this fragment
- Grounds ergonomics risk-assessment work; the chosen method's score comes from the
  engine, and the action level drives the hierarchy-of-controls recommendation.
- Missing posture/load inputs are recorded as `[GAP]`, never assumed.
