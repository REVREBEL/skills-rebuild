---
name: github-operations
description: 'Route Git and GitHub repository operations across branches, commits, pushes, issues, pull requests, Actions, automation, security review, repository documentation, and skill publication. Use when a task requires GitHub MCP, the gh CLI, local git, repository lifecycle work, CI investigation, or publishing changes safely through a branch and pull request.'
compatibility: 'Requires access to a Git repository. GitHub-hosted operations require GitHub MCP, the gh CLI, or another authenticated GitHub integration with the necessary permissions.'
metadata:
  category: github
  type: master-router
  source: custom
---

# GitHub Operations

Route Git and GitHub work to the narrowest available child skill. This parent skill defines boundaries and sequencing; child skills own execution details.

## When to Use This Skill

Use this router when the user wants to:

- Inspect or modify a GitHub repository
- Create or switch branches
- Stage and commit changes
- Push changes to a remote
- Create or manage issues
- Create, improve, review, or merge pull requests
- Diagnose GitHub Actions failures
- Build or update Actions workflows
- Review repository security
- Create repository-facing documentation such as `llms.txt`
- Publish an Agent Skill to GitHub

Do not select every child skill for one request. Choose the smallest workflow that fully satisfies the task.

## Operating Model

Use three layers deliberately:

1. **GitHub MCP or connector:** structured repository, issue, pull-request, review, and Actions operations.
2. **Local `git` and `gh`:** working-tree inspection, staging, commits, branch changes, logs, and operations not covered by MCP.
3. **GitHub operation skills:** workflow order, safety boundaries, routing, and validation.

The MCP provides capabilities. These skills define how to use them safely and coherently.

## Universal Safety Rules

- Resolve the exact repository before acting.
- Inspect repository instructions and current branch state.
- Do not assume the working tree is clean.
- Do not overwrite uncommitted user work.
- Do not commit secrets, credentials, tokens, private keys, or `.env` contents.
- Do not force-push or rewrite shared history without explicit authorization.
- Prefer a task branch and pull request for broad or multi-file work.
- Review the diff before committing.
- Verify the remote branch and pull request after publication.
- Never claim CI, merge, push, or indexing success without readback.

## Quick Routing Guide

| User goal | Primary child skill |
|---|---|
| General GitHub CLI or API operation | [GitHub](./github/SKILL.md) |
| Create a safe task branch | [Create Branch](./create-branch/SKILL.md) |
| Select a Git Flow branch type | [Flow Branch Creator](./flow-branch-creator/SKILL.md) |
| Create a conventional commit | [Commit](./commit/SKILL.md) |
| Commit and push a logical change set | [Pushing](./pushing/SKILL.md) |
| Create an issue | [Issue Creator](./issue-creator/SKILL.md) |
| Require an issue before implementation | [Create Issue Gate](./create-issue-gate/SKILL.md) |
| Track a feature through GitHub | [Feature Tracking](./feature-tracking/SKILL.md) |
| Open a basic pull request | [Create PR](./create-pr/SKILL.md) |
| Write or improve PR content | [PR Writer](./pr-writer/SKILL.md) |
| Review a pull request | [PR Review](./pr-review/SKILL.md) |
| Request reviewers | [Review Requests](./review-requests/SKILL.md) |
| Merge an approved pull request | [PR Merge Champion](./pr-merge-champion/SKILL.md) |
| Diagnose a failed Actions run | [Actions Debugger](./actions-debugger/SKILL.md) |
| Create a workflow from a template | [Actions Templates](./actions-templates/SKILL.md) |
| Design advanced Actions workflows | [Actions Advanced](./actions-advanced/SKILL.md) |
| Review workflow security | [Security Review](./security-review/SKILL.md) |
| Create repository `llms.txt` | [LLMS Create](./llms-create/SKILL.md) |
| Update an existing `llms.txt` | [LLMS Update](./llms-update/SKILL.md) |
| Publish a skill to GitHub | [Push Skill to GitHub](./push-skill-to-github/SKILL.md) |

## Child Skills by Function

### Core GitHub Access

#### [GitHub](./github/SKILL.md)

Use `gh` and GitHub API operations for issues, pull requests, workflow runs, and structured repository queries.

