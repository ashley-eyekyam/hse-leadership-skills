# deid-canary — the de-id auto-fail self-test fixtures (CR-01)

These two artifacts are **not a skill**. They are the negative/positive controls
that prove the deterministic de-identification hard block (`graders/deid.py`) is
actually wired and enforcing — independently of any model call.

- `leak.md` — a SEEDED de-id leak (real name + DOB + phone + national ID + an
  embedded re-identification key + a small injury cell). The grader MUST hard-fail
  this.
- `clean.md` — the same report properly pseudonymized/aggregated. The grader MUST
  pass this.

The `deid-auto-fail` CI job runs `run_evals.py --deid-selftest`, which grades both
and exits nonzero unless `leak.md` auto-fails AND `clean.md` passes. This is the
fix for CR-01: the keyless job previously re-executed the skill with no API key,
so the executor returned `""`, the grader scanned nothing, and the job passed
unconditionally. It now asserts the hard block against real captured artifacts.

There is deliberately no `evals/evals.json` here, so the normal `--all` /
`--changed` sweep (which scans for `evals/evals.json`) never picks this directory
up — the seeded leak must never fail the real skill eval set, only the dedicated
self-test.
