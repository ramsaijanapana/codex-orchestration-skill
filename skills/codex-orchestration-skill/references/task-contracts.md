# Task contracts

Use these when preparing a batch, dispatching workers, and accepting results. Replace example values with observed repository facts. Keep logs in artifacts accessible to the receiving agent; never paste credentials into packets or receipts.

## Batch record

```text
Outcome and acceptance invariants:
Authoritative repository / base revision:
User edits to preserve:
Authorized actions and release destination, if any:
Canonical full gate and required CI checks:
Runtime capacity (root included or excluded):
Available model / effort mappings:
```

Record each lane with its owner, absolute worktree, allowed paths, forbidden paths, dependencies, focused checks, and status. Only the root changes leases. A worker cannot expand its own scope.

Example dependency graph for save-versus-publish work:

```text
Architecture scout + verification scout
                 |
       agreed save/publish contract
                 |
       canonical state contract (A)
              /     \
   persistence (B)  frontend consumer (C)
              \     /
              integration
                  |
       cross-feature checks + fresh review
                  |
        fresh canonical verification
                  |
       authorized release or handoff
```

A owns the shared state schema. B and C start only after A's contract is accepted and their bases include the required changes. If B and C both need `src/state.ts`, change the partition or sequence their writes before dispatch.

## Worker packet

```text
Role and task ID:
Outcome: one bounded responsibility
Repository and absolute worktree:
Branch and authoritative base revision:
Current state / prior accepted dependencies:
Owned files or surface:
Forbidden paths and actions:
User changes to preserve:
Required invariants and accepted contract decisions:
Dependencies and handoff conditions:
Focused checks and acceptance criteria:
Artifact directory:
Time/effort budget and stop conditions:
Return: use the result contract below
```

For scouts, set the role to read-only and request findings with file locations, evidence, unresolved decisions, and suggested lane boundaries. For writers, require checkout and lease verification before edits. A blocked worker reports the precise dependency or contract conflict, preserves its work, and yields; it does not silently broaden its task.

## Result contract

```text
Outcome: PASS or BLOCKED (for this task's acceptance criteria only)
Changed: files, revision or patch artifact; read-only if applicable
Focused tests: commands, exit codes, revision, relevant configuration
Invariant evidence: short findings with locations or artifact references
Blockers: unresolved issue and the decision or evidence needed
Cross-lane changes: contracts affected and dependent lanes; none if unchanged
Artifacts: raw logs / receipts / patch locations
```

Use a few bullets per field. PASS from an implementation worker is not a release certificate. Report checks that were not run explicitly, with the reason.

## Verification/release packet and receipt

Give the fresh worker the integrated revision, accepted requirements, review findings and resolutions, canonical gate, environment/configuration identity, known risks, artifact location, and exact release authorization. Do not give it only the author's assurance that everything works.

```text
Candidate: exact revision and artifact identity
Environment/configuration: non-secret identity or digest
Review: findings resolved or outstanding
Gate: commands, underlying check results, exit codes, lifecycle completion
Evidence: receipt and raw log paths
Outcome: PASS or BLOCKED
Release: performed with destination/receipt, not authorized, or blocked
```

If release changes configuration or rebuilds the artifact, establish that the resulting candidate is covered by verification before promoting it. Stop on contradictory results and invalidate affected prior receipts. Rerun after an identified repair, not repeatedly until a flaky gate happens to turn green.
