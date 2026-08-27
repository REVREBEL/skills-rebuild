# Implementation Plan: Phase 05 — Define Functional Taxonomy

Design the destination category structure for all **2,286 retained skills** based strictly on the primary user outcomes they deliver, producing a comprehensive functional taxonomy report, a pure 1:1 source-to-destination map, a separate planned router map, and an automated verification suite—without moving or rewriting any physical skills during this phase.

## User Review Required

> [!IMPORTANT]
> **Map First, Move Later (Zero Physical Modifications in Phase 05)**:
> Phase 05 is strictly an audit, taxonomy, and destination mapping phase. The verification suite will actively prove via `git diff` that **zero files or directories under `task-folder/agents/skills/` are modified, moved, merged, split, or deleted** during this task.

> [!NOTE]
> **Scope & Reconciliation Ledger**:
> - Total Inventory Rows: **2,331**
> - Quarantined Population (Excluded from Active Destinations): exactly **45**
> - Retained Population (Mapped 1:1): exactly **2,286** skills (400 Converted + 14 Intrinsic + 1,872 No Conversion Required).

---

## 1. Core Classification Principles & Boundaries

### The Operating Constitution
> **Classify by the skill's primary user outcome, not by the tool it uses or the mechanism by which it performs the work.**

### Single Canonical Home (No Duplication)
Each skill receives exactly one canonical destination directory. Cross-domain relationships (e.g. accessibility testing, full-stack design systems) will later be represented via routers, aliases, metadata, and cross-references—never by duplicate files.

### 10 Top-Level Functional Categories

1. **`development`**:
   - *Primary Outcome*: Create, build, modify, and refactor software architectures, backend services, frontend applications, APIs, database schemas, and language idioms.
   - *Exclusion Boundary*: Does not include testing/verification workflows (belongs in `quality-and-security`) or visual/UI styling design without core logic (belongs in `design-and-experience`). Includes software architecture.
2. **`design-and-experience`**:
   - *Primary Outcome*: Craft visual interfaces, UI/UX workflows, design systems (Tailwind, Radix, Figma), styling taste, animations, motion graphics, and 3D assets.
   - *Exclusion Boundary*: Does not include backend system architecture (belongs in `development`) or pure frontend logic/state algorithms.
3. **`infrastructure-and-ops`**:
   - *Primary Outcome*: Provision, configure, deploy, host, and monitor cloud platforms, servers, CI/CD pipelines, containers, and operating systems.
   - *Exclusion Boundary*: Does not include standalone workflow automation or tool scripting unrelated to cloud/infrastructure management.
4. **`data-and-ai`**:
   - *Primary Outcome*: Model, fine-tune, analyze, query, and serve data, machine learning pipelines, LLM/RAG systems, embeddings, and analytics tracking.
   - *Exclusion Boundary*: Does not include agent governance or skill lifecycle management (belongs in `meta-and-agent-skills`).
5. **`quality-and-security`**:
   - *Primary Outcome*: Verify, test (unit, integration, E2E), diagnose, systematically debug, audit security, scan vulnerabilities, and ensure compliance.
   - *Exclusion Boundary*: Does not include feature development/refactoring (belongs in `development`).
6. **`marketing-and-seo`**:
   - *Primary Outcome*: Drive audience acquisition, search engine visibility (SEO/GEO), conversion rate optimization (CRO), social presence, and digital ads.
   - *Exclusion Boundary*: Does not include core copywriting/documentation without marketing intent (belongs in `content-and-documentation`).
7. **`business-and-operations`**:
   - *Primary Outcome*: Manage products, analyze market opportunities, model financial projections, optimize pricing, and ensure business/legal compliance.
   - *Exclusion Boundary*: Does not include internal agent development workflows.
8. **`content-and-documentation`**:
   - *Primary Outcome*: Produce technical documentation, articles, presentations, research summaries, and structured knowledge artifacts.
   - *Exclusion Boundary*: Does not include marketing copy/SEO optimization (belongs in `marketing-and-seo`).
9. **`workflow-and-automation`**:
   - *Primary Outcome*: Orchestrate multi-step task workflows, integrate external APIs/MCP tools, automate Git operations, and bridge external services.
   - *Exclusion Boundary*: **Strict Gate**: Use *only* when automation or orchestration itself is the primary user job. Do not classify domain skills here merely because they use an automation script or tool.
10. **`meta-and-agent-skills`**:
    - *Primary Outcome*: Author, audit, validate, optimize, benchmark, package, and govern agent skills and multi-agent systems.
    - *Exclusion Boundary*: Does not include application software development or testing.

---

## 2. Proposed Artifact Specifications

### Audit & Mapping Deliverables

