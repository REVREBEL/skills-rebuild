# Phase 08 Batch Audit Record: `batch-44-design-and-experience-ui-ux-part09`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-44-design-and-experience-ui-ux-part09`
- **Category / Subcategory**: `design-and-experience` / `ui-ux`
- **Member Skill Count**: 14
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `40bb1c0ea6d591e4fa9a258039b9902b611f6c520482f60abf798d6895dedc81`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `ux-audit` | `task-folder/agents/skills/ux/ux-audit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ux-feedback` | `task-folder/agents/skills/ux/ux-feedback` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ux-flow` | `task-folder/agents/skills/ux/ux-flow` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ux-persuasion-engineer` | `task-folder/agents/skills/ux/ux-persuasion-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `uxui-principles` | `task-folder/agents/skills/ux/uxui-principles` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `version-control-strategy` | `task-folder/agents/skills/design/designer-skills-main/design-ops/skills/version-control-strategy` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `visual-hierarchy` | `task-folder/agents/skills/design/designer-skills-main/ui-design/skills/visual-hierarchy` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `voice-analysis` | `task-folder/agents/skills/design/designer/writing/analysis/voice-analysis` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `von-restorff-effect` | `task-folder/agents/skills/design/designer-skills-main/ui-design/skills/von-restorff-effect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `webflow-code-component-component-scaffold` | `task-folder/agents/skills/webflow/webflow-code-component-component-scaffold` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `webflow-code-component-pre-deploy-check` | `task-folder/agents/skills/webflow/webflow-code-component-pre-deploy-check` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `webflow-code-components` | `task-folder/agents/skills/webflow/webflow-code-components` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `wireframe-spec` | `task-folder/agents/skills/design/designer-skills-main/prototyping-testing/skills/wireframe-spec` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `xlsx` | `task-folder/agents/skills/design/document-skills/xlsx` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `ux-audit` | User asks to execute or optimize ux audit tasks (e.g. implementing ux audit workflows and configurations). | User requests For accessibility-only issues → use `/ss-a11y` or unrelated operations outside ux audit. | User asks for general assistance with ux audit -> Disambiguate: Clarify whether the focus is specific ux audit patterns or broader ui-ux workflows. |
| `ux-feedback` | User asks to execute or optimize ux feedback tasks (e.g. implementing ux feedback workflows and configurations). | User requests For only the words inside a state → use `/ss-copy` or unrelated operations outside ux feedback. | User asks for general assistance with ux feedback -> Disambiguate: Clarify whether the focus is specific ux feedback patterns or broader ui-ux workflows. |
| `ux-flow` | User asks to execute or optimize ux flow tasks (e.g. implementing ux flow workflows and configurations). | User requests For implementing a single page → use `/ss-page` after the flow is settled or unrelated operations outside ux flow. | User asks for general assistance with ux flow -> Disambiguate: Clarify whether the focus is specific ux flow patterns or broader ui-ux workflows. |
| `ux-persuasion-engineer` | User asks to execute or optimize ux persuasion engineer tasks (e.g. implementing ux persuasion engineer workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ux persuasion engineer or unrelated operations outside ux persuasion engineer. | User asks for general assistance with ux persuasion engineer -> Disambiguate: Clarify whether the focus is specific ux persuasion engineer patterns or broader ui-ux workflows. |
| `uxui-principles` | User asks to execute or optimize uxui principles tasks (e.g. Source:** https://github.com/uxuiprinciples/agent-skills). | User requests general infrastructure administration or unrelated application development outside uxui principles or unrelated operations outside uxui principles. | User asks for general assistance with uxui principles -> Disambiguate: Clarify whether the focus is specific uxui principles patterns or broader ui-ux workflows. |
| `version-control-strategy` | User asks to execute or optimize version control strategy tasks (e.g. implementing version control strategy workflows and configurations). | User requests general infrastructure administration or unrelated application development outside version control strategy or unrelated operations outside version control strategy. | User asks for general assistance with version control strategy -> Disambiguate: Clarify whether the focus is specific version control strategy patterns or broader ui-ux workflows. |
| `visual-hierarchy` | User asks to execute or optimize visual hierarchy tasks (e.g. implementing visual hierarchy workflows and configurations). | User requests general infrastructure administration or unrelated application development outside visual hierarchy or unrelated operations outside visual hierarchy. | User asks for general assistance with visual hierarchy -> Disambiguate: Clarify whether the focus is specific visual hierarchy patterns or broader ui-ux workflows. |
| `voice-analysis` | User asks to execute or optimize voice analysis tasks (e.g. implementing voice analysis workflows and configurations). | User requests general infrastructure administration or unrelated application development outside voice analysis or unrelated operations outside voice analysis. | User asks for general assistance with voice analysis -> Disambiguate: Clarify whether the focus is specific voice analysis patterns or broader ui-ux workflows. |
| `von-restorff-effect` | User asks to execute or optimize von restorff effect tasks (e.g. implementing von restorff effect workflows and configurations). | User requests general infrastructure administration or unrelated application development outside von restorff effect or unrelated operations outside von restorff effect. | User asks for general assistance with von restorff effect -> Disambiguate: Clarify whether the focus is specific von restorff effect patterns or broader ui-ux workflows. |
| `webflow-code-component-component-scaffold` | User asks to execute or optimize webflow code component component scaffold tasks (e.g. implementing webflow code component component scaffold workflows and configurations). | User requests Converting an existing React component (use convert-component skill) or unrelated operations outside webflow code component component scaffold. | User asks for general assistance with webflow code component component scaffold -> Disambiguate: Clarify whether the focus is specific webflow code component component scaffold patterns or broader ui-ux workflows. |
| `webflow-code-component-pre-deploy-check` | User asks to execute or optimize webflow code component pre deploy check tasks (e.g. implementing webflow code component pre deploy check workflows and configurations). | User requests Deployment already failed (use troubleshoot-deploy instead) or unrelated operations outside webflow code component pre deploy check. | User asks for general assistance with webflow code component pre deploy check -> Disambiguate: Clarify whether the focus is specific webflow code component pre deploy check patterns or broader ui-ux workflows. |
| `webflow-code-components` | User asks to execute or optimize webflow code components tasks (e.g. implementing webflow code components workflows and configurations). | User requests general infrastructure administration or unrelated application development outside webflow code components or unrelated operations outside webflow code components. | User asks for general assistance with webflow code components -> Disambiguate: Clarify whether the focus is specific webflow code components patterns or broader ui-ux workflows. |
| `wireframe-spec` | User asks to execute or optimize wireframe spec tasks (e.g. implementing wireframe spec workflows and configurations). | User requests general infrastructure administration or unrelated application development outside wireframe spec or unrelated operations outside wireframe spec. | User asks for general assistance with wireframe spec -> Disambiguate: Clarify whether the focus is specific wireframe spec patterns or broader ui-ux workflows. |
| `xlsx` | User asks to execute or optimize xlsx tasks (e.g. implementing xlsx workflows and configurations). | User requests general infrastructure administration or unrelated application development outside xlsx or unrelated operations outside xlsx. | User asks for general assistance with xlsx -> Disambiguate: Clarify whether the focus is specific xlsx patterns or broader ui-ux workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/design-and-experience/ui-ux/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `40bb1c0ea6d591e4fa9a258039b9902b611f6c520482f60abf798d6895dedc81` computed deterministically.
