# Task 11: Validate the Complete Library

## Objective

Validate the rebuilt skills library structurally, semantically, and operationally before pilot use or publication.

## Preconditions

- The rebuilt filesystem and all expected audit artifacts under `agents/skills-rebuild/_audit/` exist.
- Canonical skills, resources, and router hierarchy are complete enough for whole-library validation.
- The repository-provided skill validator and other safe validation tools have been identified or recorded as unavailable.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`
- `task-skills/skills-create-manage-update/skill-audit/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`

Use `skill-check` for structural, semantic, link, and package validation; `skill-audit` for safety, compatibility, permissions, dependencies, and secrets; and `skill-review` for final disposition inconsistencies or unresolved ownership decisions. Use `task-skills/github-operations/SKILL.md` for repository diff, commit, CI, and publication-state validation.

## Work

1. Run the repository-provided skill validator when available.
2. Independently validate:
   - Every source skill has one documented final disposition
   - Active folder names match frontmatter `name`
   - YAML frontmatter parses and required fields are valid
   - Active skill names are unique
   - Descriptions explain capability and trigger conditions
   - Relative links and bundled-resource references resolve
   - Parent routers cover all active direct children
   - Overlapping triggers are distinguishable
   - Provider and application requirements are declared and supported
   - Unsupported skills remain traceably quarantined or retired
   - Write and destructive workflows contain authorization and verification gates
   - Scripts validate inputs and contain no secrets or unsafe hardcoded assumptions
   - Examples are syntactically valid for their stated environment
3. Test parent-to-child routing with representative prompts.
4. Validate bundled scripts and examples using available safe tooling.
5. Compare every source inventory row with its final disposition and filesystem destination.
6. Separate passed, failed, skipped, unavailable, and manually reviewed checks.
7. Create a repair item for every failure or unresolved validation gap.
8. Do not report a check as passed when it could not be executed.

## Artifacts

Create:

- `agents/skills-rebuild/_audit/validation-report.md`
- `agents/skills-rebuild/_audit/unresolved-items.md`

The validation report must record each check, scope, method, status, evidence, affected paths, and repair outcome. The unresolved-items file must record exact scope, impact, owner or next workflow, and blocking status.

## Reconciliation Requirements

- Reconcile the final filesystem against baseline, inventory, compatibility, destination, consolidation, split, batch, resource-cleanup, and router-validation records.
- Reconcile every active, quarantined, retired, merged, and split source to one final disposition.
- Confirm validation totals cover the full active skill and resource population.
- Confirm every failure appears in the repair history or unresolved-items file.
- Confirm no skipped or unavailable check is represented as passed.

## Completion Gate

Complete only when:

- All preconditions are satisfied or explicitly recorded as unavailable.
- Both validation artifacts exist with complete check coverage.
- Every validation failure is repaired or recorded with exact scope and impact.
- All audit records reconcile with the final filesystem.
- No silent source, skill, resource, router, or validation coverage gap remains.