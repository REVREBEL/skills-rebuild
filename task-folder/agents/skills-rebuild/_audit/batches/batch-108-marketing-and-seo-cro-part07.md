# Phase 08 Batch Audit Record: `batch-108-marketing-and-seo-cro-part07`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-108-marketing-and-seo-cro-part07`
- **Category / Subcategory**: `marketing-and-seo` / `cro`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `8f58e9710b13d6d51ebcaf59ea698bcbf39f2095640050259beb685a71c0340b`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `event-briefs` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/event-marketing/skills/event-briefs` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `expansion-playbook` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/account-management/skills/expansion-playbook` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `expansion-plays` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/customer-marketing/skills/expansion-plays` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `experience-map` | `task-folder/agents/skills/design/designer-skills-main/ux-strategy/skills/experience-map` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `fastapi-pro` | `task-folder/agents/skills/fastapi-pro` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `feature-tracking` | `task-folder/agents/skills/github/feature-tracking` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `fixing-motion-performance` | `task-folder/agents/skills/fixing-motion-performance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `form-cro` | `task-folder/agents/skills/form-cro` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `frontend-mobile-security-xss-scan` | `task-folder/agents/skills/front end/frontend-mobile-security-xss-scan` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `funnel-architect` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/funnel-architect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `funnel-audit` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/funnel-audit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `global-chat-agent-discovery` | `task-folder/agents/skills/github/global-chat-agent-discovery` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `golang-pro` | `task-folder/agents/skills/golang-pro` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `gpt-tasteskill` | `task-folder/agents/skills/design/gpt-tasteskill` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `guardrail-scorecard` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/growth-experiments/skills/guardrail-scorecard` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `event-briefs` | User asks to work with event briefs or configure event briefs in cro. | User requests general server administration, styling, or unrelated operations outside event briefs. | User asks for general assistance in cro without specifying event briefs; routes to `event-briefs` when event briefs-specific capabilities are required. |
| `expansion-playbook` | User asks to work with expansion playbook or configure expansion playbook in cro. | User requests general server administration, styling, or unrelated operations outside expansion playbook. | User asks for general assistance in cro without specifying expansion playbook; routes to `expansion-playbook` when expansion playbook-specific capabilities are required. |
| `expansion-plays` | User asks to work with expansion plays or configure expansion plays in cro. | User requests general server administration, styling, or unrelated operations outside expansion plays. | User asks for general assistance in cro without specifying expansion plays; routes to `expansion-plays` when expansion plays-specific capabilities are required. |
| `experience-map` | User asks to work with experience map or configure experience map in cro. | User requests general server administration, styling, or unrelated operations outside experience map. | User asks for general assistance in cro without specifying experience map; routes to `experience-map` when experience map-specific capabilities are required. |
| `fastapi-pro` | User asks to work with fastapi pro or configure fastapi pro in cro. | User requests general server administration, styling, or unrelated operations outside fastapi pro. | User asks for general assistance in cro without specifying fastapi pro; routes to `fastapi-pro` when fastapi pro-specific capabilities are required. |
| `feature-tracking` | User asks to work with feature tracking or configure feature tracking in cro. | User requests general server administration, styling, or unrelated operations outside feature tracking. | User asks for general assistance in cro without specifying feature tracking; routes to `feature-tracking` when feature tracking-specific capabilities are required. |
| `fixing-motion-performance` | User asks to work with fixing motion performance or configure fixing motion performance in cro. | User requests general server administration, styling, or unrelated operations outside fixing motion performance. | User asks for general assistance in cro without specifying fixing motion performance; routes to `fixing-motion-performance` when fixing motion performance-specific capabilities are required. |
| `form-cro` | User asks to work with form cro or configure form cro in cro. | User requests general server administration, styling, or unrelated operations outside form cro. | User asks for general assistance in cro without specifying form cro; routes to `form-cro` when form cro-specific capabilities are required. |
| `frontend-mobile-security-xss-scan` | User asks to work with frontend mobile security xss scan or configure frontend mobile security xss scan in cro. | User requests general server administration, styling, or unrelated operations outside frontend mobile security xss scan. | User asks for general assistance in cro without specifying frontend mobile security xss scan; routes to `frontend-mobile-security-xss-scan` when frontend mobile security xss scan-specific capabilities are required. |
| `funnel-architect` | User asks to design marketing funnels or configure funnel architect in cro. | User requests general server administration, styling, or unrelated operations outside funnel architect. | User asks for general assistance in cro without specifying funnel architect; routes to `funnel-architect` when funnel architect-specific capabilities are required. |
| `funnel-audit` | User asks to audit funnel performance or configure funnel audit in cro. | User requests general server administration, styling, or unrelated operations outside funnel audit. | User asks for general assistance in cro without specifying funnel audit; routes to `funnel-audit` when funnel audit-specific capabilities are required. |
| `global-chat-agent-discovery` | User asks to discover and search 18k+ mcp servers and ai agents across 6+ registries using global chat's cross-protocol directory and mcp server when executing global chat agent discovery operations or configure global chat agent discovery in cro. | User requests general server administration, styling, or unrelated operations outside global chat agent discovery. | User asks for general assistance in cro without specifying global chat agent discovery; routes to `global-chat-agent-discovery` when global chat agent discovery-specific capabilities are required. |
| `golang-pro` | User asks to work with golang pro or configure golang pro in cro. | User requests general server administration, styling, or unrelated operations outside golang pro. | User asks for general assistance in cro without specifying golang pro; routes to `golang-pro` when golang pro-specific capabilities are required. |
| `gpt-tasteskill` | User asks to work with gpt tasteskill or configure gpt tasteskill in cro. | User requests general server administration, styling, or unrelated operations outside gpt tasteskill. | User asks for general assistance in cro without specifying gpt tasteskill; routes to `gpt-tasteskill` when gpt tasteskill-specific capabilities are required. |
| `guardrail-scorecard` | User asks to work with guardrail scorecard or configure guardrail scorecard in cro. | User requests general server administration, styling, or unrelated operations outside guardrail scorecard. | User asks for general assistance in cro without specifying guardrail scorecard; routes to `guardrail-scorecard` when guardrail scorecard-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
