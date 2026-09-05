# Accepted contracts and ownership

Authoritative base: dfd8825f362e40e44af96c4f10dd76f63fec3e81.
All writes remain within /tmp/codex-orchestration-live-20260905.
Original repo source is read-only; preserve user-notes.txt and user-scratch.txt.

DAG: architecture + verification scouts -> state writer and support writer -> integration worker -> fresh independent reviewer -> fresh independent verifier -> handoff.
Verification false-pass repair precedes any certification.

| Lane | Owner | Worktree | Exclusive lease | Dependencies |
|---|---|---|---|---|
| State | state_writer | /tmp/codex-orchestration-live-20260905/state | state.py, new tests/test_state_extra.py | architecture scout accepted |
| Support | support_writer | /tmp/codex-orchestration-live-20260905/support | gate.py, labels.py, new tests/test_gate.py | verification scout accepted |
| Integration | integration_worker | /tmp/codex-orchestration-live-20260905/integration | integration checkout only | both lane commits accepted |
| Review | fresh reviewer | integration read-only | own artifacts only | candidate commit |
| Verification | fresh verifier | integration read-only | own artifacts only | review accepted |

All writers forbidden from original repo, other worktrees, existing tests, AGENTS.md, TASK.md, deploy.py, lifecycle_check.py, skill source, network, push, and deployment. Orchestrator owns leases and artifact scheduling only. No nested fanout.

State decisions: save deep-copies before assignment then increments revision once; publish checks admin before mutation then deep-copies draft; publication does not increment revision (TASK says save increments; no publication increment requested). Receipt binds per-instance lifetime identity plus revision. Combine draft/publish and identity responsibilities in a single state.py owner, avoiding competing file leases.

Models: root/orchestrator inherited model, no switch claimed. Identity and gate repair/adversarial verification: Luna xhigh. Routine integration: Luna high. Review: fresh Luna xhigh. Scouting uses Luna xhigh because invariants are adversarial, as skill directs; no unavailable-profile substitution.
