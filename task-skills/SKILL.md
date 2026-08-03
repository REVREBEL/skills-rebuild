---
name: task-skills
description: 'Route and coordinate the GitHub and Agent Skills workflows required to audit, classify, refactor, reorganize, validate, and publish a skills library. Use when rebuilding a skills repository, filtering application-specific skills, converting Claude-specific instructions, cataloging skills, merging or splitting skills, creating functional category routers, or publishing the rebuilt library through GitHub.'
compatibility: 'Requires filesystem access to the target skills library and GitHub access for repository operations. Resolve the active source, quarantine, and rebuilt directories before making changes.'
metadata:
  category: task-orchestration
  type: master-router
  source: custom
---

# Skills Library Rebuild Task Router

Coordinate the complete skills-library cleanup and rebuild without collapsing the work into one oversized, difficult-to-verify operation.

This is the top-level router for the task. It delegates execution to two functional skill groups:

- [GitHub Operations](./github-operations/SKILL.md): repository inspection, branching, commits, pull requests, Actions, issues, and publication.
- [Skills Create, Manage & Update](./skills-create-manage-update/SKILL.md): inventory, auditing, creation, conversion, refinement, consolidation, validation, and routing architecture.

## When to Use This Skill

Use this router when the work involves multiple stages of a skills-library rebuild, including:

- Reviewing a large source skills folder
- Comparing application-specific skills against an approved stack
- Moving unsupported skills into a quarantine or `not-needed` folder
- Identifying and converting Claude-specific instructions
- Cataloging skill metadata and dependencies
- Grouping skills by function
- Detecting duplicates and overlapping triggers
- Splitting oversized skills
- Merging similar skills
- Creating parent routers and child skill groups
- Validating and publishing the rebuilt library

Do not use this router for a single isolated GitHub operation or a single standalone skill edit. Route those requests directly to the relevant child group.

## Required Directory Resolution

At the beginning of the task, resolve and record the actual paths for:

- **Source library:** logically `agents/skills`
- **Quarantine library:** logically `agents/not-needed`
- **Rebuilt library:** logically `agents/skills-rebuild`
- **Task skills:** `task-skills`

The repository may place these folders beneath a project root such as `task-folder/`. Do not assume the physical prefix. Discover the paths and use them consistently.

## Governing Principles

1. **Inventory before movement.** Create a minimal source inventory before relocating any skill.
2. **Move, do not delete.** Unsupported or superseded skills go to quarantine with their supporting files intact.
3. **One documented disposition per source skill.** Every original skill must be traceable to a final decision.
4. **Separate classification from refactoring.** Decide what belongs before spending time rebuilding it.
5. **Use functional boundaries.** Split or merge according to independent triggers and outcomes, not file length alone.
6. **Keep parent routers thin.** Parent skills route; child skills execute.
7. **Preserve provenance.** Record source paths for converted, merged, and split skills.
8. **Work in reviewable batches.** Each phase should produce its own artifact, validation result, and Git commit.
9. **Publish through a branch and pull request.** Do not make broad unreviewed changes directly on the default branch.
10. **Verify the filesystem and repository state.** Never infer that moves, commits, pushes, or indexing succeeded.

## Recommended Execution Phases

### Phase 0: Establish the Baseline

Use the [GitHub Operations router](./github-operations/SKILL.md) to:

1. Confirm the repository and default branch.
2. Inspect the working tree and current repository structure.
3. Create a dedicated task branch.
4. Record the starting commit SHA.
5. Confirm the source, quarantine, rebuilt, and task-skill directories.

**Output:** baseline record containing repository, branch, commit, and resolved paths.

### Phase 1: Build the Source Inventory

Use the [Skills Create, Manage & Update router](./skills-create-manage-update/SKILL.md), beginning with:

1. [Skill Scanner](./skills-create-manage-update/skill-scanner/SKILL.md)
2. [Skill Audit](./skills-create-manage-update/skill-audit/SKILL.md)

Capture at minimum:

- Source path
- Skill name
- Description
- Primary function
- Application or framework dependencies
- Model-specific dependencies
- Supporting files
- Approximate size
- Initial disposition status

