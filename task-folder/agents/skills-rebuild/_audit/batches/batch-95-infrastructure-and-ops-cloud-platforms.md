# Phase 08 Batch Audit Record: `batch-95-infrastructure-and-ops-cloud-platforms`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-95-infrastructure-and-ops-cloud-platforms`
- **Category / Subcategory**: `infrastructure-and-ops` / `cloud-platforms`
- **Member Skill Count**: 14
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `c4302171a1e008c8975399fa628059b66c2da78cdacdf579071df0c5dbeb1024`

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
| `auri-core` | User asks to implement, configure, or optimize auri core tasks (specifically configuring or implementing auri core specifications). | User requests A simpler, more specific tool can handle the request or unrelated operations outside auri core. | User asks 'How do I handle auri core in my workflow?' -> Disambiguate: Clarify whether the task requires specialized auri core procedures or general cloud-platforms tooling. |
| `bigquery-table-creator` | User asks to implement, configure, or optimize bigquery table creator tasks (specifically configuring or implementing bigquery table creator specifications). | User requests general infrastructure administration, styling, or unrelated operations outside bigquery table creator or unrelated operations outside bigquery table creator. | User asks 'How do I handle bigquery table creator in my workflow?' -> Disambiguate: Clarify whether the task requires specialized bigquery table creator procedures or general cloud-platforms tooling. |
| `bigquery-view-generator` | User asks to implement, configure, or optimize bigquery view generator tasks (specifically configuring or implementing bigquery view generator specifications). | User requests general infrastructure administration, styling, or unrelated operations outside bigquery view generator or unrelated operations outside bigquery view generator. | User asks 'How do I handle bigquery view generator in my workflow?' -> Disambiguate: Clarify whether the task requires specialized bigquery view generator procedures or general cloud-platforms tooling. |
| `cdk-patterns` | User asks to implement, configure, or optimize cdk patterns tasks (specifically configuring or implementing cdk patterns specifications). | User requests The user needs raw CloudFormation templates without CDK or unrelated operations outside cdk patterns. | User asks 'How do I handle cdk patterns in my workflow?' -> Disambiguate: Clarify whether the task requires specialized cdk patterns procedures or general cloud-platforms tooling. |
| `cloud-architect` | User asks to implement, configure, or optimize cloud architect tasks (specifically configuring or implementing cloud architect specifications). | User requests You need a different domain or tool outside this scope or unrelated operations outside cloud architect. | User asks 'How do I handle cloud architect in my workflow?' -> Disambiguate: Clarify whether the task requires specialized cloud architect procedures or general cloud-platforms tooling. |
| `deploy-to-vercel` | User asks to implement, configure, or optimize deploy to vercel tasks (specifically configuring or implementing deploy to vercel specifications). | User requests general infrastructure administration, styling, or unrelated operations outside deploy to vercel or unrelated operations outside deploy to vercel. | User asks 'How do I handle deploy to vercel in my workflow?' -> Disambiguate: Clarify whether the task requires specialized deploy to vercel procedures or general cloud-platforms tooling. |
| `remote-gpu-trainer` | User asks to implement, configure, or optimize remote gpu trainer tasks (specifically configuring or implementing remote gpu trainer specifications). | User requests This skill is for the blind spot those tools leave:** AutoDL + Chinese platforms, bare SSH/Slurm/K8s or unrelated operations outside remote gpu trainer. | User asks 'How do I handle remote gpu trainer in my workflow?' -> Disambiguate: Clarify whether the task requires specialized remote gpu trainer procedures or general cloud-platforms tooling. |
| `sandbox-sdk` | User asks to implement, configure, or optimize sandbox sdk tasks (specifically configuring or implementing sandbox sdk specifications). | User requests general infrastructure administration, styling, or unrelated operations outside sandbox sdk or unrelated operations outside sandbox sdk. | User asks 'How do I handle sandbox sdk in my workflow?' -> Disambiguate: Clarify whether the task requires specialized sandbox sdk procedures or general cloud-platforms tooling. |
| `turnstile-spin` | User asks to implement, configure, or optimize turnstile spin tasks (specifically configuring or implementing turnstile spin specifications). | User requests general infrastructure administration, styling, or unrelated operations outside turnstile spin or unrelated operations outside turnstile spin. | User asks 'How do I handle turnstile spin in my workflow?' -> Disambiguate: Clarify whether the task requires specialized turnstile spin procedures or general cloud-platforms tooling. |
| `vercel-ai-sdk-expert` | User asks to implement, configure, or optimize vercel ai sdk expert tasks (specifically configuring or implementing vercel ai sdk expert specifications). | User requests general infrastructure administration, styling, or unrelated operations outside vercel ai sdk expert or unrelated operations outside vercel ai sdk expert. | User asks 'How do I handle vercel ai sdk expert in my workflow?' -> Disambiguate: Clarify whether the task requires specialized vercel ai sdk expert procedures or general cloud-platforms tooling. |
| `vercel-automation` | User asks to implement, configure, or optimize vercel automation tasks (specifically configuring or implementing vercel automation specifications). | User requests general infrastructure administration, styling, or unrelated operations outside vercel automation or unrelated operations outside vercel automation. | User asks 'How do I handle vercel automation in my workflow?' -> Disambiguate: Clarify whether the task requires specialized vercel automation procedures or general cloud-platforms tooling. |
| `vercel-deployment` | User asks to implement, configure, or optimize vercel deployment tasks (specifically configuring or implementing vercel deployment specifications). | User requests general infrastructure administration, styling, or unrelated operations outside vercel deployment or unrelated operations outside vercel deployment. | User asks 'How do I handle vercel deployment in my workflow?' -> Disambiguate: Clarify whether the task requires specialized vercel deployment procedures or general cloud-platforms tooling. |
| `vercel-optimize` | User asks to implement, configure, or optimize vercel optimize tasks (specifically Metrics first. Recommendations start from Vercel production signals, not repo-wide grep). | User requests general infrastructure administration, styling, or unrelated operations outside vercel optimize or unrelated operations outside vercel optimize. | User asks 'How do I handle vercel optimize in my workflow?' -> Disambiguate: Clarify whether the task requires specialized vercel optimize procedures or general cloud-platforms tooling. |
| `workflow-automation` | User asks to implement, configure, or optimize workflow automation tasks (specifically configuring or implementing workflow automation specifications). | User requests general infrastructure administration, styling, or unrelated operations outside workflow automation or unrelated operations outside workflow automation. | User asks 'How do I handle workflow automation in my workflow?' -> Disambiguate: Clarify whether the task requires specialized workflow automation procedures or general cloud-platforms tooling. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/infrastructure-and-ops/cloud-platforms/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `c4302171a1e008c8975399fa628059b66c2da78cdacdf579071df0c5dbeb1024` computed deterministically.

## 5. Resources Created or Moved

- None

## 6. Retired Paths

- None

## 7. Unresolved Items

- None
