# Task 04: Remove Provider-Specific Assumptions

## Objective

Convert retained skills to provider-neutral, capability-based workflows unless a specific provider or application is intrinsic to the skill's purpose.

## Required Context

Use:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/application-compatibility-report.md`
- `agents/skills-rebuild/_audit/moved-to-not-needed.csv`

Review only retained skills classified as approved, supported after conversion, provider-specific but reusable, or ambiguous after manual approval.

Search for provider-coupled elements including:

- `.claude/`, `CLAUDE.md`, Claude hooks, and Claude-specific environment variables
- Proprietary slash commands or prompt wrappers
- Hardcoded model identities or vendor-specific role instructions
- Cursor, Gemini, Codex, or other client-specific paths and commands
- Tool names that do not exist in the approved environment
- Assumptions that a connector, CLI, hook system, or subagent framework is installed

Preserve provider-specific instructions only when the provider itself is the legitimate subject of the skill and the dependency is stated in `compatibility`.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for branch, diff, commit, and publication work.

## Work

1. Review each retained provider-specific skill.
2. Decide whether the provider dependency is intrinsic, replaceable, or disqualifying.
3. Replace nonessential model identity and client-specific instructions with capability-based language.
4. Replace unavailable tool references with supported tools or explicit compatibility requirements.
5. Remove obsolete paths, hooks, commands, and environment assumptions.
6. Preserve the functional job and useful source material during conversion.
7. Record skills that cannot be converted without changing their purpose.
8. Validate every converted file and relative reference.

## Deliverable

Create:

`agents/skills-rebuild/_audit/provider-conversion-report.md`

The report must list each reviewed skill, original provider dependency, decision, changes made, retained compatibility requirements, and unresolved blockers.

Update the inventory with conversion status and destination.

## Completion Gate

Complete only when every retained provider-specific skill has a documented decision, converted skills no longer depend on undeclared provider behavior, and all unresolved cases are explicitly identified.