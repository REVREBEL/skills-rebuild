# Task 02: Build the Complete Skills Inventory

## Objective

Catalog every source skill and bundled resource before assigning destinations or modifying the library.

## Preconditions

- `agents/skills-rebuild/_audit/baseline.md` exists and contains verified repository paths, starting SHA, and source skill count.
- The resolved source library is available for complete traversal.
- No broad movement, merge, split, retirement, or rewrite is performed during this task.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-inventory/SKILL.md`

Use `task-skills/github-operations/SKILL.md` only for repository reads, branch state, commits, and remote verification. Keep inventory ownership in `skill-inventory` until coverage and reconciliation are complete.

## Work

1. Traverse the complete resolved `agents/skills` source library.
2. Create one inventory row for every source skill folder.
3. Capture for each skill:
   - Source path
   - Folder name
   - Frontmatter `name` and `description`
   - Primary functional job
   - Trigger phrases and scenarios
   - Application, framework, platform, model, and provider dependencies
   - Required tools and permissions
   - Child-skill and external-skill references
   - Bundled scripts, references, assets, and templates
   - Approximate file and line counts
   - Existing parent router
   - Structural or compatibility concerns
   - Potential overlap cluster
   - Initial review status
4. Flag folder/frontmatter mismatches, missing files, duplicate names, unsupported metadata, and unresolved dependencies.
5. Identify likely overlap clusters without deciding merges or splits.
6. Do not infer complete coverage from search results alone.

## Artifacts

Create:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/inventory-summary.md`

The summary must record total coverage, unresolved inspection gaps, duplicate-name findings, bundled-resource counts, and likely overlap clusters.

## Reconciliation Requirements

- Reconcile inventory rows against the baseline directory tree and source skill count.
- Confirm every source folder has exactly one row.
- Confirm every bundled resource is associated with a source skill or explicitly identified as orphaned.
- Record every unreadable, ambiguous, or partially inspected item instead of treating it as complete.

## Repository Checkpoint

1. Begin only after Phase 01 is approved and merged into `main`.
2. Create and complete this phase on `skills-rebuild/phase-02-inventory` from the updated `main` branch.
3. Review the final diff and confirm it contains only inventory artifacts and directly required supporting changes.
4. Commit the completed phase with: `skills-rebuild: complete phase 02 inventory`.
5. Push the branch and open a draft pull request targeting `main`.
6. The pull request must summarize inventory coverage, artifact paths, reconciliation totals, validation evidence, and unresolved inspection gaps.
7. Leave the pull request unmerged for review. Do not begin Phase 03 until this phase is approved and merged into `main`.

## Completion Gate

Complete only when:

- All preconditions are satisfied.
- Both artifacts exist with the required fields.
- Inventory count equals the verified baseline source count.
- Every source skill has exactly one row.
- All coverage gaps and unresolved inspections are explicitly documented.
- The phase branch is pushed and its draft pull request is open for review.