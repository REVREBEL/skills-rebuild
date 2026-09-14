# Phase 08 Batch Audit Record: `batch-15-data-and-ai-analytics-part03`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-15-data-and-ai-analytics-part03`
- **Category / Subcategory**: `data-and-ai` / `analytics`
- **Member Skill Count**: 11
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `cd756efdab68d7364c830850e2a3b2be7961d63069f63a28ed73826dde54b9b8`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `posthog-automation` | `task-folder/agents/skills/posthog-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pricing-strategy` | `task-folder/agents/skills/strategy/pricing-strategy` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `product-analytics` | `task-folder/agents/skills/data-analytics/data-analytics/product-analytics` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `profit-margin-analysis` | `task-folder/agents/skills/data-analytics/data-analytics/profit-margin-analysis` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `revenue-recognition-accounting` | `task-folder/agents/skills/data-analytics/data-analytics/revenue-recognition-accounting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `segment-audience` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/segment-audience` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `segment-automation` | `task-folder/agents/skills/segment-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `segment-cdp` | `task-folder/agents/skills/segment-cdp` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `sendgrid-automation` | `task-folder/agents/skills/sendgrid-automation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `stp-framework` | `task-folder/agents/skills/strategy/stp-framework` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `unit-economics-tracking` | `task-folder/agents/skills/data-analytics/data-analytics/unit-economics-tracking` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `posthog-automation` | User asks to automate posthog tasks via rube mcp (composio): events, feature flags, projects, user profiles, annotations. always search tools first for current schemas or configure posthog automation in analytics. | User requests general server administration, styling, or unrelated operations outside posthog automation. | User asks for general assistance in analytics without specifying posthog automation; routes to `posthog-automation` when posthog automation-specific capabilities are required. |
| `pricing-strategy` | User asks to design products around price using madhavan ramanujam's \ or configure pricing strategy in analytics. | User requests general server administration, styling, or unrelated operations outside pricing strategy. | User asks for general assistance in analytics without specifying pricing strategy; routes to `pricing-strategy` when pricing strategy-specific capabilities are required. |
| `product-analytics` | User asks to work with product analytics or configure product analytics in analytics. | User requests general server administration, styling, or unrelated operations outside product analytics. | User asks for general assistance in analytics without specifying product analytics; routes to `product-analytics` when product analytics-specific capabilities are required. |
| `profit-margin-analysis` | User asks to work with profit margin analysis or configure profit margin analysis in analytics. | User requests general server administration, styling, or unrelated operations outside profit margin analysis. | User asks for general assistance in analytics without specifying profit margin analysis; routes to `profit-margin-analysis` when profit margin analysis-specific capabilities are required. |
| `revenue-recognition-accounting` | User asks to work with revenue recognition accounting or configure revenue recognition accounting in analytics. | User requests general server administration, styling, or unrelated operations outside revenue recognition accounting. | User asks for general assistance in analytics without specifying revenue recognition accounting; routes to `revenue-recognition-accounting` when revenue recognition accounting-specific capabilities are required. |
| `segment-audience` | User asks to create audience segments or configure segment audience in analytics. | User requests general server administration, styling, or unrelated operations outside segment audience. | User asks for general assistance in analytics without specifying segment audience; routes to `segment-audience` when segment audience-specific capabilities are required. |
| `segment-automation` | User asks to automate segment tasks via rube mcp (composio): track events, identify users, manage groups, page views, aliases, batch operations. always search tools first for current schemas or configure segment automation in analytics. | User requests general server administration, styling, or unrelated operations outside segment automation. | User asks for general assistance in analytics without specifying segment automation; routes to `segment-automation` when segment automation-specific capabilities are required. |
| `segment-cdp` | User asks to work with segment cdp or configure segment cdp in analytics. | User requests general server administration, styling, or unrelated operations outside segment cdp. | User asks for general assistance in analytics without specifying segment cdp; routes to `segment-cdp` when segment cdp-specific capabilities are required. |
| `sendgrid-automation` | User asks to automate sendgrid email delivery workflows including marketing campaigns (single sends), contact and list management, sender identity setup, and email analytics through composio's sendgrid toolkit when executing sendgrid automation operations or configure sendgrid automation in analytics. | User requests general server administration, styling, or unrelated operations outside sendgrid automation. | User asks for general assistance in analytics without specifying sendgrid automation; routes to `sendgrid-automation` when sendgrid automation-specific capabilities are required. |
| `stp-framework` | User asks to work with stp framework or configure stp framework in analytics. | User requests general server administration, styling, or unrelated operations outside stp framework. | User asks for general assistance in analytics without specifying stp framework; routes to `stp-framework` when stp framework-specific capabilities are required. |
| `unit-economics-tracking` | User asks to work with unit economics tracking or configure unit economics tracking in analytics. | User requests general server administration, styling, or unrelated operations outside unit economics tracking. | User asks for general assistance in analytics without specifying unit economics tracking; routes to `unit-economics-tracking` when unit economics tracking-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
