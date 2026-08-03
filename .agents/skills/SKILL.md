---
name: task-skills
description: 'Coordinate the GitHub and Agent Skills workflows required to inventory, audit, classify, convert, reorganize, validate, and publish a skills library. Use when rebuilding a skills repository, filtering application-specific skills, converting model-specific instructions, merging or splitting skills, creating functional routers, or publishing the rebuilt library.'
compatibility: 'Requires filesystem access to the target skills library and GitHub access for repository operations. Resolve source, quarantine, rebuilt, and task-skill paths before changes.'
metadata:
  category: task-orchestration
  type: master-router
  source: custom
---

# Skills Library Rebuild Task Router

Coordinate the complete library rebuild as a sequence of reviewable phases.

Delegate to:

- [GitHub Operations](./github-operations/SKILL.md): branches, commits, pull requests, Actions, issues, and publication
- [Skills Create, Manage & Update](./skills-create-manage-update/SKILL.md): inventory, audit, review, creation, conversion, restructuring, and validation

## When to Use

Use this router when the work spans several of these stages:

- Cataloging a large source skills folder
- Comparing application-specific skills against an approved stack
- Moving unsupported skills into quarantine
- Converting Claude-specific or other provider-specific instructions
- Grouping retained skills by function
- Merging duplicates or splitting multi-function skills
- Building parent routers and focused children
- Validating and publishing the rebuilt library

Use the child routers directly for one isolated GitHub operation or one standalone skill edit.

## Required Path Resolution

At the beginning, resolve and record:

- Source library, logically `agents/skills`
- Quarantine library, logically `agents/not-needed`
- Rebuilt library, logically `agents/skills-rebuild`
- Task skills, canonically `.agents/skills`
- Repository, default branch, working branch, and starting commit

The task-skill path is fixed at `.agents/skills` so compatible IDEs and agents can discover the workflows. The source, quarantine, and rebuilt physical paths may include another project prefix and must be discovered rather than assumed.

Absolute local paths may be resolved transiently to verify filesystem access. Do not commit them. Persist repository-relative paths from the project root, or use a neutral placeholder such as `<repo-root>/...` only when an absolute-path example is genuinely required.

## Portability and Privacy Rule

All committed artifacts, inventories, reports, pull-request descriptions, examples, logs, and comments created by this workflow must be portable and must not expose contributor-specific environment details.

- Use repository-relative paths for files inside the project.
- Do not commit home-directory paths, usernames, workstation names, mount points, drive letters, or other machine-specific prefixes.
- Normalize transient local paths before writing artifacts or GitHub content.
- Do not replace a portable path with an absolute path merely because the local path was verified.
- Treat `/Users/<name>/...`, `/home/<name>/...`, Windows drive paths, UNC paths, and comparable environment-specific forms as validation failures unless explicitly approved and anonymized.

## Governing Rules

1. Inventory before movement.
2. Use one documented primary disposition per source skill.
3. Quarantine unsupported or unresolved sources instead of silently deleting them.
4. Separate classification from refactoring.
5. Group by functional job, not application name alone.
6. Split by independent triggers or outcomes, not length alone.
7. Merge only true workflow duplicates.
8. Parent skills route; child skills execute.
9. Preserve provenance and source-to-final traceability.
10. Work on a branch in reviewable batches.
11. Verify filesystem and repository state after every write phase.
12. Do not claim validation, pushes, moves, or indexing succeeded without evidence.
13. Keep committed paths portable and free of user-specific local environment details.

## Execution Phases

### Phase 0: Establish the Baseline

Use [GitHub Operations](./github-operations/SKILL.md) to:

1. Confirm repository and default branch
2. Create a dedicated task branch
3. Record the starting commit
4. Resolve source, quarantine, rebuilt, and task-skill paths
5. Inspect current repository structure

**Output:** baseline record.

### Phase 1: Build the Source Inventory

Use [Skill Inventory](./skills-create-manage-update/skill-inventory/SKILL.md).

Capture at minimum:

- Source path
- Folder and frontmatter names
- Description and primary function
- Application and framework dependencies
- Model/provider dependencies
- Referenced skills and bundled resources
- Size and structural signals
- Initial review status

Do not perform broad moves during this phase.

**Output:** complete inventory and unresolved-review list.

### Phase 2: Apply Compatibility and Safety Gates

Use [Skill Audit](./skills-create-manage-update/skill-audit/SKILL.md).

Classify each application-specific or provider-specific skill as:

