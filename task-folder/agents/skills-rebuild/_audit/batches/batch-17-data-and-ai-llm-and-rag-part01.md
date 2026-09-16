# Phase 08 Batch Audit Record: `batch-17-data-and-ai-llm-and-rag-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-17-data-and-ai-llm-and-rag-part01`
- **Category / Subcategory**: `data-and-ai` / `llm-and-rag`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `c8492be2e4d3a8337db37b391a83a4b0ca5680ca58d645bfc3de26d2da791a5a`

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
| `advanced-evaluation` | User asks to implement, configure, or optimize advanced evaluation tasks (specifically Key insight**: LLM-as-a-Judge is not a single technique but a family of approaches, each suited to different evaluation contexts. Choosing the right approach and mitigating known biases is the core competency this skill develops). | User requests general infrastructure administration, styling, or unrelated operations outside advanced evaluation or unrelated operations outside advanced evaluation. | User asks 'How do I handle advanced evaluation in my workflow?' -> Disambiguate: Clarify whether the task requires specialized advanced evaluation procedures or general llm-and-rag tooling. |
| `ai-agent-development` | User asks to implement, configure, or optimize ai agent development tasks (specifically configuring or implementing ai agent development specifications). | User requests general infrastructure administration, styling, or unrelated operations outside ai agent development or unrelated operations outside ai agent development. | User asks 'How do I handle ai agent development in my workflow?' -> Disambiguate: Clarify whether the task requires specialized ai agent development procedures or general llm-and-rag tooling. |
| `ai-engineer` | User asks to implement, configure, or optimize ai engineer tasks (specifically configuring or implementing ai engineer specifications). | User requests The task is pure data science or traditional ML without LLMs or unrelated operations outside ai engineer. | User asks 'How do I handle ai engineer in my workflow?' -> Disambiguate: Clarify whether the task requires specialized ai engineer procedures or general llm-and-rag tooling. |
| `ai-engineering-toolkit` | User asks to implement, configure, or optimize ai engineering toolkit tasks (specifically configuring or implementing ai engineering toolkit specifications). | User requests general infrastructure administration, styling, or unrelated operations outside ai engineering toolkit or unrelated operations outside ai engineering toolkit. | User asks 'How do I handle ai engineering toolkit in my workflow?' -> Disambiguate: Clarify whether the task requires specialized ai engineering toolkit procedures or general llm-and-rag tooling. |
| `ai-ml` | User asks to implement, configure, or optimize ai ml tasks (specifically configuring or implementing ai ml specifications). | User requests general infrastructure administration, styling, or unrelated operations outside ai ml or unrelated operations outside ai ml. | User asks 'How do I handle ai ml in my workflow?' -> Disambiguate: Clarify whether the task requires specialized ai ml procedures or general llm-and-rag tooling. |
| `audio-transcriber` | User asks to implement, configure, or optimize audio transcriber tasks (specifically configuring or implementing audio transcriber specifications). | User requests general infrastructure administration, styling, or unrelated operations outside audio transcriber or unrelated operations outside audio transcriber. | User asks 'How do I handle audio transcriber in my workflow?' -> Disambiguate: Clarify whether the task requires specialized audio transcriber procedures or general llm-and-rag tooling. |
| `bigquery-basics` | User asks to implement, configure, or optimize bigquery basics tasks (specifically configuring or implementing bigquery basics specifications). | User requests general infrastructure administration, styling, or unrelated operations outside bigquery basics or unrelated operations outside bigquery basics. | User asks 'How do I handle bigquery basics in my workflow?' -> Disambiguate: Clarify whether the task requires specialized bigquery basics procedures or general llm-and-rag tooling. |
| `clarity-gate` | User asks to implement, configure, or optimize clarity gate tasks (specifically Purpose:** Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases. Produces Clarity-Gated Documents (CGD) compliant with the Clarity Gate Format Specification v2.1). | User requests general infrastructure administration, styling, or unrelated operations outside clarity gate or unrelated operations outside clarity gate. | User asks 'How do I handle clarity gate in my workflow?' -> Disambiguate: Clarify whether the task requires specialized clarity gate procedures or general llm-and-rag tooling. |
| `clean-code-guard` | User asks to implement, configure, or optimize clean code guard tasks (specifically configuring or implementing clean code guard specifications). | User requests general infrastructure administration, styling, or unrelated operations outside clean code guard or unrelated operations outside clean code guard. | User asks 'How do I handle clean code guard in my workflow?' -> Disambiguate: Clarify whether the task requires specialized clean code guard procedures or general llm-and-rag tooling. |
| `cloudflare` | User asks to implement, configure, or optimize cloudflare tasks (specifically configuring or implementing cloudflare specifications). | User requests general infrastructure administration, styling, or unrelated operations outside cloudflare or unrelated operations outside cloudflare. | User asks 'How do I handle cloudflare in my workflow?' -> Disambiguate: Clarify whether the task requires specialized cloudflare procedures or general llm-and-rag tooling. |
| `code-review-ai-ai-review` | User asks to implement, configure, or optimize code review ai ai review tasks (specifically configuring or implementing code review ai ai review specifications). | User requests You need a different domain or tool outside this scope or unrelated operations outside code review ai ai review. | User asks 'How do I handle code review ai ai review in my workflow?' -> Disambiguate: Clarify whether the task requires specialized code review ai ai review procedures or general llm-and-rag tooling. |
| `community-marketing` | User asks to implement, configure, or optimize community marketing tasks (specifically configuring or implementing community marketing specifications). | User requests general infrastructure administration, styling, or unrelated operations outside community marketing or unrelated operations outside community marketing. | User asks 'How do I handle community marketing in my workflow?' -> Disambiguate: Clarify whether the task requires specialized community marketing procedures or general llm-and-rag tooling. |
| `comprehensive-review-pr-enhance` | User asks to implement, configure, or optimize comprehensive review pr enhance tasks (specifically configuring or implementing comprehensive review pr enhance specifications). | User requests general infrastructure administration, styling, or unrelated operations outside comprehensive review pr enhance or unrelated operations outside comprehensive review pr enhance. | User asks 'How do I handle comprehensive review pr enhance in my workflow?' -> Disambiguate: Clarify whether the task requires specialized comprehensive review pr enhance procedures or general llm-and-rag tooling. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/data-and-ai/llm-and-rag/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `c8492be2e4d3a8337db37b391a83a4b0ca5680ca58d645bfc3de26d2da791a5a` computed deterministically.
