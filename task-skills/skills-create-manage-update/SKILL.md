---
name: skills-create-manage-update
description: 'Route Agent Skill discovery, inventory, auditing, creation, authoring, validation, improvement, optimization, updating, consolidation, and library management. Use when reviewing a skills folder, creating or rebuilding SKILL.md files, checking specification compliance, improving skill discovery, converting model-specific instructions, merging or splitting skills, or organizing a router-based skills library.'
compatibility: 'Requires read access to the source skill folders. Creation and maintenance workflows require filesystem write access. Run repository-provided validation tools when available.'
metadata:
  category: agent-skills
  type: master-router
  source: custom
---

# Skills Create, Manage & Update

Route Agent Skill lifecycle work to the narrowest child skill. This parent skill coordinates discovery, review, creation, maintenance, and validation without duplicating the detailed workflows inside each child.

## When to Use This Skill

Use this router when the task involves:

- Scanning or cataloging a skills library
- Auditing skill quality, dependencies, or compatibility
- Reviewing a skill before changing it
- Creating a new Agent Skill
- Converting instructions into `SKILL.md` format
- Improving skill discovery descriptions
- Refining or optimizing an existing skill
- Updating skills after tools or applications change
- Merging overlapping skills
- Splitting oversized multi-function skills
- Creating parent routers and child skill groups
- Validating a rebuilt skills library
- Managing skill lifecycle and provenance

Do not use every child for every task. Select the smallest workflow that produces a verified result.

## Universal Skill-Library Rules

- Read the full skill and its supporting files before deciding what to do with it.
- Record a source skill before moving, converting, merging, or splitting it.
- Do not delete original skills during an audit. Move rejected or superseded skills to quarantine.
- Use one documented primary disposition per source skill.
- Preserve source attribution and final-path traceability.
- Evaluate trigger overlap, not only filenames.
- Split by independent function, trigger, or outcome, not length alone.
- Merge only when skills perform the same natural job and unique guidance can be preserved.
- Parent routers should route; child skills should execute.
- Do not retain unsupported tool claims or model-specific assumptions accidentally.
- Never claim validation succeeded unless the validation was actually run.

## Quick Routing Guide

| User goal | Primary child skill |
|---|---|
| Unsure which skill workflow applies | [Skill Router](./skill-router/SKILL.md) |
| Scan a folder and produce an inventory | [Skill Scanner](./skill-scanner/SKILL.md) |
| Perform a structured skill audit | [Skill Audit](./skill-audit/SKILL.md) |
| Check specification or structural compliance | [Skill Check](./skill-check/SKILL.md) |
| Review quality before deciding changes | [Skill Review](./skill-review/SKILL.md) |
| Scaffold a straightforward new skill | [Skill Make Template](./skill-make-template/SKILL.md) |
| Create a skill with evaluation resources and scripts | [Skill Creator](./skill-creator/SKILL.md) |
| Design and develop a production skill | [Skill Development](./skill-development/SKILL.md) |
| Use advanced skill-development patterns | [Skill Developer](./skill-developer/SKILL.md) |
| Author or synthesize skill instructions | [Skill Writer](./skill-writer/SKILL.md) |
| Apply a broad writing methodology to skills | [Skills Writing](./skills-writing/SKILL.md) |
| Improve an existing skill | [Skill Improver](./skill-improver/SKILL.md) |
| Reduce duplication and optimize structure | [Skill Optimizer](./skill-optimizer/SKILL.md) |
| Update a skill for changed requirements | [Skill Update](./skill-update/SKILL.md) |
| Manage a skill library lifecycle | [Skill Manage](./skill-manage/SKILL.md) |
| Start from an enhanced example template | [Template Skill Enhanced](./template-skill-enhanced/SKILL.md) |

## Child Skills by Function

### Discovery, Inventory & Routing

#### [Skill Router](./skill-router/SKILL.md)

Interview the user and recommend an installed skill when the correct capability is unclear.

The current child contains broad library-specific recommendations and should be treated as a routing aid, not as the master for this folder.

#### [Skill Scanner](./skill-scanner/SKILL.md)

Scan skill directories and collect paths, metadata, descriptions, dependencies, files, and structural signals.

Use this first for a large library audit.

#### [Skill Audit](./skill-audit/SKILL.md)

Perform a structured audit of skill quality, compatibility, duplication, scope, and risks.

Use after the source inventory exists.

### Review & Validation

#### [Skill Check](./skill-check/SKILL.md)

Check a skill for specification compliance, folder and frontmatter alignment, required fields, links, and validation rules.

#### [Skill Review](./skill-review/SKILL.md)

