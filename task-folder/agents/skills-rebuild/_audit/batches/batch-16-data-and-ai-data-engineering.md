# Phase 08 Batch Audit Record: `batch-16-data-and-ai-data-engineering`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-16-data-and-ai-data-engineering`
- **Category / Subcategory**: `data-and-ai` / `data-engineering`
- **Member Skill Count**: 6
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `23d08c8b711f6bfa52eeb3665a892276b1821b56779bf0c72df48b92314458a4`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `data-engineer` | `task-folder/agents/skills/data/data-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `data-engineering-data-pipeline` | `task-folder/agents/skills/data/data-engineering-data-pipeline` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ml-pipeline-workflow` | `task-folder/agents/skills/ml-pipeline-workflow` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `mlops-engineer` | `task-folder/agents/skills/mlops-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `recsys-pipeline-architect` | `task-folder/agents/skills/recsys-pipeline-architect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `scikit-learn` | `task-folder/agents/skills/scikit-learn` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `data-engineer` | User asks to execute or optimize data engineer tasks (e.g. implementing data engineer workflows and configurations). | User requests You only need exploratory data analysis or unrelated operations outside data engineer. | User asks for general assistance with data engineer -> Disambiguate: Clarify whether the focus is specific data engineer patterns or broader data-engineering workflows. |
| `data-engineering-data-pipeline` | User asks to execute or optimize data engineering data pipeline tasks (e.g. implementing data engineering data pipeline workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside data engineering data pipeline. | User asks for general assistance with data engineering data pipeline -> Disambiguate: Clarify whether the focus is specific data engineering data pipeline patterns or broader data-engineering workflows. |
| `ml-pipeline-workflow` | User asks to execute or optimize ml pipeline workflow tasks (e.g. implementing ml pipeline workflow workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside ml pipeline workflow. | User asks for general assistance with ml pipeline workflow -> Disambiguate: Clarify whether the focus is specific ml pipeline workflow patterns or broader data-engineering workflows. |
| `mlops-engineer` | User asks to execute or optimize mlops engineer tasks (e.g. implementing mlops engineer workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside mlops engineer. | User asks for general assistance with mlops engineer -> Disambiguate: Clarify whether the focus is specific mlops engineer patterns or broader data-engineering workflows. |
| `recsys-pipeline-architect` | User asks to execute or optimize recsys pipeline architect tasks (e.g. implementing recsys pipeline architect workflows and configurations). | User requests general infrastructure administration or unrelated application development outside recsys pipeline architect or unrelated operations outside recsys pipeline architect. | User asks for general assistance with recsys pipeline architect -> Disambiguate: Clarify whether the focus is specific recsys pipeline architect patterns or broader data-engineering workflows. |
| `scikit-learn` | User asks to execute or optimize scikit learn tasks (e.g. implementing scikit learn workflows and configurations). | User requests general infrastructure administration or unrelated application development outside scikit learn or unrelated operations outside scikit learn. | User asks for general assistance with scikit learn -> Disambiguate: Clarify whether the focus is specific scikit learn patterns or broader data-engineering workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/data-and-ai/data-engineering/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `23d08c8b711f6bfa52eeb3665a892276b1821b56779bf0c72df48b92314458a4` computed deterministically.
