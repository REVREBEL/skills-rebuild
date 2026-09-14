# Phase 08 Batch Audit Record: `batch-95-infrastructure-and-ops-cloud-platforms`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-95-infrastructure-and-ops-cloud-platforms`
- **Category / Subcategory**: `infrastructure-and-ops` / `cloud-platforms`
- **Member Skill Count**: 14
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `625dfbb982751a288386a89ebe905d123a2bc5a0e797f3bbf5eac81883e62c80`

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
| `auri-core` | User asks to auri: assistente de voz inteligente (alexa + modelo-inteligente). visao do produto, persona vitoria neural, stack aws, modelo free/pro/business/enterprise, roadmap 4 fases, gtm, north star wac e analise competitiva when executing auri core operations or configure auri core in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside auri core. | User asks for general assistance in cloud-platforms without specifying auri core; routes to `auri-core` when auri core-specific capabilities are required. |
| `bigquery-table-creator` | User asks to work with bigquery table creator or configure bigquery table creator in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside bigquery table creator. | User asks for general assistance in cloud-platforms without specifying bigquery table creator; routes to `bigquery-table-creator` when bigquery table creator-specific capabilities are required. |
| `bigquery-view-generator` | User asks to work with bigquery view generator or configure bigquery view generator in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside bigquery view generator. | User asks for general assistance in cloud-platforms without specifying bigquery view generator; routes to `bigquery-view-generator` when bigquery view generator-specific capabilities are required. |
| `cdk-patterns` | User asks to work with cdk patterns or configure cdk patterns in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside cdk patterns. | User asks for general assistance in cloud-platforms without specifying cdk patterns; routes to `cdk-patterns` when cdk patterns-specific capabilities are required. |
| `cloud-architect` | User asks to work with cloud architect or configure cloud architect in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside cloud architect. | User asks for general assistance in cloud-platforms without specifying cloud architect; routes to `cloud-architect` when cloud architect-specific capabilities are required. |
| `deploy-to-vercel` | User asks to deploy applications and websites to vercel or configure deploy to vercel in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside deploy to vercel. | User asks for general assistance in cloud-platforms without specifying deploy to vercel; routes to `deploy-to-vercel` when deploy to vercel-specific capabilities are required. |
| `remote-gpu-trainer` | User asks to deploy, monitor, and debug long gpu jobs on rented/remote instances (autodl, runpod, vast.ai, lambda, slurm, k8s): teardown/billing safety, spot resilience, resumable checkpointing, oom/nan triage when executing remote gpu trainer operations or configure remote gpu trainer in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside remote gpu trainer. | User asks for general assistance in cloud-platforms without specifying remote gpu trainer; routes to `remote-gpu-trainer` when remote gpu trainer-specific capabilities are required. |
| `sandbox-sdk` | User asks to work with sandbox sdk or configure sandbox sdk in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside sandbox sdk. | User asks for general assistance in cloud-platforms without specifying sandbox sdk; routes to `sandbox-sdk` when sandbox sdk-specific capabilities are required. |
| `turnstile-spin` | User asks to work with turnstile spin or configure turnstile spin in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside turnstile spin. | User asks for general assistance in cloud-platforms without specifying turnstile spin; routes to `turnstile-spin` when turnstile spin-specific capabilities are required. |
| `vercel-ai-sdk-expert` | User asks to work with vercel ai sdk expert or configure vercel ai sdk expert in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside vercel ai sdk expert. | User asks for general assistance in cloud-platforms without specifying vercel ai sdk expert; routes to `vercel-ai-sdk-expert` when vercel ai sdk expert-specific capabilities are required. |
| `vercel-automation` | User asks to automate vercel tasks via rube mcp (composio): manage deployments, domains, dns, env vars, projects, and teams. always search tools first for current schemas or configure vercel automation in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside vercel automation. | User asks for general assistance in cloud-platforms without specifying vercel automation; routes to `vercel-automation` when vercel automation-specific capabilities are required. |
| `vercel-deployment` | User asks to work with vercel deployment or configure vercel deployment in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside vercel deployment. | User asks for general assistance in cloud-platforms without specifying vercel deployment; routes to `vercel-deployment` when vercel deployment-specific capabilities are required. |
| `vercel-optimize` | User asks to work with vercel optimize or configure vercel optimize in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside vercel optimize. | User asks for general assistance in cloud-platforms without specifying vercel optimize; routes to `vercel-optimize` when vercel optimize-specific capabilities are required. |
| `workflow-automation` | User asks to patterns for automating github workflows with ai assistance, inspired by [gemini cli](https://github.com/google-gemini/gemini-cli) and modern devops practices or configure workflow automation in cloud-platforms. | User requests general server administration, styling, or unrelated operations outside workflow automation. | User asks for general assistance in cloud-platforms without specifying workflow automation; routes to `workflow-automation` when workflow automation-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