Review an individual skill’s purpose, triggers, clarity, workflow quality, size, overlap, and readiness.

Use before deciding whether to keep, refine, merge, split, or reject a skill.

### Creation, Scaffolding & Authoring

#### [Skill Make Template](./skill-make-template/SKILL.md)

Create a straightforward Agent Skill scaffold and `SKILL.md` using the Agent Skills specification.

Use this as the default for simple new skills.

#### [Skill Creator](./skill-creator/SKILL.md)

Create and evaluate more elaborate skills with bundled analyzers, comparators, graders, scripts, reports, and reference material.

Bundled resources include:

- `agents/`
- `assets/`
- `eval-viewer/`
- `references/`
- `scripts/`

Use only when the task genuinely requires the larger evaluation framework.

#### [Skill Development](./skill-development/SKILL.md)

Develop production-ready Agent Skills with a comprehensive workflow, including requirements, structure, authoring, and validation.

Supporting reference:

- [Original Skill Creator Reference](./skill-development/references/skill-creator-original.md)

#### [Skill Developer](./skill-developer/SKILL.md)

Apply advanced skill-development patterns, trigger design, hooks, rules, and troubleshooting guidance.

Supporting references:

- [Advanced Patterns](./skill-developer/ADVANCED.md)
- [Hook Mechanisms](./skill-developer/HOOK_MECHANISMS.md)
- [Patterns Library](./skill-developer/PATTERNS_LIBRARY.md)
- [Rules Reference](./skill-developer/SKILL_RULES_REFERENCE.md)
- [Trigger Types](./skill-developer/TRIGGER_TYPES.md)
- [Troubleshooting](./skill-developer/TROUBLESHOOTING.md)

#### [Skill Writer](./skill-writer/SKILL.md)

Author, synthesize, and revise skill instructions using the bundled writing, evaluation, iteration, and registration references.

Key references include:

- [Authoring Path](./skill-writer/references/authoring-path.md)
- [Description Optimization](./skill-writer/references/description-optimization.md)
- [Design Principles](./skill-writer/references/design-principles.md)
- [Evaluation Path](./skill-writer/references/evaluation-path.md)
- [Iteration Path](./skill-writer/references/iteration-path.md)
- [Mode Selection](./skill-writer/references/mode-selection.md)
- [Output Patterns](./skill-writer/references/output-patterns.md)
- [Registration Validation](./skill-writer/references/registration-validation.md)
- [Skill Patterns](./skill-writer/references/skill-patterns.md)
- [Synthesis Path](./skill-writer/references/synthesis-path.md)
- [Workflow Patterns](./skill-writer/references/workflow-patterns.md)

#### [Skills Writing](./skills-writing/SKILL.md)

Apply a broader framework for writing, testing, structuring, and governing skills.

This package includes Anthropic-oriented and subagent-oriented material that must be reviewed during the model-specific conversion phase before being treated as platform-neutral.

#### [Template Skill Enhanced](./template-skill-enhanced/SKILL.md)

Use an enhanced example skill template with examples, references, and a validation rubric.

Supporting resources:

- [Basic Example](./template-skill-enhanced/examples/basic.md)
- [Reference Guide](./template-skill-enhanced/references/README.md)
- [Validation Rubric](./template-skill-enhanced/validation/rubric.yaml)

### Improvement, Optimization & Maintenance

#### [Skill Improver](./skill-improver/SKILL.md)

Improve an existing skill’s description, workflow, structure, safeguards, and completion checks while preserving its intent.

#### [Skill Optimizer](./skill-optimizer/SKILL.md)

Reduce duplication, tighten trigger boundaries, move supporting detail out of the main file, and improve routing efficiency.

#### [Skill Update](./skill-update/SKILL.md)

Update a skill after application, tool, specification, or workflow requirements change.

#### [Skill Manage](./skill-manage/SKILL.md)

Manage the broader skill lifecycle, organization, registration, maintenance, and library-level operations.

## Full Child Index

- [Skill Audit](./skill-audit/SKILL.md)
- [Skill Check](./skill-check/SKILL.md)
- [Skill Creator](./skill-creator/SKILL.md)
- [Skill Developer](./skill-developer/SKILL.md)
- [Skill Development](./skill-development/SKILL.md)
- [Skill Improver](./skill-improver/SKILL.md)
- [Skill Make Template](./skill-make-template/SKILL.md)
- [Skill Manage](./skill-manage/SKILL.md)
- [Skill Optimizer](./skill-optimizer/SKILL.md)
- [Skill Review](./skill-review/SKILL.md)
- [Skill Router](./skill-router/SKILL.md)
- [Skill Scanner](./skill-scanner/SKILL.md)
- [Skill Update](./skill-update/SKILL.md)
- [Skill Writer](./skill-writer/SKILL.md)
- [Skills Writing](./skills-writing/SKILL.md)
- [Template Skill Enhanced](./template-skill-enhanced/SKILL.md)

