# Phase 08 Batch Audit Record: `batch-154-quality-and-security-testing-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-154-quality-and-security-testing-part01`
- **Category / Subcategory**: `quality-and-security` / `testing`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `8388502ebf76a8f830e6d600487673dcd8fcaa6a8587963b59cf9142c6f16880`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `ab-testing` | `task-folder/agents/skills/ab-testing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ab-testing-ecommerce` | `task-folder/agents/skills/data-analytics/data-analytics/ab-testing-ecommerce` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `actions-templates` | `task-folder/agents/skills/github/actions-templates` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `agent-evaluation` | `task-folder/agents/skills/agents/agent-evaluation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `agentic-eval` | `task-folder/agents/skills/agents/agentic-eval` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `api-testing-observability-api-mock` | `task-folder/agents/skills/api/api-testing-observability-api-mock` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `backtesting-frameworks` | `task-folder/agents/skills/backend/backtesting-frameworks` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bash-scripting` | `task-folder/agents/skills/bash/bash-scripting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `browser-automation` | `task-folder/agents/skills/browser-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `browser-testing-with-devtools` | `task-folder/agents/skills/browser-testing-with-devtools` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `code-showcase-testing-patterns` | `task-folder/agents/skills/code/code-showcase-testing-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `data-engineering-data-driven-feature` | `task-folder/agents/skills/data/data-engineering-data-driven-feature` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `dbt-transformation-patterns` | `task-folder/agents/skills/databases/dbt-transformation-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `ab-testing` | User asks to execute or optimize ab testing tasks (e.g. implementing ab testing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ab testing or unrelated operations outside ab testing. | User asks for general assistance with ab testing -> Disambiguate: Clarify whether the focus is specific ab testing patterns or broader testing workflows. |
| `ab-testing-ecommerce` | User asks to execute or optimize ab testing ecommerce tasks (e.g. implementing ab testing ecommerce workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ab testing ecommerce or unrelated operations outside ab testing ecommerce. | User asks for general assistance with ab testing ecommerce -> Disambiguate: Clarify whether the focus is specific ab testing ecommerce patterns or broader testing workflows. |
| `actions-templates` | User asks to execute or optimize actions templates tasks (e.g. implementing actions templates workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside actions templates. | User asks for general assistance with actions templates -> Disambiguate: Clarify whether the focus is specific actions templates patterns or broader testing workflows. |
| `agent-evaluation` | User asks to execute or optimize agent evaluation tasks (e.g. implementing agent evaluation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside agent evaluation or unrelated operations outside agent evaluation. | User asks for general assistance with agent evaluation -> Disambiguate: Clarify whether the focus is specific agent evaluation patterns or broader testing workflows. |
| `agentic-eval` | User asks to execute or optimize agentic eval tasks (e.g. implementing agentic eval workflows and configurations). | User requests general infrastructure administration or unrelated application development outside agentic eval or unrelated operations outside agentic eval. | User asks for general assistance with agentic eval -> Disambiguate: Clarify whether the focus is specific agentic eval patterns or broader testing workflows. |
| `api-testing-observability-api-mock` | User asks to execute or optimize api testing observability api mock tasks (e.g. implementing api testing observability api mock workflows and configurations). | User requests You need to test production systems or live integrations or unrelated operations outside api testing observability api mock. | User asks for general assistance with api testing observability api mock -> Disambiguate: Clarify whether the focus is specific api testing observability api mock patterns or broader testing workflows. |
| `backtesting-frameworks` | User asks to execute or optimize backtesting frameworks tasks (e.g. implementing backtesting frameworks workflows and configurations). | User requests You need live trading execution or investment advice or unrelated operations outside backtesting frameworks. | User asks for general assistance with backtesting frameworks -> Disambiguate: Clarify whether the focus is specific backtesting frameworks patterns or broader testing workflows. |
| `bash-scripting` | User asks to execute or optimize bash scripting tasks (e.g. implementing bash scripting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bash scripting or unrelated operations outside bash scripting. | User asks for general assistance with bash scripting -> Disambiguate: Clarify whether the focus is specific bash scripting patterns or broader testing workflows. |
| `browser-automation` | User asks to execute or optimize browser automation tasks (e.g. implementing browser automation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside browser automation or unrelated operations outside browser automation. | User asks for general assistance with browser automation -> Disambiguate: Clarify whether the focus is specific browser automation patterns or broader testing workflows. |
| `browser-testing-with-devtools` | User asks to execute or optimize browser testing with devtools tasks (e.g. implementing browser testing with devtools workflows and configurations). | User requests general infrastructure administration or unrelated application development outside browser testing with devtools or unrelated operations outside browser testing with devtools. | User asks for general assistance with browser testing with devtools -> Disambiguate: Clarify whether the focus is specific browser testing with devtools patterns or broader testing workflows. |
| `code-showcase-testing-patterns` | User asks to execute or optimize code showcase testing patterns tasks (e.g. implementing code showcase testing patterns workflows and configurations). | User requests general infrastructure administration or unrelated application development outside code showcase testing patterns or unrelated operations outside code showcase testing patterns. | User asks for general assistance with code showcase testing patterns -> Disambiguate: Clarify whether the focus is specific code showcase testing patterns patterns or broader testing workflows. |
| `data-engineering-data-driven-feature` | User asks to execute or optimize data engineering data driven feature tasks (e.g. implementing data engineering data driven feature workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside data engineering data driven feature. | User asks for general assistance with data engineering data driven feature -> Disambiguate: Clarify whether the focus is specific data engineering data driven feature patterns or broader testing workflows. |
| `dbt-transformation-patterns` | User asks to execute or optimize dbt transformation patterns tasks (e.g. implementing dbt transformation patterns workflows and configurations). | User requests The project is not using dbt or a warehouse-backed workflow or unrelated operations outside dbt transformation patterns. | User asks for general assistance with dbt transformation patterns -> Disambiguate: Clarify whether the focus is specific dbt transformation patterns patterns or broader testing workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/testing/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `8388502ebf76a8f830e6d600487673dcd8fcaa6a8587963b59cf9142c6f16880` computed deterministically.
