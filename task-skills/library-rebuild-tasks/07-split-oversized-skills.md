# Task 07: Split Oversized Skills

## Objective

Split retained skills only when they contain independently triggered jobs with different workflows, tools, outputs, risks, or validation paths.

## Preconditions

- Inventory, taxonomy, destination, consolidation, and merge-decision artifacts exist and reconcile.
- Canonical owners for overlap clusters are established.
- Candidate skills have been reviewed for true multi-job behavior rather than length alone.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`

Use `skill-review` for split approval, `skill-library-restructure` for parent-child architecture and destination updates, and `skill-writer` for substantial source-backed child or router authoring. Use `task-skills/github-operations/SKILL.md` for repository operations and reviewable publication batches.

## Work

1. Identify retained skills with multiple independent jobs.
2. Distinguish true multi-job skills from singular jobs with extensive supporting material.
3. Approve a split only when sections have independent:
   - Trigger phrases or user goals
   - Required inputs
   - Tools, applications, or permissions
   - Execution sequences
   - Risk or authorization requirements
   - Outputs and completion evidence
4. Define each child skill's trigger, scope, output, tools, and completion evidence.
5. Create a parent router only when several focused children share a coherent category and require routing.
6. Move shared category policy to the parent without duplicating child execution workflows.
7. Move long supporting detail into `references/` when the functional job remains singular.
8. Update destination and provenance mappings for every resulting child.
9. Verify parent links, child links, and retired source paths.

## Artifacts

Create:

- `agents/skills-rebuild/_audit/split-map.md`

The map must record original path, split decision, rationale, parent destination, child destinations, content allocation, shared resources, routing boundaries, retired source path, and validation status.

## Reconciliation Requirements

- Reconcile every approved or rejected split candidate to the split map.
- Account for every source section and bundled resource in a child, parent, reference, canonical destination, or documented retirement.
- Reconcile all new child paths with the destination map and inventory provenance.
- Confirm parent routers link only to existing children and contain no duplicated end-to-end child workflow.

## Completion Gate

Complete only when:

- All preconditions are satisfied.
- The split map exists and accounts for every reviewed candidate.
- Every approved child has a distinct trigger, job, and outcome.
- Parent, child, reference, destination, and provenance records reconcile.
- No content or resource disappears without a documented disposition.