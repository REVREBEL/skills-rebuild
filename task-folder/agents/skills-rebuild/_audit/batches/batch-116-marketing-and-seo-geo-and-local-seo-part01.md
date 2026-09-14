# Phase 08 Batch Audit Record: `batch-116-marketing-and-seo-geo-and-local-seo-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-116-marketing-and-seo-geo-and-local-seo-part01`
- **Category / Subcategory**: `marketing-and-seo` / `geo-and-local-seo`
- **Member Skill Count**: 12
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `af26b820d36de688f4ccd934c4b73691d8ae0073bff9b5f874c6da1ee645f54d`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `aeo-geo` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/aeo-geo` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `agent-manager-skill` | `task-folder/agents/skills/agents/agent-manager-skill` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `analytics-integration` | `task-folder/agents/skills/seo/seo-skills-main/geo-audit-report/SEO Audit/G4A/analytics-integration` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `asset-tracking` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/content-pipeline-orchestration/skills/asset-tracking` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bot-protection` | `task-folder/agents/skills/seo/seo-skills-main/geo-audit-report/SEO Audit/bot-protection` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `brand-governance` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/design-creative/skills/brand-governance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `brand-voice-glossary` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/brand-strategy/skills/brand-voice-glossary` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `c2pa-metadata` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/c2pa-metadata` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `capacity-modeling` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/sales-operations/skills/capacity-modeling` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cognitive-biases` | `task-folder/agents/skills/strategy/cognitive-biases` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `competitive-ads-extractor` | `task-folder/agents/skills/seo/seo-skills-main/geo-audit-report/SEO Audit/seo-skills/competitive-ads-extractor` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `content-quality-auditor` | `task-folder/agents/skills/seo/seo-skills-main/geo-audit-report/SEO Audit/seo-geo-claude-skills-main 2/cross-cutting/content-quality-auditor` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `aeo-geo` | User asks to optimize ai engine visibility or configure aeo geo in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside aeo geo. | User asks for general assistance in geo-and-local-seo without specifying aeo geo; routes to `aeo-geo` when aeo geo-specific capabilities are required. |
| `agent-manager-skill` | User asks to work with agent manager skill or configure agent manager skill in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside agent manager skill. | User asks for general assistance in geo-and-local-seo without specifying agent manager skill; routes to `agent-manager-skill` when agent manager skill-specific capabilities are required. |
| `analytics-integration` | User asks to work with analytics integration or configure analytics integration in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside analytics integration. | User asks for general assistance in geo-and-local-seo without specifying analytics integration; routes to `analytics-integration` when analytics integration-specific capabilities are required. |
| `asset-tracking` | User asks to work with asset tracking or configure asset tracking in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside asset tracking. | User asks for general assistance in geo-and-local-seo without specifying asset tracking; routes to `asset-tracking` when asset tracking-specific capabilities are required. |
| `bot-protection` | User asks to work with bot protection or configure bot protection in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside bot protection. | User asks for general assistance in geo-and-local-seo without specifying bot protection; routes to `bot-protection` when bot protection-specific capabilities are required. |
| `brand-governance` | User asks to work with brand governance or configure brand governance in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside brand governance. | User asks for general assistance in geo-and-local-seo without specifying brand governance; routes to `brand-governance` when brand governance-specific capabilities are required. |
| `brand-voice-glossary` | User asks to work with brand voice glossary or configure brand voice glossary in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside brand voice glossary. | User asks for general assistance in geo-and-local-seo without specifying brand voice glossary; routes to `brand-voice-glossary` when brand voice glossary-specific capabilities are required. |
| `c2pa-metadata` | User asks to embed c2pa (content authenticity initiative) provenance manifests in ai-generated marketing assets (image/video/audio/pdf) or configure c2pa metadata in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside c2pa metadata. | User asks for general assistance in geo-and-local-seo without specifying c2pa metadata; routes to `c2pa-metadata` when c2pa metadata-specific capabilities are required. |
| `capacity-modeling` | User asks to work with capacity modeling or configure capacity modeling in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside capacity modeling. | User asks for general assistance in geo-and-local-seo without specifying capacity modeling; routes to `capacity-modeling` when capacity modeling-specific capabilities are required. |
| `cognitive-biases` | User asks to work with cognitive biases or configure cognitive biases in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside cognitive biases. | User asks for general assistance in geo-and-local-seo without specifying cognitive biases; routes to `cognitive-biases` when cognitive biases-specific capabilities are required. |
| `competitive-ads-extractor` | User asks to extracts and analyzes competitors' ads from ad libraries (facebook, linkedin, etc.) to understand what messaging, problems, and creative approaches are working. helps inspire and improve your own ad campaigns when executing competitive ads extractor operations or configure competitive ads extractor in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside competitive ads extractor. | User asks for general assistance in geo-and-local-seo without specifying competitive ads extractor; routes to `competitive-ads-extractor` when competitive ads extractor-specific capabilities are required. |
| `content-quality-auditor` | User asks to work with content quality auditor or configure content quality auditor in geo-and-local-seo. | User requests general server administration, styling, or unrelated operations outside content quality auditor. | User asks for general assistance in geo-and-local-seo without specifying content quality auditor; routes to `content-quality-auditor` when content quality auditor-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
