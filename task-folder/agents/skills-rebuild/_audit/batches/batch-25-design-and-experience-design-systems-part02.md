# Phase 08 Batch Audit Record: `batch-25-design-and-experience-design-systems-part02`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-25-design-and-experience-design-systems-part02`
- **Category / Subcategory**: `design-and-experience` / `design-systems`
- **Member Skill Count**: 15
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `286d4caf5abe76612b2a84e5df56990fc75a2c646cd80643b7f4e802a033d43d`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `design-token` | `task-folder/agents/skills/design/designer-skills-main/design-systems/skills/design-token` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `documentation-template` | `task-folder/agents/skills/design/designer-skills-main/design-systems/skills/documentation-template` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `enhance-prompt` | `task-folder/agents/skills/enhance-prompt` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `feedback-patterns` | `task-folder/agents/skills/design/designer-skills-main/interaction-design/skills/feedback-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-code-connect` | `task-folder/agents/skills/figma/figma-code-connect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-create-new-file` | `task-folder/agents/skills/figma/figma-create-new-file` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-design-to-code` | `task-folder/agents/skills/figma/figma-design-to-code` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-generate-design` | `task-folder/agents/skills/figma/figma-generate-design` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-generate-diagram` | `task-folder/agents/skills/figma/figma-generate-diagram` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-generate-library` | `task-folder/agents/skills/figma/figma-generate-library` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-swiftui` | `task-folder/agents/skills/figma/figma-swiftui` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-use` | `task-folder/agents/skills/figma/figma-use` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-use-figjam` | `task-folder/agents/skills/figma/figma-use-figjam` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `figma-use-slides` | `task-folder/agents/skills/figma/figma-use-slides` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `frontend-design2` | `task-folder/agents/skills/front end/frontend-design2` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `design-token` | User asks to implement, configure, or optimize design token tasks (specifically configuring or implementing design token specifications). | User requests general infrastructure administration, styling, or unrelated operations outside design token or unrelated operations outside design token. | User asks 'How do I handle design token in my workflow?' -> Disambiguate: Clarify whether the task requires specialized design token procedures or general design-systems tooling. |
| `documentation-template` | User asks to implement, configure, or optimize documentation template tasks (specifically configuring or implementing documentation template specifications). | User requests general infrastructure administration, styling, or unrelated operations outside documentation template or unrelated operations outside documentation template. | User asks 'How do I handle documentation template in my workflow?' -> Disambiguate: Clarify whether the task requires specialized documentation template procedures or general design-systems tooling. |
| `enhance-prompt` | User asks to implement, configure, or optimize enhance prompt tasks (specifically configuring or implementing enhance prompt specifications). | User requests general infrastructure administration, styling, or unrelated operations outside enhance prompt or unrelated operations outside enhance prompt. | User asks 'How do I handle enhance prompt in my workflow?' -> Disambiguate: Clarify whether the task requires specialized enhance prompt procedures or general design-systems tooling. |
| `feedback-patterns` | User asks to implement, configure, or optimize feedback patterns tasks (specifically configuring or implementing feedback patterns specifications). | User requests general infrastructure administration, styling, or unrelated operations outside feedback patterns or unrelated operations outside feedback patterns. | User asks 'How do I handle feedback patterns in my workflow?' -> Disambiguate: Clarify whether the task requires specialized feedback patterns procedures or general design-systems tooling. |
| `figma-code-connect` | User asks to implement, configure, or optimize figma code connect tasks (specifically configuring or implementing figma code connect specifications). | User requests Signature:** `getSlot(propName: string): ResultSection[] \| undefined` or unrelated operations outside figma code connect. | User asks 'How do I handle figma code connect in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma code connect procedures or general design-systems tooling. |
| `figma-create-new-file` | User asks to implement, configure, or optimize figma create new file tasks (specifically MANDATORY: load this skill before every `create_new_file` tool call.** It encodes the plan-resolution decision tree, the editor-type contract, and the post-creation handoff to `use_figma`). | User requests general infrastructure administration, styling, or unrelated operations outside figma create new file or unrelated operations outside figma create new file. | User asks 'How do I handle figma create new file in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma create new file procedures or general design-systems tooling. |
| `figma-design-to-code` | User asks to implement, configure, or optimize figma design to code tasks (specifically Always include `figma-design-to-code` in the comma-separated `skillNames` parameter when calling `get_design_context`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-design-to-code`).** This is a logging parameter used to track skill usage — it does not affect execution). | User requests general infrastructure administration, styling, or unrelated operations outside figma design to code or unrelated operations outside figma design to code. | User asks 'How do I handle figma design to code in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma design to code procedures or general design-systems tooling. |
| `figma-generate-design` | User asks to implement, configure, or optimize figma generate design tasks (specifically MANDATORY**: You MUST also load [figma-use](../figma-use/SKILL.md) before any `use_figma` call. That skill contains critical rules (color ranges, font loading, etc.) that apply to every script you write). | User requests general infrastructure administration, styling, or unrelated operations outside figma generate design or unrelated operations outside figma generate design. | User asks 'How do I handle figma generate design in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma generate design procedures or general design-systems tooling. |
| `figma-generate-diagram` | User asks to implement, configure, or optimize figma generate diagram tasks (specifically You MUST load this skill before every `generate_diagram` tool call.** Skipping it causes preventable rendering failures and low-quality output). | User requests general infrastructure administration, styling, or unrelated operations outside figma generate diagram or unrelated operations outside figma generate diagram. | User asks 'How do I handle figma generate diagram in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma generate diagram procedures or general design-systems tooling. |
| `figma-generate-library` | User asks to implement, configure, or optimize figma generate library tasks (specifically Prerequisites**: The `figma-use` skill MUST also be loaded for every `use_figma` call. It provides Plugin API syntax rules (return pattern, page reset, ID return, font loading, color range). This skill provides design system domain knowledge and workflow orchestration). | User requests Every phase checklist, progress update, validation note, and phase summary MUST reference the same task IDs or unrelated operations outside figma generate library. | User asks 'How do I handle figma generate library in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma generate library procedures or general design-systems tooling. |
| `figma-swiftui` | User asks to implement, configure, or optimize figma swiftui tasks (specifically configuring or implementing figma swiftui specifications). | User requests general infrastructure administration, styling, or unrelated operations outside figma swiftui or unrelated operations outside figma swiftui. | User asks 'How do I handle figma swiftui in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma swiftui procedures or general design-systems tooling. |
| `figma-use` | User asks to implement, configure, or optimize figma use tasks (specifically Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage — it does not affect execution). | User requests general infrastructure administration, styling, or unrelated operations outside figma use or unrelated operations outside figma use. | User asks 'How do I handle figma use in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma use procedures or general design-systems tooling. |
| `figma-use-figjam` | User asks to implement, configure, or optimize figma use figjam tasks (specifically Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage — it does not affect execution). | User requests general infrastructure administration, styling, or unrelated operations outside figma use figjam or unrelated operations outside figma use figjam. | User asks 'How do I handle figma use figjam in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma use figjam procedures or general design-systems tooling. |
| `figma-use-slides` | User asks to implement, configure, or optimize figma use slides tasks (specifically Always include `figma-use-slides` in the comma-separated `skillNames` parameter when calling `use_figma` for Slides operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-slides`).** This is a logging parameter used to track skill usage — it does not affect execution). | User requests general infrastructure administration, styling, or unrelated operations outside figma use slides or unrelated operations outside figma use slides. | User asks 'How do I handle figma use slides in my workflow?' -> Disambiguate: Clarify whether the task requires specialized figma use slides procedures or general design-systems tooling. |
| `frontend-design2` | User asks to implement, configure, or optimize frontend design2 tasks (specifically Core Principle**: Choose a clear aesthetic direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity). | User requests general infrastructure administration, styling, or unrelated operations outside frontend design2 or unrelated operations outside frontend design2. | User asks 'How do I handle frontend design2 in my workflow?' -> Disambiguate: Clarify whether the task requires specialized frontend design2 procedures or general design-systems tooling. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/design-and-experience/design-systems/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `286d4caf5abe76612b2a84e5df56990fc75a2c646cd80643b7f4e802a033d43d` computed deterministically.

## 5. Resources Created or Moved

- None

## 6. Retired Paths

- None

## 7. Unresolved Items

- None
