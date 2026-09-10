---
name: 1password-cli
description: 'Execute 1Password CLI (op) operations for local development, secret retrieval, item/vault CRUD, and configuration injection. Use when running op read, op run, op inject, managing items, or configuring developer shell plugins.'
compatibility: 'Requires 1Password CLI v2+ installed and authenticated via op signin.'
metadata:
  category: infrastructure-and-ops
  type: execution-child
  source: custom
---

# 1Password CLI

Retrieve secrets and manage 1Password items and vaults using the native `op` CLI.

## When to Use

- Reading individual secret fields (`op read`)
- Running local processes with injected secrets (`op run`)
- Populating configuration templates (`op inject`)
- Creating, editing, or inspecting vaults, items, and documents

## Required Inputs

- Secret URI formatted as `op://<vault>/<item>/[section/]<field>`
- Template file paths for configuration injection

## Workflow

### 1. Authentication Check

```bash
op whoami || op signin
```

### 2. Secret Retrieval

```bash
# Read a single secret value
op read "op://Development/Database/password"

# Run a command with environment variables populated from 1Password
op run --env-file=.env.template -- npm start

# Inject secrets into a template file
op inject -i template.env -o .env
```

### 3. Vault & Item Management

```bash
# List and inspect vaults
op vault list
op vault get "Development"

# Item operations
op item list --vault "Development"
op item get "Database"
op item create --category login --title "API Key" --vault "Development"
```

## Completion Evidence

- Exit code 0 from `op` command.
- Verified secret injection without terminal exposure.
