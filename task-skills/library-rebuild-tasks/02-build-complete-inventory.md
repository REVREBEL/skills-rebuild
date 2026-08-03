# Task 02: Build the Complete Skills Inventory

## Objective

Catalog every source skill and its bundled resources before assigning destinations or modifying the library.

## Required Context

Use the verified paths and starting commit recorded in:

`agents/skills-rebuild/_audit/baseline.md`

The inventory must cover every skill folder under the resolved `agents/skills` source path. Do not infer coverage from search results alone; reconcile the inventory against the filesystem tree.

For each source skill capture:

- Source path
- Folder name
- Frontmatter `name`
- Frontmatter `description`
- Primary functional job
- Trigger phrases and scenarios
- Application, framework, and platform dependencies
- Model or provider dependencies
- Required tools and permissions
- Child-skill or external-skill references
- Bundled scripts, references, assets, and templates
- Approximate file and line counts
- Existing parent router
- Structural or compatibility concerns
- Potential overlap cluster
- Initial review status

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-inventory/SKILL.md`

Use `task-skills/github-operations/SKILL.md` only for repository reads, branch state, commits, or publication operations required by this task.

## Work

1. Traverse the complete source library.
2. Create one inventory row for every source skill folder.
3. Record bundled resources and referenced paths.
4. Flag folder/frontmatter mismatches, missing files, duplicate names, unsupported metadata, and unresolved dependencies.
5. Identify likely overlap clusters without deciding merges or splits.
6. Reconcile inventory row count against the baseline source count.
7. Do not move, delete, merge, split, or broadly rewrite skills during this task.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/inventory-summary.md`

The summary must state total coverage, unresolved items, duplicate-name findings, resource counts, and likely overlap clusters.

## Completion Gate

Complete only when every source skill has exactly one inventory row, the inventory count reconciles with the baseline, and all unresolved inspection gaps are documented.