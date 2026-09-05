# Codex Orchestration Skill

A reusable Codex skill for running large engineering batches with a principal engineer as orchestrator, bounded implementation workers, and fresh independent verification.

Adapted from the supplied social post, **“I tested GPT-6 Astra both solo and as an 8-agent orchestrator — here’s what actually worked.”** The central idea: reserve expensive reasoning for ambiguity and architecture; give implementation workers clear contracts and exclusive ownership.

## Install

Clone this public repository, then copy the skill into your Codex skills directory. These commands stop if either destination already exists; inspect an existing installation before replacing it.

```bash
git clone https://github.com/ramsaijanapana/codex-orchestration-skill.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
test ! -e "${CODEX_HOME:-$HOME/.codex}/skills/codex-orchestration-skill" && \
  cp -R codex-orchestration-skill/skills/codex-orchestration-skill \
  "${CODEX_HOME:-$HOME/.codex}/skills/codex-orchestration-skill"
```

Open a new Codex session after installation so it can discover the skill.

## Use

```text
Use $codex-orchestration-skill to complete this development batch:
[describe the requested changes and acceptance criteria].
```

The skill is also available for normal automatic discovery on relevant large engineering tasks. It does not require a plugin, change your root model, raise runtime concurrency limits, or grant release authorization.

## What it provides

- Two scouts establish architecture and verification constraints before most writers start.
- A dependency DAG and exclusive file/worktree ownership keep lanes independent.
- Fresh worker contexts receive compact task packets instead of the full parent conversation.
- Astra medium is the preferred root profile; Luna medium/high/xhigh handles bounded work according to difficulty. Terra is an optional exploration profile.
- Four to six useful workers is a heuristic; eight is a burst ceiling. Actual runtime capacity takes precedence, including the root when applicable.
- Focused checks during development lead to integration, fresh review, and a canonical full gate on each stable candidate.
- Contradictory verification evidence blocks release immediately.

Read the [skill](skills/codex-orchestration-skill/SKILL.md) and [task contracts](skills/codex-orchestration-skill/references/task-contracts.md).

## Scope and evidence

This is an instruction skill, not an executable scheduler or isolation system. It relies on the host's available delegation and Git tools. When isolated worktrees are unavailable, writers run sequentially; without delegation, the stages run sequentially in one agent.

The source is a single reported experiment, not a controlled benchmark. Its parallel phase was still being integrated, so it does not establish superior final release quality or a universal speedup. Model profiles are configurable preferences. Historical token totals, pricing estimates, and quota observations are intentionally not presented as current product facts or cost promises.

No source traces, account logs, or private project artifacts are included.

## Validation

The [live validation harness](validation/README.md) creates a deliberately broken disposable repository for an agent to repair using this skill. An independent assessor checks acceptance tests, injected verification failures, state invariants, and preservation of user work.

The [evaluation report](validation/results/2026-09-05/REPORT.md) records a completed delegated run, a sequential fallback run, the evidence gaps found, and the resulting skill corrections.

These checks provide bounded evidence, not a guarantee of reliability. Instruction skills cannot enforce filesystem isolation or ensure that every future model follows every instruction.
