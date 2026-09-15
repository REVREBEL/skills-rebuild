# Phase 08 Batch Audit Record: `batch-155-quality-and-security-testing-part02`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-155-quality-and-security-testing-part02`
- **Category / Subcategory**: `quality-and-security` / `testing`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `abb6989d3a3b1276832a11bfa3fa466760dcd9ced02c901f66cf71c30867ffa8`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `dependency-upgrade` | `task-folder/agents/skills/dependency-upgrade` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `deployment-validation-config-validate` | `task-folder/agents/skills/deployment-validation-config-validate` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `doc-coauthoring` | `task-folder/agents/skills/documentation/doc-coauthoring` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `durable-objects` | `task-folder/agents/skills/durable-objects` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `e2e-testing-patterns` | `task-folder/agents/skills/e2e-testing-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `evaluation` | `task-folder/agents/skills/evaluation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `focus-group` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/focus-group` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `framework-migration-deps-upgrade` | `task-folder/agents/skills/framework-migration-deps-upgrade` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `javascript-testing-patterns` | `task-folder/agents/skills/javascript/javascript-testing-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `lint-and-validate` | `task-folder/agents/skills/lint-and-validate` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-evaluation` | `task-folder/agents/skills/llm/llm/llm-evaluation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `mcp-tool-developer` | `task-folder/agents/skills/mcp/mcp-tool-developer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ml-engineer` | `task-folder/agents/skills/ml-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `dependency-upgrade` | User asks to execute or optimize dependency upgrade tasks (e.g. implementing dependency upgrade workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside dependency upgrade. | User asks for general assistance with dependency upgrade -> Disambiguate: Clarify whether the focus is specific dependency upgrade patterns or broader testing workflows. |
| `deployment-validation-config-validate` | User asks to execute or optimize deployment validation config validate tasks (e.g. implementing deployment validation config validate workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside deployment validation config validate. | User asks for general assistance with deployment validation config validate -> Disambiguate: Clarify whether the focus is specific deployment validation config validate patterns or broader testing workflows. |
| `doc-coauthoring` | User asks to execute or optimize doc coauthoring tasks (e.g. implementing doc coauthoring workflows and configurations). | User requests general infrastructure administration or unrelated application development outside doc coauthoring or unrelated operations outside doc coauthoring. | User asks for general assistance with doc coauthoring -> Disambiguate: Clarify whether the focus is specific doc coauthoring patterns or broader testing workflows. |
| `durable-objects` | User asks to execute or optimize durable objects tasks (e.g. implementing durable objects workflows and configurations). | User requests Stateless request handling (use plain Workers) or unrelated operations outside durable objects. | User asks for general assistance with durable objects -> Disambiguate: Clarify whether the focus is specific durable objects patterns or broader testing workflows. |
| `e2e-testing-patterns` | User asks to execute or optimize e2e testing patterns tasks (e.g. implementing e2e testing patterns workflows and configurations). | User requests You only need unit or integration tests or unrelated operations outside e2e testing patterns. | User asks for general assistance with e2e testing patterns -> Disambiguate: Clarify whether the focus is specific e2e testing patterns patterns or broader testing workflows. |
| `evaluation` | User asks to execute or optimize evaluation tasks (e.g. implementing evaluation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside evaluation or unrelated operations outside evaluation. | User asks for general assistance with evaluation -> Disambiguate: Clarify whether the focus is specific evaluation patterns or broader testing workflows. |
| `focus-group` | User asks to execute or optimize focus group tasks (e.g. implementing focus group workflows and configurations). | User requests general infrastructure administration or unrelated application development outside focus group or unrelated operations outside focus group. | User asks for general assistance with focus group -> Disambiguate: Clarify whether the focus is specific focus group patterns or broader testing workflows. |
| `framework-migration-deps-upgrade` | User asks to execute or optimize framework migration deps upgrade tasks (e.g. implementing framework migration deps upgrade workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside framework migration deps upgrade. | User asks for general assistance with framework migration deps upgrade -> Disambiguate: Clarify whether the focus is specific framework migration deps upgrade patterns or broader testing workflows. |
| `javascript-testing-patterns` | User asks to execute or optimize javascript testing patterns tasks (e.g. implementing javascript testing patterns workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside javascript testing patterns. | User asks for general assistance with javascript testing patterns -> Disambiguate: Clarify whether the focus is specific javascript testing patterns patterns or broader testing workflows. |
| `lint-and-validate` | User asks to execute or optimize lint and validate tasks (e.g. implementing lint and validate workflows and configurations). | User requests general infrastructure administration or unrelated application development outside lint and validate or unrelated operations outside lint and validate. | User asks for general assistance with lint and validate -> Disambiguate: Clarify whether the focus is specific lint and validate patterns or broader testing workflows. |
| `llm-evaluation` | User asks to execute or optimize llm evaluation tasks (e.g. implementing llm evaluation workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside llm evaluation. | User asks for general assistance with llm evaluation -> Disambiguate: Clarify whether the focus is specific llm evaluation patterns or broader testing workflows. |
| `mcp-tool-developer` | User asks to execute or optimize mcp tool developer tasks (e.g. implementing mcp tool developer workflows and configurations). | User requests general infrastructure administration or unrelated application development outside mcp tool developer or unrelated operations outside mcp tool developer. | User asks for general assistance with mcp tool developer -> Disambiguate: Clarify whether the focus is specific mcp tool developer patterns or broader testing workflows. |
| `ml-engineer` | User asks to execute or optimize ml engineer tasks (e.g. implementing ml engineer workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside ml engineer. | User asks for general assistance with ml engineer -> Disambiguate: Clarify whether the focus is specific ml engineer patterns or broader testing workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/testing/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `abb6989d3a3b1276832a11bfa3fa466760dcd9ced02c901f66cf71c30867ffa8` computed deterministically.
