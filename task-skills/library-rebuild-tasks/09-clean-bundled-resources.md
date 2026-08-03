# Task 09: Clean Bundled Resources

## Objective

Ensure every bundled script, reference, asset, and template in the rebuilt library is necessary, correctly classified, safely usable, and linked from an active canonical skill.

## Required Context

Use:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/destination-map.csv`
- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/split-map.md`
- Completed batch records under `agents/skills-rebuild/_audit/batches/`

Review the rebuilt canonical library, not quarantined or retired sources, except when tracing provenance or comparing duplicate resources.

Inspect for:

- Unused or orphaned resources
- Duplicate scripts with different names
- Scripts with materially different behavior despite similar names
- Broken relative paths
- Missing referenced files
- Stale API or platform documentation
- Oversized examples that belong in references
- Editable scaffolds stored as assets
- Static files incorrectly stored as templates
- Embedded credentials, tokens, private keys, internal URLs, or personal data
- Generated files, caches, `__MACOSX`, `.DS_Store`, and `._*`

Do not delete similarly named scripts without comparing their behavior.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-audit/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for repository history, diff review, commits, and publication.

## Work

1. Enumerate all bundled resources under active canonical skill folders.
2. Map each resource to the skill and workflow that uses it.
3. Compare suspected duplicates by content and behavior.
4. Remove generated metadata and confirmed unused resources while preserving Git history.
5. Move resources into the correct `scripts/`, `references/`, `assets/`, or `templates/` location.
6. Repair every active relative reference.
7. Review scripts for input validation, destructive behavior, secrets, hardcoded paths, and undeclared dependencies.
8. Validate the final resource tree against active skills.

## Deliverable

Create:

`agents/skills-rebuild/_audit/resource-cleanup-report.md`

The report must list resources retained, moved, merged, removed, repaired, or deferred, including the owning skill and evidence for each decision.

## Completion Gate

Complete only when every bundled resource is referenced by an active skill or preserved for a documented reason, all active paths resolve, no generated metadata remains, and no secret or unsafe hardcoded dependency is present.