This is a general-purpose child skill, not the parent router.

### Branches, Commits & Local Git

#### [Create Branch](./create-branch/SKILL.md)

Create a task branch from an explicitly resolved base branch or commit.

#### [Flow Branch Creator](./flow-branch-creator/SKILL.md)

Analyze current changes and select a Git Flow-style feature, release, or hotfix branch.

Use only when the repository actually follows Git Flow. Prefer `create-branch` for trunk-based or simpler repositories.

#### [Commit](./commit/SKILL.md)

Analyze a diff, stage a logical change set, and create a Conventional Commit.

#### [Pushing](./pushing/SKILL.md)

Commit and push changes safely, including the bundled smart-commit script when appropriate.

#### [Advanced Workflows](./advanced-workflows/SKILL.md)

Handle advanced Git workflows that exceed a basic branch, commit, and push cycle.

#### [Hooks Automation](./hooks-automation/SKILL.md)

Create or maintain Git hooks and hook-driven automation.

#### [Workflow Versioning](./workflow-versioning/SKILL.md)

Manage Git workflow conventions, releases, tags, or versioning policies.

### Issues & Feature Tracking

#### [Issue Creator](./issue-creator/SKILL.md)

Create a well-structured GitHub issue from a bug, feature, task, or request.

#### [Create Issue Gate](./create-issue-gate/SKILL.md)

Require or create an issue before implementation begins, preserving traceability between work and repository planning.

#### [Feature Tracking](./feature-tracking/SKILL.md)

Track a feature across issues, branches, commits, pull requests, and delivery status.

### Pull Request Lifecycle

#### [Create PR](./create-pr/SKILL.md)

Open a basic pull request after a branch has been pushed.

#### [PR Writer](./pr-writer/SKILL.md)

Draft or improve a pull-request title and body using the actual change set.

#### [PR Review](./pr-review/SKILL.md)

Review a pull request for correctness, risk, regressions, and maintainability.

#### [Review Requests](./review-requests/SKILL.md)

Select and request appropriate individual or team reviewers.

#### [PR Merge Champion](./pr-merge-champion/SKILL.md)

Confirm readiness and merge a pull request using the repository’s allowed merge strategy.

#### [PR Workflows: Onboard](./pr-workflows-onboard/SKILL.md)

Set up or onboard a repository or team to a pull-request workflow.

#### [PR Workflows: Enhance](./pr-workflows-pr-enhance/SKILL.md)

Improve an existing pull-request workflow using its bundled implementation playbook.

Supporting reference:

- [Implementation Playbook](./pr-workflows-pr-enhance/resources/implementation-playbook.md)

#### [PR Workflows: Workflow](./pr-workflows-workflow/SKILL.md)

Define or execute a broader Git and pull-request workflow.

### GitHub Actions & Automation

#### [Actions Debugger](./actions-debugger/SKILL.md)

Investigate failing GitHub Actions runs, jobs, steps, and logs.

#### [Actions Templates](./actions-templates/SKILL.md)

Create reusable GitHub Actions workflows from common templates.

#### [Actions Advanced](./actions-advanced/SKILL.md)

Design or troubleshoot complex Actions workflows, matrices, caching, artifacts, environments, permissions, and orchestration.

#### [Automation](./automation/SKILL.md)

Handle focused GitHub automation tasks.

#### [Workflow Automation](./workflow-automation/SKILL.md)

Design broader repository workflow automation spanning issues, pull requests, Actions, or release operations.

These two automation skills currently overlap and should be compared during the consolidation phase.

### Security & Governance

#### [Security Review](./security-review/SKILL.md)

Review GitHub Actions or repository workflows for permissions, secret handling, dependency risks, injection risks, and supply-chain risks.

### Repository Presence, Discovery & Documentation

#### [Presence](./presence/SKILL.md)

Improve repository presence, presentation, discoverability, and project-facing metadata.

Supporting documentation:

- [Presence README](./presence/README.md)

#### [Image](./image/SKILL.md)

Handle GitHub-hosted image or repository image workflows.

#### [LLMS Create](./llms-create/SKILL.md)

Create a repository-root `llms.txt` navigation file.

#### [LLMS Update](./llms-update/SKILL.md)

