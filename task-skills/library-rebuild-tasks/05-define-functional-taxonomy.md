# Task 05: Define the Functional Taxonomy

## Objective

Design the destination category structure for retained skills based on the jobs they perform, without moving or rewriting the full library during this task.

## Required Context

Use:

- `agents/skills-rebuild/_audit/baseline.md`
- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/application-compatibility-report.md`
- `agents/skills-rebuild/_audit/provider-conversion-report.md`

Include only retained or approved-for-conversion skills. Exclude quarantined and retired sources from the active taxonomy.

Group skills by functional outcome and trigger, not by source repository, model vendor, programming language, or application name alone. Keep the hierarchy shallow and create a category only when it has a coherent purpose and enough children to justify routing.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`

Use `task-skills/github-operations/SKILL.md` only for repository operations required to record and publish the taxonomy work.

## Work

1. Review the retained capabilities and overlap clusters.
2. Propose a small set of functional top-level categories.
3. Define the purpose, inclusion criteria, and exclusion boundaries for each category.
4. Assign every retained source skill one proposed functional destination.
5. Identify skills that should remain root-level meta-skills or routers.
6. Flag ambiguous destinations for review.
7. Identify category names that would create overlapping routing and revise them.
8. Do not perform broad moves, merges, splits, or rewrites during this task.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/functional-taxonomy.md`
- `agents/skills-rebuild/_audit/destination-map.csv`

The destination map must include source path, proposed category, proposed final path, routing role, and unresolved placement concerns.

## Completion Gate

Complete only when every retained skill has one proposed functional home, every category has explicit boundaries, and unresolved placements are documented rather than silently assigned.