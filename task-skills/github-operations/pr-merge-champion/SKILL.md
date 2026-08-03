---
name: pr-merge-champion
description: 'Verify that a GitHub pull request is ready, select an allowed merge strategy, perform an authorized merge, and confirm the target branch contains the expected result. Use when asked to merge, enable auto-merge, queue, or finalize an approved pull request.'
compatibility: 'Requires authenticated GitHub write access and permission to merge the target pull request.'
metadata:
  category: github
  type: pull-request-merge
  source: consolidated
---

# Pull Request Merge

Merge only when repository policy, current revision identity, required checks, and user authorization all align.

## When to Use

Use when the user asks to:

- merge an approved pull request
- enable auto-merge
- add a PR to a merge queue
- determine the exact blocker preventing merge
- verify a recently merged PR

Use `pr-review` for code review and `actions-debugger` for failing checks.

## Workflow

### 1. Resolve exact PR identity

Read:

- repository and PR number
- base branch and full base SHA
- head branch and full head SHA
- draft state
- author and fork identity
- mergeability and merge-state status

All readiness evidence must correspond to the current head SHA.

### 2. Read repository merge policy

Inspect:

- branch protection and rulesets
- required checks
- required approvals and code owners
- unresolved-review-thread policy
- merge queue or auto-merge requirements
- allowed merge methods
- repository-specific maintainer or release commands

Do not replace a guarded repository command with a generic merge API.

### 3. Evaluate readiness

Confirm:

- PR is open and not draft
- required checks are successful and current
- required approvals are present
- no blocking change requests remain
- required conversations are resolved
- branch is mergeable or queued according to policy
- issue, changelog, migration, or release requirements are satisfied

Pending and skipped are not equivalent to passed.

### 4. Recheck immediately before mutation

Refresh the head SHA, base SHA, checks, reviews, and mergeability. Stop when any evidence changed or became stale.

### 5. Select the merge path

Use, in order:

1. repository-required merge queue or maintainer command
2. authorized auto-merge when required checks are still running
3. allowed direct merge method after all gates pass

Choose squash, merge commit, or rebase according to repository policy. Do not impose a preferred strategy.

### 6. Merge or queue

Perform the exact authorized operation. Enabling auto-merge or adding to a queue is not the same as completing a merge.

### 7. Verify the final state

Read back:

- PR state and merged timestamp
- resulting merge commit SHA, when applicable
- target branch head
- queue or auto-merge state when not yet merged
- post-merge checks, deployment, or release state only when requested

Do not delete the source branch unless requested or repository policy handles it automatically.

## Blocker Output

When merge cannot proceed, report one exact blocker set, such as:

- required check failing or pending
- missing approval
- unresolved requested changes
- merge conflict
- stale head SHA
- permission failure
- merge queue required
- repository-specific release gate

## Safety Rules

- Never bypass branch protection, required reviews, or merge queues
- Never dismiss reviews or resolve threads merely to make a merge pass
- Never merge a different head SHA than the one reviewed
- Never force-update branches during the merge workflow without explicit authorization
- Never claim merge completion from an auto-merge enablement response

## Completion

Report the PR URL, reviewed head SHA, merge method or queue action, resulting target SHA, and any remaining post-merge work.
