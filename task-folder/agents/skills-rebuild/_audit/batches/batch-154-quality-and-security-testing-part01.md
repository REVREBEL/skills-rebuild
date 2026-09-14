# Phase 08 Batch Audit Record: `batch-154-quality-and-security-testing-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-154-quality-and-security-testing-part01`
- **Category / Subcategory**: `quality-and-security` / `testing`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `9e6ece9bece271c307eb771bd03522a4adb68a7d500101688c37d3a309cf2a65`

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
| `ab-testing` | User asks to when the user wants to plan, design, or implement an a/b test or experiment, or build a growth experimentation program. also use when the user mentions or configure ab testing in testing. | User requests general server administration, styling, or unrelated operations outside ab testing. | User asks for general assistance in testing without specifying ab testing; routes to `ab-testing` when ab testing-specific capabilities are required. |
| `ab-testing-ecommerce` | User asks to work with ab testing ecommerce or configure ab testing ecommerce in testing. | User requests general server administration, styling, or unrelated operations outside ab testing ecommerce. | User asks for general assistance in testing without specifying ab testing ecommerce; routes to `ab-testing-ecommerce` when ab testing ecommerce-specific capabilities are required. |
| `actions-templates` | User asks to work with actions templates or configure actions templates in testing. | User requests general server administration, styling, or unrelated operations outside actions templates. | User asks for general assistance in testing without specifying actions templates; routes to `actions-templates` when actions templates-specific capabilities are required. |
| `agent-evaluation` | User asks to work with agent evaluation or configure agent evaluation in testing. | User requests general server administration, styling, or unrelated operations outside agent evaluation. | User asks for general assistance in testing without specifying agent evaluation; routes to `agent-evaluation` when agent evaluation-specific capabilities are required. |
| `agentic-eval` | User asks to work with agentic eval or configure agentic eval in testing. | User requests general server administration, styling, or unrelated operations outside agentic eval. | User asks for general assistance in testing without specifying agentic eval; routes to `agentic-eval` when agentic eval-specific capabilities are required. |
| `api-testing-observability-api-mock` | User asks to work with api testing observability api mock or configure api testing observability api mock in testing. | User requests general server administration, styling, or unrelated operations outside api testing observability api mock. | User asks for general assistance in testing without specifying api testing observability api mock; routes to `api-testing-observability-api-mock` when api testing observability api mock-specific capabilities are required. |
| `backtesting-frameworks` | User asks to work with backtesting frameworks or configure backtesting frameworks in testing. | User requests general server administration, styling, or unrelated operations outside backtesting frameworks. | User asks for general assistance in testing without specifying backtesting frameworks; routes to `backtesting-frameworks` when backtesting frameworks-specific capabilities are required. |
| `bash-scripting` | User asks to work with bash scripting or configure bash scripting in testing. | User requests general server administration, styling, or unrelated operations outside bash scripting. | User asks for general assistance in testing without specifying bash scripting; routes to `bash-scripting` when bash scripting-specific capabilities are required. |
| `browser-automation` | User asks to work with browser automation or configure browser automation in testing. | User requests general server administration, styling, or unrelated operations outside browser automation. | User asks for general assistance in testing without specifying browser automation; routes to `browser-automation` when browser automation-specific capabilities are required. |
| `browser-testing-with-devtools` | User asks to work with browser testing with devtools or configure browser testing with devtools in testing. | User requests general server administration, styling, or unrelated operations outside browser testing with devtools. | User asks for general assistance in testing without specifying browser testing with devtools; routes to `browser-testing-with-devtools` when browser testing with devtools-specific capabilities are required. |
| `code-showcase-testing-patterns` | User asks to work with code showcase testing patterns or configure code showcase testing patterns in testing. | User requests general server administration, styling, or unrelated operations outside code showcase testing patterns. | User asks for general assistance in testing without specifying code showcase testing patterns; routes to `code-showcase-testing-patterns` when code showcase testing patterns-specific capabilities are required. |
| `data-engineering-data-driven-feature` | User asks to work with data engineering data driven feature or configure data engineering data driven feature in testing. | User requests general server administration, styling, or unrelated operations outside data engineering data driven feature. | User asks for general assistance in testing without specifying data engineering data driven feature; routes to `data-engineering-data-driven-feature` when data engineering data driven feature-specific capabilities are required. |
| `dbt-transformation-patterns` | User asks to work with dbt transformation patterns or configure dbt transformation patterns in testing. | User requests general server administration, styling, or unrelated operations outside dbt transformation patterns. | User asks for general assistance in testing without specifying dbt transformation patterns; routes to `dbt-transformation-patterns` when dbt transformation patterns-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
