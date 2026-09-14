# Phase 08 Batch Audit Record: `batch-99-marketing-and-seo-content-and-campaigns-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-99-marketing-and-seo-content-and-campaigns-part01`
- **Category / Subcategory**: `marketing-and-seo` / `content-and-campaigns`
- **Member Skill Count**: 12
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `c27eb9b0d42856df79b25152615e2f925d2b12ef22edc9c843170bb308f00429`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `ad-creative` | `task-folder/agents/skills/ads/ad-creative` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `brand-guardrails` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/social-scheduler-orchestration/skills/brand-guardrails` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `brand-voice-analyzer` | `task-folder/agents/skills/design/designer/clean-gemini-agents/gemini-agents/skills/branding/brand-voice-analyzer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `channel-roadmap-kit` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/social-media-marketing/skills/channel-roadmap-kit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cold-outreach` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/sales-prospecting/skills/cold-outreach` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `community-engagement` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/social-media/skills/community-engagement` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `competitor-alerts` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/competitor-alerts` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `content-calendar` | `task-folder/agents/skills/marketing/content-calendar` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `content-creator` | `task-folder/agents/skills/content/content-creator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `content-repurposer` | `task-folder/agents/skills/seo/seo-skills-main/automation/content-repurposer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `creative-health` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/creative-health` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `creative-iteration-playbook` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/social-media-marketing/skills/creative-iteration-playbook` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `ad-creative` | User asks to work with ad creative or configure ad creative in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside ad creative. | User asks for general assistance in content-and-campaigns without specifying ad creative; routes to `ad-creative` when ad creative-specific capabilities are required. |
| `brand-guardrails` | User asks to work with brand guardrails or configure brand guardrails in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside brand guardrails. | User asks for general assistance in content-and-campaigns without specifying brand guardrails; routes to `brand-guardrails` when brand guardrails-specific capabilities are required. |
| `brand-voice-analyzer` | User asks to analyzes a company's content to extract and codify their brand voice into a comprehensive style guide. reads website copy, blog posts, emails, and social media to identify tone, vocabulary patterns, sentence structure, personality traits, and word preferences. generates a brand-voice-guide.md and reviews new content against it when executing brand voice analyzer operations or configure brand voice analyzer in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside brand voice analyzer. | User asks for general assistance in content-and-campaigns without specifying brand voice analyzer; routes to `brand-voice-analyzer` when brand voice analyzer-specific capabilities are required. |
| `channel-roadmap-kit` | User asks to work with channel roadmap kit or configure channel roadmap kit in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside channel roadmap kit. | User asks for general assistance in content-and-campaigns without specifying channel roadmap kit; routes to `channel-roadmap-kit` when channel roadmap kit-specific capabilities are required. |
| `cold-outreach` | User asks to work with cold outreach or configure cold outreach in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside cold outreach. | User asks for general assistance in content-and-campaigns without specifying cold outreach; routes to `cold-outreach` when cold outreach-specific capabilities are required. |
| `community-engagement` | User asks to work with community engagement or configure community engagement in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside community engagement. | User asks for general assistance in content-and-campaigns without specifying community engagement; routes to `community-engagement` when community engagement-specific capabilities are required. |
| `competitor-alerts` | User asks to configure competitor alerts or configure competitor alerts in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside competitor alerts. | User asks for general assistance in content-and-campaigns without specifying competitor alerts; routes to `competitor-alerts` when competitor alerts-specific capabilities are required. |
| `content-calendar` | User asks to work with content calendar or configure content calendar in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside content calendar. | User asks for general assistance in content-and-campaigns without specifying content calendar; routes to `content-calendar` when content calendar-specific capabilities are required. |
| `content-creator` | User asks to work with content creator or configure content creator in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside content creator. | User asks for general assistance in content-and-campaigns without specifying content creator; routes to `content-creator` when content creator-specific capabilities are required. |
| `content-repurposer` | User asks to transform long-form content into multiple short-form pieces or configure content repurposer in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside content repurposer. | User asks for general assistance in content-and-campaigns without specifying content repurposer; routes to `content-repurposer` when content repurposer-specific capabilities are required. |
| `creative-health` | User asks to assess ad creative fatigue or configure creative health in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside creative health. | User asks for general assistance in content-and-campaigns without specifying creative health; routes to `creative-health` when creative health-specific capabilities are required. |
| `creative-iteration-playbook` | User asks to work with creative iteration playbook or configure creative iteration playbook in content-and-campaigns. | User requests general server administration, styling, or unrelated operations outside creative iteration playbook. | User asks for general assistance in content-and-campaigns without specifying creative iteration playbook; routes to `creative-iteration-playbook` when creative iteration playbook-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
