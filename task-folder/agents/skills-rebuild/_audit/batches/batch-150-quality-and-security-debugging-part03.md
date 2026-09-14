# Phase 08 Batch Audit Record: `batch-150-quality-and-security-debugging-part03`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-150-quality-and-security-debugging-part03`
- **Category / Subcategory**: `quality-and-security` / `debugging`
- **Member Skill Count**: 12
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `24d7e617056309e715c71d36cb18aca3dcb316700a807648ad999a83b24ca877`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `first-party-data-collection` | `task-folder/agents/skills/marketing/first-party-data-collection` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `huggingface-spaces` | `task-folder/agents/skills/hugging face/huggingface-spaces` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `incident-response-smart-fix` | `task-folder/agents/skills/incident-response-smart-fix` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `langfuse` | `task-folder/agents/skills/langfuse` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `linux-troubleshooting` | `task-folder/agents/skills/linux/linux-troubleshooting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `manifest` | `task-folder/agents/skills/manifest` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-code-javascript` | `task-folder/agents/skills/n8n/n8n-code-javascript` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-expression-syntax` | `task-folder/agents/skills/n8n/n8n-expression-syntax` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `os-scripting` | `task-folder/agents/skills/os-scripting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `performance-optimization` | `task-folder/agents/skills/performance/performance-optimization` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `performance-profiling` | `task-folder/agents/skills/performance/performance-profiling` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `phase-gated-debugging` | `task-folder/agents/skills/phase-gated-debugging` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `first-party-data-collection` | User asks to work with first party data collection or configure first party data collection in debugging. | User requests general server administration, styling, or unrelated operations outside first party data collection. | User asks for general assistance in debugging without specifying first party data collection; routes to `first-party-data-collection` when first party data collection-specific capabilities are required. |
| `huggingface-spaces` | User asks to work with huggingface spaces or configure huggingface spaces in debugging. | User requests general server administration, styling, or unrelated operations outside huggingface spaces. | User asks for general assistance in debugging without specifying huggingface spaces; routes to `huggingface-spaces` when huggingface spaces-specific capabilities are required. |
| `incident-response-smart-fix` | User asks to [extended thinking: this workflow implements a sophisticated debugging and resolution pipeline that leverages ai-assisted debugging tools and observability platforms to systematically diagnose and res or configure incident response smart fix in debugging. | User requests general server administration, styling, or unrelated operations outside incident response smart fix. | User asks for general assistance in debugging without specifying incident response smart fix; routes to `incident-response-smart-fix` when incident response smart fix-specific capabilities are required. |
| `langfuse` | User asks to work with langfuse or configure langfuse in debugging. | User requests general server administration, styling, or unrelated operations outside langfuse. | User asks for general assistance in debugging without specifying langfuse; routes to `langfuse` when langfuse-specific capabilities are required. |
| `linux-troubleshooting` | User asks to work with linux troubleshooting or configure linux troubleshooting in debugging. | User requests general server administration, styling, or unrelated operations outside linux troubleshooting. | User asks for general assistance in debugging without specifying linux troubleshooting; routes to `linux-troubleshooting` when linux troubleshooting-specific capabilities are required. |
| `manifest` | User asks to work with manifest or configure manifest in debugging. | User requests general server administration, styling, or unrelated operations outside manifest. | User asks for general assistance in debugging without specifying manifest; routes to `manifest` when manifest-specific capabilities are required. |
| `n8n-code-javascript` | User asks to work with n8n code javascript or configure n8n code javascript in debugging. | User requests general server administration, styling, or unrelated operations outside n8n code javascript. | User asks for general assistance in debugging without specifying n8n code javascript; routes to `n8n-code-javascript` when n8n code javascript-specific capabilities are required. |
| `n8n-expression-syntax` | User asks to work with n8n expression syntax or configure n8n expression syntax in debugging. | User requests general server administration, styling, or unrelated operations outside n8n expression syntax. | User asks for general assistance in debugging without specifying n8n expression syntax; routes to `n8n-expression-syntax` when n8n expression syntax-specific capabilities are required. |
| `os-scripting` | User asks to work with os scripting or configure os scripting in debugging. | User requests general server administration, styling, or unrelated operations outside os scripting. | User asks for general assistance in debugging without specifying os scripting; routes to `os-scripting` when os scripting-specific capabilities are required. |
| `performance-optimization` | User asks to work with performance optimization or configure performance optimization in debugging. | User requests general server administration, styling, or unrelated operations outside performance optimization. | User asks for general assistance in debugging without specifying performance optimization; routes to `performance-optimization` when performance optimization-specific capabilities are required. |
| `performance-profiling` | User asks to work with performance profiling or configure performance profiling in debugging. | User requests general server administration, styling, or unrelated operations outside performance profiling. | User asks for general assistance in debugging without specifying performance profiling; routes to `performance-profiling` when performance profiling-specific capabilities are required. |
| `phase-gated-debugging` | User asks to work with phase gated debugging or configure phase gated debugging in debugging. | User requests general server administration, styling, or unrelated operations outside phase gated debugging. | User asks for general assistance in debugging without specifying phase gated debugging; routes to `phase-gated-debugging` when phase gated debugging-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
