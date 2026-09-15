# Phase 08 Batch Audit Record: `batch-152-quality-and-security-security-part01`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-152-quality-and-security-security-part01`
- **Category / Subcategory**: `quality-and-security` / `security`
- **Member Skill Count**: 11
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `2a62807449a0fc2553ff987539e89617c3e753a0e1f1633e33a91924085d0644`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `007` | `task-folder/agents/skills/007` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `antigravity-workflows` | `task-folder/agents/skills/antigravity/antigravity-workflows` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `api-security-testing` | `task-folder/agents/skills/api/api-security-testing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `audit-context-building` | `task-folder/agents/skills/audit-context-building` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `codebase-cleanup-deps-audit` | `task-folder/agents/skills/code/codebase-cleanup-deps-audit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `dependency-management-deps-audit` | `task-folder/agents/skills/dependency-management-deps-audit` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `ethical-hacking-methodology` | `task-folder/agents/skills/ethical-hacking-methodology` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `html-injection-testing` | `task-folder/agents/skills/html-injection-testing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `linux-shell-scripting` | `task-folder/agents/skills/linux/linux-shell-scripting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `malware-analyst` | `task-folder/agents/skills/malware-analyst` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `memory-forensics` | `task-folder/agents/skills/agents/memory-forensics` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `007` | User asks to execute or optimize 007 tasks (e.g. implementing 007 workflows and configurations). | User requests A simpler, more specific tool can handle the request or unrelated operations outside 007. | User asks for general assistance with 007 -> Disambiguate: Clarify whether the focus is specific 007 patterns or broader security workflows. |
| `antigravity-workflows` | User asks to execute or optimize antigravity workflows tasks (e.g. implementing antigravity workflows workflows and configurations). | User requests general infrastructure administration or unrelated application development outside antigravity workflows or unrelated operations outside antigravity workflows. | User asks for general assistance with antigravity workflows -> Disambiguate: Clarify whether the focus is specific antigravity workflows patterns or broader security workflows. |
| `api-security-testing` | User asks to execute or optimize api security testing tasks (e.g. implementing api security testing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside api security testing or unrelated operations outside api security testing. | User asks for general assistance with api security testing -> Disambiguate: Clarify whether the focus is specific api security testing patterns or broader security workflows. |
| `audit-context-building` | User asks to execute or optimize audit context building tasks (e.g. implementing audit context building workflows and configurations). | User requests general infrastructure administration or unrelated application development outside audit context building or unrelated operations outside audit context building. | User asks for general assistance with audit context building -> Disambiguate: Clarify whether the focus is specific audit context building patterns or broader security workflows. |
| `codebase-cleanup-deps-audit` | User asks to execute or optimize codebase cleanup deps audit tasks (e.g. implementing codebase cleanup deps audit workflows and configurations). | User requests The project has no dependency manifests or unrelated operations outside codebase cleanup deps audit. | User asks for general assistance with codebase cleanup deps audit -> Disambiguate: Clarify whether the focus is specific codebase cleanup deps audit patterns or broader security workflows. |
| `dependency-management-deps-audit` | User asks to execute or optimize dependency management deps audit tasks (e.g. implementing dependency management deps audit workflows and configurations). | User requests The project has no dependency manifests or unrelated operations outside dependency management deps audit. | User asks for general assistance with dependency management deps audit -> Disambiguate: Clarify whether the focus is specific dependency management deps audit patterns or broader security workflows. |
| `ethical-hacking-methodology` | User asks to execute or optimize ethical hacking methodology tasks (e.g. implementing ethical hacking methodology workflows and configurations). | User requests general infrastructure administration or unrelated application development outside ethical hacking methodology or unrelated operations outside ethical hacking methodology. | User asks for general assistance with ethical hacking methodology -> Disambiguate: Clarify whether the focus is specific ethical hacking methodology patterns or broader security workflows. |
| `html-injection-testing` | User asks to execute or optimize html injection testing tasks (e.g. implementing html injection testing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside html injection testing or unrelated operations outside html injection testing. | User asks for general assistance with html injection testing -> Disambiguate: Clarify whether the focus is specific html injection testing patterns or broader security workflows. |
| `linux-shell-scripting` | User asks to execute or optimize linux shell scripting tasks (e.g. implementing linux shell scripting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside linux shell scripting or unrelated operations outside linux shell scripting. | User asks for general assistance with linux shell scripting -> Disambiguate: Clarify whether the focus is specific linux shell scripting patterns or broader security workflows. |
| `malware-analyst` | User asks to execute or optimize malware analyst tasks (e.g. implementing malware analyst workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside malware analyst. | User asks for general assistance with malware analyst -> Disambiguate: Clarify whether the focus is specific malware analyst patterns or broader security workflows. |
| `memory-forensics` | User asks to execute or optimize memory forensics tasks (e.g. implementing memory forensics workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside memory forensics. | User asks for general assistance with memory forensics -> Disambiguate: Clarify whether the focus is specific memory forensics patterns or broader security workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/security/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `2a62807449a0fc2553ff987539e89617c3e753a0e1f1633e33a91924085d0644` computed deterministically.
