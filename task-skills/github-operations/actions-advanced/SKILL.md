---
name: actions-advanced
description: 'Create, update, optimize, or modernize GitHub Actions workflows for testing, building, deployment, release, issue triage, and repository automation. Use when working with .github/workflows, reusable workflows, matrices, caching, artifacts, environments, OIDC, permissions, or workflow orchestration.'
compatibility: 'Requires repository write access to modify workflow files. Live validation requires permission to push or dispatch GitHub Actions runs.'
metadata:
  category: github
  type: actions-authoring
  source: consolidated
---

# GitHub Actions Workflows

Design secure, maintainable Actions workflows that fit the repository's actual stack and delivery model.

## When to Use

Use when the user wants to:

- add or change CI checks
- automate tests, builds, deployments, or releases
- create reusable workflows or composite actions
- configure matrices, caching, artifacts, concurrency, or environments
- add issue or PR automation through Actions
- migrate deprecated action versions or workflow syntax
- improve workflow performance or maintainability

Use `actions-debugger` for a failing run and `security-review` for an exploit-focused security assessment.

## Workflow

### 1. Inspect repository context

Read:

- existing `.github/workflows/*.yml` and `.yaml`
- local composite actions
- package manifests and supported runtimes
- deployment and release documentation
- branch protection and required checks
- existing secret, environment, or OIDC conventions

Do not introduce AWS, Kubernetes, Windows, or another platform unless the repository actually uses it or the user requests it.

### 2. Define the workflow contract

Resolve:

- events and branch or path filters
- required jobs and dependencies
- runner operating systems and versions
- inputs, outputs, secrets, and environments
- permissions and approval gates
- artifacts, caches, and retention
- failure, retry, and concurrency behavior
- success evidence

### 3. Apply secure defaults

- declare least-privilege `permissions`
- pin third-party actions to reviewed immutable SHAs when repository policy requires it
- set `timeout-minutes`
- use `concurrency` where duplicate runs waste resources or create deployment races
- keep untrusted data out of shell-expanded `run` commands
- avoid checking out fork code in privileged `pull_request_target` workflows
- prefer OIDC or short-lived credentials over long-lived cloud keys
- isolate deployment jobs behind GitHub Environments when approvals are needed

### 4. Keep workflows composable

Use reusable workflows for repeated multi-job pipelines and composite actions for repeated step sequences.

Avoid one enormous workflow that combines unrelated validation, deployment, release, and maintenance behavior.

### 5. Implement from repository scripts

Prefer workflows that call tested repository scripts or package commands rather than duplicating complex shell logic in YAML.

Use expressions in `if`, `with`, or `env` deliberately. Quote shell values and write multiline outputs through supported environment files.

### 6. Optimize execution

Use:

- dependency caches with precise keys
- job outputs and `needs`
- matrices only for supported combinations
- path filters when they do not hide required checks
- artifacts for handoff between isolated jobs
- fail-fast behavior appropriate to the matrix
- pinned runner images when reproducibility matters

### 7. Validate locally and remotely

Validate syntax and referenced scripts. Run available workflow linters such as `actionlint` when the repository supports them.

After publication, verify a real run or dispatch when authorized. Read job and step status rather than assuming the YAML is valid.

## Automation Boundaries

Provider-neutral issue triage, PR labeling, release notes, and scheduled maintenance may live in Actions. Do not hardcode a particular AI provider, model, or secret into a generic workflow. Treat AI-generated issue or PR content as untrusted and require bounded permissions.

## Completion

Report:

- workflows and triggers added or changed
- permissions and secret requirements
- validation run
- live run status, when available
- deployment or release actions that remain intentionally unexecuted
