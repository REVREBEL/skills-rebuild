# Phase 08 Batch Audit Record: `batch-27-design-and-experience-design-systems-part04`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-27-design-and-experience-design-systems-part04`
- **Category / Subcategory**: `design-and-experience` / `design-systems`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `d3b9072150e9e55a79a44c7cdeb0b0e4949810a9b0bcd66cee3a2c533f5493d8`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `tailwind-theme-builder` | `task-folder/agents/skills/tailwind/tailwind-theme-builder` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `theme-factory` | `task-folder/agents/skills/theme-factory` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `threat-modeling-expert` | `task-folder/agents/skills/threat-modeling-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `transilience-report-style` | `task-folder/agents/skills/report-writing/formats/transilience-report-style` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-lint` | `task-folder/agents/skills/ui/ui-lint` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-pattern` | `task-folder/agents/skills/ui/ui-pattern` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-review` | `task-folder/agents/skills/ui/ui-review` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-setup` | `task-folder/agents/skills/ui/ui-setup` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-ux-designer` | `task-folder/agents/skills/ui/ui-ux-designer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ui-visual-validator` | `task-folder/agents/skills/ui/ui-visual-validator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `visual-design-foundations` | `task-folder/agents/skills/design/designer/clean-gemini-agents/gemini-agents/skills/ux-design/visual-design-foundations` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `web-component-design` | `task-folder/agents/skills/design/designer/clean-gemini-agents/gemini-agents/skills/ux-design/web-component-design` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `writing-skills` | `task-folder/agents/skills/figma/writing-skills` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `tailwind-theme-builder` | User asks to execute or optimize tailwind theme builder tasks (e.g. implementing tailwind theme builder workflows and configurations). | User requests general infrastructure administration or unrelated application development outside tailwind theme builder or unrelated operations outside tailwind theme builder. | User asks for general assistance with tailwind theme builder -> Disambiguate: Clarify whether the focus is specific tailwind theme builder patterns or broader design-systems workflows. |
| `theme-factory` | User asks to execute or optimize theme factory tasks (e.g. implementing theme factory workflows and configurations). | User requests general infrastructure administration or unrelated application development outside theme factory or unrelated operations outside theme factory. | User asks for general assistance with theme factory -> Disambiguate: Clarify whether the focus is specific theme factory patterns or broader design-systems workflows. |
| `threat-modeling-expert` | User asks to execute or optimize threat modeling expert tasks (e.g. implementing threat modeling expert workflows and configurations). | User requests You lack scope or authorization for security review or unrelated operations outside threat modeling expert. | User asks for general assistance with threat modeling expert -> Disambiguate: Clarify whether the focus is specific threat modeling expert patterns or broader design-systems workflows. |
| `transilience-report-style` | User asks to execute or optimize transilience report style tasks (e.g. Version:** 4.0). | User requests general infrastructure administration or unrelated application development outside transilience report style or unrelated operations outside transilience report style. | User asks for general assistance with transilience report style -> Disambiguate: Clarify whether the focus is specific transilience report style patterns or broader design-systems workflows. |
| `ui-lint` | User asks to execute or optimize ui lint tasks (e.g. implementing ui lint workflows and configurations). | User requests For deeper review of design judgment (composition, hierarchy, rhythm) → use `/ss-review` or unrelated operations outside ui lint. | User asks for general assistance with ui lint -> Disambiguate: Clarify whether the focus is specific ui lint patterns or broader design-systems workflows. |
| `ui-pattern` | User asks to execute or optimize ui pattern tasks (e.g. implementing ui pattern workflows and configurations). | User requests For a single primitive component → use `/ss-component` or unrelated operations outside ui pattern. | User asks for general assistance with ui pattern -> Disambiguate: Clarify whether the focus is specific ui pattern patterns or broader design-systems workflows. |
| `ui-review` | User asks to execute or optimize ui review tasks (e.g. implementing ui review workflows and configurations). | User requests For accessibility-only issues → use `/ss-a11y` or unrelated operations outside ui review. | User asks for general assistance with ui review -> Disambiguate: Clarify whether the focus is specific ui review patterns or broader design-systems workflows. |
| `ui-setup` | User asks to execute or optimize ui setup tasks (e.g. implementing ui setup workflows and configurations). | User requests For projects already configured with StyleSeed → use `/ss-update` instead or unrelated operations outside ui setup. | User asks for general assistance with ui setup -> Disambiguate: Clarify whether the focus is specific ui setup patterns or broader design-systems workflows. |
| `ui-ux-designer` | User asks to execute or optimize ui ux designer tasks (e.g. implementing ui ux designer workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside ui ux designer. | User asks for general assistance with ui ux designer -> Disambiguate: Clarify whether the focus is specific ui ux designer patterns or broader design-systems workflows. |
| `ui-visual-validator` | User asks to execute or optimize ui visual validator tasks (e.g. implementing ui visual validator workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside ui visual validator. | User asks for general assistance with ui visual validator -> Disambiguate: Clarify whether the focus is specific ui visual validator patterns or broader design-systems workflows. |
| `visual-design-foundations` | User asks to execute or optimize visual design foundations tasks (e.g. implementing visual design foundations workflows and configurations). | User requests general infrastructure administration or unrelated application development outside visual design foundations or unrelated operations outside visual design foundations. | User asks for general assistance with visual design foundations -> Disambiguate: Clarify whether the focus is specific visual design foundations patterns or broader design-systems workflows. |
| `web-component-design` | User asks to execute or optimize web component design tasks (e.g. implementing web component design workflows and configurations). | User requests general infrastructure administration or unrelated application development outside web component design or unrelated operations outside web component design. | User asks for general assistance with web component design -> Disambiguate: Clarify whether the focus is specific web component design patterns or broader design-systems workflows. |
| `writing-skills` | User asks to execute or optimize writing skills tasks (e.g. implementing writing skills workflows and configurations). | User requests general infrastructure administration or unrelated application development outside writing skills or unrelated operations outside writing skills. | User asks for general assistance with writing skills -> Disambiguate: Clarify whether the focus is specific writing skills patterns or broader design-systems workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/design-and-experience/design-systems/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `d3b9072150e9e55a79a44c7cdeb0b0e4949810a9b0bcd66cee3a2c533f5493d8` computed deterministically.
