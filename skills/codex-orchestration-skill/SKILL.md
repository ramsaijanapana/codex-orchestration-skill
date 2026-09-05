---
name: codex-orchestration-skill
description: Use when a large software engineering batch has independent workstreams, cross-cutting architecture decisions, or costly repeated verification, especially with an Astra root and Luna implementation agents in Codex. Small local edits usually do not need this workflow.
---

# Codex Orchestration

Keep the root focused on architecture, ambiguity, scheduling, contract decisions, and acceptance. Delegate bounded implementation and evidence gathering to fresh-context workers. Optimize useful completed work, not agent count.

## Establish the batch

Read repository instructions and current checkout state. Define the requested outcome, acceptance invariants, authoritative base revision, user changes to preserve, and authorized external actions. This skill does not grant deployment or publication permission.

Check available delegation tools, supported models and reasoning efforts, isolation facilities, and concurrency limits. The model table below is a preferred profile, not a promise of availability. Do not pretend to switch the running root model. When a requested profile is unavailable, state the substitution and preserve its role. Without delegation, implement and self-check sequentially, then deliver the candidate and evidence with independent review/verification explicitly outstanding. Self-review cannot satisfy the independent certification stages below.

For a complex batch, start two read-heavy scouts before most writers:

- Architecture scout: data contracts, state lifecycle and identity, permissions, ownership, and blocking semantic decisions.
- Verification scout: canonical checks, failure propagation, runtime configuration, expected versus live state, and release prerequisites.

Resolve cross-lane questions, then record a dependency DAG and exclusive ownership matrix using [the task contracts](references/task-contracts.md). Keep ambiguous tasks with the root until they have testable boundaries.

## Dispatch independent work

| Role or work | Preferred model | Effort |
|---|---|---|
| Root architecture and adjudication | GPT-6 Astra | medium |
| Concurrency, transactions, permissions, identity invariants | GPT-5.6 Luna | xhigh |
| Normal frontend/backend implementation, adapters, focused tests | GPT-5.6 Luna | high |
| Mechanical changes, translations, evidence and log extraction | GPT-5.6 Luna | medium |
| Exploratory reading and secondary evidence | GPT-5.6 Terra | supported moderate effort |

Choose effort by uncertainty and reasoning difficulty, not importance alone. A scout or verifier handling adversarial invariants needs the corresponding stronger profile.

Aim for 4–6 useful workers only when independent work and capacity justify them; eight is a burst ceiling. If the runtime counts the root, subtract it from total capacity. Count scouts, reviewers, and nested agents too. With four total slots, run at most three children. Queue dependent lanes and avoid recursive fan-out outside the root's capacity budget.

Spawn workers with `fork_turns: "none"` when supported. Supply a self-contained task packet with the relevant requirements and decisions rather than parent history. Use the runtime's actual model identifiers and tool schema; do not assume a portable spawning API.

Each writer gets one isolated worktree, an authoritative starting revision, an exclusive file/surface lease, and explicit forbidden paths. Before writing, verify the absolute working directory, repository root, branch, base, and existing diff. Shared preview, integration, and release checkouts are read-only to implementation workers. File leases are coordination rules, not a filesystem security boundary.

If isolation is unavailable, serialize writers in the shared checkout; read-only scouting can remain parallel. If lanes need the same file, combine them or schedule an explicit ownership handoff. Contract changes return to the root before dependent writers proceed. On a wrong-checkout write, stop the writer, preserve and inspect its patch, and move only its changes without overwriting user work.

## Develop and integrate

Workers implement their bounded changes and run relevant focused checks. Store raw logs as artifacts; return the compact result contract. Root tool use should answer a cross-agent decision or unresolved ambiguity; delegate routine discovery, log reading, and test operation when a useful independent lane exists.

Before accepting a worker's PASS, confirm that each required check has a receipt naming the tested candidate, command, exit code, and an accessible raw log. Read enough of the log to confirm it supports the claimed result; existence alone is insufficient. If a log is missing or incomplete, recover it or obtain the missing evidence with a focused rerun. Capture output during the original invocation, and check the saved streams before returning. Record the gap and repair rather than treating a summary as a complete receipt. Independent review should name the uncertainty it is checking before duplicating successful checks.

Integrate completed lanes in dependency order through a designated integration worker with the sole write lease on the integration checkout. It may resolve merge conflicts and integration defects within the accepted contracts; new contract decisions return to the root. Review patch scope and cross-lane compatibility, then run cross-feature checks. Do not rerun successful work without a reason: changed code or dependencies, changed configuration, insufficient evidence, or conflicting findings.

## Verify independently

A fresh-context reviewer who did not author implementation or integration changes examines the integrated candidate. After findings are resolved, a separate fresh-context verification/release worker who also did not author those changes runs the canonical full gate on the final candidate. Preserve independence even when roles execute sequentially because slots are scarce.

Batch the full gate after integration; required repository or CI checks still apply. Every post-gate candidate change invalidates its receipt and requires the applicable checks and canonical gate again. “One full gate” means one per stable candidate, never permission to reuse stale evidence.

**If verification can falsely pass, repair that immediately before relying on further certification.** Pause the release path and affected work; repair failure propagation and demonstrate that a failing child check makes the gate fail. A PASS label cannot override contradictory underlying evidence.

Passing assertions followed by a teardown crash are useful diagnostic evidence, but the process did not pass. Resolve the lifecycle failure and obtain a clean completed run. Do not suppress it to manufacture a green result.

Bind receipts to the exact revision/artifact, configuration, commands, exit codes, and completed process lifecycle. Release only within existing user authorization and against that verified candidate. Otherwise deliver the verified candidate and remaining release step. Root adjudicates conflicts; missing evidence means BLOCKED, not assumed success.

## Measure without inventing precision

Track useful concurrency, blocked time, root execution volume, and avoidable gate reruns when telemetry exists. Model-level JSONL telemetry may support model attribution; account quota bars do not. Cached input, uncached input, output, and agent-minutes are distinct measures. The source post's timings and pricing weights are observations, not current prices, subscription charges, or guarantees of speed or quality.
