---
name: 1password-cli
description: 'Execute 1Password CLI (op) operations for local development, secret retrieval, item/vault CRUD, configuration injection, shell plugins, and git credential workflows. Use when running op read, op run, op inject, managing items/vaults/documents, or configuring developer shell plugins.'
compatibility: 'Requires 1Password CLI v2+ installed and authenticated via op signin.'
metadata:
  category: infrastructure-and-ops
  type: execution-child
  source: custom
---

# 1Password CLI

Retrieve secrets and manage 1Password items, vaults, and documents using the native `op` CLI.

## When to Use

- Reading individual secret fields (`op read`)
- Running local processes with injected secrets (`op run`)
- Populating configuration templates (`op inject`)
- Creating, editing, or inspecting vaults, items, and documents
- Configuring developer shell plugins (AWS, GitHub, Stripe) and Git credential helpers

## Quick Reference & Command Structure

```bash
# Authentication
op whoami || eval $(op signin)

# Secret Retrieval
op read "op://<vault>/<item>/<field>"
op run --env-file=.env.template -- <command>
op inject -i template.env -o .env

# Item & Vault Management
op item list --vault "<vault>"
op item get "<item>"
op item create --category login --title "<title>" --vault "<vault>"
op item edit "<item>" "<field>=<value>"
op vault list
op vault get "<vault>"
op document get "<doc-name>" --out-file ./secret.pem
```

## Secret Retrieval Workflows

### Secret Reference Format
The canonical URI structure is: `op://<vault>/<item>/[section/]<field>`.

### Direct Retrieval & JSON Output
```bash
# Read specific field
op read "op://Development/Database/password"

# Read formatted JSON
op item get "Database" --format json
```

### Injecting Secrets into Commands (`op run`)
Use `.env.tpl` references:
```bash
AWS_ACCESS_KEY_ID=op://Development/AWS/access_key_id
AWS_SECRET_ACCESS_KEY=op://Development/AWS/secret_access_key
```
Execute with:
```bash
op run --env-file=.env.tpl -- npm start
```

### Injecting Secrets into Configuration Files (`op inject`)
```bash
op inject -i config.tpl.yaml -o config.yaml
```

## Item & Document Management

- **Creating Items**: Use `op item create --category login --title "API Key" --vault "Development"`.
- **Editing Items**: Update fields with `op item edit "API Key" "password=new-secret"`.
- **Document Management**: Securely download and store private keys and certificates with `op document get` and `op document create`.

## Shell Plugins & Git Workflow

### Shell Plugins Setup
Initialize plugins for AWS, GitHub, Stripe, or Vercel:
```bash
op plugin init aws
op plugin init gh
```

### Git Workflow & Credential Helper
1. Initialize `gh` plugin: `op plugin init gh`.
2. Configure Git credential helper:
   ```bash
   git config --global credential.helper ""
   git config --global credential.https://github.com.helper "!gh auth git-credential"
   ```
3. Run helper script: `bash ./scripts/setup-gh-plugin.sh`.

## Troubleshooting & Common Issues

- **Session Expired**: Run `eval $(op signin)`.
- **Item Not Found**: Check item ID with `op item list --vault "<vault>"`. Use item UUID instead of name for deterministic lookup.
- **Broken Plugin Configuration**: Reset configuration with `op plugin init <plugin> --reset`.

## Completion Evidence

- Exit code 0 from `op` command.
- Verified secret injection without stdout/terminal exposure.
