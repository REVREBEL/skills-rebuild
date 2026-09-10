---
name: 1password-developer-environments
description: 'Manage 1Password Developer Environments for project environment variables using TypeScript (Bun) and Python SDK tools. Use when creating, updating, exporting, or resolving project secrets programmatically.'
compatibility: 'Requires Bun or Python 3.9+ with OP_SERVICE_ACCOUNT_TOKEN.'
metadata:
  category: infrastructure-and-ops
  type: execution-child
  source: custom
---

# 1Password Developer Environments

Manage project secrets and environment variables using TypeScript (Bun) and Python SDK tooling.

## When to Use

- Creating and managing project developer environments in 1Password
- Exporting environments directly to `.env` files
- Programmatic secret resolution via `SecretsManager` in Python services

## Tool Setup

### TypeScript CLI (Bun)

```bash
cd tools
bun run create -- --help
bun run list -- --help
bun run export -- --help
```

### Python SDK CLI (uv)

```bash
cd tools-python
uv sync
uv run op-env-create --help
uv run op-env-list --help
uv run op-env-export --help
```

## Programmatic Integration (Python SDK)

```python
from op_env.secrets_manager import SecretsManager

async def main():
    sm = await SecretsManager.create()
    api_key = await sm.get("op://Production/API/key")
    env = await sm.resolve_environment("my-app-prod", "Production")
```

## Completion Evidence

- Validated environment creation or export.
- Successful resolution of environment references.
