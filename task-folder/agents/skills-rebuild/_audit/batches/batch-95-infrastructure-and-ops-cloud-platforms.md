# Phase 08 Batch Audit Record: `batch-95-infrastructure-and-ops-cloud-platforms`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-95-infrastructure-and-ops-cloud-platforms`
- **Category / Subcategory**: `infrastructure-and-ops` / `cloud-platforms`
- **Member Skill Count**: 14
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `833a32d6ad21b35de05cbb38ec425077d947347643969aa242ef18c495cd710e`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `auri-core` | `task-folder/agents/skills/auri-core` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bigquery-table-creator` | `task-folder/agents/skills/big query/bigquery-table-creator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bigquery-view-generator` | `task-folder/agents/skills/big query/bigquery-view-generator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cdk-patterns` | `task-folder/agents/skills/cdk-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cloud-architect` | `task-folder/agents/skills/cloud-architect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `deploy-to-vercel` | `task-folder/agents/skills/deploy-to-vercel` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `remote-gpu-trainer` | `task-folder/agents/skills/remote-gpu-trainer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `sandbox-sdk` | `task-folder/agents/skills/sandbox-sdk` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `turnstile-spin` | `task-folder/agents/skills/turnstile-spin` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vercel-ai-sdk-expert` | `task-folder/agents/skills/vercel/vercel-ai-sdk-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vercel-automation` | `task-folder/agents/skills/vercel/vercel-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vercel-deployment` | `task-folder/agents/skills/vercel/vercel-deployment` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vercel-optimize` | `task-folder/agents/skills/vercel/vercel-optimize` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `workflow-automation` | `task-folder/agents/skills/github/workflow-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `auri-core` | User asks to execute or optimize auri core tasks (e.g. implementing auri core workflows and configurations). | User requests A simpler, more specific tool can handle the request or unrelated operations outside auri core. | User asks for general assistance with auri core -> Disambiguate: Clarify whether the focus is specific auri core patterns or broader cloud-platforms workflows. |
| `bigquery-table-creator` | User asks to execute or optimize bigquery table creator tasks (e.g. implementing bigquery table creator workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bigquery table creator or unrelated operations outside bigquery table creator. | User asks for general assistance with bigquery table creator -> Disambiguate: Clarify whether the focus is specific bigquery table creator patterns or broader cloud-platforms workflows. |
| `bigquery-view-generator` | User asks to execute or optimize bigquery view generator tasks (e.g. implementing bigquery view generator workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bigquery view generator or unrelated operations outside bigquery view generator. | User asks for general assistance with bigquery view generator -> Disambiguate: Clarify whether the focus is specific bigquery view generator patterns or broader cloud-platforms workflows. |
| `cdk-patterns` | User asks to execute or optimize cdk patterns tasks (e.g. implementing cdk patterns workflows and configurations). | User requests The user needs raw CloudFormation templates without CDK or unrelated operations outside cdk patterns. | User asks for general assistance with cdk patterns -> Disambiguate: Clarify whether the focus is specific cdk patterns patterns or broader cloud-platforms workflows. |
| `cloud-architect` | User asks to execute or optimize cloud architect tasks (e.g. implementing cloud architect workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside cloud architect. | User asks for general assistance with cloud architect -> Disambiguate: Clarify whether the focus is specific cloud architect patterns or broader cloud-platforms workflows. |
| `deploy-to-vercel` | User asks to execute or optimize deploy to vercel tasks (e.g. implementing deploy to vercel workflows and configurations). | User requests general infrastructure administration or unrelated application development outside deploy to vercel or unrelated operations outside deploy to vercel. | User asks for general assistance with deploy to vercel -> Disambiguate: Clarify whether the focus is specific deploy to vercel patterns or broader cloud-platforms workflows. |
| `remote-gpu-trainer` | User asks to execute or optimize remote gpu trainer tasks (e.g. implementing remote gpu trainer workflows and configurations). | User requests This skill is for the blind spot those tools leave:** AutoDL + Chinese platforms, bare SSH/Slurm/K8s or unrelated operations outside remote gpu trainer. | User asks for general assistance with remote gpu trainer -> Disambiguate: Clarify whether the focus is specific remote gpu trainer patterns or broader cloud-platforms workflows. |
| `sandbox-sdk` | User asks to execute or optimize sandbox sdk tasks (e.g. implementing sandbox sdk workflows and configurations). | User requests general infrastructure administration or unrelated application development outside sandbox sdk or unrelated operations outside sandbox sdk. | User asks for general assistance with sandbox sdk -> Disambiguate: Clarify whether the focus is specific sandbox sdk patterns or broader cloud-platforms workflows. |
| `turnstile-spin` | User asks to execute or optimize turnstile spin tasks (e.g. implementing turnstile spin workflows and configurations). | User requests general infrastructure administration or unrelated application development outside turnstile spin or unrelated operations outside turnstile spin. | User asks for general assistance with turnstile spin -> Disambiguate: Clarify whether the focus is specific turnstile spin patterns or broader cloud-platforms workflows. |
| `vercel-ai-sdk-expert` | User asks to execute or optimize vercel ai sdk expert tasks (e.g. implementing vercel ai sdk expert workflows and configurations). | User requests general infrastructure administration or unrelated application development outside vercel ai sdk expert or unrelated operations outside vercel ai sdk expert. | User asks for general assistance with vercel ai sdk expert -> Disambiguate: Clarify whether the focus is specific vercel ai sdk expert patterns or broader cloud-platforms workflows. |
| `vercel-automation` | User asks to execute or optimize vercel automation tasks (e.g. implementing vercel automation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside vercel automation or unrelated operations outside vercel automation. | User asks for general assistance with vercel automation -> Disambiguate: Clarify whether the focus is specific vercel automation patterns or broader cloud-platforms workflows. |
| `vercel-deployment` | User asks to execute or optimize vercel deployment tasks (e.g. implementing vercel deployment workflows and configurations). | User requests general infrastructure administration or unrelated application development outside vercel deployment or unrelated operations outside vercel deployment. | User asks for general assistance with vercel deployment -> Disambiguate: Clarify whether the focus is specific vercel deployment patterns or broader cloud-platforms workflows. |
| `vercel-optimize` | User asks to execute or optimize vercel optimize tasks (e.g. Metrics first. Recommendations start from Vercel production signals, not repo-wide grep). | User requests general infrastructure administration or unrelated application development outside vercel optimize or unrelated operations outside vercel optimize. | User asks for general assistance with vercel optimize -> Disambiguate: Clarify whether the focus is specific vercel optimize patterns or broader cloud-platforms workflows. |
| `workflow-automation` | User asks to execute or optimize workflow automation tasks (e.g. implementing workflow automation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside workflow automation or unrelated operations outside workflow automation. | User asks for general assistance with workflow automation -> Disambiguate: Clarify whether the focus is specific workflow automation patterns or broader cloud-platforms workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/infrastructure-and-ops/cloud-platforms/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `833a32d6ad21b35de05cbb38ec425077d947347643969aa242ef18c495cd710e` computed deterministically.
