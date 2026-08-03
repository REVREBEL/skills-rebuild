# Task 01: Establish the Skills Library Baseline

## Objective

Create a fixed, traceable baseline of the current skills library before any files are moved, rewritten, merged, split, or retired.

## Required Context

Resolve and record the physical repository paths corresponding to:

- Source library: `agents/skills`
- Quarantine library: `agents/not-needed`
- Rebuilt library: `agents/skills-rebuild`
- Task workflow library: `task-skills`

Record the repository, default branch, working branch, starting commit SHA, current source-library tree, skill-folder count, existing routers, and protected or excluded paths.

Ignore generated or operating-system metadata such as `__MACOSX`, `.DS_Store`, and `._*`.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/github-operations/SKILL.md`

Use the GitHub operation children selected by that router for repository inspection, branch creation, commit preparation, and remote verification.

## Work

1. Confirm the exact repository and current default branch.
2. Create or confirm a dedicated working branch.
3. Record the starting commit SHA.
4. Resolve the physical source, quarantine, rebuilt, and task-skill paths.
5. Capture the complete `agents/skills` directory tree and count its skill folders.
6. Identify existing root and category routers.
7. Record protected files, excluded paths, and any pre-existing work that must not be overwritten.
8. Do not move or rewrite source skills during this task.

## Deliverable

Create:

`agents/skills-rebuild/_audit/baseline.md`

The file must contain the repository identity, branch information, starting SHA, resolved paths, source-tree summary, skill count, existing router locations, exclusions, and rollback reference.

## Completion Gate

Complete only when the recorded baseline can be used to reconstruct where every source skill originated and all repository and path assumptions have been verified.