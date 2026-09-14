# Phase 08 Batch Audit Record: `batch-20-data-and-ai-llm-and-rag-part04`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-20-data-and-ai-llm-and-rag-part04`
- **Category / Subcategory**: `data-and-ai` / `llm-and-rag`
- **Member Skill Count**: 13
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `a416687b4c27e03fe1733b18a9dfa021262c3a7265a1d5e4cae0a8483a79237a`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `prompt-caching` | `task-folder/agents/skills/prompts/prompt-caching` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `prompt-engineering-patterns` | `task-folder/agents/skills/prompts/prompt-engineering-patterns` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `public-relations` | `task-folder/agents/skills/public-relations` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `quant-analyst` | `task-folder/agents/skills/quant-analyst` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `rag-engineer` | `task-folder/agents/skills/rag-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `rag-implementation` | `task-folder/agents/skills/rag-implementation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `rclone-cli` | `task-folder/agents/skills/rclone-cli` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `routerbase-model-gateway` | `task-folder/agents/skills/routerbase-model-gateway` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `unslop-commit` | `task-folder/agents/skills/unslop-commit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `unslop-file` | `task-folder/agents/skills/unslop-file` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vector-database-engineer` | `task-folder/agents/skills/vector-database-engineer` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vibe-code-auditor` | `task-folder/agents/skills/vibe-code-auditor` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `vibe-code-cleanup` | `task-folder/agents/skills/vibe-code-cleanup` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `prompt-caching` | User asks to work with prompt caching or configure prompt caching in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside prompt caching. | User asks for general assistance in llm-and-rag without specifying prompt caching; routes to `prompt-caching` when prompt caching-specific capabilities are required. |
| `prompt-engineering-patterns` | User asks to work with prompt engineering patterns or configure prompt engineering patterns in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside prompt engineering patterns. | User asks for general assistance in llm-and-rag without specifying prompt engineering patterns; routes to `prompt-engineering-patterns` when prompt engineering patterns-specific capabilities are required. |
| `public-relations` | User asks to when the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). also use when the user mentions 'pr,' 'public relations,' 'press,' 'press release,' 'press coverage,' 'media outreach,' 'pitch a journalist,' 'get or configure public relations in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside public relations. | User asks for general assistance in llm-and-rag without specifying public relations; routes to `public-relations` when public relations-specific capabilities are required. |
| `quant-analyst` | User asks to work with quant analyst or configure quant analyst in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside quant analyst. | User asks for general assistance in llm-and-rag without specifying quant analyst; routes to `quant-analyst` when quant analyst-specific capabilities are required. |
| `rag-engineer` | User asks to work with rag engineer or configure rag engineer in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside rag engineer. | User asks for general assistance in llm-and-rag without specifying rag engineer; routes to `rag-engineer` when rag engineer-specific capabilities are required. |
| `rag-implementation` | User asks to work with rag implementation or configure rag implementation in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside rag implementation. | User asks for general assistance in llm-and-rag without specifying rag implementation; routes to `rag-implementation` when rag implementation-specific capabilities are required. |
| `rclone-cli` | User asks to work with rclone cli or configure rclone cli in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside rclone cli. | User asks for general assistance in llm-and-rag without specifying rclone cli; routes to `rclone-cli` when rclone cli-specific capabilities are required. |
| `routerbase-model-gateway` | User asks to work with routerbase model gateway or configure routerbase model gateway in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside routerbase model gateway. | User asks for general assistance in llm-and-rag without specifying routerbase model gateway; routes to `routerbase-model-gateway` when routerbase model gateway-specific capabilities are required. |
| `unslop-commit` | User asks to rewrites commit messages so they sound like a careful human engineer wrote them. strips ai/marketing slop ( or configure unslop commit in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside unslop commit. | User asks for general assistance in llm-and-rag without specifying unslop commit; routes to `unslop-commit` when unslop commit-specific capabilities are required. |
| `unslop-file` | User asks to humanize natural-language memory files (claude.md, todos, preferences, docs) by removing ai-isms and adding burstiness while preserving every code block, url, path, command, and heading exactly. two modes: --deterministic (fast, regex-based, no api) and llm (default, calls claude for or configure unslop file in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside unslop file. | User asks for general assistance in llm-and-rag without specifying unslop file; routes to `unslop-file` when unslop file-specific capabilities are required. |
| `vector-database-engineer` | User asks to work with vector database engineer or configure vector database engineer in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside vector database engineer. | User asks for general assistance in llm-and-rag without specifying vector database engineer; routes to `vector-database-engineer` when vector database engineer-specific capabilities are required. |
| `vibe-code-auditor` | User asks to work with vibe code auditor or configure vibe code auditor in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside vibe code auditor. | User asks for general assistance in llm-and-rag without specifying vibe code auditor; routes to `vibe-code-auditor` when vibe code auditor-specific capabilities are required. |
| `vibe-code-cleanup` | User asks to work with vibe code cleanup or configure vibe code cleanup in llm-and-rag. | User requests general server administration, styling, or unrelated operations outside vibe code cleanup. | User asks for general assistance in llm-and-rag without specifying vibe code cleanup; routes to `vibe-code-cleanup` when vibe code cleanup-specific capabilities are required. |

## 4. Provider Reconciliation & Security Audit

- **Undeclared Provider Lock-in**: 0 occurrences. All provider APIs declared in compatibility metadata.
- **Workstation / Machine Path Leaks**: 0 occurrences.
- **Broken Relative References**: 0 broken links.

## 5. Unresolved Items Ledger

| Item ID | Skill Name | Issue Type | Disposition | Rationale |
|---|---|---|---|---|
| None | None | None | deliberate_state_completed | All member skills successfully rewritten, normalized, and validated. |