## Recommended Workflow Routes

### Audit a Large Skills Library

1. [Skill Scanner](./skill-scanner/SKILL.md): build the source inventory.
2. [Skill Audit](./skill-audit/SKILL.md): classify compatibility, scope, overlap, and risk.
3. [Skill Review](./skill-review/SKILL.md): inspect ambiguous or high-impact skills individually.
4. [Skill Check](./skill-check/SKILL.md): validate retained or rebuilt skills.

### Create a Simple New Skill

1. [Skill Make Template](./skill-make-template/SKILL.md): scaffold the folder and initial `SKILL.md`.
2. [Skill Writer](./skill-writer/SKILL.md): refine instructions and discovery language when needed.
3. [Skill Check](./skill-check/SKILL.md): validate the result.

### Create a Complex Evaluated Skill

1. [Skill Development](./skill-development/SKILL.md): define requirements and architecture.
2. [Skill Creator](./skill-creator/SKILL.md): add evaluation infrastructure only when justified.
3. [Skill Developer](./skill-developer/SKILL.md): apply advanced patterns selectively.
4. [Skill Check](./skill-check/SKILL.md): validate.

### Improve an Existing Skill

1. [Skill Review](./skill-review/SKILL.md): identify the actual weaknesses.
2. [Skill Improver](./skill-improver/SKILL.md): repair content and workflow.
3. [Skill Optimizer](./skill-optimizer/SKILL.md): reduce size, duplication, and trigger overlap.
4. [Skill Check](./skill-check/SKILL.md): validate.

### Reorganize a Skills Library

1. [Skill Scanner](./skill-scanner/SKILL.md): inventory the source.
2. [Skill Audit](./skill-audit/SKILL.md): assign dispositions and categories.
3. [Skill Optimizer](./skill-optimizer/SKILL.md): identify merge and split candidates.
4. [Skill Development](./skill-development/SKILL.md): build parent routers and focused children.
5. [Skill Manage](./skill-manage/SKILL.md): maintain library organization and provenance.
6. [Skill Check](./skill-check/SKILL.md): validate every final path and router.

### Convert Claude-Specific Skills

1. [Skill Scanner](./skill-scanner/SKILL.md): locate Claude-specific files, commands, paths, hooks, and tool names.
2. [Skill Review](./skill-review/SKILL.md): decide whether the capability can be generalized.
3. [Skill Improver](./skill-improver/SKILL.md): replace model-specific assumptions with capability-based instructions.
4. [Skill Writer](./skill-writer/SKILL.md): rewrite descriptions and workflows.
5. [Skill Check](./skill-check/SKILL.md): search for accidental remaining dependencies and validate the conversion.

## Known Consolidation Candidates

These children substantially overlap and require comparison before the final rebuild:

- `skill-make-template`, `skill-development`, and portions of `skill-creator`
- `skill-developer` and portions of `skill-development`
- `skill-writer` and `skills-writing`
- `skill-review`, `skill-audit`, and `skill-check`
- `skill-improver`, `skill-optimizer`, and `skill-update`
- `skill-router` and future parent-router logic
- `template-skill-enhanced` and the templates embedded in other creation skills

Do not merge them merely because they share the Agent Skills domain. Compare:

- Trigger phrases
- Required inputs
- Expected outputs
- Workflow stages
- Supporting resources
- Unique instructions
- Validation responsibilities

## Suggested Final Functional Shape

After the consolidation audit, this folder may reasonably shrink toward a structure such as:

```text
skills-create-manage-update/
├── SKILL.md
├── discover-and-inventory/
│   └── SKILL.md
├── audit-and-classify/
│   └── SKILL.md
├── create-skill/
│   └── SKILL.md
├── improve-skill/
│   └── SKILL.md
├── restructure-library/
│   └── SKILL.md
└── validate-skill/
    └── SKILL.md
```

This is a hypothesis for the later consolidation phase, not an instruction to discard unique material now.

## Completion Checks

Before completing skill lifecycle work, confirm:

- The source skill or library was fully read
- The requested scope and target path are explicit
- The source disposition is documented
- Folder names and frontmatter names match
- Descriptions explain both what and when
- Trigger boundaries do not silently collide
- Supporting links and relative paths resolve
- Model-specific assumptions are intentional
- Validation was run or its unavailability is disclosed
- No source skill disappeared without a recorded final decision
