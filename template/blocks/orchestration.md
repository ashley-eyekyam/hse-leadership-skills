## Agentic Execution

This block governs **runtime fan-out** (decomposing the work of a single
invocation). It is platform-neutral: it never names a host API, only the pattern.

**Step 0 — Triage gate.** First judge the work. Map complexity to a subagent
budget, with MAX=6 fixed: simple → 0 subagents (single-threaded); moderate → 2–3
subagents; complex → 4–6 subagents. Never exceed MAX=6.

**Fan-out contract (when the triage gate calls for subagents).** For each job:
spin up a subagent with **fresh context**; **paste in all the context it needs**
(it cannot see this conversation); state its **scope-in / scope-out** explicitly
and name the sibling jobs so work is not duplicated; require a **bounded, cited
output** (findings traced to evidence, within a stated effort budget); then
**synthesize** the returned outputs into one coherent artifact.

**If your host has no subagent capability, execute each job sequentially in this
same context — keep the scope discipline and the required Critic/QA pass.**

**Critic/QA pass is mandatory** for any regulatory/safety/legal output (every
skill in this pack): after synthesis, run a dedicated critic that checks
specificity, the hierarchy of controls, defensibility, de-identification, and
citation accuracy before the artifact is returned.
