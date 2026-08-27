# Task List — Phase 04 Execution

- [x] Create/Confirm Git branch `skills-rebuild/phase-04-provider-conversion` from the updated `main` branch.
- [x] Implement folder renames (git mv) for the 4 confirmed non-intrinsic coupled skills.
- [x] Create and execute a comprehensive conversion script that neutralizes provider coupling across the 407 convertible skills using our constrained context-aware pipeline.
- [x] Process and clean `.claude-plugin/` directories under the 407 converted skills, migrating valuable text instructions into `SKILL.md` before removing obsolete config files.
- [x] Update all repository-relative cross-references to point to the new renamed paths.
- [x] Generate the Phase 04 audit deliverable: `task-folder/agents/skills-rebuild/_audit/provider-conversion-report.md`.
- [x] Update `task-folder/agents/skills-rebuild/_audit/skills-inventory.csv` with final conversion status, basis, new destination paths, and current destination.
- [x] Write the reproducible validation script: `task-folder/agents/skills-rebuild/_audit/verify_phase_04.py`.
- [x] Execute `verify_phase_04.py` to confirm perfect filesystem-to-database reconciliation and zero absolute local path leaks.
- [x] Review final git diff to ensure a tight, Phase 04-only commit scope.
- [x] Commit with message: `skills-rebuild: complete phase 04 provider conversion`.
- [x] Push branch and open a draft pull request on GitHub targeting `main`.
