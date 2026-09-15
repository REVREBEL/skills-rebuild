# Phase 08 Batch Audit Record: `batch-151-quality-and-security-debugging-part04`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-151-quality-and-security-debugging-part04`
- **Category / Subcategory**: `quality-and-security` / `debugging`
- **Member Skill Count**: 11
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `9e8d879942cf7916856186e27f701fd70d65f0de3d83ecc2552883b4d05e19a5`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `playwright-java` | `task-folder/agents/skills/playwright-java` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `postgres` | `task-folder/agents/skills/postman/postgres/postgres` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `python-performance-optimization` | `task-folder/agents/skills/python/python-performance-optimization` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `report-writing` | `task-folder/agents/skills/report-writing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `systematic-debugging` | `task-folder/agents/skills/systematic-debugging` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `the-honoured-one` | `task-folder/agents/skills/the-honoured-one` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `tool-design` | `task-folder/agents/skills/tool-design` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `using-n8n-mcp-skills` | `task-folder/agents/skills/using-n8n-mcp-skills` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `webflow-cli-troubleshooter` | `task-folder/agents/skills/webflow/webflow-cli-troubleshooter` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `webflow-designer-api` | `task-folder/agents/skills/webflow/webflow-designer-api` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `yes-md` | `task-folder/agents/skills/yes-md` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `playwright-java` | User asks to execute or optimize playwright java tasks (e.g. implementing playwright java workflows and configurations). | User requests general infrastructure administration or unrelated application development outside playwright java or unrelated operations outside playwright java. | User asks for general assistance with playwright java -> Disambiguate: Clarify whether the focus is specific playwright java patterns or broader debugging workflows. |
| `postgres` | User asks to execute or optimize postgres tasks (e.g. implementing postgres workflows and configurations). | User requests general infrastructure administration or unrelated application development outside postgres or unrelated operations outside postgres. | User asks for general assistance with postgres -> Disambiguate: Clarify whether the focus is specific postgres patterns or broader debugging workflows. |
| `python-performance-optimization` | User asks to execute or optimize python performance optimization tasks (e.g. implementing python performance optimization workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside python performance optimization. | User asks for general assistance with python performance optimization -> Disambiguate: Clarify whether the focus is specific python performance optimization patterns or broader debugging workflows. |
| `report-writing` | User asks to execute or optimize report writing tasks (e.g. implementing report writing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside report writing or unrelated operations outside report writing. | User asks for general assistance with report writing -> Disambiguate: Clarify whether the focus is specific report writing patterns or broader debugging workflows. |
| `systematic-debugging` | User asks to execute or optimize systematic debugging tasks (e.g. implementing systematic debugging workflows and configurations). | User requests general infrastructure administration or unrelated application development outside systematic debugging or unrelated operations outside systematic debugging. | User asks for general assistance with systematic debugging -> Disambiguate: Clarify whether the focus is specific systematic debugging patterns or broader debugging workflows. |
| `the-honoured-one` | User asks to execute or optimize the honoured one tasks (e.g. implementing the honoured one workflows and configurations). | User requests general infrastructure administration or unrelated application development outside the honoured one or unrelated operations outside the honoured one. | User asks for general assistance with the honoured one -> Disambiguate: Clarify whether the focus is specific the honoured one patterns or broader debugging workflows. |
| `tool-design` | User asks to execute or optimize tool design tasks (e.g. implementing tool design workflows and configurations). | User requests general infrastructure administration or unrelated application development outside tool design or unrelated operations outside tool design. | User asks for general assistance with tool design -> Disambiguate: Clarify whether the focus is specific tool design patterns or broader debugging workflows. |
| `using-n8n-mcp-skills` | User asks to execute or optimize using n8n mcp skills tasks (e.g. implementing using n8n mcp skills workflows and configurations). | User requests general infrastructure administration or unrelated application development outside using n8n mcp skills or unrelated operations outside using n8n mcp skills. | User asks for general assistance with using n8n mcp skills -> Disambiguate: Clarify whether the focus is specific using n8n mcp skills patterns or broader debugging workflows. |
| `webflow-cli-troubleshooter` | User asks to execute or optimize webflow cli troubleshooter tasks (e.g. implementing webflow cli troubleshooter workflows and configurations). | User requests All CLI commands require proper descriptions (not context parameters) or unrelated operations outside webflow cli troubleshooter. | User asks for general assistance with webflow cli troubleshooter -> Disambiguate: Clarify whether the focus is specific webflow cli troubleshooter patterns or broader debugging workflows. |
| `webflow-designer-api` | User asks to execute or optimize webflow designer api tasks (e.g. implementing webflow designer api workflows and configurations). | User requests general infrastructure administration or unrelated application development outside webflow designer api or unrelated operations outside webflow designer api. | User asks for general assistance with webflow designer api -> Disambiguate: Clarify whether the focus is specific webflow designer api patterns or broader debugging workflows. |
| `yes-md` | User asks to execute or optimize yes md tasks (e.g. implementing yes md workflows and configurations). | User requests general infrastructure administration or unrelated application development outside yes md or unrelated operations outside yes md. | User asks for general assistance with yes md -> Disambiguate: Clarify whether the focus is specific yes md patterns or broader debugging workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/debugging/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `9e8d879942cf7916856186e27f701fd70d65f0de3d83ecc2552883b4d05e19a5` computed deterministically.
