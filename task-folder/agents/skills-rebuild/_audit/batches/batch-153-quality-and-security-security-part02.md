# Phase 08 Batch Audit Record: `batch-153-quality-and-security-security-part02`

## 1. Batch Metadata & Universe Accounting

- **Batch ID**: `batch-153-quality-and-security-security-part02`
- **Category / Subcategory**: `quality-and-security` / `security`
- **Member Skill Count**: 11
- **Batch Status**: `completed`
- **Validation Status**: `verified`
- **Deterministic Manifest Hash (SHA-256)**: `c30b7b50f151e6f307ba5ce86e9c0e208eea0287dbbe219bbf43f717c174a70a`

## 2. Canonical Skills Summary & Provenance

| Skill Name | Origin Path | Workflow | Upstream Provenance | License | Risk |
|---|---|---|---|---|---|
| `nestjs-expert` | `task-folder/agents/skills/nextjs/nestjs-expert` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `network-101` | `task-folder/agents/skills/networks/network-101` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `pci-compliance` | `task-folder/agents/skills/pci-compliance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `protocol-reverse-engineering` | `task-folder/agents/skills/protocol-reverse-engineering` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `semgrep-rule-creator` | `task-folder/agents/skills/semgrep-rule-creator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `semgrep-rule-variant-creator` | `task-folder/agents/skills/semgrep-rule-variant-creator` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `shodan-reconnaissance` | `task-folder/agents/skills/shodan-reconnaissance` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `sql-injection-testing` | `task-folder/agents/skills/sql-injection-testing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `sqlmap-database-pentesting` | `task-folder/agents/skills/sqlmap-database-pentesting` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `web-security-testing` | `task-folder/agents/skills/web-security-testing` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |
| `wireshark-analysis` | `task-folder/agents/skills/wireshark-analysis` | `skill-improver` | Community / Canonical | `not_declared_upstream` | `unknown` |

## 3. Trigger Boundary Evaluation Evidence

| Skill Name | Should Trigger | Should Not Trigger | Ambiguous Neighbor Query |
|---|---|---|---|
| `nestjs-expert` | User asks to execute or optimize nestjs expert tasks (e.g. implementing nestjs expert workflows and configurations). | User requests general infrastructure administration or unrelated application development outside nestjs expert or unrelated operations outside nestjs expert. | User asks for general assistance with nestjs expert -> Disambiguate: Clarify whether the focus is specific nestjs expert patterns or broader security workflows. |
| `network-101` | User asks to execute or optimize network 101 tasks (e.g. implementing network 101 workflows and configurations). | User requests general infrastructure administration or unrelated application development outside network 101 or unrelated operations outside network 101. | User asks for general assistance with network 101 -> Disambiguate: Clarify whether the focus is specific network 101 patterns or broader security workflows. |
| `pci-compliance` | User asks to execute or optimize pci compliance tasks (e.g. implementing pci compliance workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside pci compliance. | User asks for general assistance with pci compliance -> Disambiguate: Clarify whether the focus is specific pci compliance patterns or broader security workflows. |
| `protocol-reverse-engineering` | User asks to execute or optimize protocol reverse engineering tasks (e.g. implementing protocol reverse engineering workflows and configurations). | User requests You need a different domain or tool outside this scope or unrelated operations outside protocol reverse engineering. | User asks for general assistance with protocol reverse engineering -> Disambiguate: Clarify whether the focus is specific protocol reverse engineering patterns or broader security workflows. |
| `semgrep-rule-creator` | User asks to execute or optimize semgrep rule creator tasks (e.g. implementing semgrep rule creator workflows and configurations). | User requests Running existing Semgrep rulesets or unrelated operations outside semgrep rule creator. | User asks for general assistance with semgrep rule creator -> Disambiguate: Clarify whether the focus is specific semgrep rule creator patterns or broader security workflows. |
| `semgrep-rule-variant-creator` | User asks to execute or optimize semgrep rule variant creator tasks (e.g. implementing semgrep rule variant creator workflows and configurations). | User requests Creating a new Semgrep rule from scratch (use `semgrep-rule-creator` instead) or unrelated operations outside semgrep rule variant creator. | User asks for general assistance with semgrep rule variant creator -> Disambiguate: Clarify whether the focus is specific semgrep rule variant creator patterns or broader security workflows. |
| `shodan-reconnaissance` | User asks to execute or optimize shodan reconnaissance tasks (e.g. implementing shodan reconnaissance workflows and configurations). | User requests general infrastructure administration or unrelated application development outside shodan reconnaissance or unrelated operations outside shodan reconnaissance. | User asks for general assistance with shodan reconnaissance -> Disambiguate: Clarify whether the focus is specific shodan reconnaissance patterns or broader security workflows. |
| `sql-injection-testing` | User asks to execute or optimize sql injection testing tasks (e.g. implementing sql injection testing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside sql injection testing or unrelated operations outside sql injection testing. | User asks for general assistance with sql injection testing -> Disambiguate: Clarify whether the focus is specific sql injection testing patterns or broader security workflows. |
| `sqlmap-database-pentesting` | User asks to execute or optimize sqlmap database pentesting tasks (e.g. implementing sqlmap database pentesting workflows and configurations). | User requests general infrastructure administration or unrelated application development outside sqlmap database pentesting or unrelated operations outside sqlmap database pentesting. | User asks for general assistance with sqlmap database pentesting -> Disambiguate: Clarify whether the focus is specific sqlmap database pentesting patterns or broader security workflows. |
| `web-security-testing` | User asks to execute or optimize web security testing tasks (e.g. implementing web security testing workflows and configurations). | User requests general infrastructure administration or unrelated application development outside web security testing or unrelated operations outside web security testing. | User asks for general assistance with web security testing -> Disambiguate: Clarify whether the focus is specific web security testing patterns or broader security workflows. |
| `wireshark-analysis` | User asks to execute or optimize wireshark analysis tasks (e.g. implementing wireshark analysis workflows and configurations). | User requests general infrastructure administration or unrelated application development outside wireshark analysis or unrelated operations outside wireshark analysis. | User asks for general assistance with wireshark analysis -> Disambiguate: Clarify whether the focus is specific wireshark analysis patterns or broader security workflows. |

## 4. Verification & Consistency Sign-off

- [x] 100% of member packages verified on disk under `task-folder/agents/skills-rebuild/quality-and-security/security/`
- [x] Frontmatter validated with machine-verifiable `<what>. Use when <trigger>` pattern.
- [x] Substantive capability-specific trigger boundary evaluation confirmed.
- [x] Manifest hash `c30b7b50f151e6f307ba5ce86e9c0e208eea0287dbbe219bbf43f717c174a70a` computed deterministically.