#### [NEW] [functional-taxonomy.md](file:///Users/garystringham/github-revrebel/skills-rebuild/task-folder/agents/skills-rebuild/_audit/functional-taxonomy.md)
Comprehensive audit report containing:
- Executive Summary & Taxonomy Architecture.
- Canonical Classification Constitution & Domain Boundaries.
- Detailed Category Specifications (Purpose, Inclusion Criteria, Exclusion Boundaries, Proposed Subcategories).
- Difficult Classification Decision Rules with concrete disambiguation examples (e.g. Figma component creation, GitHub Actions deployment, Linear triage, SEO pipelines).
- Structural Router Architecture (Root, Category, Subcategory routers).
- Mathematically Closed Category Distribution Matrix (summing to exactly 2,286).
- Unresolved Placements, Review Concerns, and Future Merge/Split Structural Candidates.

#### [NEW] [destination-map.csv](file:///Users/garystringham/github-revrebel/skills-rebuild/task-folder/agents/skills-rebuild/_audit/destination-map.csv)
Pure 1:1 mapping database for all 2,286 retained skills with schema:
- `source_path`: Source directory path from `skills-inventory.csv`.
- `compatibility_status`: Compatibility classification (`Capability-Based / Generalized`, `Intrinsic Platform Dependency`, or `General`).
- `proposed_category`: One of the 10 top-level categories.
- `proposed_subcategory`: Functional subcategory cluster.
- `proposed_final_path`: Canonical target path (`task-folder/agents/skills/<category>/<subcategory>/<skill-name>` or `<category>/<skill-name>`).
- `placement_confidence`: `high`, `medium`, or `low`.
- `placement_basis`: Explicit reasoning for category and subcategory selection.
- `placement_concern`: Specific ambiguity notes if confidence is `medium`/`low`, otherwise `None`.
- `future_structure_candidate`: `none`, `merge_candidate`, `split_candidate`, `refine_candidate`, or `router_candidate`.

#### [NEW] [router-map.csv](file:///Users/garystringham/github-revrebel/skills-rebuild/task-folder/agents/skills-rebuild/_audit/router-map.csv)
Dedicated architectural inventory for planned routers:
- `router_type`: `root_router`, `category_router`, or `subcategory_router`.
- `category`: Target top-level category.
- `subcategory`: Target subcategory (or `None`).
- `proposed_path`: Directory path of the router.
- `responsibility`: Routing scope and delegation boundaries.
- `routing_scope`: List of child skills or categories routed.

#### [NEW] [verify_phase_05.py](file:///Users/garystringham/github-revrebel/skills-rebuild/task-folder/agents/skills-rebuild/_audit/verify_phase_05.py)
Automated verification suite implementing all 18 validation gates:
1. `skills-inventory.csv` contains exactly 2,331 rows.
2. Exactly 45 quarantined rows are excluded from destination mapping.
3. Exactly 2,286 active rows are mapped.
4. Every active source path appears exactly once.
5. No quarantined source path appears in `destination-map.csv`.
6. Every mapped row has a valid top-level category from the 10 allowed categories.
7. Every mapped row has a valid compatibility classification.
8. Every mapped row has a non-empty `proposed_final_path`.
9. Destination paths are globally unique (1:1 mapping, no duplicate target destinations).
10. Destination paths are unique case-insensitively.
11. No router/path namespace collisions exist between `destination-map.csv` and `router-map.csv`.
12. Target paths follow naming conventions (kebab-case, shallow depth).
13. Category counts in `destination-map.csv` sum to exactly 2,286.
14. Report category counts in `functional-taxonomy.md` equal `destination-map.csv` counts.
15. `placement_confidence` strictly belongs to `{'high', 'medium', 'low'}`.
16. Every `low` confidence row contains an explicit, non-`None` placement concern.
17. Zero workstation absolute path leaks in committed Phase 05 files.
18. **Git diff proves ZERO modifications under `task-folder/agents/skills/`** (proving no premature moves or edits occurred).

---

## 3. Execution & Verification Workflow

1. **Branch Checkpoint**:
   - Verify `main` is clean and up to date with PR #45 merged.
   - Create branch: `git checkout -b skills-rebuild/phase-05-taxonomy`.
2. **Generate Mapping & Router Datasets**:
   - Build classification engine adhering to the outcome-first classification constitution.
   - Classify all 2,286 retained skills with explicit subcategories, confidence scores, and placement bases.
   - Generate `destination-map.csv` and `router-map.csv`.
3. **Generate Taxonomy Report**:
   - Write `task-folder/agents/skills-rebuild/_audit/functional-taxonomy.md` with complete disambiguation rules, router architecture, and closed reconciliation matrix.
4. **Execute Verification Suite**:
   - Run `python3 task-folder/agents/skills-rebuild/_audit/verify_phase_05.py` and confirm 100% clean passes across all 18 checks.
5. **Git Operations & Draft PR**:
   - Review `git diff` to confirm only audit and mapping files are changed.
   - Commit: `git commit -m "skills-rebuild: complete phase 05 functional taxonomy"`.
   - Push branch and open Draft PR targeting `main`.
   - Update `walkthrough.md`.