- Approved and supported
- Optional and replaceable
- Generalizable
- Unsupported and intrinsic
- Ambiguous and requiring review

Record the decision before moving unsupported skills to quarantine.

Commit the quarantine pass independently.

**Output:** compatibility report, audit findings, and quarantine manifest.

### Phase 3: Assign Primary Dispositions

Use [Skill Review](./skills-create-manage-update/skill-review/SKILL.md).

Assign every source skill exactly one primary disposition:

- Keep as-is
- Refine
- Convert
- Split
- Merge
- Quarantine
- Retire

Resolve ambiguous and high-impact skills individually.

**Output:** frozen decision map.

### Phase 4: Convert Model-Specific Skills

Use:

- [Skill Review](./skills-create-manage-update/skill-review/SKILL.md) to decide whether conversion is viable
- [Skill Improver](./skills-create-manage-update/skill-improver/SKILL.md) for targeted repairs
- [Skill Writer](./skills-create-manage-update/skill-writer/SKILL.md) for substantial rewrites

Search for provider-specific paths, hooks, slash commands, tool names, prompt wrappers, and identity assumptions.

Retain provider-specific content only when it is legitimate, approved, and intrinsic to the skill's job.

**Output:** conversion report and converted-skill batch.

### Phase 5: Rebuild by Function

Use [Skill Library Restructure](./skills-create-manage-update/skill-library-restructure/SKILL.md).

1. Design functional categories from retained capabilities
2. Select canonical skills for overlap clusters
3. Merge duplicated workflows
4. Split independent jobs
5. Build category routers and focused children
6. Move superseded sources out of active discovery
7. Reconcile every source path with its final destination

Use [Skills Writing](./skills-create-manage-update/skills-writing/SKILL.md) only as a supporting pattern library.
Use [Enhanced Template](./skills-create-manage-update/template-skill-enhanced/SKILL.md) only as a structural example.

**Output:** complete router-based rebuilt library, merge map, and split map.

### Phase 6: Repair Canonical Skills

Use [Skill Improver](./skills-create-manage-update/skill-improver/SKILL.md) for approved repairs.

Use:

- [Skill Make Template](./skills-create-manage-update/skill-make-template/SKILL.md) for straightforward new skills
- [Skill Writer](./skills-create-manage-update/skill-writer/SKILL.md) for complex source-backed authoring
- [Skill Creator](./skills-create-manage-update/skill-creator/SKILL.md) only when benchmarks, graders, reports, or packaging are justified

**Output:** finalized canonical skills.

### Phase 7: Validate the Rebuilt Library

Use [Skill Check](./skills-create-manage-update/skill-check/SKILL.md).

Validate:

- Inventory coverage
- Unique skill names
- Valid frontmatter
- Folder-name alignment
- Relative links
- Parent-to-child routing
- Trigger separation
- Supporting-resource references
- Application compatibility
- Model-specific cleanup
- Quarantine and provenance records
- Absence of user-specific absolute paths in committed artifacts

Use [Skill Optimizer](./skills-create-manage-update/skill-optimizer/SKILL.md) only when real usage data is available and behavior diagnostics are useful.

**Output:** validation report and repair list with no silent omissions.

### Phase 8: Publish and Review

Use [GitHub Operations](./github-operations/SKILL.md) to:

1. Review the complete diff
2. Separate unrelated changes when needed
3. Commit with meaningful messages
4. Push the branch
5. Open a draft pull request
6. Confirm CI and validation results
7. Address review feedback
8. Merge only after repository state is verified

Use [Skill Manage](./skills-create-manage-update/skill-manage/SKILL.md) for final installation, synchronization, movement, or retirement operations.

**Output:** reviewable pull request and publication record.

## Phase Boundary Rule

Do not collapse the entire rebuild into one unverified pass.

Each phase should end with:

- A concrete artifact or report
- A coverage check
- A concise decision summary
- A repository diff review
- A dedicated commit when files changed

## Completion Requirements

The broader task is complete only when:

- Every source skill appears in the inventory
- Every source skill has one documented disposition
- Unsupported skills are quarantined or retired traceably
- Convertible provider-specific skills are generalized or rebuilt
- Retained skills are grouped by function
- Duplicate and multi-function skills are resolved
- Parent routers link to every retained child
- The rebuilt library validates
- Audit reports reconcile with the filesystem
- Committed artifacts contain no unapproved user-specific absolute paths
- Repository changes are committed, reviewed, and verified
