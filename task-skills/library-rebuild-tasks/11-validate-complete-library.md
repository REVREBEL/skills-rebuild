# Task 11: Validate the Complete Library

## Objective

Validate the rebuilt skills library structurally, semantically, and operationally before pilot use or publication.

## Required Context

Use the final rebuilt filesystem and all audit records under:

`agents/skills-rebuild/_audit/`

Validation must reconcile the filesystem against the baseline, inventory, compatibility decisions, destination map, merge decisions, split map, batch records, resource cleanup report, and router validation record.

Validate at minimum:

- Every source skill has one documented final disposition
- Active folder names match frontmatter `name`
- YAML frontmatter parses and required fields are valid
- Active skill names are unique
- Descriptions explain both capability and trigger conditions
- Relative links and bundled-resource references resolve
- Parent routers cover all active direct children
- Overlapping triggers are distinguishable
- Provider and application requirements are declared and supported
- Unsupported skills remain traceably quarantined or retired
- Write and destructive workflows contain authorization and verification gates
- Scripts validate inputs and do not contain secrets or unsafe hardcoded assumptions
- Examples are syntactically valid for their stated environment

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`
- `task-skills/skills-create-manage-update/skill-audit/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`

Use `skill-optimizer` only when real usage evidence is available. Use `task-skills/github-operations/SKILL.md` for repository diff, commit, CI, and publication validation.

## Work

1. Run the repository-provided skill validator when available.
2. Perform independent filesystem and link reconciliation.
3. Check frontmatter, descriptions, naming, and active-name uniqueness.
4. Test parent-to-child routing with representative prompts.
5. Review application and provider compatibility against the approved environment.
6. Validate bundled scripts and examples using available safe tooling.
7. Compare every source inventory row with its recorded final disposition and filesystem destination.
8. Create a repair list for every failure or unresolved validation gap.
9. Do not report a check as passed when it could not be executed.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/validation-report.md`
- `agents/skills-rebuild/_audit/unresolved-items.md`

The validation report must separate passed, failed, skipped, unavailable, and manually reviewed checks.

## Completion Gate

Complete only when every validation failure has been repaired or appears in `unresolved-items.md` with exact scope and impact, all audit records reconcile with the filesystem, and no silent coverage gaps remain.