Review and update an existing `llms.txt` as repository contents change.

#### [Global Chat Agent Discovery](./global-chat-agent-discovery/SKILL.md)

Configure or document repository-level agent discovery for supported chat or coding environments.

### Skill Publication

#### [Push Skill to GitHub](./push-skill-to-github/SKILL.md)

Publish an Agent Skill to a GitHub repository using an appropriate branch, commit, push, and pull-request workflow.

### Full Child Index

- [Actions Advanced](./actions-advanced/SKILL.md)
- [Actions Debugger](./actions-debugger/SKILL.md)
- [Actions Templates](./actions-templates/SKILL.md)
- [Advanced Workflows](./advanced-workflows/SKILL.md)
- [Automation](./automation/SKILL.md)
- [Commit](./commit/SKILL.md)
- [Create Branch](./create-branch/SKILL.md)
- [Create Issue Gate](./create-issue-gate/SKILL.md)
- [Create PR](./create-pr/SKILL.md)
- [Feature Tracking](./feature-tracking/SKILL.md)
- [Flow Branch Creator](./flow-branch-creator/SKILL.md)
- [GitHub](./github/SKILL.md)
- [Global Chat Agent Discovery](./global-chat-agent-discovery/SKILL.md)
- [Hooks Automation](./hooks-automation/SKILL.md)
- [Image](./image/SKILL.md)
- [Issue Creator](./issue-creator/SKILL.md)
- [LLMS Create](./llms-create/SKILL.md)
- [LLMS Update](./llms-update/SKILL.md)
- [PR Merge Champion](./pr-merge-champion/SKILL.md)
- [PR Review](./pr-review/SKILL.md)
- [PR Workflows: Onboard](./pr-workflows-onboard/SKILL.md)
- [PR Workflows: Enhance](./pr-workflows-pr-enhance/SKILL.md)
- [PR Workflows: Workflow](./pr-workflows-workflow/SKILL.md)
- [PR Writer](./pr-writer/SKILL.md)
- [Presence](./presence/SKILL.md)
- [Push Skill to GitHub](./push-skill-to-github/SKILL.md)
- [Pushing](./pushing/SKILL.md)
- [Review Requests](./review-requests/SKILL.md)
- [Security Review](./security-review/SKILL.md)
- [Workflow Automation](./workflow-automation/SKILL.md)
- [Workflow Versioning](./workflow-versioning/SKILL.md)

## Recommended End-to-End Repository Change Route

For a normal multi-file task:

1. [GitHub](./github/SKILL.md): resolve repository context and inspect remote state.
2. [Create Branch](./create-branch/SKILL.md): create a dedicated branch.
3. Perform the requested implementation or file operations.
4. [Commit](./commit/SKILL.md): review and commit a logical change set.
5. [Pushing](./pushing/SKILL.md): push and verify the remote branch.
6. [PR Writer](./pr-writer/SKILL.md): prepare the pull-request narrative.
7. [Create PR](./create-pr/SKILL.md): open a draft pull request.
8. [Actions Debugger](./actions-debugger/SKILL.md): investigate failures when checks do not pass.
9. [PR Review](./pr-review/SKILL.md): review the complete change set.
10. [PR Merge Champion](./pr-merge-champion/SKILL.md): merge only after approval and validation.

## Known Consolidation Candidates

Do not merge these automatically yet, but compare them during the later audit:

- `automation` and `workflow-automation`
- `commit` and portions of `pushing`
- `create-branch` and `flow-branch-creator`
- `create-pr` and `pr-writer`
- `advanced-workflows`, `workflow-versioning`, and portions of the PR workflow group
- `actions-advanced` and `actions-templates`
- `presence`, `image`, and portions of `global-chat-agent-discovery`

A shared application is not sufficient reason to merge. Compare triggers, outcomes, and unique instructions.

## Completion Checks

Before completing a GitHub operation, confirm:

- The intended repository and branch were used
- The working tree was inspected
- Secrets and unrelated files were excluded
- The final diff matches the requested scope
- Commits exist locally and remotely when publication was requested
- The pull request targets the correct base branch
- CI status was read rather than assumed
- Every destructive or history-rewriting action was explicitly authorized
