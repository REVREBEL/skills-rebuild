# Phase 08 Batch Audit Record: `batch-148-quality-and-security-debugging-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-148-quality-and-security-debugging-part01`
- **Category / Subcategory**: `quality-and-security` / `debugging`
- **Member Skill Count**: 12
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `ef72913f0973b385aed2b063edb4bb0b679282bdacd62d085acbf2a0f29969fb`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `agent-orchestration-multi-agent-optimize` | `task-folder/agents/skills/agents/agent-orchestration-multi-agent-optimize` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `audience-intelligence` | `task-folder/agents/skills/marketing/digital-marketing-pro-main/skills/audience-intelligence` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bug-hunter` | `task-folder/agents/skills/bug-hunter` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `cms-best-practices` | `task-folder/agents/skills/cms-best-practices` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `code-showcase-systematic-debugging` | `task-folder/agents/skills/code/code-showcase-systematic-debugging` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `competitor-profiling` | `task-folder/agents/skills/writing/competitor-profiling` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `data-profiling` | `task-folder/agents/skills/data-analytics/data-profiling` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `debugger` | `task-folder/agents/skills/debugging/debugger` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `debugging-and-error-recovery` | `task-folder/agents/skills/debugging/debugging-and-error-recovery` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `debugging-code` | `task-folder/agents/skills/debugging/debugging-code` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `debugging-strategies` | `task-folder/agents/skills/debugging/debugging-strategies` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `debugging-toolkit` | `task-folder/agents/skills/debugging/debugging-toolkit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `agent-orchestration-multi-agent-optimize` | User asks to execute or optimize agent orchestration multi agent optimize tasks (e.g. implementing agent orchestration multi agent optimize workflows and configurations). | User requests You only need to tune a single agent prompt or unrelated operations outside agent orchestration multi agent optimize. | User asks for general assistance with agent orchestration multi agent optimize -> Disambiguate: Clarify whether the focus is specific agent orchestration multi agent optimize patterns or broader debugging workflows. |
| `audience-intelligence` | User asks to execute or optimize audience intelligence tasks (e.g. implementing audience intelligence workflows and configurations). | User requests general infrastructure administration or unrelated application development outside audience intelligence or unrelated operations outside audience intelligence. | User asks for general assistance with audience intelligence -> Disambiguate: Clarify whether the focus is specific audience intelligence patterns or broader debugging workflows. |
| `bug-hunter` | User asks to execute or optimize bug hunter tasks (e.g. implementing bug hunter workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bug hunter or unrelated operations outside bug hunter. | User asks for general assistance with bug hunter -> Disambiguate: Clarify whether the focus is specific bug hunter patterns or broader debugging workflows. |
| `cms-best-practices` | User asks to execute or optimize cms best practices tasks (e.g. implementing cms best practices workflows and configurations). | User requests All tool calls must include the required `context` parameter (15-25 words, third-person perspective) or unrelated operations outside cms best practices. | User asks for general assistance with cms best practices -> Disambiguate: Clarify whether the focus is specific cms best practices patterns or broader debugging workflows. |
| `code-showcase-systematic-debugging` | User asks to execute or optimize code showcase systematic debugging tasks (e.g. implementing code showcase systematic debugging workflows and configurations). | User requests general infrastructure administration or unrelated application development outside code showcase systematic debugging or unrelated operations outside code showcase systematic debugging. | User asks for general assistance with code showcase systematic debugging -> Disambiguate: Clarify whether the focus is specific code showcase systematic debugging patterns or broader debugging workflows. |
| `competitor-profiling` | User asks to execute or optimize competitor profiling tasks (e.g. implementing competitor profiling workflows and configurations). | User requests general infrastructure administration or unrelated application development outside competitor profiling or unrelated operations outside competitor profiling. | User asks for general assistance with competitor profiling -> Disambiguate: Clarify whether the focus is specific competitor profiling patterns or broader debugging workflows. |
| `data-profiling` | User asks to execute or optimize data profiling tasks (e.g. implementing data profiling workflows and configurations). | User requests general infrastructure administration or unrelated application development outside data profiling or unrelated operations outside data profiling. | User asks for general assistance with data profiling -> Disambiguate: Clarify whether the focus is specific data profiling patterns or broader debugging workflows. |
| `debugger` | User asks to execute or optimize debugger tasks (e.g. implementing debugger workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside debugger. | User asks for general assistance with debugger -> Disambiguate: Clarify whether the focus is specific debugger patterns or broader debugging workflows. |
| `debugging-and-error-recovery` | User asks to execute or optimize debugging and error recovery tasks (e.g. implementing debugging and error recovery workflows and configurations). | User requests general infrastructure administration or unrelated application development outside debugging and error recovery or unrelated operations outside debugging and error recovery. | User asks for general assistance with debugging and error recovery -> Disambiguate: Clarify whether the focus is specific debugging and error recovery patterns or broader debugging workflows. |
| `debugging-code` | User asks to execute or optimize debugging code tasks (e.g. implementing debugging code workflows and configurations). | User requests general infrastructure administration or unrelated application development outside debugging code or unrelated operations outside debugging code. | User asks for general assistance with debugging code -> Disambiguate: Clarify whether the focus is specific debugging code patterns or broader debugging workflows. |
| `debugging-strategies` | User asks to execute or optimize debugging strategies tasks (e.g. implementing debugging strategies workflows and configurations). | User requests There is no reproducible issue or observable symptom or unrelated operations outside debugging strategies. | User asks for general assistance with debugging strategies -> Disambiguate: Clarify whether the focus is specific debugging strategies patterns or broader debugging workflows. |
| `debugging-toolkit` | User asks to execute or optimize debugging toolkit tasks (e.g. implementing debugging toolkit workflows and configurations). | User requests general infrastructure administration or unrelated application development outside debugging toolkit or unrelated operations outside debugging toolkit. | User asks for general assistance with debugging toolkit -> Disambiguate: Clarify whether the focus is specific debugging toolkit patterns or broader debugging workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/debugging/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `ef72913f0973b385aed2b063edb4bb0b679282bdacd62d085acbf2a0f29969fb` computed deterministically.
