# Task 10: Build the Router Hierarchy

## Objective

Create the final root and category routers after canonical child skills are stable, ensuring each request can reach the narrowest correct workflow without duplicated execution.

## Required Context

Use:

- `agents/skills-rebuild/_audit/functional-taxonomy.md`
- `agents/skills-rebuild/_audit/destination-map.csv`
- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/split-map.md`
- Completed batch records under `agents/skills-rebuild/_audit/batches/`
- `agents/skills-rebuild/_audit/resource-cleanup-report.md`

Build routers from the actual final filesystem. Do not link to planned or nonexistent children.

Each router must:

- Define its functional domain
- Explain when the router applies
- Route to the narrowest active child
- Distinguish overlapping child triggers
- Explain control and handoff boundaries
- List every active direct child
- Contain shared safety rules only when they apply across the category
- Avoid repeating complete child workflows

Keep the hierarchy shallow unless an additional level is necessary to resolve a real routing problem.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skills-writing/SKILL.md`
- `task-skills/skills-create-manage-update/template-skill-enhanced/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for repository writes, diff review, commits, and publication.

## Work

1. Read the final category and child-skill tree.
2. Create or update the root `agents/skills-rebuild/SKILL.md` router.
3. Create one router `SKILL.md` for each approved functional category.
4. Add routing tables based on user goals and child outcomes.
5. Add explicit handoff rules where a child delegates general operations or transitions to another workflow.
6. Remove stale links, aliases, and superseded child entries.
7. Verify every direct router link and every child parent assignment.
8. Test representative prompts against the routing hierarchy and record ambiguities for correction.

## Deliverable

Create or update:

- `agents/skills-rebuild/SKILL.md`
- Each approved category-level `SKILL.md`

Create:

`agents/skills-rebuild/_audit/router-validation.md`

The validation record must include link checks, active child coverage, representative routing tests, ambiguities found, and corrections made.

## Completion Gate

Complete only when every active canonical child is linked from exactly one appropriate parent, all links resolve, routing tests reach the intended child, and no router duplicates a child’s end-to-end workflow.