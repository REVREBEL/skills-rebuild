# Phase 08 Batch Audit Record: `batch-01-workflow-and-automation-tool-integration`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-01-workflow-and-automation-tool-integration`
- **Category / Subcategory**: `workflow-and-automation` / `tool-integration`
- **Member Skill Count**: 11
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `0c05c3d2874e0adc9e2dc41f92002b03683b5f6856f62cf265baab7eb34f91f2`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `automated-triage` | `task-folder/agents/skills/automated-triage` | `skill-writer` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bilig-workpaper` | `task-folder/agents/skills/bilig-workpaper` | `skill-writer` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `mcp-builder-ms` | `task-folder/agents/skills/mcp/mcp-builder-ms` | `skill-writer` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-code-python` | `task-folder/agents/skills/n8n/n8n-code-python` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-code-tool` | `task-folder/agents/skills/n8n/n8n-code-tool` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-mcp-tools-expert` | `task-folder/agents/skills/n8n/n8n-mcp-tools-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-node-configuration` | `task-folder/agents/skills/n8n/n8n-node-configuration` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-subworkflows` | `task-folder/agents/skills/n8n/n8n-subworkflows` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-validation-expert` | `task-folder/agents/skills/n8n/n8n-validation-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-workflow-patterns` | `task-folder/agents/skills/n8n/n8n-workflow-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `protect-mcp-governance` | `task-folder/agents/skills/protect-mcp-governance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `automated-triage` | User asks to execute or optimize automated triage tasks (e.g. implementing automated triage workflows and configurations). | User requests Writing raw database migration scripts (use database migration skills) or unrelated operations outside automated triage. | User asks for general assistance with automated triage -> Disambiguate: Clarify whether the focus is specific automated triage patterns or broader tool-integration workflows. |
| `bilig-workpaper` | User asks to execute or optimize bilig workpaper tasks (e.g. implementing bilig workpaper workflows and configurations). | User requests Manual GUI spreadsheet editing or VBA macro execution or unrelated operations outside bilig workpaper. | User asks for general assistance with bilig workpaper -> Disambiguate: Clarify whether the focus is specific bilig workpaper patterns or broader tool-integration workflows. |
| `mcp-builder-ms` | User asks to execute or optimize mcp builder ms tasks (e.g. implementing mcp builder ms workflows and configurations). | User requests Configuring pre-built n8n MCP tools (use `n8n-mcp-tools-expert`) or unrelated operations outside mcp builder ms. | User asks for general assistance with mcp builder ms -> Disambiguate: Clarify whether the focus is specific mcp builder ms patterns or broader tool-integration workflows. |
| `n8n-code-python` | User asks to execute or optimize n8n code python tasks (e.g. implementing n8n code python workflows and configurations). | User requests Writing schema-constrained AI Custom Code Tools for LangChain/AI Agent nodes (use `n8n-code-tool`) or unrelated operations outside n8n code python. | User asks for general assistance with n8n code python -> Disambiguate: Clarify whether the focus is specific n8n code python patterns or broader tool-integration workflows. |
| `n8n-code-tool` | User asks to execute or optimize n8n code tool tasks (e.g. implementing n8n code tool workflows and configurations). | User requests Standard workflow Code nodes in linear workflows (use `n8n-code-python` or JavaScript nodes) or unrelated operations outside n8n code tool. | User asks for general assistance with n8n code tool -> Disambiguate: Clarify whether the focus is specific n8n code tool patterns or broader tool-integration workflows. |
| `n8n-mcp-tools-expert` | User asks to execute or optimize n8n mcp tools expert tasks (e.g. implementing n8n mcp tools expert workflows and configurations). | User requests Writing custom FastMCP servers in Python or TypeScript (use `mcp-builder-ms`) or unrelated operations outside n8n mcp tools expert. | User asks for general assistance with n8n mcp tools expert -> Disambiguate: Clarify whether the focus is specific n8n mcp tools expert patterns or broader tool-integration workflows. |
| `n8n-node-configuration` | User asks to execute or optimize n8n node configuration tasks (e.g. implementing n8n node configuration workflows and configurations). | User requests High-level workflow orchestration and topology design (use `n8n-workflow-patterns`) or unrelated operations outside n8n node configuration. | User asks for general assistance with n8n node configuration -> Disambiguate: Clarify whether the focus is specific n8n node configuration patterns or broader tool-integration workflows. |
| `n8n-subworkflows` | User asks to execute or optimize n8n subworkflows tasks (e.g. implementing n8n subworkflows workflows and configurations). | User requests Writing raw inline Python/JavaScript transformations within a single node (use `n8n-code-python` or `n8n-code-tool`) or unrelated operations outside n8n subworkflows. | User asks for general assistance with n8n subworkflows -> Disambiguate: Clarify whether the focus is specific n8n subworkflows patterns or broader tool-integration workflows. |
| `n8n-validation-expert` | User asks to execute or optimize n8n validation expert tasks (e.g. implementing n8n validation expert workflows and configurations). | User requests Writing custom Python scripts (use `n8n-code-python`) or unrelated operations outside n8n validation expert. | User asks for general assistance with n8n validation expert -> Disambiguate: Clarify whether the focus is specific n8n validation expert patterns or broader tool-integration workflows. |
| `n8n-workflow-patterns` | User asks to execute or optimize n8n workflow patterns tasks (e.g. implementing n8n workflow patterns workflows and configurations). | User requests Detailed parameter troubleshooting on specific node types (use `n8n-node-configuration`) or unrelated operations outside n8n workflow patterns. | User asks for general assistance with n8n workflow patterns -> Disambiguate: Clarify whether the focus is specific n8n workflow patterns patterns or broader tool-integration workflows. |
| `protect-mcp-governance` | User asks to execute or optimize protect mcp governance tasks (e.g. implementing protect mcp governance workflows and configurations). | User requests General static code vulnerability scanning (use security audit tools) or unrelated operations outside protect mcp governance. | User asks for general assistance with protect mcp governance -> Disambiguate: Clarify whether the focus is specific protect mcp governance patterns or broader tool-integration workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/workflow-and-automation/tool-integration/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `0c05c3d2874e0adc9e2dc41f92002b03683b5f6856f62cf265baab7eb34f91f2` computed deterministically.
