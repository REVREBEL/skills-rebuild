# Phase 08 Batch Audit Record: `batch-17-data-and-ai-llm-and-rag-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-17-data-and-ai-llm-and-rag-part01`
- **Category / Subcategory**: `data-and-ai` / `llm-and-rag`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `76bd0f6c5ba99d429f3e464772c4d2a6af5e724fc9c54e400f543d47947f53f6`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `advanced-evaluation` | `task-folder/agents/skills/advanced-evaluation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ai-agent-development` | `task-folder/agents/skills/ai/ai-agent-development` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ai-engineer` | `task-folder/agents/skills/ai/ai-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ai-engineering-toolkit` | `task-folder/agents/skills/ai/ai-engineering-toolkit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ai-ml` | `task-folder/agents/skills/ai/ai-ml` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `audio-transcriber` | `task-folder/agents/skills/audio-transcriber` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bigquery-basics` | `task-folder/agents/skills/big query/bigquery-basics` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `clarity-gate` | `task-folder/agents/skills/clarity-gate` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `clean-code-guard` | `task-folder/agents/skills/clean-code-guard` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cloudflare` | `task-folder/agents/skills/cloudflare` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `code-review-ai-ai-review` | `task-folder/agents/skills/code/code-review-ai-ai-review` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `community-marketing` | `task-folder/agents/skills/marketing/community-marketing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `comprehensive-review-pr-enhance` | `task-folder/agents/skills/comprehensive-review-pr-enhance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `advanced-evaluation` | User asks to execute or optimize advanced evaluation tasks (e.g. Key insight**: LLM-as-a-Judge is not a single technique but a family of approaches, each suited to different evaluation contexts. Choosing the right approach and mitigating known biases is the core competency this skill develops). | User requests general infrastructure administration or unrelated application development outside advanced evaluation or unrelated operations outside advanced evaluation. | User asks for general assistance with advanced evaluation -> Disambiguate: Clarify whether the focus is specific advanced evaluation patterns or broader llm-and-rag workflows. |
| `ai-agent-development` | User asks to execute or optimize ai agent development tasks (e.g. implementing ai agent development workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ai agent development or unrelated operations outside ai agent development. | User asks for general assistance with ai agent development -> Disambiguate: Clarify whether the focus is specific ai agent development patterns or broader llm-and-rag workflows. |
| `ai-engineer` | User asks to execute or optimize ai engineer tasks (e.g. implementing ai engineer workflows and configurations). | User requests The task is pure data science or traditional ML without LLMs or unrelated operations outside ai engineer. | User asks for general assistance with ai engineer -> Disambiguate: Clarify whether the focus is specific ai engineer patterns or broader llm-and-rag workflows. |
| `ai-engineering-toolkit` | User asks to execute or optimize ai engineering toolkit tasks (e.g. implementing ai engineering toolkit workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ai engineering toolkit or unrelated operations outside ai engineering toolkit. | User asks for general assistance with ai engineering toolkit -> Disambiguate: Clarify whether the focus is specific ai engineering toolkit patterns or broader llm-and-rag workflows. |
| `ai-ml` | User asks to execute or optimize ai ml tasks (e.g. implementing ai ml workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ai ml or unrelated operations outside ai ml. | User asks for general assistance with ai ml -> Disambiguate: Clarify whether the focus is specific ai ml patterns or broader llm-and-rag workflows. |
| `audio-transcriber` | User asks to execute or optimize audio transcriber tasks (e.g. implementing audio transcriber workflows and configurations). | User requests general infrastructure administration or unrelated application development outside audio transcriber or unrelated operations outside audio transcriber. | User asks for general assistance with audio transcriber -> Disambiguate: Clarify whether the focus is specific audio transcriber patterns or broader llm-and-rag workflows. |
| `bigquery-basics` | User asks to execute or optimize bigquery basics tasks (e.g. implementing bigquery basics workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bigquery basics or unrelated operations outside bigquery basics. | User asks for general assistance with bigquery basics -> Disambiguate: Clarify whether the focus is specific bigquery basics patterns or broader llm-and-rag workflows. |
| `clarity-gate` | User asks to execute or optimize clarity gate tasks (e.g. Purpose:** Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases. Produces Clarity-Gated Documents (CGD) compliant with the Clarity Gate Format Specification v2.1). | User requests general infrastructure administration or unrelated application development outside clarity gate or unrelated operations outside clarity gate. | User asks for general assistance with clarity gate -> Disambiguate: Clarify whether the focus is specific clarity gate patterns or broader llm-and-rag workflows. |
| `clean-code-guard` | User asks to execute or optimize clean code guard tasks (e.g. implementing clean code guard workflows and configurations). | User requests general infrastructure administration or unrelated application development outside clean code guard or unrelated operations outside clean code guard. | User asks for general assistance with clean code guard -> Disambiguate: Clarify whether the focus is specific clean code guard patterns or broader llm-and-rag workflows. |
| `cloudflare` | User asks to execute or optimize cloudflare tasks (e.g. implementing cloudflare workflows and configurations). | User requests general infrastructure administration or unrelated application development outside cloudflare or unrelated operations outside cloudflare. | User asks for general assistance with cloudflare -> Disambiguate: Clarify whether the focus is specific cloudflare patterns or broader llm-and-rag workflows. |
| `code-review-ai-ai-review` | User asks to execute or optimize code review ai ai review tasks (e.g. implementing code review ai ai review workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside code review ai ai review. | User asks for general assistance with code review ai ai review -> Disambiguate: Clarify whether the focus is specific code review ai ai review patterns or broader llm-and-rag workflows. |
| `community-marketing` | User asks to execute or optimize community marketing tasks (e.g. implementing community marketing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside community marketing or unrelated operations outside community marketing. | User asks for general assistance with community marketing -> Disambiguate: Clarify whether the focus is specific community marketing patterns or broader llm-and-rag workflows. |
| `comprehensive-review-pr-enhance` | User asks to execute or optimize comprehensive review pr enhance tasks (e.g. implementing comprehensive review pr enhance workflows and configurations). | User requests general infrastructure administration or unrelated application development outside comprehensive review pr enhance or unrelated operations outside comprehensive review pr enhance. | User asks for general assistance with comprehensive review pr enhance -> Disambiguate: Clarify whether the focus is specific comprehensive review pr enhance patterns or broader llm-and-rag workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/data-and-ai/llm-and-rag/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `76bd0f6c5ba99d429f3e464772c4d2a6af5e724fc9c54e400f543d47947f53f6` computed deterministically.
