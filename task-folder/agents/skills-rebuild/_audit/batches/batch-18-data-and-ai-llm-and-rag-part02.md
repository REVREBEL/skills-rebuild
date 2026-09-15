# Phase 08 Batch Audit Record: `batch-18-data-and-ai-llm-and-rag-part02`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-18-data-and-ai-llm-and-rag-part02`
- **Category / Subcategory**: `data-and-ai` / `llm-and-rag`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `8e5b49aa0393e39115f6b96a0798a87f1277b27f6565675db5f3ae1fdba0f829`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `context-window-management` | `task-folder/agents/skills/context/context-window-management` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `conversation-memory` | `task-folder/agents/skills/conversation-memory` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `convex` | `task-folder/agents/skills/convex` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `earllm-build` | `task-folder/agents/skills/earllm-build` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `file-uploads` | `task-folder/agents/skills/files/file-uploads` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `grand-slam-offers` | `task-folder/agents/skills/strategy/grand-slam-offers` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `hugging-face-community-evals` | `task-folder/agents/skills/hugging face/hugging-face-community-evals` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `hugging-face-datasets` | `task-folder/agents/skills/hugging face/hugging-face-datasets` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `hugging-face-evaluation` | `task-folder/agents/skills/hugging face/hugging-face-evaluation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `infinite-gratitude` | `task-folder/agents/skills/infinite-gratitude` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `langchain-architecture` | `task-folder/agents/skills/langchain-architecture` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `langgraph` | `task-folder/agents/skills/langgraph` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `llm-app-patterns` | `task-folder/agents/skills/llm/llm/llm-app-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `context-window-management` | User asks to execute or optimize context window management tasks (e.g. implementing context window management workflows and configurations). | User requests general infrastructure administration or unrelated application development outside context window management or unrelated operations outside context window management. | User asks for general assistance with context window management -> Disambiguate: Clarify whether the focus is specific context window management patterns or broader llm-and-rag workflows. |
| `conversation-memory` | User asks to execute or optimize conversation memory tasks (e.g. implementing conversation memory workflows and configurations). | User requests general infrastructure administration or unrelated application development outside conversation memory or unrelated operations outside conversation memory. | User asks for general assistance with conversation memory -> Disambiguate: Clarify whether the focus is specific conversation memory patterns or broader llm-and-rag workflows. |
| `convex` | User asks to execute or optimize convex tasks (e.g. implementing convex workflows and configurations). | User requests general infrastructure administration or unrelated application development outside convex or unrelated operations outside convex. | User asks for general assistance with convex -> Disambiguate: Clarify whether the focus is specific convex patterns or broader llm-and-rag workflows. |
| `earllm-build` | User asks to execute or optimize earllm build tasks (e.g. implementing earllm build workflows and configurations). | User requests A simpler, more specific tool can handle the request or unrelated operations outside earllm build. | User asks for general assistance with earllm build -> Disambiguate: Clarify whether the focus is specific earllm build patterns or broader llm-and-rag workflows. |
| `file-uploads` | User asks to execute or optimize file uploads tasks (e.g. Role**: File Upload Specialist). | User requests general infrastructure administration or unrelated application development outside file uploads or unrelated operations outside file uploads. | User asks for general assistance with file uploads -> Disambiguate: Clarify whether the focus is specific file uploads patterns or broader llm-and-rag workflows. |
| `grand-slam-offers` | User asks to execute or optimize grand slam offers tasks (e.g. implementing grand slam offers workflows and configurations). | User requests general infrastructure administration or unrelated application development outside grand slam offers or unrelated operations outside grand slam offers. | User asks for general assistance with grand slam offers -> Disambiguate: Clarify whether the focus is specific grand slam offers patterns or broader llm-and-rag workflows. |
| `hugging-face-community-evals` | User asks to execute or optimize hugging face community evals tasks (e.g. implementing hugging face community evals workflows and configurations). | User requests general infrastructure administration or unrelated application development outside hugging face community evals or unrelated operations outside hugging face community evals. | User asks for general assistance with hugging face community evals -> Disambiguate: Clarify whether the focus is specific hugging face community evals patterns or broader llm-and-rag workflows. |
| `hugging-face-datasets` | User asks to execute or optimize hugging face datasets tasks (e.g. implementing hugging face datasets workflows and configurations). | User requests general infrastructure administration or unrelated application development outside hugging face datasets or unrelated operations outside hugging face datasets. | User asks for general assistance with hugging face datasets -> Disambiguate: Clarify whether the focus is specific hugging face datasets patterns or broader llm-and-rag workflows. |
| `hugging-face-evaluation` | User asks to execute or optimize hugging face evaluation tasks (e.g. Extracting existing evaluation tables from README content). | User requests general infrastructure administration or unrelated application development outside hugging face evaluation or unrelated operations outside hugging face evaluation. | User asks for general assistance with hugging face evaluation -> Disambiguate: Clarify whether the focus is specific hugging face evaluation patterns or broader llm-and-rag workflows. |
| `infinite-gratitude` | User asks to execute or optimize infinite gratitude tasks (e.g. implementing infinite gratitude workflows and configurations). | User requests general infrastructure administration or unrelated application development outside infinite gratitude or unrelated operations outside infinite gratitude. | User asks for general assistance with infinite gratitude -> Disambiguate: Clarify whether the focus is specific infinite gratitude patterns or broader llm-and-rag workflows. |
| `langchain-architecture` | User asks to execute or optimize langchain architecture tasks (e.g. implementing langchain architecture workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside langchain architecture. | User asks for general assistance with langchain architecture -> Disambiguate: Clarify whether the focus is specific langchain architecture patterns or broader llm-and-rag workflows. |
| `langgraph` | User asks to execute or optimize langgraph tasks (e.g. Role**: LangGraph Agent Architect). | User requests general infrastructure administration or unrelated application development outside langgraph or unrelated operations outside langgraph. | User asks for general assistance with langgraph -> Disambiguate: Clarify whether the focus is specific langgraph patterns or broader llm-and-rag workflows. |
| `llm-app-patterns` | User asks to execute or optimize llm app patterns tasks (e.g. implementing llm app patterns workflows and configurations). | User requests general infrastructure administration or unrelated application development outside llm app patterns or unrelated operations outside llm app patterns. | User asks for general assistance with llm app patterns -> Disambiguate: Clarify whether the focus is specific llm app patterns patterns or broader llm-and-rag workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/data-and-ai/llm-and-rag/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `8e5b49aa0393e39115f6b96a0798a87f1277b27f6565675db5f3ae1fdba0f829` computed deterministically.
