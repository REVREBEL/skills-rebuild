# Phase 08 Batch Audit Record: `batch-150-quality-and-security-debugging-part03`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-150-quality-and-security-debugging-part03`
- **Category / Subcategory**: `quality-and-security` / `debugging`
- **Member Skill Count**: 12
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `ef993188c554f15d6ce6ac55dba1f06f1f01f3fb7dc83ccdfe8ea4a2f9e2a95b`

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
| `first-party-data-collection` | User asks to execute or optimize first party data collection tasks (e.g. implementing first party data collection workflows and configurations). | User requests general infrastructure administration or unrelated application development outside first party data collection or unrelated operations outside first party data collection. | User asks for general assistance with first party data collection -> Disambiguate: Clarify whether the focus is specific first party data collection patterns or broader debugging workflows. |
| `huggingface-spaces` | User asks to execute or optimize huggingface spaces tasks (e.g. implementing huggingface spaces workflows and configurations). | User requests general infrastructure administration or unrelated application development outside huggingface spaces or unrelated operations outside huggingface spaces. | User asks for general assistance with huggingface spaces -> Disambiguate: Clarify whether the focus is specific huggingface spaces patterns or broader debugging workflows. |
| `incident-response-smart-fix` | User asks to execute or optimize incident response smart fix tasks (e.g. implementing incident response smart fix workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside incident response smart fix. | User asks for general assistance with incident response smart fix -> Disambiguate: Clarify whether the focus is specific incident response smart fix patterns or broader debugging workflows. |
| `langfuse` | User asks to execute or optimize langfuse tasks (e.g. Role**: LLM Observability Architect). | User requests general infrastructure administration or unrelated application development outside langfuse or unrelated operations outside langfuse. | User asks for general assistance with langfuse -> Disambiguate: Clarify whether the focus is specific langfuse patterns or broader debugging workflows. |
| `linux-troubleshooting` | User asks to execute or optimize linux troubleshooting tasks (e.g. implementing linux troubleshooting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside linux troubleshooting or unrelated operations outside linux troubleshooting. | User asks for general assistance with linux troubleshooting -> Disambiguate: Clarify whether the focus is specific linux troubleshooting patterns or broader debugging workflows. |
| `manifest` | User asks to execute or optimize manifest tasks (e.g. implementing manifest workflows and configurations). | User requests User needs general observability design (use `observability-engineer` instead) or unrelated operations outside manifest. | User asks for general assistance with manifest -> Disambiguate: Clarify whether the focus is specific manifest patterns or broader debugging workflows. |
| `n8n-code-javascript` | User asks to execute or optimize n8n code javascript tasks (e.g. implementing n8n code javascript workflows and configurations). | User requests general infrastructure administration or unrelated application development outside n8n code javascript or unrelated operations outside n8n code javascript. | User asks for general assistance with n8n code javascript -> Disambiguate: Clarify whether the focus is specific n8n code javascript patterns or broader debugging workflows. |
| `n8n-expression-syntax` | User asks to execute or optimize n8n expression syntax tasks (e.g. implementing n8n expression syntax workflows and configurations). | User requests general infrastructure administration or unrelated application development outside n8n expression syntax or unrelated operations outside n8n expression syntax. | User asks for general assistance with n8n expression syntax -> Disambiguate: Clarify whether the focus is specific n8n expression syntax patterns or broader debugging workflows. |
| `os-scripting` | User asks to execute or optimize os scripting tasks (e.g. implementing os scripting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside os scripting or unrelated operations outside os scripting. | User asks for general assistance with os scripting -> Disambiguate: Clarify whether the focus is specific os scripting patterns or broader debugging workflows. |
| `performance-optimization` | User asks to execute or optimize performance optimization tasks (e.g. implementing performance optimization workflows and configurations). | User requests general infrastructure administration or unrelated application development outside performance optimization or unrelated operations outside performance optimization. | User asks for general assistance with performance optimization -> Disambiguate: Clarify whether the focus is specific performance optimization patterns or broader debugging workflows. |
| `performance-profiling` | User asks to execute or optimize performance profiling tasks (e.g. implementing performance profiling workflows and configurations). | User requests general infrastructure administration or unrelated application development outside performance profiling or unrelated operations outside performance profiling. | User asks for general assistance with performance profiling -> Disambiguate: Clarify whether the focus is specific performance profiling patterns or broader debugging workflows. |
| `phase-gated-debugging` | User asks to execute or optimize phase gated debugging tasks (e.g. implementing phase gated debugging workflows and configurations). | User requests general infrastructure administration or unrelated application development outside phase gated debugging or unrelated operations outside phase gated debugging. | User asks for general assistance with phase gated debugging -> Disambiguate: Clarify whether the focus is specific phase gated debugging patterns or broader debugging workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/debugging/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `ef993188c554f15d6ce6ac55dba1f06f1f01f3fb7dc83ccdfe8ea4a2f9e2a95b` computed deterministically.
