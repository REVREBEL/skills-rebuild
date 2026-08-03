# Task 10: Build the Router Hierarchy

## Objective

Create the final root and category routers after canonical child skills are stable, ensuring each request can reach the narrowest correct workflow without duplicated execution.

## Preconditions

- Functional taxonomy, destination, consolidation, split, batch, and resource-cleanup artifacts exist and reconcile.
- Canonical child skills are stable at their final paths.
- Router construction is based on the actual rebuilt filesystem, not planned or nonexistent children.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`

Use `skill-library-restructure` for hierarchy and parent-child ownership, `skill-writer` for substantial router authoring, and `skill-check` for link and routing validation. Use `task-skills/github-operations/SKILL.md` for repository writes, diff review, commits, and publication.

## Work

1. Read the final category and child-skill filesystem.
2. Create or update the root `agents/skills-rebuild/SKILL.md` router.
3. Create one router `SKILL.md` for each approved functional category.
4. Ensure each router:
   - Defines its functional domain
   - Explains when the router applies
   - Routes to the narrowest active child
   - Distinguishes overlapping child triggers
   - Explains control and handoff boundaries
   - Lists every active direct child
   - Contains only shared rules that apply across the category
   - Avoids repeating complete child workflows
5. Keep the hierarchy shallow unless another level resolves a real routing problem.
6. Remove stale links, aliases, and superseded child entries.
7. Verify every direct router link and every child parent assignment.
8. Test representative prompts against the hierarchy and correct ambiguities.

## Artifacts

Create or update:

- `agents/skills-rebuild/SKILL.md`
- Each approved category-level `SKILL.md`

Create:

- `agents/skills-rebuild/_audit/router-validation.md`

The validation record must include router paths, direct-child coverage, link checks, representative prompts, expected and actual routes, ambiguities found, corrections made, and unresolved routing issues.

## Reconciliation Requirements

- Reconcile every active canonical child to exactly one appropriate direct parent.
- Reconcile root and category indexes to the actual filesystem.
- Confirm every router link resolves and every listed child is active.
- Confirm no active child is omitted or linked from conflicting parents without an explicit design reason.
- Confirm routers contain routing and shared policy rather than duplicated end-to-end child workflows.

## Completion Gate

Complete only when:

- All preconditions are satisfied.
- Root, category, and router-validation artifacts exist.
- Every active child has one reconciled parent assignment.
- All links resolve and representative prompts reach the intended child.
- Every routing ambiguity is corrected or explicitly documented.