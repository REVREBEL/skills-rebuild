# Phase 08 Batch Audit Record: `batch-105-marketing-and-seo-cro-part04`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-105-marketing-and-seo-cro-part04`
- **Category / Subcategory**: `marketing-and-seo` / `cro`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `d249d135493c232173299ede16d3dcf26fd09ea4189fa7ff41d9de5c74a4ca39`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `content-repurposing` | `task-folder/agents/skills/marketing/content-repurposing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `content-writing` | `task-folder/agents/skills/seo/seo-skills-main/automation/content/content-writing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `conversion-copywriting` | `task-folder/agents/skills/seo/seo-skills-main/automation/content/conversion-copywriting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `conversion-diagnostic-kit` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/e-commerce/skills/conversion-diagnostic-kit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `conversion-rate-optimization` | `task-folder/agents/skills/marketing/conversion-rate-optimization` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `copywriting-classic` | `task-folder/agents/skills/seo/seo-skills-main/automation/content/copywriting-classic` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cost-allocation-analysis` | `task-folder/agents/skills/data-analytics/data-analytics/cost-allocation-analysis` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cost-optimization` | `task-folder/agents/skills/cost-optimization` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cowork-setup` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/cowork-setup` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `creative-testing-framework` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/creative-testing-framework` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `creative-variants` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/paid-media/skills/creative-variants` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `crm-hygiene` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/sales-pipeline/skills/crm-hygiene` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cro` | `task-folder/agents/skills/cro` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cron-doctor` | `task-folder/agents/skills/cron-doctor` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cross-sell-upsell-engine` | `task-folder/agents/skills/marketing/cross-sell-upsell-engine` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `content-repurposing` | User asks to repurpose and atomize content across platforms and formats or configure content repurposing in cro. | User requests general server administration, styling, or unrelated operations outside content repurposing. | User asks for general assistance in cro without specifying content repurposing; routes to `content-repurposing` when content repurposing-specific capabilities are required. |
| `content-writing` | User asks to create ridiculously good content using ann handley's \ or configure content writing in cro. | User requests general server administration, styling, or unrelated operations outside content writing. | User asks for general assistance in cro without specifying content writing; routes to `content-writing` when content writing-specific capabilities are required. |
| `conversion-copywriting` | User asks to write copy that gets a \ or configure conversion copywriting in cro. | User requests general server administration, styling, or unrelated operations outside conversion copywriting. | User asks for general assistance in cro without specifying conversion copywriting; routes to `conversion-copywriting` when conversion copywriting-specific capabilities are required. |
| `conversion-diagnostic-kit` | User asks to work with conversion diagnostic kit or configure conversion diagnostic kit in cro. | User requests general server administration, styling, or unrelated operations outside conversion diagnostic kit. | User asks for general assistance in cro without specifying conversion diagnostic kit; routes to `conversion-diagnostic-kit` when conversion diagnostic kit-specific capabilities are required. |
| `conversion-rate-optimization` | User asks to systematically improve your store's revenue per visitor by auditing checkout drop-off, running heatmaps, and implementing cro best practices when executing conversion rate optimization operations or configure conversion rate optimization in cro. | User requests general server administration, styling, or unrelated operations outside conversion rate optimization. | User asks for general assistance in cro without specifying conversion rate optimization; routes to `conversion-rate-optimization` when conversion rate optimization-specific capabilities are required. |
| `copywriting-classic` | User asks to master david ogilvy's timeless advertising principles from \ or configure copywriting classic in cro. | User requests general server administration, styling, or unrelated operations outside copywriting classic. | User asks for general assistance in cro without specifying copywriting classic; routes to `copywriting-classic` when copywriting classic-specific capabilities are required. |
| `cost-allocation-analysis` | User asks to work with cost allocation analysis or configure cost allocation analysis in cro. | User requests general server administration, styling, or unrelated operations outside cost allocation analysis. | User asks for general assistance in cro without specifying cost allocation analysis; routes to `cost-allocation-analysis` when cost allocation analysis-specific capabilities are required. |
| `cost-optimization` | User asks to work with cost optimization or configure cost optimization in cro. | User requests general server administration, styling, or unrelated operations outside cost optimization. | User asks for general assistance in cro without specifying cost optimization; routes to `cost-optimization` when cost optimization-specific capabilities are required. |
| `cowork-setup` | User asks to one-shot setup that wires digital marketing pro for team usage in anthropic cowork. verifies the cowork sandbox, checks for a google drive integration, creates the canonical drive folder layout, and confirms team-ready brand-state routing. use this the first time a cowork user installs dmp or when brand profiles aren't persisting across sessions or configure cowork setup in cro. | User requests general server administration, styling, or unrelated operations outside cowork setup. | User asks for general assistance in cro without specifying cowork setup; routes to `cowork-setup` when cowork setup-specific capabilities are required. |
| `creative-testing-framework` | User asks to work with creative testing framework or configure creative testing framework in cro. | User requests general server administration, styling, or unrelated operations outside creative testing framework. | User asks for general assistance in cro without specifying creative testing framework; routes to `creative-testing-framework` when creative testing framework-specific capabilities are required. |
| `creative-variants` | User asks to work with creative variants or configure creative variants in cro. | User requests general server administration, styling, or unrelated operations outside creative variants. | User asks for general assistance in cro without specifying creative variants; routes to `creative-variants` when creative variants-specific capabilities are required. |
| `crm-hygiene` | User asks to work with crm hygiene or configure crm hygiene in cro. | User requests general server administration, styling, or unrelated operations outside crm hygiene. | User asks for general assistance in cro without specifying crm hygiene; routes to `crm-hygiene` when crm hygiene-specific capabilities are required. |
| `cro` | User asks to when the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pages, lead capture forms, or contact forms. also use when the user says 'cro,' 'conversion rate optimization,' 'this page isn't or configure cro in cro. | User requests general server administration, styling, or unrelated operations outside cro. | User asks for general assistance in cro without specifying cro; routes to `cro` when cro-specific capabilities are required. |
| `cron-doctor` | User asks to diagnose and validate cron expressions before they ship. catches the five silent death-traps: impossible dates that never fire, or-semantics that fire too often, midnight spikes, uneven step drift, and leap-year february 29 or configure cron doctor in cro. | User requests general server administration, styling, or unrelated operations outside cron doctor. | User asks for general assistance in cro without specifying cron doctor; routes to `cron-doctor` when cron doctor-specific capabilities are required. |
| `cross-sell-upsell-engine` | User asks to work with cross sell upsell engine or configure cross sell upsell engine in cro. | User requests general server administration, styling, or unrelated operations outside cross sell upsell engine. | User asks for general assistance in cro without specifying cross sell upsell engine; routes to `cross-sell-upsell-engine` when cross sell upsell engine-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
