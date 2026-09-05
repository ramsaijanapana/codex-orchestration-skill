# Evaluation report — 2026-09-05

**The skill completed a real disposable engineering batch, but did not produce perfect process compliance.** The evaluation found evidence-handling weaknesses, corrected the final evidence, and led to narrower, clearer skill instructions. No confidence percentage or universal reliability guarantee follows from these results.

## Live delegated run

The run started with skill repository revision `13469efe0af1f716d7445d818af2862a010b2c70`. A fresh orchestrator received the fixture requirements and skill, without the supervisor's implementation plan. It actually dispatched two scouts, two writers, an integrator, a non-author reviewer, and a separate non-author verifier. The [dispatch manifest](dispatch-manifest.json) records profiles and fresh contexts; the [ownership record](ownership-dag.md) records leases and dependencies.

The limit was four active agents including supervisor and orchestrator, leaving at most two concurrent children. Draft/publish and receipt identity shared `state.py` and were combined under one writer. Writers used separate worktrees. This validates a constrained run, not eight-agent throughput.

Baseline: nine tests, seven failures, while the broken gate printed PASS and exited zero. Both injected child and teardown failures also falsely passed.

Final fixture candidate: `364b9bda4409b2093a4487ffbafc31e302b3c654`.

| Check | Observed result |
|---|---|
| Final canonical gate | Exit 0; 12 tests passed; lifecycle completed |
| Forced child failure | Exit 7; no PASS marker |
| Crash after lifecycle assertions | Exit 1; no PASS marker |
| Supervisor independent assessment | All 16 checks passed |
| User work and original tests | Preserved |
| Deployment | Not performed |

The [assessment](live-assessment.json) includes real command output. The [independent verifier receipt](independent-verifier/verification-receipt.json) binds the candidate and environment to saved streams. The supervisor checked the final clean HEAD, stream contents, and normal-stream SHA-256 values against that receipt. The [candidate patch](candidate.patch) can be replayed on a new fixture; it is test evidence, not part of the skill's implementation.

## Observed failures and corrections

- The support worker supplied a focused-check summary without its separate raw log. Reviewer probes likewise lacked some raw artifacts. Later integration and final verification covered the candidate, but did not retroactively make earlier receipts complete.
- The verifier initially left `normal.stderr` empty while its narrative claimed it contained the 12-test output. Supervisor and orchestrator caught the contradiction and held certification. A controlled capture rerun produced the real stream; content and hashes were checked before acceptance.
- The reviewer repeated successful discovery, and the verifier repeated commands to capture output. This was avoidable overhead. The normal rerun needed to repair contradictory evidence was justified.
- The run exceeded its approximate twelve-minute planning budget. It did not demonstrate a speed or cost improvement.

The skill now requires per-check raw-log paths, inspection of supporting contents, capture during the original invocation, and evidence recovery or a focused rerun before accepting an incomplete receipt. Reviewers must identify why they are duplicating a successful check.

## Fallback and targeted regression

A separate fresh agent repaired a new fixture with delegation and additional worktrees forbidden. It committed only `state.py`, `labels.py`, and `gate.py` as `b83e3bbbed7de6bd20c75545bb80acc90a7f007b`. Author-run checks passed, and the supervisor's [independent assessment](fallback-assessment.json) passed all 16 checks. The agent correctly reported independent certification BLOCKED because it could not obtain the required independent roles.

That exposed ambiguous fallback wording: sequential work cannot provide fresh independent review. The skill now explicitly distinguishes delivering an implemented, self-checked candidate from completing independent certification.

A fresh agent then read the hardened skill and inspected a real synthetic receipt with a missing log and an empty stderr stream contradicting its claimed test result. It returned BLOCKED, requested candidate/configuration binding and recovered or rerun evidence, and correctly explained the unavailable-delegation limit. This is one targeted behavioral sample, not a statistical result.

## Reproduction and limits

Run the commands in the [validation guide](../../README.md). The harness has negative and positive controls and refuses to overwrite an existing directory. Its positive control replays the archived patch without calling a model.

These are small Python fixtures on one local environment. Production repositories, other model versions, persistent scheduling, hostile tools, forced wrong-checkout writes, real deployment, and larger fan-out remain untested. File leases remain instructions, not access controls. The mutation probe shows the gate detects a changed candidate when rerun; it cannot guarantee an agent always invalidates stale receipts. No deployment or private project data is included in these artifacts.
