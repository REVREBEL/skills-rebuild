---
name: 1password
description: 'Route 1Password secrets management requests across CLI retrieval, Developer Environments, Kubernetes integrations, and Service Account CI/CD workflows. Use when determining the correct 1Password workflow for local development, environment variable sync, Kubernetes secret injection, or automated deployments.'
compatibility: 'Requires 1Password CLI (op) v2+, 1Password account, or OP_SERVICE_ACCOUNT_TOKEN.'
metadata:
  category: infrastructure-and-ops
  type: category-router
  source: custom
---

# 1Password Router

Route secrets management tasks to the appropriate specialized 1Password child skill.

## When to Use

Use this router to navigate 1Password capabilities across development, environment management, and deployment pipelines:

- Retrieving secrets, reading items, or injecting into configuration files -> [1Password CLI](./1password-cli/SKILL.md)
- Managing project environment variables and Developer Environments via Bun/Python SDK -> [1Password Developer Environments](./1password-developer-environments/SKILL.md)
- Syncing secrets to Kubernetes via External Secrets Operator or native 1Password Operator -> [1Password Kubernetes](./1password-kubernetes/SKILL.md)
- Automating CI/CD pipelines using Service Account tokens -> [1Password Service Accounts](./1password-service-accounts/SKILL.md)

## Workflow Decision Matrix

| User Goal | Tool / Runtime | Specialized Child Skill |
|---|---|---|
| Retrieve single secret (`op read`), run commands with env vars (`op run`), manage items/vaults | `op` CLI | [1Password CLI](./1password-cli/SKILL.md) |
| Manage project environment variables, sync `.env` files, bulk resolve via Python SDK/TypeScript CLI | Bun / Python SDK CLI | [1Password Developer Environments](./1password-developer-environments/SKILL.md) |
| Inject secrets into Kubernetes pods, configure ExternalSecret or OnePasswordItem CRDs | K8s Operator / ESO | [1Password Kubernetes](./1password-kubernetes/SKILL.md) |
| CI/CD pipeline automation (GitHub Actions, GitLab CI) with scoped service account tokens | Service Account Token | [1Password Service Accounts](./1password-service-accounts/SKILL.md) |

## Category Policies & Security Guidelines

- **Zero Credential Exposure**: Never log, print, or commit raw tokens or secrets.
- **Principle of Least Privilege**: Grant service accounts access only to the specific vaults required.
- **Environment Isolation**: Separate Production, Staging, and Development secrets into distinct vaults.
