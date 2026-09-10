---
name: 1password-kubernetes
description: 'Configure and deploy Kubernetes secret synchronization using the native 1Password Operator and External Secrets Operator (ESO). Use when injecting 1Password secrets into Kubernetes cluster secrets or pod volumes.'
compatibility: 'Requires Kubernetes cluster access, Helm, and 1Password Connect or ESO CRDs.'
metadata:
  category: infrastructure-and-ops
  type: execution-child
  source: custom
---

# 1Password Kubernetes Integration

Synchronize 1Password secrets with Kubernetes clusters using External Secrets Operator or native 1Password Operator.

## When to Use

- Configuring External Secrets Operator (ESO) `SecretStore` and `ExternalSecret` manifests.
- Deploying and configuring 1Password Connect server and `OnePasswordItem` CRDs.

## External Secrets Operator (ESO) Example

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: onepassword
  namespace: default
spec:
  provider:
    onepassword:
      connectHost: http://onepassword-connect:8080
      vaults:
        Production: 1
      auth:
        secretRef:
          connectTokenSecretRef:
            name: op-connect-token
            key: token
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: default
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: onepassword
    kind: SecretStore
  target:
    name: app-secrets
  data:
    - secretKey: DB_PASSWORD
      remoteRef:
        key: Production/Database
        property: password
```

## Completion Evidence

- Kubernetes secret created and synced from 1Password.
- Verified status in `kubectl get externalsecret app-secrets`.
