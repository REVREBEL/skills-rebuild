# Phase 08 Batch Audit Record: `batch-80-development-fullstack-part21`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-80-development-fullstack-part21`
- **Category / Subcategory**: `development` / `fullstack`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `ac35d10570efed1af46d8e229142290ba018c5dab8b754b6dfb2fb5dfa83e947`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `pr-review` | `task-folder/agents/skills/github/pr-review` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pr-workflows-onboard` | `task-folder/agents/skills/github/pr-workflows-onboard` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pr-workflows-pr-enhance` | `task-folder/agents/skills/github/pr-workflows-pr-enhance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pr-workflows-workflow` | `task-folder/agents/skills/github/pr-workflows-workflow` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pr-writer` | `task-folder/agents/skills/github/pr-writer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pre-mortem` | `task-folder/agents/skills/strategy/pre-mortem` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pre-release-review` | `task-folder/agents/skills/pre-release-review` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `product-launch-campaigns` | `task-folder/agents/skills/marketing/product-launch-campaigns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `product-manager-toolkit` | `task-folder/agents/skills/product-manager-toolkit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `product-marketing` | `task-folder/agents/skills/marketing/product-marketing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `production-scheduling` | `task-folder/agents/skills/production-scheduling` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `progressive-estimation` | `task-folder/agents/skills/progressive-estimation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `progressive-web-app` | `task-folder/agents/skills/progressive-web-app` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `prompt-engineer` | `task-folder/agents/skills/prompts/prompt-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `prompt-engineering` | `task-folder/agents/skills/prompts/prompt-engineering` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `pr-review` | User asks to work with pr review or configure pr review in fullstack. | User requests general server administration, styling, or unrelated operations outside pr review. | User asks for general assistance in fullstack without specifying pr review; routes to `pr-review` when pr review-specific capabilities are required. |
| `pr-workflows-onboard` | User asks to work with pr workflows onboard or configure pr workflows onboard in fullstack. | User requests general server administration, styling, or unrelated operations outside pr workflows onboard. | User asks for general assistance in fullstack without specifying pr workflows onboard; routes to `pr-workflows-onboard` when pr workflows onboard-specific capabilities are required. |
| `pr-workflows-pr-enhance` | User asks to work with pr workflows pr enhance or configure pr workflows pr enhance in fullstack. | User requests general server administration, styling, or unrelated operations outside pr workflows pr enhance. | User asks for general assistance in fullstack without specifying pr workflows pr enhance; routes to `pr-workflows-pr-enhance` when pr workflows pr enhance-specific capabilities are required. |
| `pr-workflows-workflow` | User asks to work with pr workflows workflow or configure pr workflows workflow in fullstack. | User requests general server administration, styling, or unrelated operations outside pr workflows workflow. | User asks for general assistance in fullstack without specifying pr workflows workflow; routes to `pr-workflows-workflow` when pr workflows workflow-specific capabilities are required. |
| `pr-writer` | User asks to create pull requests following sentry's engineering practices when executing pr writer operations or configure pr writer in fullstack. | User requests general server administration, styling, or unrelated operations outside pr writer. | User asks for general assistance in fullstack without specifying pr writer; routes to `pr-writer` when pr writer-specific capabilities are required. |
| `pre-mortem` | User asks to imagine your project has failed spectacularly—then work backward to identify why. apply gary klein's \ or configure pre mortem in fullstack. | User requests general server administration, styling, or unrelated operations outside pre mortem. | User asks for general assistance in fullstack without specifying pre mortem; routes to `pre-mortem` when pre mortem-specific capabilities are required. |
| `pre-release-review` | User asks to work with pre release review or configure pre release review in fullstack. | User requests general server administration, styling, or unrelated operations outside pre release review. | User asks for general assistance in fullstack without specifying pre release review; routes to `pre-release-review` when pre release review-specific capabilities are required. |
| `product-launch-campaigns` | User asks to work with product launch campaigns or configure product launch campaigns in fullstack. | User requests general server administration, styling, or unrelated operations outside product launch campaigns. | User asks for general assistance in fullstack without specifying product launch campaigns; routes to `product-launch-campaigns` when product launch campaigns-specific capabilities are required. |
| `product-manager-toolkit` | User asks to work with product manager toolkit or configure product manager toolkit in fullstack. | User requests general server administration, styling, or unrelated operations outside product manager toolkit. | User asks for general assistance in fullstack without specifying product manager toolkit; routes to `product-manager-toolkit` when product manager toolkit-specific capabilities are required. |
| `product-marketing` | User asks to when the user wants to create or update their product marketing context document. also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'icp,' 'ideal customer profile,' or wants to or configure product marketing in fullstack. | User requests general server administration, styling, or unrelated operations outside product marketing. | User asks for general assistance in fullstack without specifying product marketing; routes to `product-marketing` when product marketing-specific capabilities are required. |
| `production-scheduling` | User asks to work with production scheduling or configure production scheduling in fullstack. | User requests general server administration, styling, or unrelated operations outside production scheduling. | User asks for general assistance in fullstack without specifying production scheduling; routes to `production-scheduling` when production scheduling-specific capabilities are required. |
| `progressive-estimation` | User asks to work with progressive estimation or configure progressive estimation in fullstack. | User requests general server administration, styling, or unrelated operations outside progressive estimation. | User asks for general assistance in fullstack without specifying progressive estimation; routes to `progressive-estimation` when progressive estimation-specific capabilities are required. |
| `progressive-web-app` | User asks to build progressive web apps (pwas) with offline support, installability, and caching strategies. trigger whenever the user mentions pwa, service workers, web app manifests, workbox, 'add to home screen', or wants their web app to work offline, feel native, or be installable or configure progressive web app in fullstack. | User requests general server administration, styling, or unrelated operations outside progressive web app. | User asks for general assistance in fullstack without specifying progressive web app; routes to `progressive-web-app` when progressive web app-specific capabilities are required. |
| `prompt-engineer` | User asks to work with prompt engineer or configure prompt engineer in fullstack. | User requests general server administration, styling, or unrelated operations outside prompt engineer. | User asks for general assistance in fullstack without specifying prompt engineer; routes to `prompt-engineer` when prompt engineer-specific capabilities are required. |
| `prompt-engineering` | User asks to work with prompt engineering or configure prompt engineering in fullstack. | User requests general server administration, styling, or unrelated operations outside prompt engineering. | User asks for general assistance in fullstack without specifying prompt engineering; routes to `prompt-engineering` when prompt engineering-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
