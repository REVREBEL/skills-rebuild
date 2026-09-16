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
| `agents-sdk` | User asks to implement, configure, or optimize agents sdk tasks (specifically configuring or implementing agents sdk specifications). | User requests general infrastructure administration, styling, or unrelated operations outside agents sdk or unrelated operations outside agents sdk. | User asks 'How do I handle agents sdk in my workflow?' -> Disambiguate: Clarify whether the task requires specialized agents sdk procedures or general server-management tooling. |
| `bash-linux` | User asks to implement, configure, or optimize bash linux tasks (specifically configuring or implementing bash linux specifications). | User requests general infrastructure administration, styling, or unrelated operations outside bash linux or unrelated operations outside bash linux. | User asks 'How do I handle bash linux in my workflow?' -> Disambiguate: Clarify whether the task requires specialized bash linux procedures or general server-management tooling. |
| `linux-privilege-escalation` | User asks to implement, configure, or optimize linux privilege escalation tasks (specifically configuring or implementing linux privilege escalation specifications). | User requests general infrastructure administration, styling, or unrelated operations outside linux privilege escalation or unrelated operations outside linux privilege escalation. | User asks 'How do I handle linux privilege escalation in my workflow?' -> Disambiguate: Clarify whether the task requires specialized linux privilege escalation procedures or general server-management tooling. |
| `pm2` | User asks to implement, configure, or optimize pm2 tasks (specifically configuring or implementing pm2 specifications). | User requests Detached terminal sessions** → use [holdpty](https://github.com/marcfargas/holdpty) (PTY output, attach/view) or unrelated operations outside pm2. | User asks 'How do I handle pm2 in my workflow?' -> Disambiguate: Clarify whether the task requires specialized pm2 procedures or general server-management tooling. |
| `react-best-practices` | User asks to implement, configure, or optimize react best practices tasks (specifically configuring or implementing react best practices specifications). | User requests general infrastructure administration, styling, or unrelated operations outside react best practices or unrelated operations outside react best practices. | User asks 'How do I handle react best practices in my workflow?' -> Disambiguate: Clarify whether the task requires specialized react best practices procedures or general server-management tooling. |
| `server-management` | User asks to implement, configure, or optimize server management tasks (specifically configuring or implementing server management specifications). | User requests general infrastructure administration, styling, or unrelated operations outside server management or unrelated operations outside server management. | User asks 'How do I handle server management in my workflow?' -> Disambiguate: Clarify whether the task requires specialized server management procedures or general server-management tooling. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/infrastructure-and-ops/server-management/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `e91cd43a7bf5cfad67a899486d6fe7a40a87cea4f14b8c97fbdcf0b2c380a01f` computed deterministically.

## 5. Resources Created or Moved

- None

## 6. Retired Paths

- None

## 7. Unresolved Items

- None
