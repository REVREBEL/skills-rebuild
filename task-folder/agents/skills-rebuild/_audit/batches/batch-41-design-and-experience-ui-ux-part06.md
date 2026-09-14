# Phase 08 Batch Audit Record: `batch-41-design-and-experience-ui-ux-part06`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-41-design-and-experience-ui-ux-part06`
- **Category / Subcategory**: `design-and-experience` / `ui-ux`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `11ac201c3af866cdf159d27f4516edd2d0f145f4f39800669d9cfe8535942ad8`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `loading-states` | `task-folder/agents/skills/design/designer-skills-main/interaction-design/skills/loading-states` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `localization-design` | `task-folder/agents/skills/design/designer-skills-main/design-systems/skills/localization-design` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `lookdev` | `task-folder/agents/skills/lookdev` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `magic-ui-generator` | `task-folder/agents/skills/magic-ui-generator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `mermaid-expert` | `task-folder/agents/skills/mermaid-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `metrics-definition` | `task-folder/agents/skills/design/designer-skills-main/ux-strategy/skills/metrics-definition` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `millers-law` | `task-folder/agents/skills/design/designer-skills-main/interaction-design/skills/millers-law` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `minimalist-skill` | `task-folder/agents/skills/design/minimalist-skill` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `navigation-patterns` | `task-folder/agents/skills/design/designer-skills-main/interaction-design/skills/navigation-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `non-fiction-revision` | `task-folder/agents/skills/design/designer/writing/revision/non-fiction-revision` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `north-star-vision` | `task-folder/agents/skills/design/designer-skills-main/ux-strategy/skills/north-star-vision` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `onboarding-design` | `task-folder/agents/skills/design/designer-skills-main/interaction-design/skills/onboarding-design` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `opportunity-framework` | `task-folder/agents/skills/design/designer-skills-main/ux-strategy/skills/opportunity-framework` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `organize` | `task-folder/agents/skills/design/organize` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `output-skill` | `task-folder/agents/skills/design/output-skill` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `loading-states` | User asks to work with loading states or configure loading states in ui-ux. | User requests general server administration, styling, or unrelated operations outside loading states. | User asks for general assistance in ui-ux without specifying loading states; routes to `loading-states` when loading states-specific capabilities are required. |
| `localization-design` | User asks to work with localization design or configure localization design in ui-ux. | User requests general server administration, styling, or unrelated operations outside localization design. | User asks for general assistance in ui-ux without specifying localization design; routes to `localization-design` when localization design-specific capabilities are required. |
| `lookdev` | User asks to work with lookdev or configure lookdev in ui-ux. | User requests general server administration, styling, or unrelated operations outside lookdev. | User asks for general assistance in ui-ux without specifying lookdev; routes to `lookdev` when lookdev-specific capabilities are required. |
| `magic-ui-generator` | User asks to work with magic ui generator or configure magic ui generator in ui-ux. | User requests general server administration, styling, or unrelated operations outside magic ui generator. | User asks for general assistance in ui-ux without specifying magic ui generator; routes to `magic-ui-generator` when magic ui generator-specific capabilities are required. |
| `mermaid-expert` | User asks to work with mermaid expert or configure mermaid expert in ui-ux. | User requests general server administration, styling, or unrelated operations outside mermaid expert. | User asks for general assistance in ui-ux without specifying mermaid expert; routes to `mermaid-expert` when mermaid expert-specific capabilities are required. |
| `metrics-definition` | User asks to work with metrics definition or configure metrics definition in ui-ux. | User requests general server administration, styling, or unrelated operations outside metrics definition. | User asks for general assistance in ui-ux without specifying metrics definition; routes to `metrics-definition` when metrics definition-specific capabilities are required. |
| `millers-law` | User asks to apply miller's law — chunk information into groups of ~4 to work within working memory limits or configure millers law in ui-ux. | User requests general server administration, styling, or unrelated operations outside millers law. | User asks for general assistance in ui-ux without specifying millers law; routes to `millers-law` when millers law-specific capabilities are required. |
| `minimalist-skill` | User asks to work with minimalist skill or configure minimalist skill in ui-ux. | User requests general server administration, styling, or unrelated operations outside minimalist skill. | User asks for general assistance in ui-ux without specifying minimalist skill; routes to `minimalist-skill` when minimalist skill-specific capabilities are required. |
| `navigation-patterns` | User asks to work with navigation patterns or configure navigation patterns in ui-ux. | User requests general server administration, styling, or unrelated operations outside navigation patterns. | User asks for general assistance in ui-ux without specifying navigation patterns; routes to `navigation-patterns` when navigation patterns-specific capabilities are required. |
| `non-fiction-revision` | User asks to diagnose and guide revisions in non-fiction books. use for non-fiction book revision, when arguments feel weak, evidence is outdated, readers report confusion, thesis is unclear, or book structure has problems. keywords: non-fiction, revision, thesis, argument, evidence, structure or configure non fiction revision in ui-ux. | User requests general server administration, styling, or unrelated operations outside non fiction revision. | User asks for general assistance in ui-ux without specifying non fiction revision; routes to `non-fiction-revision` when non fiction revision-specific capabilities are required. |
| `north-star-vision` | User asks to work with north star vision or configure north star vision in ui-ux. | User requests general server administration, styling, or unrelated operations outside north star vision. | User asks for general assistance in ui-ux without specifying north star vision; routes to `north-star-vision` when north star vision-specific capabilities are required. |
| `onboarding-design` | User asks to work with onboarding design or configure onboarding design in ui-ux. | User requests general server administration, styling, or unrelated operations outside onboarding design. | User asks for general assistance in ui-ux without specifying onboarding design; routes to `onboarding-design` when onboarding design-specific capabilities are required. |
| `opportunity-framework` | User asks to work with opportunity framework or configure opportunity framework in ui-ux. | User requests general server administration, styling, or unrelated operations outside opportunity framework. | User asks for general assistance in ui-ux without specifying opportunity framework; routes to `opportunity-framework` when opportunity framework-specific capabilities are required. |
| `organize` | User asks to work with organize or configure organize in ui-ux. | User requests general server administration, styling, or unrelated operations outside organize. | User asks for general assistance in ui-ux without specifying organize; routes to `organize` when organize-specific capabilities are required. |
| `output-skill` | User asks to work with output skill or configure output skill in ui-ux. | User requests general server administration, styling, or unrelated operations outside output skill. | User asks for general assistance in ui-ux without specifying output skill; routes to `output-skill` when output skill-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
