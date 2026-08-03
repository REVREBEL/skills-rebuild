# Task 08: Rewrite and Normalize Canonical Skills

## Objective

Rewrite retained canonical skills in manageable functional batches so each skill is discoverable, executable, provider-appropriate, and structurally consistent.

## Preconditions

- Inventory, destination, consolidation, merge-decision, split, and provider-conversion artifacts exist and reconcile.
- Canonical owners and approved child structures are established.
- One functional batch of approximately 10 to 20 related skills is selected.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`
- `task-skills/skills-create-manage-update/skill-make-template/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`

Use `skill-improver` for approved repairs to existing canonical skills, `skill-writer` for substantial source-backed rewrites, `skill-make-template` for straightforward new skills, and `skill-check` for per-skill and per-batch validation. Use `task-skills/github-operations/SKILL.md` for branch, commit, pull-request, and review operations.

## Work

1. Select one approved functional batch rather than working alphabetically or across the whole library.
2. Rewrite or repair each canonical skill using the approved merge and split decisions.
3. Ensure each canonical skill has:
   - Folder and frontmatter `name` alignment
   - A discovery-focused description explaining what and when
   - Clear use and exclusion boundaries
   - Required inputs, tools, permissions, and compatibility
   - Ordered workflow
   - Safety and authorization rules
   - Handoff boundaries
   - Validation and completion requirements
4. Preserve valid source provenance and unique instructions.
5. Remove stale aliases, unsupported metadata, undeclared provider assumptions, and broken references.
6. Use progressive disclosure through `references/`, `scripts/`, `assets/`, or `templates/` when supporting content would obscure the primary workflow.
7. Validate each skill before completing the batch.
8. Commit each validated functional batch separately.

## Artifacts

Create or update canonical skill folders under the resolved `agents/skills-rebuild` path.

For each batch, create:

- `agents/skills-rebuild/_audit/batches/<batch-name>.md`

The batch record must list canonical skills completed, source paths incorporated, authoring workflow used, validation performed, resources created or moved, retired paths, and unresolved items.

## Reconciliation Requirements

- Reconcile every batch skill to the destination, merge, split, provider-conversion, and inventory records.
- Reconcile every incorporated source path to one canonical destination.
- Confirm every active reference and bundled resource exists.
- Confirm trigger boundaries within the batch are distinguishable.
- Confirm no unresolved overlap remains within the completed batch.

## Completion Gate

Complete a batch only when:

- All preconditions are satisfied.
- Canonical files and the batch record exist.
- Every included skill passes `skill-check` or has an explicit unresolved validation item.
- Sources, destinations, resources, retirements, and validation evidence reconcile.
- The batch contains no silent overlap, missing provenance, or broken path.