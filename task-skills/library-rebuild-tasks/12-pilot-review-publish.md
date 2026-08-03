# Task 12: Pilot, Review, and Publish the Rebuilt Library

## Objective

Test representative end-to-end use cases, correct routing or execution failures, and publish the rebuilt library only after current validation evidence and repository review support the release.

## Preconditions

- The final `agents/skills-rebuild` filesystem and audit records exist.
- `validation-report.md`, `unresolved-items.md`, and `router-validation.md` reconcile with the filesystem.
- No unresolved item is marked as a blocking structural, compatibility, security, routing, or provenance failure.
- Applicable rebuilt root and category routers are ready for pilot use.

## Canonical Task Skills

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-check/SKILL.md`
- `task-skills/skills-create-manage-update/skill-improver/SKILL.md`
- `task-skills/skills-create-manage-update/skill-manage/SKILL.md`
- `task-skills/github-operations/SKILL.md`

Use `skill-check` for retesting, `skill-improver` for approved defects found during pilots, `skill-manage` for final movement or synchronization, and the GitHub router for diff review, commits, pull requests, review feedback, merge, and remote verification. Use `skill-optimizer` only after the pilot produces real usage evidence and only for evidence-based performance or discovery optimization.

## Work

1. Confirm no blocking unresolved item remains.
2. Run representative pilot scenarios against the rebuilt routers and children, including:
   - Create a new skill
   - Find and review an existing skill
   - Publish a GitHub change
   - Debug a workflow failure
   - Analyze a dataset
   - Create or revise documentation
   - Perform a marketing or SEO task when retained
   - Route a hospitality-specific task when retained
3. Record the selected route, child skill, required tools, outcome, handoffs, and duplicated or missing steps.
4. Correct discovery descriptions, router boundaries, broken handoffs, and execution defects found during the pilot.
5. Rerun affected validation and pilot scenarios after every correction.
6. Reconcile the final inventory and destination records with the publishable filesystem.
7. Review the complete repository diff and exclude unrelated changes.
8. Commit and push the final validated batches.
9. Open or update a reviewable pull request with truthful validation and unresolved-item status.
10. Address review feedback and merge only after current checks, approvals, and repository policy are satisfied.
11. Verify the target branch and published library after merge.

## Artifacts

Create:

- `agents/skills-rebuild/_audit/pilot-report.md`
- `agents/skills-rebuild/_audit/publication-record.md`

The pilot report must record each scenario, expected route, actual route, result, defect, correction, retest result, and any accepted limitation. The publication record must include branch, commits, pull request, review state, validation evidence, unresolved-item status, merge result, target branch, and final target SHA.

## Reconciliation Requirements

- Reconcile every pilot scenario to the router path and active child used.
- Reconcile every pilot defect to a correction, accepted limitation, or unresolved item.
- Reconcile final inventory, destination, router, validation, and filesystem state before publication.
- Reconcile published commits and pull-request head to the reviewed diff.
- Reconcile the merge result and final target SHA through remote readback.

## Repository Checkpoint

1. Begin only after Phase 11 is approved and merged into `main`.
2. Create and complete this phase on `skills-rebuild/phase-12-pilot-publish` from the updated `main` branch.
3. Use focused commits for pilot corrections and final publication preparation, then review the complete phase diff.
4. Commit the final phase checkpoint with: `skills-rebuild: complete phase 12 pilot and publication`.
5. Push the branch and open a draft pull request targeting `main`.
6. The pull request must summarize pilot scenarios, corrections, retest evidence, artifact paths, final reconciliation, validation status, and accepted limitations.
7. Address review feedback on the same branch. Merge only after explicit approval, current checks, and repository policy are satisfied.
8. After merge, verify the final target SHA and update `publication-record.md` with the confirmed result.

## Completion Gate

Complete only when:

- All preconditions are satisfied.
- Both pilot and publication artifacts exist with complete evidence.
- All pilot scenarios pass or have explicitly accepted non-blocking limitations.
- Blocking validation issues are resolved.
- Audit records reconcile with the final filesystem.
- Changes are merged according to repository policy and the published target state is verified.