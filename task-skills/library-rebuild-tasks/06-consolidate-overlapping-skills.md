# Task 06: Consolidate Overlapping Skills

## Objective

Resolve retained skills that share substantially the same trigger, workflow, or output by selecting canonical owners and preserving unique material without duplicate active discovery.

## Required Context

Use:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/destination-map.csv`
- `agents/skills-rebuild/_audit/functional-taxonomy.md`
- `agents/skills-rebuild/_audit/provider-conversion-report.md`

Review one functional overlap cluster at a time. A shared application, language, or source repository is not sufficient reason to merge skills.

For each cluster compare:

- User triggers
- Functional outcome
- Required inputs
- Required tools and permissions
- Execution workflow
- Risk and authorization gates
- Validation and completion evidence
- Bundled scripts, references, assets, and templates
- Unique instructions worth preserving

Assign each cluster one decision:

- Keep separately
- Merge into one canonical skill
- Convert one source into a reference or template
- Preserve a temporary compatibility alias
- Retire a true duplicate
- Defer for manual review

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for reviewable branches, commits, diffs, and publication.

## Work

1. Group overlapping retained skills by functional job.
2. Compare actual contents and bundled resources, not filenames alone.
3. Select the canonical owner for each duplicate workflow.
4. Merge unique, valid material into the canonical destination.
5. Move superseded active sources out of discovery without deleting Git history.
6. Preserve provenance from every source path to the canonical destination.
7. Verify no active router still links to retired or superseded skills.
8. Commit each manageable functional consolidation batch separately.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/merge-decisions.csv`

The decision log must record cluster, source paths, canonical destination, decision rationale, unique material preserved, resources moved, and retired paths.

## Completion Gate

Complete only when every identified overlap cluster has an explicit decision, each merged workflow has one canonical active owner, all unique retained material is traceable, and no active router points to a superseded path.