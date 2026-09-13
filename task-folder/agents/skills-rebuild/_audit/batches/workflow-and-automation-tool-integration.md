# Functional Batch Record: workflow-and-automation-tool-integration

## 1. Batch Metadata & Universe Accounting

- **Category**: `workflow-and-automation`
- **Subcategory**: `tool-integration`
- **Active Skills Universe**: 2,103 skills (2,094 canonical active paths + 9 Phase 07 split children accounted in `phase08-canonical-registry.csv`)
- **Batch Skills Count**: 11 skills
- **Branch**: `skills-rebuild/phase-08-canonical-rewrites`
- **Destination Path**: `task-folder/agents/skills-rebuild/workflow-and-automation/tool-integration/`

---

## 2. Canonical Skills Summary Table

| Canonical Skill Name | Source Path | Authoring Workflow | Provenance / License | Resources Created / Moved | Validation Status |
|---|---|---|---|---|---|
| `n8n-workflow-patterns` | `task-folder/agents/skills/n8n/n8n-workflow-patterns` | `skill-improver` | Community / Unspecified | None | Verified (Pass) |
| `n8n-node-configuration` | `task-folder/agents/skills/n8n/n8n-node-configuration` | `skill-improver` | Community / Unspecified | `references/NODE_FAMILY_GOTCHAS.md` | Verified (Pass) |
| `n8n-subworkflows` | `task-folder/agents/skills/n8n/n8n-subworkflows` | `skill-improver` | `czlonkowski/n8n-skills` / MIT | `references/SUBWORKFLOW_PATTERNS.md`, `references/NAMING_AND_DISCOVERY.md` | Verified (Pass) |
| `n8n-code-python` | `task-folder/agents/skills/n8n/n8n-code-python` | `skill-improver` | Community / Unspecified | `references/LEGACY_PYODIDE_COMPATIBILITY.md` | Verified (Pass) |
| `n8n-code-tool` | `task-folder/agents/skills/n8n/n8n-code-tool` | `skill-improver` | `czlonkowski/n8n-skills` / MIT | `references/ERROR_PATTERNS.md`, `references/INPUT_SCHEMA.md` | Verified (Pass) |
| `n8n-validation-expert` | `task-folder/agents/skills/n8n/n8n-validation-expert` | `skill-improver` | Community / Unspecified | None | Verified (Pass) |
| `n8n-mcp-tools-expert` | `task-folder/agents/skills/n8n/n8n-mcp-tools-expert` | `skill-improver` | Community / Unspecified | None | Verified (Pass) |
| `mcp-builder-ms` | `task-folder/agents/skills/mcp/mcp-builder-ms` | `skill-writer` | Community / Microsoft Ecosystem | `references/LEGACY_V1_MIGRATION.md` | Verified (Pass) |
| `protect-mcp-governance` | `task-folder/agents/skills/protect-mcp-governance` | `skill-improver` | `scopeblind/scopeblind-gateway` / Official | None | Verified (Pass) |
| `automated-triage` | `task-folder/agents/skills/automated-triage` | `skill-writer` | `monte-carlo-data/mc-agent-toolkit` / Apache-2.0 | `references/triage-stages.md`, `references/triage-example.md` | Verified (Pass) |
| `bilig-workpaper` | `task-folder/agents/skills/bilig-workpaper` | `skill-writer` | `proompteng/bilig` / Community | None | Verified (Pass) |

---

## 3. Authoritative Source & Currentness Evidence

For substantial rewrites (`skill-writer`):

### `mcp-builder-ms`
- **Authoritative Sources**: Model Context Protocol Specification (modelcontextprotocol.io, 2026-07-28 protocol), FastMCP Python Documentation, `@modelcontextprotocol/server` official v2 SDK repository.
- **Source Checked Date**: 2026-09-12
- **Technical Validation**: Validated v2 TypeScript `McpServer` registration, `serveStdio`, `createMcpHandler`, and provided progressive disclosure migration guide in `references/LEGACY_V1_MIGRATION.md`.

