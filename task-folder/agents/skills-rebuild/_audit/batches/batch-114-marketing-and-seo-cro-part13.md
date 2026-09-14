# Phase 08 Batch Audit Record: `batch-114-marketing-and-seo-cro-part13`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-114-marketing-and-seo-cro-part13`
- **Category / Subcategory**: `marketing-and-seo` / `cro`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `2d351b2c93c5bc9e797c0fb29d9aea6fd336d8e9fa96cca54ee0ee4bfb9b593d`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `signup` | `task-folder/agents/skills/marketing/signup` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `signup-flow-cro` | `task-folder/agents/skills/signup-flow-cro` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `social-calendar-system` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/social-media-marketing/skills/social-calendar-system` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `social-metadata-hardening` | `task-folder/agents/skills/social/social-metadata-hardening` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `social-orchestrator` | `task-folder/agents/skills/social/social-orchestrator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `specify` | `task-folder/agents/skills/design/specify` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `stakeholder-ops` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/customer-feedback-orchestration/skills/stakeholder-ops` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `statsmodels` | `task-folder/agents/skills/statsmodels` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `stitch-loop` | `task-folder/agents/skills/stitch-loop` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `stitch-skill` | `task-folder/agents/skills/design/stitch-skill` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `storyboard-manager` | `task-folder/agents/skills/design/intent/storyboard-manager` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `supabase` | `task-folder/agents/skills/supabase` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `suppression-logic` | `task-folder/agents/skills/seo/seo-skills-main/gtm-agents-main/plugins/intent-signal-orchestration/skills/suppression-logic` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `sync-memory` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/sync-memory` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `taisly-social-media-posting` | `task-folder/agents/skills/taisly-social-media-posting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `signup` | User asks to when the user wants to optimize signup, registration, account creation, or trial activation flows. also use when the user mentions or configure signup in cro. | User requests general server administration, styling, or unrelated operations outside signup. | User asks for general assistance in cro without specifying signup; routes to `signup` when signup-specific capabilities are required. |
| `signup-flow-cro` | User asks to work with signup flow cro or configure signup flow cro in cro. | User requests general server administration, styling, or unrelated operations outside signup flow cro. | User asks for general assistance in cro without specifying signup flow cro; routes to `signup-flow-cro` when signup flow cro-specific capabilities are required. |
| `social-calendar-system` | User asks to work with social calendar system or configure social calendar system in cro. | User requests general server administration, styling, or unrelated operations outside social calendar system. | User asks for general assistance in cro without specifying social calendar system; routes to `social-calendar-system` when social calendar system-specific capabilities are required. |
| `social-metadata-hardening` | User asks to work with social metadata hardening or configure social metadata hardening in cro. | User requests general server administration, styling, or unrelated operations outside social metadata hardening. | User asks for general assistance in cro without specifying social metadata hardening; routes to `social-metadata-hardening` when social metadata hardening-specific capabilities are required. |
| `social-orchestrator` | User asks to work with social orchestrator or configure social orchestrator in cro. | User requests general server administration, styling, or unrelated operations outside social orchestrator. | User asks for general assistance in cro without specifying social orchestrator; routes to `social-orchestrator` when social orchestrator-specific capabilities are required. |
| `specify` | User asks to work with specify or configure specify in cro. | User requests general server administration, styling, or unrelated operations outside specify. | User asks for general assistance in cro without specifying specify; routes to `specify` when specify-specific capabilities are required. |
| `stakeholder-ops` | User asks to work with stakeholder ops or configure stakeholder ops in cro. | User requests general server administration, styling, or unrelated operations outside stakeholder ops. | User asks for general assistance in cro without specifying stakeholder ops; routes to `stakeholder-ops` when stakeholder ops-specific capabilities are required. |
| `statsmodels` | User asks to statsmodels is python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods or configure statsmodels in cro. | User requests general server administration, styling, or unrelated operations outside statsmodels. | User asks for general assistance in cro without specifying statsmodels; routes to `statsmodels` when statsmodels-specific capabilities are required. |
| `stitch-loop` | User asks to work with stitch loop or configure stitch loop in cro. | User requests general server administration, styling, or unrelated operations outside stitch loop. | User asks for general assistance in cro without specifying stitch loop; routes to `stitch-loop` when stitch loop-specific capabilities are required. |
| `stitch-skill` | User asks to work with stitch skill or configure stitch skill in cro. | User requests general server administration, styling, or unrelated operations outside stitch skill. | User asks for general assistance in cro without specifying stitch skill; routes to `stitch-skill` when stitch skill-specific capabilities are required. |
| `storyboard-manager` | User asks to assist writers with story planning, character development, plot structuring, chapter writing, timeline tracking, and consistency checking. use this skill when working with creative writing projects organized in folders containing characters, chapters, story planning documents, and summaries. trigger this skill for tasks like or configure storyboard manager in cro. | User requests general server administration, styling, or unrelated operations outside storyboard manager. | User asks for general assistance in cro without specifying storyboard manager; routes to `storyboard-manager` when storyboard manager-specific capabilities are required. |
| `supabase` | User asks to work with supabase or configure supabase in cro. | User requests general server administration, styling, or unrelated operations outside supabase. | User asks for general assistance in cro without specifying supabase; routes to `supabase` when supabase-specific capabilities are required. |
| `suppression-logic` | User asks to work with suppression logic or configure suppression logic in cro. | User requests general server administration, styling, or unrelated operations outside suppression logic. | User asks for general assistance in cro without specifying suppression logic; routes to `suppression-logic` when suppression logic-specific capabilities are required. |
| `sync-memory` | User asks to batch sync session learnings to memory or configure sync memory in cro. | User requests general server administration, styling, or unrelated operations outside sync memory. | User asks for general assistance in cro without specifying sync memory; routes to `sync-memory` when sync memory-specific capabilities are required. |
| `taisly-social-media-posting` | User asks to work with taisly social media posting or configure taisly social media posting in cro. | User requests general server administration, styling, or unrelated operations outside taisly social media posting. | User asks for general assistance in cro without specifying taisly social media posting; routes to `taisly-social-media-posting` when taisly social media posting-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