Do not perform broad moves during this phase.

**Output:** complete source inventory and unresolved-review list.

### Phase 2: Apply the Application Compatibility Gate

Compare every application-specific skill against the approved application-stack reference.

Classify each skill as:

- Approved application
- Generalizable capability
- Unsupported application
- Ambiguous and requiring review

Move unsupported skills to the quarantine directory only after their inventory row and reason are recorded.

Use GitHub operations to commit the quarantine pass independently.

**Output:** application compatibility report, quarantine manifest, and verified file moves.

### Phase 3: Convert Model-Specific Skills

Identify Claude-specific or other model-specific assumptions, including proprietary paths, commands, hooks, tool names, and prompt wrappers.

For each affected skill, decide whether to:

- Generalize it
- Convert it for Codex-compatible operation
- Preserve a legitimate provider-specific integration
- Move it to quarantine

Use the skill authoring and improvement workflows routed by the [Skills Create, Manage & Update master](./skills-create-manage-update/SKILL.md).

**Output:** conversion report and converted-skill batch.

### Phase 4: Classify by Function

Assign every retained capability to a functional category.

Possible categories may include:

- AI and agents
- Automation and integrations
- Data and analytics
- Design and UX
- Development
- Documentation and knowledge management
- Frontend and UI
- GitHub and source control
- Infrastructure and deployment
- Marketing and SEO
- Research
- Testing and debugging
- Writing and content

Create categories from the actual retained library. Do not create empty categories to satisfy a preconceived taxonomy.

**Output:** functional classification map.

### Phase 5: Detect Overlap and Scope Problems

Review retained skills for:

- Duplicate triggers
- Equivalent workflows
- Conflicting instructions
- Overly broad skills
- Tiny fragments that belong together
- Parent skills containing child-level implementation detail
- Missing routers

Use:

- [Skill Review](./skills-create-manage-update/skill-review/SKILL.md)
- [Skill Improver](./skills-create-manage-update/skill-improver/SKILL.md)
- [Skill Optimizer](./skills-create-manage-update/skill-optimizer/SKILL.md)

**Output:** merge map, split map, and refinement queue.

### Phase 6: Rebuild the Functional Library

Create the final category routers and focused child skills.

Use:

- [Skill Make Template](./skills-create-manage-update/skill-make-template/SKILL.md)
- [Skill Writer](./skills-create-manage-update/skill-writer/SKILL.md)
- [Skill Development](./skills-create-manage-update/skill-development/SKILL.md)
- [Skill Check](./skills-create-manage-update/skill-check/SKILL.md)

Write finalized skills only into the rebuilt directory.

**Output:** complete router-based rebuilt library.

### Phase 7: Validate the Rebuilt Library

Validate:

- Inventory coverage
- Unique skill names
- Valid frontmatter
- Folder-name alignment
- Relative links
- Parent-to-child routing
- Trigger separation
- Supporting-file references
- Application compatibility
- Model-specific reference cleanup
- Quarantine and provenance records

Use the validation and review workflows in the [Skills Create, Manage & Update master](./skills-create-manage-update/SKILL.md).

**Output:** validation report and repair list with no silent omissions.

### Phase 8: Publish and Review

Use the [GitHub Operations router](./github-operations/SKILL.md) to:

1. Review the complete diff.
2. Separate unrelated changes when needed.
3. Commit with meaningful messages.
4. Push the branch.
5. Open a draft pull request.
6. Confirm CI and validation results.
7. Address review feedback.
8. Merge only after the repository state is verified.

**Output:** reviewable pull request and final publication record.

## Phase Boundary Rule

Do not combine the entire rebuild into one commit or one unverified execution pass.

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
- Unsupported skills are quarantined rather than deleted
- Convertible model-specific skills are generalized or rebuilt
- Retained skills are grouped by function
- Duplicate and oversized skills are resolved
- Parent routers link to every retained child
- The rebuilt library validates
- Audit reports reconcile with the filesystem
- Repository changes are committed, pushed, reviewed, and verified
