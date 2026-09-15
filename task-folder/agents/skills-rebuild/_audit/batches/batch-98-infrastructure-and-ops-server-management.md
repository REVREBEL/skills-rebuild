# Phase 08 Batch Audit Record: `batch-98-infrastructure-and-ops-server-management`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-98-infrastructure-and-ops-server-management`
- **Category / Subcategory**: `infrastructure-and-ops` / `server-management`
- **Member Skill Count**: 6
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `e91cd43a7bf5cfad67a899486d6fe7a40a87cea4f14b8c97fbdcf0b2c380a01f`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `agents-sdk` | `task-folder/agents/skills/agents/agents-sdk` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `bash-linux` | `task-folder/agents/skills/bash/bash-linux` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `linux-privilege-escalation` | `task-folder/agents/skills/linux/linux-privilege-escalation` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pm2` | `task-folder/agents/skills/pm2` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `react-best-practices` | `task-folder/agents/skills/react/react-best-practices` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `server-management` | `task-folder/agents/skills/server-management` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `agents-sdk` | User asks to execute or optimize agents sdk tasks (e.g. implementing agents sdk workflows and configurations). | User requests general infrastructure administration or unrelated application development outside agents sdk or unrelated operations outside agents sdk. | User asks for general assistance with agents sdk -> Disambiguate: Clarify whether the focus is specific agents sdk patterns or broader server-management workflows. |
| `bash-linux` | User asks to execute or optimize bash linux tasks (e.g. implementing bash linux workflows and configurations). | User requests general infrastructure administration or unrelated application development outside bash linux or unrelated operations outside bash linux. | User asks for general assistance with bash linux -> Disambiguate: Clarify whether the focus is specific bash linux patterns or broader server-management workflows. |
| `linux-privilege-escalation` | User asks to execute or optimize linux privilege escalation tasks (e.g. implementing linux privilege escalation workflows and configurations). | User requests general infrastructure administration or unrelated application development outside linux privilege escalation or unrelated operations outside linux privilege escalation. | User asks for general assistance with linux privilege escalation -> Disambiguate: Clarify whether the focus is specific linux privilege escalation patterns or broader server-management workflows. |
| `pm2` | User asks to execute or optimize pm2 tasks (e.g. implementing pm2 workflows and configurations). | User requests Detached terminal sessions** → use [holdpty](https://github.com/marcfargas/holdpty) (PTY output, attach/view) or unrelated operations outside pm2. | User asks for general assistance with pm2 -> Disambiguate: Clarify whether the focus is specific pm2 patterns or broader server-management workflows. |
| `react-best-practices` | User asks to execute or optimize react best practices tasks (e.g. implementing react best practices workflows and configurations). | User requests general infrastructure administration or unrelated application development outside react best practices or unrelated operations outside react best practices. | User asks for general assistance with react best practices -> Disambiguate: Clarify whether the focus is specific react best practices patterns or broader server-management workflows. |
| `server-management` | User asks to execute or optimize server management tasks (e.g. implementing server management workflows and configurations). | User requests general infrastructure administration or unrelated application development outside server management or unrelated operations outside server management. | User asks for general assistance with server management -> Disambiguate: Clarify whether the focus is specific server management patterns or broader server-management workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/infrastructure-and-ops/server-management/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `e91cd43a7bf5cfad67a899486d6fe7a40a87cea4f14b8c97fbdcf0b2c380a01f` computed deterministically.
