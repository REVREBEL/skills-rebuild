---
name: 1password-service-accounts
description: 'Configure 1Password Service Accounts for CI/CD automation, GitHub Actions, GitLab CI, and container environments. Use when provisioning service account tokens and configuring secure automated secret injection.'
compatibility: 'Requires 1Password CLI v2+ with service account admin permissions.'
metadata:
  category: infrastructure-and-ops
  type: execution-child
  source: custom
---

# 1Password Service Accounts

Automate secret access in CI/CD pipelines and headless environments using Service Account tokens.

## When to Use

- Provisioning service account tokens with scoped vault permissions
- Integrating 1Password into GitHub Actions workflows
- Configuring GitLab CI/CD or Docker container secret injection

## GitHub Actions Workflow Example

```yaml
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: 1password/load-secrets-action@v2
        with:
          export-env: true
        env:
          OP_SERVICE_ACCOUNT_TOKEN: ${{ secrets.OP_SERVICE_ACCOUNT_TOKEN }}
          DB_PASSWORD: "op://Production/Database/password"
          API_KEY: "op://Production/Stripe/api_key"
      - run: npm run deploy
```

## Completion Evidence

- Verified workflow execution with injected environment variables.
- Zero secret exposure in CI build logs.
