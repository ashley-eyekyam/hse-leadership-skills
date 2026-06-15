# Risk-assessment intake — Noise exposure, Press Shop (PPE-only proposal)

De-identified intake. All personnel are role labels. This case deliberately proposes
ONLY a PPE control so the skill must escalate the hierarchy of controls.

## Scope (Q0)
Occupational safety.

## Jurisdiction (Q1)
UK.

## Industry (Q2)
Manufacturing — metal pressing.

## Task / activity (Q3)
Operating the mechanical power press line in the press shop during a production run:
load blank -> press stroke -> eject -> stack. Continuous high-noise environment
(measured ~92 dB(A) at the operator position over an 8-hour shift).

## Location / site (Q4)
Press shop, line 2.

## Who is exposed? (Q5)
Own workers (press operators, stackers).

## Existing controls already in place (Q6)
The ONLY control currently proposed for the noise hazard is hearing protection
(disposable ear plugs issued to operators). No engineering or substitution control is
proposed; no justification is recorded for why higher-order controls are not used.

## Likelihood / severity / matrix (Q7 / Q8 / Q9)
Org 5x5 matrix.

## Assessment type (Q10)
Issue-based (the noise hazard specifically).

## Notes for the assessor
This is a PPE-only treatment of a noise hazard. The skill must NOT accept hearing
protection as the sole control: controls.rank_controls should return
ppe_admin_only = True, and the output must EITHER add a higher-order control
(engineering: enclose/dampen the press, acoustic guarding; substitution: quieter
tooling/press) OR record an explicit "higher-order controls not reasonably
practicable because…" justification. An output shipping ear plugs alone, with no
higher-order option and no justification, scores <=2 on hierarchy_of_controls.
