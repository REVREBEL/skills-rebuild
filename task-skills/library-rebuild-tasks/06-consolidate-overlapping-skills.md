# Task 06: Consolidate Overlapping Skills

## Objective

Resolve retained skills that share substantially the same trigger, workflow, or output by selecting canonical owners and preserving unique material without duplicate active discovery.

## Preconditions

- Inventory, compatibility, provider-conversion, taxonomy, and destination-map artifacts exist and reconcile.
- Retained skills are assigned to proposed functional destinations.
- Overlap clusters are identified but not assumed to be duplicates by name alone.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`

Use `skill-review` for canonical-owner and disposition decisions, `skill-library-restructure` for merge structure and routing consequences, and `skill-improver` for approved canonical repairs. Use `task-skills/github-operations/SKILL.md` for reviewable branches, diffs, commits, and publication.

## Work

1. Review one functional overlap cluster at a time.
2. Compare actual contents and bundled resources, including:
   - User triggers and functional outcome
   - Required inputs, tools, permissions, and applications
   - Execution workflow
   - Risk and authorization gates
   - Validation and completion evidence
   - Scripts, references, assets, and templates
   - Unique instructions worth preserving
3. Assign one decision to each cluster:
   - Keep separately
   - Merge into one canonical skill
   - Convert one source into a reference or template
   - Preserve a temporary compatibility alias
   - Retire a true duplicate
   - Defer for manual review
4. Select the canonical owner for each duplicate workflow.
5. Merge unique, valid material into the canonical destination.
6. Move superseded active sources out of discovery without deleting Git history.
7. Preserve source-to-canonical provenance.
8. Verify no active router links to a superseded path.
9. Commit each manageable functional consolidation batch separately.

## Artifacts

Create:

- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/merge-decisions.csv`

The decision log must record cluster, source paths, canonical destination, decision, rationale, unique material preserved, resources moved, aliases retained, and retired paths.

## Reconciliation Requirements

- Reconcile every identified overlap cluster to one decision-log entry.
- Reconcile every merged source path to one canonical destination.
- Confirm unique retained material and bundled resources are accounted for.
- Confirm active routers and destination records contain no superseded paths.
- Confirm retained, merged, retired, aliased, and deferred counts reconcile with the cluster population.

## Completion Gate

Complete only when:

- All preconditions are satisfied.
- Both artifacts exist with complete cluster decisions.
- Every duplicate workflow has one canonical active owner.
- Unique retained material and provenance are traceable.
- Filesystem, routers, destination map, and consolidation records reconcile.