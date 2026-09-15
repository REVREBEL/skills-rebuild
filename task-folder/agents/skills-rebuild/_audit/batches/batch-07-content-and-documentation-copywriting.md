# Phase 08 Batch Audit Record: `batch-07-content-and-documentation-copywriting`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-07-content-and-documentation-copywriting`
- **Category / Subcategory**: `content-and-documentation` / `copywriting`
- **Member Skill Count**: 4
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `50f339c9cf5e991948e0d8045ce7a9e964ffa63ccd6413a62ee8b5b16bea4629`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `copywriting` | `task-folder/agents/skills/content/copywriting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `copywriting-psychologist` | `task-folder/agents/skills/content/copywriting-psychologist` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `devrel-content` | `task-folder/agents/skills/devrel-content` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `professional-proofreader` | `task-folder/agents/skills/professional-proofreader` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `copywriting` | User asks to execute or optimize copywriting tasks (e.g. implementing copywriting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside copywriting or unrelated operations outside copywriting. | User asks for general assistance with copywriting -> Disambiguate: Clarify whether the focus is specific copywriting patterns or broader copywriting workflows. |
| `copywriting-psychologist` | User asks to execute or optimize copywriting psychologist tasks (e.g. implementing copywriting psychologist workflows and configurations). | User requests general infrastructure administration or unrelated application development outside copywriting psychologist or unrelated operations outside copywriting psychologist. | User asks for general assistance with copywriting psychologist -> Disambiguate: Clarify whether the focus is specific copywriting psychologist patterns or broader copywriting workflows. |
| `devrel-content` | User asks to execute or optimize devrel content tasks (e.g. implementing devrel content workflows and configurations). | User requests general infrastructure administration or unrelated application development outside devrel content or unrelated operations outside devrel content. | User asks for general assistance with devrel content -> Disambiguate: Clarify whether the focus is specific devrel content patterns or broader copywriting workflows. |
| `professional-proofreader` | User asks to execute or optimize professional proofreader tasks (e.g. implementing professional proofreader workflows and configurations). | User requests general infrastructure administration or unrelated application development outside professional proofreader or unrelated operations outside professional proofreader. | User asks for general assistance with professional proofreader -> Disambiguate: Clarify whether the focus is specific professional proofreader patterns or broader copywriting workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/content-and-documentation/copywriting/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `50f339c9cf5e991948e0d8045ce7a9e964ffa63ccd6413a62ee8b5b16bea4629` computed deterministically.
