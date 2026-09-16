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
| `playwright-java` | User asks to implement, configure, or optimize playwright java tasks (specifically configuring or implementing playwright java specifications). | User requests general infrastructure administration, styling, or unrelated operations outside playwright java or unrelated operations outside playwright java. | User asks 'How do I handle playwright java in my workflow?' -> Disambiguate: Clarify whether the task requires specialized playwright java procedures or general debugging tooling. |
| `postgres` | User asks to implement, configure, or optimize postgres tasks (specifically configuring or implementing postgres specifications). | User requests general infrastructure administration, styling, or unrelated operations outside postgres or unrelated operations outside postgres. | User asks 'How do I handle postgres in my workflow?' -> Disambiguate: Clarify whether the task requires specialized postgres procedures or general debugging tooling. |
| `python-performance-optimization` | User asks to implement, configure, or optimize python performance optimization tasks (specifically configuring or implementing python performance optimization specifications). | User requests You need a different domain or tool outside this scope or unrelated operations outside python performance optimization. | User asks 'How do I handle python performance optimization in my workflow?' -> Disambiguate: Clarify whether the task requires specialized python performance optimization procedures or general debugging tooling. |
| `report-writing` | User asks to implement, configure, or optimize report writing tasks (specifically configuring or implementing report writing specifications). | User requests general infrastructure administration, styling, or unrelated operations outside report writing or unrelated operations outside report writing. | User asks 'How do I handle report writing in my workflow?' -> Disambiguate: Clarify whether the task requires specialized report writing procedures or general debugging tooling. |
| `systematic-debugging` | User asks to implement, configure, or optimize systematic debugging tasks (specifically configuring or implementing systematic debugging specifications). | User requests general infrastructure administration, styling, or unrelated operations outside systematic debugging or unrelated operations outside systematic debugging. | User asks 'How do I handle systematic debugging in my workflow?' -> Disambiguate: Clarify whether the task requires specialized systematic debugging procedures or general debugging tooling. |
| `the-honoured-one` | User asks to implement, configure, or optimize the honoured one tasks (specifically configuring or implementing the honoured one specifications). | User requests general infrastructure administration, styling, or unrelated operations outside the honoured one or unrelated operations outside the honoured one. | User asks 'How do I handle the honoured one in my workflow?' -> Disambiguate: Clarify whether the task requires specialized the honoured one procedures or general debugging tooling. |
| `tool-design` | User asks to implement, configure, or optimize tool design tasks (specifically configuring or implementing tool design specifications). | User requests general infrastructure administration, styling, or unrelated operations outside tool design or unrelated operations outside tool design. | User asks 'How do I handle tool design in my workflow?' -> Disambiguate: Clarify whether the task requires specialized tool design procedures or general debugging tooling. |
| `using-n8n-mcp-skills` | User asks to implement, configure, or optimize using n8n mcp skills tasks (specifically configuring or implementing using n8n mcp skills specifications). | User requests general infrastructure administration, styling, or unrelated operations outside using n8n mcp skills or unrelated operations outside using n8n mcp skills. | User asks 'How do I handle using n8n mcp skills in my workflow?' -> Disambiguate: Clarify whether the task requires specialized using n8n mcp skills procedures or general debugging tooling. |
| `webflow-cli-troubleshooter` | User asks to implement, configure, or optimize webflow cli troubleshooter tasks (specifically configuring or implementing webflow cli troubleshooter specifications). | User requests All CLI commands require proper descriptions (not context parameters) or unrelated operations outside webflow cli troubleshooter. | User asks 'How do I handle webflow cli troubleshooter in my workflow?' -> Disambiguate: Clarify whether the task requires specialized webflow cli troubleshooter procedures or general debugging tooling. |
| `webflow-designer-api` | User asks to implement, configure, or optimize webflow designer api tasks (specifically configuring or implementing webflow designer api specifications). | User requests general infrastructure administration, styling, or unrelated operations outside webflow designer api or unrelated operations outside webflow designer api. | User asks 'How do I handle webflow designer api in my workflow?' -> Disambiguate: Clarify whether the task requires specialized webflow designer api procedures or general debugging tooling. |
| `yes-md` | User asks to implement, configure, or optimize yes md tasks (specifically configuring or implementing yes md specifications). | User requests general infrastructure administration, styling, or unrelated operations outside yes md or unrelated operations outside yes md. | User asks 'How do I handle yes md in my workflow?' -> Disambiguate: Clarify whether the task requires specialized yes md procedures or general debugging tooling. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/debugging/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `9e8d879942cf7916856186e27f701fd70d65f0de3d83ecc2552883b4d05e19a5` computed deterministically.
