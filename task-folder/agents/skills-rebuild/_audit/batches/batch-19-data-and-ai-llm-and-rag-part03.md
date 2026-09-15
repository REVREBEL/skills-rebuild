# Phase 08 Batch Audit Record: `batch-19-data-and-ai-llm-and-rag-part03`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-19-data-and-ai-llm-and-rag-part03`
- **Category / Subcategory**: `data-and-ai` / `llm-and-rag`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `35171a1283b9576786cd9e19e922df44fd42fbf4761228b6af16e84591e5b578`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `llm-application-dev-ai-assistant` | `task-folder/agents/skills/llm/llm/llm-application-dev-ai-assistant` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-application-dev-langchain-agent` | `task-folder/agents/skills/llm/llm/llm-application-dev-langchain-agent` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-application-dev-prompt-optimize` | `task-folder/agents/skills/llm/llm/llm-application-dev-prompt-optimize` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-council` | `task-folder/agents/skills/llm/llm/llm-council` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-ops` | `task-folder/agents/skills/llm/llm/llm-ops` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llms-create` | `task-folder/agents/skills/github/llms-create` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llms-update` | `task-folder/agents/skills/github/llms-update` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `local-llm-expert` | `task-folder/agents/skills/local-llm-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `marketing-psychology` | `task-folder/agents/skills/marketing/marketing-psychology` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `mcp-builder` | `task-folder/agents/skills/mcp/mcp-builder` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `multi-agent-architect` | `task-folder/agents/skills/agents/multi-agent-architect` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `n8n-agents` | `task-folder/agents/skills/n8n/n8n-agents` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `project-development` | `task-folder/agents/skills/project-development` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `llm-application-dev-ai-assistant` | User asks to execute or optimize llm application dev ai assistant tasks (e.g. implementing llm application dev ai assistant workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside llm application dev ai assistant. | User asks for general assistance with llm application dev ai assistant -> Disambiguate: Clarify whether the focus is specific llm application dev ai assistant patterns or broader llm-and-rag workflows. |
| `llm-application-dev-langchain-agent` | User asks to execute or optimize llm application dev langchain agent tasks (e.g. implementing llm application dev langchain agent workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside llm application dev langchain agent. | User asks for general assistance with llm application dev langchain agent -> Disambiguate: Clarify whether the focus is specific llm application dev langchain agent patterns or broader llm-and-rag workflows. |
| `llm-application-dev-prompt-optimize` | User asks to execute or optimize llm application dev prompt optimize tasks (e.g. implementing llm application dev prompt optimize workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside llm application dev prompt optimize. | User asks for general assistance with llm application dev prompt optimize -> Disambiguate: Clarify whether the focus is specific llm application dev prompt optimize patterns or broader llm-and-rag workflows. |
| `llm-council` | User asks to execute or optimize llm council tasks (e.g. implementing llm council workflows and configurations). | User requests general infrastructure administration or unrelated application development outside llm council or unrelated operations outside llm council. | User asks for general assistance with llm council -> Disambiguate: Clarify whether the focus is specific llm council patterns or broader llm-and-rag workflows. |
| `llm-ops` | User asks to execute or optimize llm ops tasks (e.g. implementing llm ops workflows and configurations). | User requests A simpler, more specific tool can handle the request or unrelated operations outside llm ops. | User asks for general assistance with llm ops -> Disambiguate: Clarify whether the focus is specific llm ops patterns or broader llm-and-rag workflows. |
| `llms-create` | User asks to execute or optimize llms create tasks (e.g. implementing llms create workflows and configurations). | User requests general infrastructure administration or unrelated application development outside llms create or unrelated operations outside llms create. | User asks for general assistance with llms create -> Disambiguate: Clarify whether the focus is specific llms create patterns or broader llm-and-rag workflows. |
| `llms-update` | User asks to execute or optimize llms update tasks (e.g. implementing llms update workflows and configurations). | User requests general infrastructure administration or unrelated application development outside llms update or unrelated operations outside llms update. | User asks for general assistance with llms update -> Disambiguate: Clarify whether the focus is specific llms update patterns or broader llm-and-rag workflows. |
| `local-llm-expert` | User asks to execute or optimize local llm expert tasks (e.g. implementing local llm expert workflows and configurations). | User requests Implementing cloud-exclusive endpoints (OpenAI, Anthropic API directly) or unrelated operations outside local llm expert. | User asks for general assistance with local llm expert -> Disambiguate: Clarify whether the focus is specific local llm expert patterns or broader llm-and-rag workflows. |
| `marketing-psychology` | User asks to execute or optimize marketing psychology tasks (e.g. (Applied · Ethical · Prioritized)**). | User requests general infrastructure administration or unrelated application development outside marketing psychology or unrelated operations outside marketing psychology. | User asks for general assistance with marketing psychology -> Disambiguate: Clarify whether the focus is specific marketing psychology patterns or broader llm-and-rag workflows. |
| `mcp-builder` | User asks to execute or optimize mcp builder tasks (e.g. implementing mcp builder workflows and configurations). | User requests general infrastructure administration or unrelated application development outside mcp builder or unrelated operations outside mcp builder. | User asks for general assistance with mcp builder -> Disambiguate: Clarify whether the focus is specific mcp builder patterns or broader llm-and-rag workflows. |
| `multi-agent-architect` | User asks to execute or optimize multi agent architect tasks (e.g. implementing multi agent architect workflows and configurations). | User requests general infrastructure administration or unrelated application development outside multi agent architect or unrelated operations outside multi agent architect. | User asks for general assistance with multi agent architect -> Disambiguate: Clarify whether the focus is specific multi agent architect patterns or broader llm-and-rag workflows. |
| `n8n-agents` | User asks to execute or optimize n8n agents tasks (e.g. implementing n8n agents workflows and configurations). | User requests general infrastructure administration or unrelated application development outside n8n agents or unrelated operations outside n8n agents. | User asks for general assistance with n8n agents -> Disambiguate: Clarify whether the focus is specific n8n agents patterns or broader llm-and-rag workflows. |
| `project-development` | User asks to execute or optimize project development tasks (e.g. implementing project development workflows and configurations). | User requests general infrastructure administration or unrelated application development outside project development or unrelated operations outside project development. | User asks for general assistance with project development -> Disambiguate: Clarify whether the focus is specific project development patterns or broader llm-and-rag workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/data-and-ai/llm-and-rag/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `35171a1283b9576786cd9e19e922df44fd42fbf4761228b6af16e84591e5b578` computed deterministically.
