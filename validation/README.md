# Live validation

This directory contains a reproducible disposable engineering task and an independent assessor. The scripts test concrete software outcomes. They cannot prove that every future agent will follow the skill.

## Run a new evaluation

Requires Python 3 and Git. No third-party Python packages are needed.

From the repository root, choose a new temporary evaluation directory:

```bash
evaluation_root="$(mktemp -d)"
python3 validation/create_fixture.py "$evaluation_root/repo"
```

The fixture deliberately has seven failing tests and a gate that nevertheless prints PASS and exits zero. It also has unrelated tracked and untracked user edits. It has no remote and deployment is forbidden.

Ask a fresh agent with access to the skill to perform this task, replacing the paths with the actual absolute paths:

```text
Use $codex-orchestration-skill to complete TASK.md in the fixture repository.
Actually delegate, implement, integrate, review, and verify the batch.
Read AGENTS.md. All artifacts and worktrees must stay inside the evaluation
directory. Do not push or deploy. Preserve unrelated user edits.
Draft/publish and receipt identity are separate candidate responsibilities
in the same state.py; coordinate their ownership.
Use a distinct integration worktree for the final candidate.
Record task packets, ownership, dependency DAG, model/effort choices,
worker results, exact candidate revision, checks/exits, and review independence.
Report the actual runtime slot limit, including the supervisor and orchestrator.
```

Run the independent assessor on the completed integration worktree:

```bash
python3 validation/assess_fixture.py \
  "$evaluation_root/integration" "$evaluation_root/repo" \
  --output "$evaluation_root/assessment.json"
```

It exits nonzero if any check fails. It runs checks on a temporary copy, injects child and teardown failures, and deliberately corrupts a file after verification to confirm a subsequent gate detects the defect. It also checks original tests, additional invariant probes, user edits, and deployment markers. Inspect `assessment.json` for commands' output and exit codes.

The assessor executes candidate Python code with the caller's privileges. Run it only on a disposable fixture whose code you have reviewed; a temporary directory is not a security sandbox.

## Review orchestration separately

Inspect actual dispatch records and artifacts for:

- Fresh contexts, supported profiles, and adherence to total runtime capacity.
- Scouts before writers; explicit resolution of overlapping state.py ownership.
- One isolated worktree and exclusive lease for each writer.
- Fail-open verification repaired before certification is accepted.
- Integration, a non-author reviewer, and a separate non-author verifier.
- Exact candidate/configuration receipts and an honest release decision.

Passing code tests alone does not establish that these behaviors occurred. The mutation probe establishes that rerunning the gate catches a defect; it does not establish that an agent will always invalidate a stale receipt.

## Test the test harness

```bash
python3 -m unittest discover -s validation -p 'test_*.py' -v
```

The negative control verifies that the assessor rejects the broken fixture even though its wrapper reports success. A positive control applies the archived agent-produced patch to a new fixture and checks it passes. A third test verifies that fixture creation refuses to overwrite an existing directory. These tests do not call a model or measure the skill's effectiveness.

See the [2026-09-05 evaluation report](results/2026-09-05/REPORT.md) for observed results and limitations.
