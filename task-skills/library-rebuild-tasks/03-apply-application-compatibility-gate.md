# Task 03: Apply the Application Compatibility Gate

## Objective

Determine which source skills meet the approved application and environment requirements before investing in consolidation or rewriting.

## Required Context

Use:

- `agents/skills-rebuild/_audit/baseline.md`
- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/inventory-summary.md`

Review the current approved application list and target-agent capabilities before assigning compatibility. Do not assume a tool is supported because it appears in a skill.

Assign each source skill one compatibility classification:

- Approved and supported
- Supported after conversion
- Optional dependency with a supported replacement
- Unsupported application or platform
- Unsupported tool or permission dependency
- Provider-specific but potentially reusable
- Unrelated to the target library
- Ambiguous and requiring manual review

Unsupported or unrelated skills must be moved traceably to the resolved `agents/not-needed` path, not deleted.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-audit/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-manage/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for the dedicated branch, diff review, commit, and remote verification.

## Work

1. Review every inventory row against the approved application and environment requirements.
2. Record evidence for the compatibility classification.
3. Separate intrinsic unsupported dependencies from replaceable implementation details.
4. Mark ambiguous skills for individual review instead of guessing.
5. Move only clearly unsupported or unrelated skills to `agents/not-needed`.
6. Preserve source-relative paths or another unambiguous provenance key in the quarantine manifest.
7. Commit the compatibility and quarantine pass separately from later rewrites.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/application-compatibility-report.md`
- `agents/skills-rebuild/_audit/moved-to-not-needed.csv`

Update `agents/skills-rebuild/_audit/skills-inventory.csv` with the final compatibility classification and current destination.

## Completion Gate

Complete only when every inventoried skill has a documented compatibility classification, every moved skill appears in the quarantine manifest, no skill was deleted, and the post-move filesystem reconciles with the reports.