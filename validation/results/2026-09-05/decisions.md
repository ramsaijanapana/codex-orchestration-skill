# Adjudication and ambiguities

- Two candidate responsibilities overlap in state.py. Architecture scout recommends combination; accepted as one exclusive state writer, no simultaneous shared-file writers.
- Verification scout recommended a broad single writer across state/labels/gate. Root chose two disjoint leases because labels/gate do not depend on state implementation. This preserves file ownership and allows urgent gate repair in parallel with the state lane.
- Baseline gate falsely prints PASS after failing tests and both diagnostic failures. Certification paused; support writer repairs gate before integrated canonical evidence is trusted. Baseline receipts are failure demonstrations, not certificates.
- Task does not say publication increments revision. Root specifies only save increments, so publication leaves revision unchanged.
- Unique lifetime identity representation is unspecified. An immutable per-instance token (UUID or object token) is acceptable; worker selects within contract.
- Skill capacity example assumes a single root. Here supervisor also consumes capacity, so only two children run concurrently. Finished child turns are not active capacity.
- Skill prefers two scouts before most writers. Both completed before the second writer; first writer depended only on completed architecture contract.
- Skill does not mandate a specific profile for independent review. Luna xhigh chosen for permissions, identity and false-pass adversarial analysis. Scouts used corresponding stronger Luna xhigh profile rather than Terra moderate for the same reason. No model availability substitution needed. Running orchestrator model inherited, not switched.
- Evidence artifacts are outside candidate worktree to avoid changing the verified source revision. Python cache writes are ignored and are not source candidate mutations.

- Scheduling update: integrator began accepted state cherry-pick while support writer finalized evidence. Integration support step explicitly waits for accepted support SHA; no uncommitted work copied. Both lanes must complete before cross-feature acceptance.

- Final-stage overlap: fresh verifier prepares environment/source identity while independent reviewer examines frozen candidate. Canonical gate is explicitly blocked until review acceptance. This overlaps read-only preparation without bypassing review dependency.
- Support writer reported focused checks but did not preserve a separate raw focused-test log; integrated worker raw 12-test output and independent final gate provide stronger final-candidate evidence. Support raw actual gate/lifecycle diagnostic logs are preserved.

- Review accepted on exact frozen SHA 364b9bda4409b2093a4487ffbafc31e302b3c654 with no findings. Verifier released to run canonical gate only after receipt existed and was read.
- Evidence quality limitation: reviewer receipt reports probes and exits but did not preserve separate raw logs; final independent verifier is required to preserve raw gate output. Reviewer reran unit discovery despite integrator success, an avoidable repeat beyond the requested targeted independent probes. No extra canonical normal gate was run by orchestrator workers before final verifier; supervisor separately ran its own independent assessment.

- Final verifier evidence contradiction: normal.stderr was zero bytes while gate-runs.md claimed it contained unit-test output. Orchestrator and supervisor independently found it by reading actual files. Certification blocked; verifier instructed to recover streams or run one controlled capture rerun, inspect saved bytes, and bind receipt to corrected completed invocation. This is a justified gate rerun for insufficient/contradictory evidence, not a source change. Verifier also reported an initial direct invocation plus capture invocation for each mode; capture planning could have avoided that duplication.

- Evidence correction accepted: actual normal.stderr now 111 bytes with Ran 12 tests / OK; stdout and stderr match receipt SHA-256 values. Both diagnostic logs contain full test output and expected failures. Orchestrator final-evidence-audit.json checked files directly; candidate HEAD unchanged and clean.
