# Task 07: Split Oversized Skills

## Objective

Split retained skills only when they contain independently triggered jobs that require different workflows, tools, outputs, risks, or validation paths.

## Required Context

Use:

- `agents/skills-rebuild/_audit/skills-inventory.csv`
- `agents/skills-rebuild/_audit/functional-taxonomy.md`
- `agents/skills-rebuild/_audit/destination-map.csv`
- `agents/skills-rebuild/_audit/consolidation-map.md`
- `agents/skills-rebuild/_audit/merge-decisions.csv`

Do not split a skill solely because it is long. Move supporting detail into references when the job remains singular.

A split is justified when major sections have independent:

- Trigger phrases or user goals
- Required inputs
- Tools, applications, or permissions
- Execution sequences
- Risk or authorization requirements
- Outputs and completion evidence

Use a parent router only when several focused children share a coherent functional category.

## Task Skills to Use

Read and follow:

- `task-skills/SKILL.md`
- `task-skills/skills-create-manage-update/SKILL.md`
- `task-skills/skills-create-manage-update/skill-review/SKILL.md`
- `task-skills/skills-create-manage-update/skill-library-restructure/SKILL.md`
- `task-skills/skills-create-manage-update/skill-writer/SKILL.md`
- `task-skills/skills-create-manage-update/skills-writing/SKILL.md`

Use `task-skills/github-operations/SKILL.md` for repository operations and reviewable publication batches.

## Work

1. Identify retained skills with multiple independent jobs.
2. Distinguish true multi-job skills from single jobs with extensive supporting material.
3. Define each proposed child skill's trigger, scope, output, tools, and completion gate.
4. Create a parent router only where routing is necessary.
5. Move shared policies to the parent and keep execution details in children.
6. Preserve reusable long-form material in `references/` when splitting is unnecessary.
7. Update destination and provenance mappings for every resulting child.
8. Verify parent links, child links, and retired source paths.

## Deliverable

Create:

`agents/skills-rebuild/_audit/split-map.md`

The map must record original path, split rationale, parent destination, child destinations, content allocation, shared resources, and routing boundaries.

## Completion Gate

Complete only when every approved split has distinct child triggers and outcomes, parent routers contain routing rather than duplicated workflows, and every source section is accounted for in a final destination or documented retirement.