### `automated-triage`
- **Authoritative Sources**: Monte Carlo Data Observability API Documentation, Monte Carlo Agent Toolkit repository (`monte-carlo-data/mc-agent-toolkit`).
- **Source Checked Date**: 2026-09-12
- **Technical Validation**: Validated tool calling names (`get_alerts`, `alert_assessment`, `run_troubleshooting_agent`) and provided self-contained reference guides replacing broken relative paths.

### `bilig-workpaper`
- **Authoritative Sources**: `@bilig/workpaper` official documentation and GitHub repository (`proompteng/bilig`).
- **Source Checked Date**: 2026-09-12
- **Technical Validation**: Validated `WorkPaper.buildFromSheets`, cell coordinate mutation signatures, and headless MCP server configuration patterns.

---

## 4. Trigger Boundary Evaluation & Query Sets

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `n8n-workflow-patterns` | "Design a webhook-based n8n workflow for customer signups" | "Fix a Python syntax error in my n8n Code node" | "How should I structure my n8n workflow?" -> Routes to `n8n-workflow-patterns` |
| `n8n-node-configuration` | "How do I configure the Google Sheets node to append rows in n8n?" | "Build a custom MCP server for my API" | "What properties are required for this n8n node?" -> Routes to `n8n-node-configuration` |
| `n8n-subworkflows` | "Extract this customer lookup logic into a reusable n8n subworkflow" | "Write Cedar policies for tool governance" | "How do I call another workflow in n8n?" -> Routes to `n8n-subworkflows` |
| `n8n-code-python` | "Write Python code in an n8n Code node using _items to transform data" | "Write a standalone FastAPI service" | "How do I transform data with Python in n8n?" -> Routes to `n8n-code-python` |
| `n8n-code-tool` | "Create an AI agent custom code tool with an input schema in n8n" | "Configure standard n8n Slack node" | "Build a tool for my n8n AI agent" -> Routes to `n8n-code-tool` |
| `n8n-validation-expert` | "Fix missing_required property validation error in n8n" | "Design high-level workflow architecture" | "Why is my n8n node showing a validation error?" -> Routes to `n8n-validation-expert` |
| `n8n-mcp-tools-expert` | "Use n8n-mcp to search for available nodes and validate my JSON" | "Write an MCP server from scratch" | "Search n8n nodes using MCP tools" -> Routes to `n8n-mcp-tools-expert` |
| `mcp-builder-ms` | "Build an MCP server in TypeScript with v2 SDK or Python FastMCP to expose tools" | "Configure Monte Carlo alert webhook" | "How do I build an MCP server?" -> Routes to `mcp-builder-ms` |
| `protect-mcp-governance` | "Enforce Cedar policies on MCP tool calls and verify signed receipts" | "Write n8n workflow patterns" | "How do I secure agent tool calls with policies?" -> Routes to `protect-mcp-governance` |
| `automated-triage` | "Triage Monte Carlo data freshness alerts and run troubleshooting" | "Write a spreadsheet formula model" | "Investigate Monte Carlo alert activity" -> Routes to `automated-triage` |
| `bilig-workpaper` | "Execute spreadsheet formula calculations via WorkPaper JSON and MCP" | "Fix n8n node configuration" | "Run formula calculations without opening Excel" -> Routes to `bilig-workpaper` |

---

## 5. Provider Reconciliation Audit

- `automated-triage`: Neutralized vendor plugin prefixes while maintaining full Monte Carlo MCP tool capabilities and self-contained reference files.
- `bilig-workpaper`: Reconciled provider compatibility restrictions with capability-based execution instructions and clear runtime limitations.
- `protect-mcp-governance`: Maintained official Cedar policy evaluation and Ed25519 receipt verification instructions.

---

## 6. Unresolved Items Ledger

- **Unresolved Items**: None. All 11 canonical skills in Batch 1 are fully rewritten, normalized, self-contained, and validated.
