# Task 12: Pilot, Review, and Publish the Rebuilt Library

## Objective

Test representative end-to-end use cases, correct routing or execution failures, and publish the rebuilt library only after current validation evidence and repository review support the release.

## Required Context

Use:

- The final `agents/skills-rebuild` filesystem
- `agents/skills-rebuild/_audit/validation-report.md`
- `agents/skills-rebuild/_audit/unresolved-items.md`
- `agents/skills-rebuild/_audit/router-validation.md`
- All completed batch and disposition records under `agents/skills-rebuild/_audit/`

Do not publish while unresolved items include blocking structural, compatibility, security, routing, or provenance failures.

Pilot representative scenarios that exercise different categories and handoffs, including:

- Create a new skill
- Find and review an existing skill
- Publish a GitHub change
- Debug a workflow failure
- Analyze a dataset
- Create or revise documentation
- Perform a marketing or SEO task when those skills are retained
- Route a hospitality-specific task when those skills are retained

Use realistic prompts and record the selected router path, child skill, required tools, outcome, and any duplicated or missing steps.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/github-operations/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`
- `task-skills/skills-create-manage-update/skill-manage/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`

Use the applicable rebuilt root and category routers during every pilot scenario. Use the GitHub operation children selected by the GitHub router for final diff review, commits, pull request creation, review feedback, merge, and remote verification.

## Work

1. Confirm no blocking unresolved item remains.
2. Run the representative pilot scenarios against the rebuilt routers and child skills.
3. Record routing, tool use, outputs, handoffs, failures, and duplicated steps.
4. Correct discovery descriptions, router boundaries, broken handoffs, and execution defects found during the pilot.
5. Rerun affected validation and pilot scenarios after every correction.
6. Reconcile the final inventory and destination records with the published filesystem.
7. Review the complete repository diff and exclude unrelated changes.
8. Commit and push the final validated batches.
9. Open or update a reviewable pull request with truthful validation and unresolved-item status.
10. Address review feedback and merge only after current checks, approvals, and repository policy are satisfied.
11. Verify the target branch and published library after merge.

## Deliverables

Create:

- `agents/skills-rebuild/_audit/pilot-report.md`
- `agents/skills-rebuild/_audit/publication-record.md`

The pilot report must record each scenario, route selected, result, defects found, corrections, and retest outcome. The publication record must include branch, commits, pull request, review status, validation evidence, merge result, and final target SHA.

## Completion Gate

Complete only when all pilot scenarios pass or have explicitly accepted limitations, blocking validation issues are resolved, audit records reconcile with the final filesystem, the reviewed changes are merged according to repository policy, and the published target state is verified.