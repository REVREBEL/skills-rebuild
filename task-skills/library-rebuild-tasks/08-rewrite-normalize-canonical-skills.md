# Task 08: Rewrite and Normalize Canonical Skills

## Objective

Rewrite retained canonical skills in manageable functional batches so each skill is discoverable, executable, provider-appropriate, and structurally consistent.

## Required Context

Use:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/destination-map.csv`
- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/merge-decisions.csv`
- `agents/skills-rebuild/_audit/split-map.md`
- `agents/skills-rebuild/_audit/provider-conversion-report.md`

Work by functional batch, normally 10 to 20 related skills, rather than alphabetically or across the entire library at once.

Each canonical skill must have:

- Folder and frontmatter `name` alignment
- A discovery-focused description explaining what and when
- Clear use and exclusion boundaries
- Required inputs, tools, permissions, and compatibility
- Ordered workflow
- Safety and authorization rules
- Handoff boundaries
- Validation and completion requirements
- Troubleshooting only when it supports execution
- Progressive disclosure into `references/`, `scripts/`, `assets/`, or `templates/` when needed

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`
- `task-skills/skills-create-manage-update/skill-make-template/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`

Use `skill-creator` only when benchmarks, graders, packaging, or evaluation assets are justified. Use `task-skills/github-operations/SKILL.md` for branch, commit, PR, and review operations.

## Work

1. Select one functional batch from the approved destination map.
2. Rewrite or repair each canonical skill using the approved merge and split decisions.
3. Preserve valid source provenance and unique instructions.
4. Remove stale aliases, unsupported metadata, accidental provider assumptions, and broken references.
5. Move long supporting content out of the main `SKILL.md` when progressive disclosure improves execution.
6. Validate each skill before completing the batch.
7. Reconcile the batch against destination, merge, split, and inventory records.
8. Commit each validated functional batch separately.

## Deliverable

Create or update the canonical skill folders under the resolved `agents/skills-rebuild` path.

For each completed batch, create:

`agents/skills-rebuild/_audit/batches/<batch-name>.md`

The batch record must list skills completed, source paths incorporated, validation performed, retired paths, and unresolved items.

## Completion Gate

Complete a batch only when every included skill validates, all referenced resources exist, trigger boundaries are distinguishable, provenance records reconcile, and no unresolved overlap remains within that batch.